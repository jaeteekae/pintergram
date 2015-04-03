from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from .models import Post
from .serializers import PostSerializer


class PostRouter(ModelPubRouter):
    valid_verbs = ['subscribe'] ## dont know what this is?
    route_name = 'posts'
    model = Post
    serializer_class = PostSerializer


route_handler.register(PostRouter)