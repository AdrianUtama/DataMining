import urllib.request


user_comment = input("Enter your comment: ")

print ("comment received:", user_comment)

words = user_comment.split()

max_results = 0
max_word = ''

for word in words:
	url = 'http://localhost:8983/solr/second/select?q=comment:' + word + '&spellcheck=on&rows=1000&wt=python'
	connection = urllib.request.urlopen(url)
	response = eval(connection.read())
	if response['response']['numFound'] > max_results:
		max_results = response['response']['numFound']
		max_word = word


url = 'http://localhost:8983/solr/second/select?q=comment:' + max_word + '&spellcheck=on&rows=1000&wt=python'
connection = urllib.request.urlopen(url)
response = eval(connection.read())

array_of_subreddits = []

for document in response['response']['docs']:
  #print ('\n')
  #print(document['subreddit'])
  array_of_subreddits.append(document['subreddit'][0])

set_of_subreddits = set(array_of_subreddits)

for subreddit in set_of_subreddits:
	print('subreddit: ', subreddit)