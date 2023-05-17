import re
import urllib.request
import os
import json
import base64

aws_session_token = os.environ.get('AWS_SESSION_TOKEN')


def lambda_handler(event, context):
    try:
        # Retrieve credentials form the request
        authorizationHeader = event['headers']['Authorization']
        print("authorizationHeader: " + authorizationHeader)

        authorizationToken = authorizationHeader.split(' ')
        creds = base64.b64decode(authorizationToken[1]).decode('utf-8').split(':')
        req_user = creds[0]
        req_pwd = creds[1]
        print("req_user: " + req_user)
        print("req_pwd: " + req_pwd)

        # Retrieve credentials from Parameter Store using extension cache
        req = urllib.request.Request(
            'http://localhost:2773/systemsmanager/parameters/get?name=/forrester/apigw/dev/us-east-1/secret/basicauth/credentials&withDecryption=true')
        req.add_header('X-Aws-Parameters-Secrets-Token', aws_session_token)
        config = urllib.request.urlopen(req).read()

        paramValues = json.loads(config)
        paramValues2 = json.loads(paramValues['Parameter']['Value'])
        param_user = paramValues2['ADYEN_USER']
        param_pwd = paramValues2['ADYEN_PASSWORD']
        print("ADYEN_USER: " + param_user)
        print("ADYEN_PASSWORD: " + param_pwd)

        if (req_user == param_user and req_pwd == param_pwd):
            print("ALL OK - Access granted")
        else:
            print("WRONG CREDS - Access denied")
            raise Exception('Unauthorized')

        principalId = 'user|basicAuth123'
        resource = event['path']
        method = event['httpMethod']

        '''
        You can send a 401 Unauthorized response to the client by failing like so:
          raise Exception('Unauthorized')

        If the token is valid, a policy must be generated which will allow or deny access to the client.
        If access is denied, the client will receive a 403 Access Denied response.
        If access is allowed, API Gateway will proceed with the backend integration configured on the method that was called.

        This function must generate a policy that is associated with the recognized principal user identifier.

        Keep in mind, the policy is cached for 5 minutes by default (TTL is configurable in the authorizer) and will apply to
        subsequent calls to any method/resource in the RestApi made with the same token.
        '''
        tmp = event['methodArn'].split(':')
        apiGatewayArnTmp = tmp[5].split('/')
        awsAccountId = tmp[4]

        policy = AuthPolicy(principalId, awsAccountId)
        policy.restApiId = apiGatewayArnTmp[0]  # ex: 2cofgkxpa6
        policy.region = tmp[3]  # ex: us-east-1
        policy.stage = apiGatewayArnTmp[1]  # ex: dev

        # policy.denyAllMethods()
        policy.allowMethod(method, resource)

        # Finally, build the policy
        authResponse = policy.build()

        # Asign a usage identifier (an apiKey) to apply usage limits from within the API gateway system.
        usageIdentifierKey = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
        authResponse['usageIdentifierKey'] = usageIdentifierKey

        return authResponse

    except Exception as e:
        print("Authorization header does not exist in the request")
        print(str(e))
        raise Exception('Unauthorized')


class HttpVerb:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    HEAD = 'HEAD'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'
    ALL = '*'


