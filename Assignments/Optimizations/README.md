Performance Report - Team 14 -  Leg 4

Emma, Julia, James


1. Optimization Techniques

	To optimize our product we used Redis, HTML5 appcache, JS and CSS minification, JS and CSS
	combination and JS at the bottom of pages.

2. Tools Used

	To test the speedup from changing the JS and CSS files we used yslow and to see differences in
	page loads from redis we used the PageLoadTime chrome extension. 

3. Performance Changes

Some highlights of the performance changes from the JS and CSS:

combining css - increased performance score by 2 points
combining js - increased performance score by 7 points
minifying js - increased performance score by 0 points
minifying css - increased performance score by 0 points

And changes in page load times by using redis:

single_post: .35 to .25 ms
index: .65 to .33 ms

4. Lingering Issues

	The biggest issue we still have is the lack of a cdn to serve our static content from an S3 buckett.
	We will definitely be implementing this moving forward as we also want to upload user media to an
	S3 as well so we don't keep it in our own file system like the current setup.

5. Implementation Issues

	We only have redis working on one of our members computers. This probably means that there is
	something wrong with what's on github vs our local machines. Also the HTML5 appcache doesn't save
	most content at the moment so the site looks pretty incomplete because we are waiting to add the
	cdn to hold static images and fonts.