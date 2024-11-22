import requests

token = 'xxxxxxxxxxxxxxx'

items_per_page = 100
pages = 8

for page in range(1, pages + 1):
    url = 'https://api.github.com/orgs/ForresterTM/repos?per_page=' + str(items_per_page) + '&page=' + str(page)
    response = requests.get(url, headers={'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + token})
    #print("Status code: ", response.status_code)

    response_list = response.json()
    #print(response_list)

    for item in response_list:
        #print(">> " + item["name"])
        repo = item["name"]
        #repo = 'WEB_FE_Tempo'
        # verify if any workflow exist in every repo
        url = 'https://api.github.com/repos/ForresterTM/' + repo + '/actions/workflows'
        response = requests.get(url, headers={'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + token})
        response_list = response.json()
        #print(response_list)
        #print(repo + " > Status code: ", response.status_code)
        if response_list['total_count'] > 0:
            print("Repository: " + repo)
        for wf in response_list['workflows']:
            print("    >>  Workflow name: " + wf["name"] + " - path: " + wf["path"])
