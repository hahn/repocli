import requests
import math

def getTotalRepos():
	r = requests.get("https://api.github.com/orgs/blankon-packages")
	status_code = r.status_code
	if status_code == 200:
		response = r.json()
		total_repos = response["public_repos"]
		return total_repos
	else:
		return 0

def getTotalReposPage(total_repos):
	print("total repos: {}".format(total_repos))
	per_page = 30
	page = math.ceil(total_repos/per_page)
	print("total page: {}".format(page))
	return page

def getListRepoNamePerPage(page):
	r = requests.get("https://api.github.com/orgs/blankon-packages/repos?page={}".format(page))
	status_code = r.status_code
	if status_code == 200:
		repos_name = []
		results = r.json()
		for repo in results:
			repos_name.append(repo["name"])
		print(repos_name)


if __name__=="__main__":
#	total = getTotalRepos()
#	pages = getTotalReposPage(total)
	getListRepoNamePerPage(1)
