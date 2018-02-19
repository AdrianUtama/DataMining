import praw
import os

reddit = praw.Reddit(client_id='yvtEWUUqvd0tYQ',
					 client_secret='JVrzr8bzhejekYdCkyqhg9SijTU',
					 user_agent='nobusohaju')

from praw.models import MoreComments


f = open('subredditlist.txt', 'r')

for line2 in f:
	
	line = line2.replace("\n", "")


	subreddit = reddit.subreddit(line)

	x = 0

	#run a loop through the top 10 posts
	for submission in subreddit.top(limit = 65):

		num = str(x) 
		name = line + "-" + num + ".txt"
		filepath = os.path.join("D:\\output",name)

		out = open(filepath, mode='w', encoding='utf-8')
		out.write(' ')

		#grab the title of the post
		#grab the ID of the post
		postTitle = submission.title
		postID = submission.id

		#this should work, but iterate through the comment tree grabbing each comment
		#next two lines are how we clean up the comment tree and allow for iterative search of comments
		submission.comments.replace_more(limit=None)

		#run through comments
		for comment in submission.comments.list():
			
			#save the comment to a text so we can output it to wherever we decide
			text = comment.body

			#we now have the body just need to save it somewhere
			out.write(text)
			out.write(' ')
		x += 1

#should be end of program


