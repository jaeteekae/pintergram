Authentication README

We implemented authentication and authorization using Django REST Framework and the 'django.contrib.
auth' User model. We switched our DB over to using this model for users so that Django will handle the
passwords and hashing.

After switching over our user we updated the serializers and models for posts to keep posts associated
with a user. This way if a request is coming to a update or delete a post from a user other than the
one that's linked to it we can catch it and they will only have read-only access.

We also added some object level permissions to allow for viewing of posts and post info even if not
logged in. If the user is not a superuser, they can only read posts from the using the API. Also, only superusers can view the user API.