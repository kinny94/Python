from models.post import Post
from database import Database
__author__ = "Arjun"

Database.initialize()

import pymongo

post = Post("Post-1 Title", "Post-1 Content", "Post-1 Author")
post2 = Post("Post-2 Title", "Post-2 Content", "Post-2 Author")
post3 = Post("Post-3 Title", "Post-3 Content", "Post-3 Author")


print (post.content)
print (post2.content)
