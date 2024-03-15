import boto3
import json
import os


def get_application_id_by_name(app_name, region='us-east-1'):
    print(f"Getting application id by name in region: {region}")

    # Create a boto3 client for the AppConfig service
    appconfig_client = boto3.client('appconfig', region_name=region)

    # Initialize the paginator for the list_applications operation
    paginator = appconfig_client.get_paginator('list_applications')

    try:
        if app_name is None:
            raise Exception("Incorrect value for app_name.")

        # Iterate through the pages of applications
        for page in paginator.paginate():
            print("listing applications")
            # Search each application in the current page
            for app in page['Items']:
                print("app: ", app)
                print("app name: ", app['Name'])
                if app['Name'] == app_name:
                    return app['Id']
        # If no matching application is found
        return None

    except Exception as e:
        print(f"Error occurred while searching for application ID: {e}.")
        print(f"Maybe you don't have an AppConfig application named {app_name} in {region}?")
        return None


def get_appconfig_details_by_id(application_id, environment_id, region='us-east-1'):
    print(f"Getting appconfig details by id in region: {region}")

    # Create a boto3 client for the AppConfig service
    appconfig_client_origin = boto3.client('appconfig', region_name=region)

    try:
        if application_id is None or environment_id is None:
            raise Exception("Incorrect value for application_id or environment_id.")

        # Get application details based on the application ID
        response = appconfig_client_origin.get_application(ApplicationId=application_id)

        # Extract the application name from the response
        application_name = response.get('Name', 'Unknown Application')

        # Get name of the environment ("Staging", "Prod", etc)
        env_response = appconfig_client_origin.get_environment(ApplicationId=application_id, EnvironmentId=environment_id)

        env_name = env_response.get('Name', 'Unknown Environment')

        return {'app_name': application_name, 'env_name': env_name}

    except Exception as e:
        print(f"Error occurred while retrieving application name: {e}")
        return 'Unknown Application'


def get_env_id(app_id, env_name, region='us-east-1'):
    print(f"Getting environment id in region: {region}")

    # Create a boto3 client for the AppConfig service
    appconfig_client = boto3.client('appconfig', region_name=region)

    # Initialize the paginator for the list_environments operation
    paginator = appconfig_client.get_paginator('list_environments')

    try:
        if app_id is None or env_name is None:
            raise Exception("Incorrect value for app_id or env_name.")

        print(f"Listing environments for application ID: {app_id}")
        # Iterate through the pages of environments
        for page in paginator.paginate(ApplicationId=app_id):
            print("Checking page of environments...")
            # Search each environment in the current page
            for env in page['Items']:
                print(f"Found environment: {env['Name']} (ID: {env['Id']})")
                if env['Name'] == env_name:
                    print(f"Match found for environment name '{env_name}' with ID: {env['Id']}")
                    return env['Id']
        print(f"No matching environment found for name: {env_name} in application ID: {app_id}")
        # If no matching environment is found
        return None

    except Exception as e:
        print(f"Error occurred while searching for environment ID in {region}: {e}")
        return None


def get_config_profile_name_by_id(application_id, config_profile_id, region='us-east-1'):
    print(f"Getting profile name by id in region: {region}")

    # Create a boto3 client for the AppConfig service
    appconfig_client = boto3.client('appconfig', region_name=region)

    try:
        if application_id is None or config_profile_id is None:
            raise Exception("Incorrect value for application_id or config_profile_id.")

        response = appconfig_client.get_configuration_profile(ApplicationId=application_id, ConfigurationProfileId=config_profile_id)
        return response['Name']
    except Exception as e:
        print(f"Error occurred while retrieving configuration profile name: {e}")
        return None


def get_hosted_configuration_content(application_id, config_profile_id, version_number, region='us-east-1'):
    print(f"Getting hosted configuration content in region: {region}")

    # Create a boto3 client for the AppConfig service
    appconfig_client = boto3.client('appconfig', region_name=region)

    try:
        if application_id is None or config_profile_id is None:
            raise Exception("Incorrect value for application_id or config_profile_id.")

        config_version_response = appconfig_client.get_hosted_configuration_version(ApplicationId=application_id, ConfigurationProfileId=config_profile_id, VersionNumber=int(version_number))
        content = config_version_response['Content'].read()
        return content
    except Exception as e:
        print(f"Error occurred while fetching hosted configuration content: {e}")
        return None


