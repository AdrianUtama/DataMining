from urllib2 import *

connection = urlopen('http://127.0.0.1:8983/solr/CORE/select?q=*:*&rows=100&wt=python')

response = eval(connection.read())

print response['response']['numFound'], "documents found."

#for document in response['response']['docs']:
#	print " Subreddit =", document['subreddit'], document['comment']


category = raw_input('Type the category: ')
search = raw_input('Type the keyword: ')

updated_url = 'http://127.0.0.1:8983/solr/CORE/select?q=' + category + ':' + search + '&rows=100&wt=python'

print updated_url


connection = urlopen(updated_url)
response = eval(connection.read())
print response['response']['numFound'], "documents found."

for document in response['response']['docs']:
	print " Subreddit =", document['subreddit'], document['comment']