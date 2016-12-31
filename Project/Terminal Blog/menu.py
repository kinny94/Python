from database import Database
from models.blog import Blog
__author__ = "Arjun"

class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None

        #underscore before a function means that these function belongs to that class and preferably shouldn't be called from outside the class. Doesn't mean anything in python

        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        #read or write a blog
        read_or_write = input("Do you want to read (R) or write (W) blogs?")
        if read_or_write == "R" or read_or_write == "r":
            self._list_blogs()
            self._view_blogs()
        elif read_or_write == "W" or read_or_write == 'w':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!!!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print ("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("Enter the id of the blog you would like to read!: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, Title: {} \n\n{}".format(post['date'], post['title'], post['content']))