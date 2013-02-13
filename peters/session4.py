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

	password = getpass.getpass()



	repos = get_repos(user,password,url)


	commits_series = get_commits(user,password,repos)

	df = DataFrame(commits_series)
	return df

def analyse_dataframe(df):
	dic_weekday = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	dates = list(df.index)
	week_day_list = []
	hour_list = []
	
	for entry in dates:
		week_day_list.append(entry.weekday())
		hour_list.append(entry.hour)
	week_dict = Counter(week_day_list)
	hour_dict = Counter(hour_list)

	print "The most common day for a commit is " + dic_weekday[week_dict.most_common(1)[0][0]] + " and the most common hour is " + str(hour_dict.most_common(1)[0][0]) +"."

df = get_dataframe()
analyse_dataframe(df)