import requests
import getpass
from pandas import DataFrame
from pandas import Series
from dateutil import parser
from collections import Counter


def get_commits(user,password, repos):
	dates = []
	messages = []
	for repo in repos:
		c_url = repo[1] + "/commits"
		data = requests.get(c_url, auth=(user, password))
		if data.status_code == 401:
			print "Wrong password"
			exit()
		
		for entry in data.json():
			try:
				dates.append(parser.parse(entry["commit"]["committer"]["date"]))
				messages.append(entry["commit"]["message"])
			except TypeError:
				pass


	return Series(messages,index=dates)

def get_repos(user,password,url):
	r_url = url + "repos"
	data = requests.get(r_url, auth=(user, password))
	if data.status_code == 401:
		print "Wrong password"
		exit()
	repos = []
	for repo in data.json():
		repos.append([repo['name'],repo['url']])

	return repos

def get_dataframe():
	url = r"https://api.github.com/orgs/pythonkurs/"
	user = raw_input("Enter your name: ")

	#print parser.parse("2013-02-04T16:58:05Z")

	password = getpass.getpass()



	repos = get_repos(user,password,url)


	commits_series = get_commits(user,password,repos)

	df = DataFrame(commits_series)
	return df

def analyse_dataframe(df):
	dates = list(df.index)
	week_dict = Counter()
	print dates
	"""for entry in dates:
		parsed_time = parser.parse(entry)
		week_dict.update(parsed_time.weekday())
	print week_dict"""

df = get_dataframe()
analyse_dataframe(df)