class AuthPolicy(object):
    # The AWS account id the policy will be generated for. This is used to create the method ARNs.
    awsAccountId = ''
    # The principal used for the policy, this should be a unique identifier for the end user.
    principalId = ''
    # The policy version used for the evaluation. This should always be '2012-10-17'
    version = '2012-10-17'
    # The regular expression used to validate resource paths for the policy
    pathRegex = '^[/._@a-zA-Z0-9-\*]+$'

    '''Internal lists of allowed and denied methods.

    These are lists of objects and each object has 2 properties:
    - A resource ARN and a nullable conditions statement.
    - The build method processes these lists and generates the approriate statements for the final policy.
    '''
    allowMethods = []
    denyMethods = []

    """Replace the placeholder value with a default API Gateway API id to be used in the policy.
    Beware of using '*' since it will not simply mean any API Gateway API id, because stars will greedily expand over '/' or other separators.
    See https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html for more details."""
    restApiId = "<<restApiId>>"

    """Replace the placeholder value with a default region to be used in the policy.
    Beware of using '*' since it will not simply mean any region, because stars will greedily expand over '/' or other separators.
    See https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html for more details."""
    region = "<<region>>"

    """Replace the placeholder value with a default stage to be used in the policy.
    Beware of using '*' since it will not simply mean any stage, because stars will greedily expand over '/' or other separators.
    See https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html for more details."""
    stage = "<<stage>>"

    def __init__(self, principal, awsAccountId):
        self.awsAccountId = awsAccountId
        self.principalId = principal
        self.allowMethods = []
        self.denyMethods = []

    def _addMethod(self, effect, verb, resource, conditions):
        '''Adds a method to the internal lists of allowed or denied methods. Each object in the internal list contains a resource ARN
        and a condition statement. The condition statement can be null.'''
        if verb != '*' and not hasattr(HttpVerb, verb):
            raise NameError('Invalid HTTP verb ' + verb + '. Allowed verbs in HttpVerb class')
        resourcePattern = re.compile(self.pathRegex)
        if not resourcePattern.match(resource):
            raise NameError('Invalid resource path: ' + resource + '. Path should match ' + self.pathRegex)

        if resource[:1] == '/':
            resource = resource[1:]

        resourceArn = 'arn:aws:execute-api:{}:{}:{}/{}/{}/{}'.format(self.region, self.awsAccountId, self.restApiId,
                                                                     self.stage, verb, resource)

        if effect.lower() == 'allow':
            self.allowMethods.append({
                'resourceArn': resourceArn,
                'conditions': conditions
            })
        elif effect.lower() == 'deny':
            self.denyMethods.append({
                'resourceArn': resourceArn,
                'conditions': conditions
            })

    def _getEmptyStatement(self, effect):
        '''Returns an empty statement object prepopulated with the correct action and the desired effect.'''
        statement = {
            'Action': 'execute-api:Invoke',
            'Effect': effect[:1].upper() + effect[1:].lower(),
            'Resource': []
        }

        return statement

    def _getStatementForEffect(self, effect, methods):
        '''This function loops over an array of objects containing a resourceArn and conditions statement and generates the array of statements for the policy.'''
        statements = []

        if len(methods) > 0:
            statement = self._getEmptyStatement(effect)

            for curMethod in methods:
                if curMethod['conditions'] is None or len(curMethod['conditions']) == 0:
                    statement['Resource'].append(curMethod['resourceArn'])
                else:
                    conditionalStatement = self._getEmptyStatement(effect)
                    conditionalStatement['Resource'].append(curMethod['resourceArn'])
                    conditionalStatement['Condition'] = curMethod['conditions']
                    statements.append(conditionalStatement)

            if statement['Resource']:
                statements.append(statement)

        return statements

    def allowAllMethods(self):
        '''Adds a '*' allow to the policy to authorize access to all methods of an API'''
        self._addMethod('Allow', HttpVerb.ALL, '*', [])

    def denyAllMethods(self):
        '''Adds a '*' allow to the policy to deny access to all methods of an API'''
        self._addMethod('Deny', HttpVerb.ALL, '*', [])

    def allowMethod(self, verb, resource):
        '''Adds an API Gateway method (Http verb + Resource path) to the list of allowed methods for the policy'''
        self._addMethod('Allow', verb, resource, [])

    def denyMethod(self, verb, resource):
        '''Adds an API Gateway method (Http verb + Resource path) to the list of denied methods for the policy'''
        self._addMethod('Deny', verb, resource, [])

    def allowMethodWithConditions(self, verb, resource, conditions):
        '''Adds an API Gateway method (Http verb + Resource path) to the list of allowed methods and includes a condition
        for the policy statement. More on AWS policy conditions here: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition'''
        self._addMethod('Allow', verb, resource, conditions)

    def denyMethodWithConditions(self, verb, resource, conditions):
        '''Adds an API Gateway method (Http verb + Resource path) to the list of denied
        methods and includes a condition for the policy statement. More on AWS policy
        conditions here: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition'''
        self._addMethod('Deny', verb, resource, conditions)

    def build(self):
        '''Generates the policy document based on the internal lists of allowed and denied conditions.
        This will generate a policy with two main statements for the effect: one statement for Allow and one statement for Deny.
        Methods that includes conditions will have their own statement in the policy.'''
        if ((self.allowMethods is None or len(self.allowMethods) == 0) and
                (self.denyMethods is None or len(self.denyMethods) == 0)):
            raise NameError('No statements defined for the policy')

        policy = {
            'principalId': self.principalId,
            'policyDocument': {
                'Version': self.version,
                'Statement': []
            }
        }

        policy['policyDocument']['Statement'].extend(self._getStatementForEffect('Allow', self.allowMethods))
        policy['policyDocument']['Statement'].extend(self._getStatementForEffect('Deny', self.denyMethods))

        return policy