def create_or_get_config_profile(app_id, profile_name, region='us-east-1', content=None):
    print(f"Creating or getting config profile in region: {region}")

    # Create a boto3 client for the AppConfig service
    appconfig_client = boto3.client('appconfig', region_name=region)

    try:
        if app_id is None or profile_name is None:
            raise Exception("Incorrect value for app_id or profile_name.")

        print(f"Checking for existing configuration profiles for application ID: {app_id}")
        profiles = appconfig_client.list_configuration_profiles(ApplicationId=app_id)
        profile_id = None

        for profile in profiles['Items']:
            if profile['Name'] == profile_name:
                profile_id = profile['Id']
                print(f"Matching profile found for '{profile_name}' with ID: {profile_id}")
                break

        if profile_id is None:
            print(f"No matching profile found for '{profile_name}', creating a new profile...")
            response = appconfig_client.create_configuration_profile(ApplicationId=app_id, Name=profile_name, LocationUri='hosted', Type='AWS.AppConfig.FeatureFlags')
            profile_id = response['Id']
            print(f"Created new configuration profile: {response['Name']} (ID: {profile_id})")

        # Create a new configuration version
        print(f"Creating new configuration version for profile '{profile_name}'")
        version_response = appconfig_client.create_hosted_configuration_version(ApplicationId=app_id, ConfigurationProfileId=profile_id, Content=content, ContentType='application/json')
        print(f"Created configuration version {version_response['VersionNumber']} for profile '{profile_name}'")
        return [profile_id, version_response['VersionNumber']]

    except Exception as e:
        print(f"Error occurred in create_or_get_config_profile: {e}")
        return None


def lambda_handler(event, context):
    print(event)

    # Parse the event data
    application_id = event['detail']['Application']['Id']
    environment_id = event['detail']['Environment']['Id']
    configuration_profile_id = event['detail']['ConfigurationProfile']['Id']
    configuration_version = event['detail']['ConfigurationVersion']

    # Log the extracted data
    print("Application ID:", application_id)
    print("Environment ID:", environment_id)
    print("Configuration Profile ID:", configuration_profile_id)
    print("Configuration Version:", configuration_version)

    # Read and log the destination region from environment variables
    target_region = os.environ['TARGET_REGION']
    print("Target Region:", target_region)

    names = get_appconfig_details_by_id(application_id, environment_id)
    app_name = names['app_name']
    env_name = names['env_name']
    print("App Name: %s, Env Name: %s" % (app_name, env_name))

    # Find the app ID and environment ID based on the origin region's app name and environment name
    app_id = get_application_id_by_name(app_name, target_region)
    print(f"Target Application ID: {app_id}")

    target_env_id = get_env_id(app_id, env_name, target_region)
    print('Target Env ID: ', target_env_id)

    # Initialize AppConfig client for the origin region
    appconfig_origin = boto3.client('appconfig')

    # Get the configuration content from the origin region
    origin_config_content = appconfig_origin.get_hosted_configuration_version(ApplicationId=application_id, ConfigurationProfileId=configuration_profile_id, VersionNumber=int(configuration_version))['Content'].read()
    print('origin_config_content: ', origin_config_content)

    # Get the name of the configuration profile in the origin region
    config_profile_name = get_config_profile_name_by_id(application_id, configuration_profile_id)
    print("Configuration Profile Name:", config_profile_name)

    # Get or create the configuration profile ID in the target region
    target_config_profile_id, target_config_version = create_or_get_config_profile(app_id, config_profile_name, target_region, content=origin_config_content)
    print("Target Configuration Profile ID:", target_config_profile_id)

    # Initialize AppConfig client for the target region
    appconfig_target = boto3.client('appconfig', region_name=target_region)

    # Deploy the configuration in the target region
    try:
        response = appconfig_target.start_deployment(ApplicationId=app_id, EnvironmentId=target_env_id, DeploymentStrategyId='AppConfig.AllAtOnce', ConfigurationProfileId=target_config_profile_id, ConfigurationVersion=str(target_config_version))
        print(f"Deployment initiated in {target_region}: {str(response)}")
    except Exception as e:
        print(f"Error deploying configuration: {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Deployment Process Initiated')
    }
