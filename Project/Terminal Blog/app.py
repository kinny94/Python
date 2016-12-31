# from models.post import Post
from menu import Menu
from database import Database
import pymongo

__author__ = "Arjun"

Database.initialize()

menu = Menu()
menu.run_menu()

"""
post = Post.from_mongo('c7592cfcb89f45c1b8ed6c282b87059c')
print(post)

#this will get all the posts
blog = Post.from_blog('123')
for post in blog:
    print post

"""
