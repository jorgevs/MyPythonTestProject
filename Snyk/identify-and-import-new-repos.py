import requests

snyk_forrester_org = 'xxxxxxxxxxxxxxxxxxxxxx'
snyk_forresterTM_org = 'xxxxxxxxxxxxxxxxxxxxxx'

github_token = 'xxxxxxxxxxxxxxxxxxxxxx'
snyk_token = 'xxxxxxxxxxxxxxxxxxxxxx'  # ServiceAccount: SnykAPIAutoImportProcess

github_enterprise_integration_id = "xxxxxxxxxxxxxxxxxxxxxx"

def get_github_repos():
    repos_list = []

    items_per_page = 100  # 100
    pages = 8  # 8
    for page in range(1, pages + 1):
        url = 'https://api.github.com/orgs/ForresterTM/repos?per_page=' + str(items_per_page) + '&page=' + str(page)
        response = requests.get(url, headers={'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + github_token})
        #print("Status code: ", response.status_code)

        response_list = response.json()
        #print(response_list)

        for item in response_list:
            repos_list.append(item["name"])
            #print(">> " + item["name"])

    return repos_list


def get_snyk_projects():
    project_list = []
    snyk_domain = 'https://api.snyk.io'
    url = '/rest/orgs/' + snyk_forrester_org + '/projects?version=2023-11-27&limit=20'
    multiple_pages = True

    while multiple_pages:
        #print("URL: " + url)
        response = requests.get(snyk_domain + url, headers={'Authorization': 'Token ' + snyk_token})
        #print("Status code: ", response.status_code)

        response_list = response.json()
        #print(response_list)
        #print(response_list["data"])

        # Retrieves projects and filter them
        for item in response_list["data"]:
            if item["type"] == "project" and item["attributes"]["type"] == "sast" and item["attributes"]["origin"] == "github-enterprise" :
                #print(">> " + item["type"] + " - " + item["attributes"]["name"] + " - " + item["attributes"]["type"] + " - " + item["attributes"]["origin"])
                project_name = item["attributes"]["name"]
                project_list.append(project_name[len("ForresterTM/"):])

        # Detect pagination params
        try:
            pagination_params = str(response_list["links"])
            #print("pagination_params: " + pagination_params)

            next_link = str(response_list["links"]["next"])
            url = next_link
        except KeyError:
            multiple_pages = False

    return project_list

def import_repos(repos_to_import):
    snyk_domain = 'https://snyk.io'
    url = "/api/v1/org/" + snyk_forrester_org + "/integrations/" + github_enterprise_integration_id + "/import"

    for repo in repos_to_import:
        print("Adding repo: " + repo)
        data = '{ "target": { "owner": "ForresterTM", "name": "' + repo + '", "branch": "main"} }'

        response = requests.post(snyk_domain + url, data=data,  headers={'Authorization': 'Token ' + snyk_token, 'Content-Type': 'application/json; charset=utf-8'})
        print(repo + " > Status code: ", response.status_code, response.reason)
        # If Status code = 201 then it means that it got added to the team successfully


print(get_github_repos())
print(get_snyk_projects())
reposToImport = set(get_github_repos()).difference(set(get_snyk_projects()))
print(reposToImport)

import_repos(reposToImport)
