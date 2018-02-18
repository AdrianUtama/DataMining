import praw

reddit = praw.Reddit(client_id='yvtEWUUqvd0tYQ',
                     client_secret='JVrzr8bzhejekYdCkyqhg9SijTU',
                     user_agent='nobusohaju')

from praw.models import MoreComments

#run a loop through top 500 subreddits
for each string s in list of subreddits


	subreddit = reddit.subreddit(s)


	#run a loop through the top 10 posts
	for submission in subreddit.top(limit = 65)


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


