import requests

# This script adds all existing repositories in the ForresterTM organization into the "devops-integration" team
# with a reading access level.

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

items_per_page = 100
pages = 8

data = '{"permission": "pull"}'


for page in range(1, pages + 1):
    url = 'https://api.github.com/orgs/ForresterTM/repos?per_page=' + str(items_per_page) + '&page=' + str(page)
    response = requests.get(url, headers={'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + token})
    #print("Status code: ", response.status_code)

    response_list = response.json()
    # print(response_list)

    for item in response_list:
        print(">> " + item["name"])
        repo = item["name"]
        # Adds every repo to the 'devops-integration' team
        url = 'https://api.github.com/orgs/ForresterTM/teams/devops-integration/repos/ForresterTM/' + repo
        response = requests.put(url, data=data, headers={'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + token})
        print(repo + " > Status code: ", response.status_code)
        # If Status code = 204 then it means that it got added to the team successfully
