Data Schema and Wireframe README - Team 14
==========================================
James McCants, Julia Knight, Emma


--pintergram--

Overview:

	The goal is to create a sort of Pinterest/Instagram/Reddit mashup where 
	users can post photos with associated text, plain text or just a photo.

Driving Idea:

	Based on client feedback, there was a clear emphasis placed upon the 
	ability to easily share content with friends and a larger audience. The 
	goal is to show off. With this idea in mind we want to create an 
	experience that shows a clear link between content and the person posting 
	it.

Design Choices:

	We decided to use (for now) four tables to accomplish our above goals.

	users- The users table has a PK id so that it can be linked to other
	instances with FKs later on. We include a username, full_name and email
	but no more due to the client requesting minimal personal info. The
	avatar_path field is used to store an image path in the file system for
	the users avatar image. Upvotes show how popular a user is as a whole.

	posts- The posts table has PK id so that it can be linked to other things
	later on. The FK for user_id links a post to a user by id. The title, 
	text, timestamp and image_path field all pretatin to the content of the 
	image. There are no restrictions on what can and cannot be null in the db 
	because posts of just text, just images, or both are allowed so we will 
	handle validation on the front end. The upvotes show how popular an image 
	is.

	tags- Allow for easier sorting of images into groups, you can just search 
	for a tag. The FK is used to associate a post to a tag. Once can just 
	querey the tags table for all entries with the same tag (string) and then 
	display all the associated posts.

	followers- using two FKs users are linked together based on who they 
	follow and who follows them. Both FKs would correspond to users.

Wireframe Choices:
	
	We wanted to have a timeline view which would allow the user to scroll 
	through and look at what has been posted sorted by timestamp, more like a 
	newsfeed. We also wanted to have more of a grid view allowing for the 
	grouping of images that the client asked for. There is also the user page 
	that doesn't share too much personal information but stores all of their 
	work in one place to allow for easier showing off. From every page it is 
	easy to create a new post, go to the home page, or go to your own page if 
	you are not already on it. Creating a new post will be a responsive 
	dropdown menu where a user can upload a photo and write about it. Posting 
	should be easy because that is the real point of this site.

