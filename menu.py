from database import Database
from models.blog import Blog

__author__ = 'dhairya'


class Menu(object):

    def __init__(self):
        # ask user for author name
        # check if they already have an account
        # if not, prompt to create a new one
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one(collection="blogs", query={'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(id=blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # user read or write bolg?
        read_write = input("Do you want to read (r) or write (w) blogs? ")
        if read_write == 'r':
            # if read
            # list the blog in database
            # allow user to pick the blog
            # display the posts
            self._list_blogs()
            self._view_blog()
        elif read_write == 'w':
            # if write
            # check if user has a blog
            # if they do, prompt to write a post
            # if don't, prompt to create a blog
            # self._prompt_write_post()
            self.user_blog.new_post()  # because of the object we are able to call the new post method directly
        else:
            print("Thank you for blogging")

#    def _prompt_write_post(self):
#        self.user_blog.new_post()

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the id of the blog you'd like to read: ")
        blog = Blog.get_from_mongo(id=blog_to_see)
        posts = blog.get_post()
        for post in posts:
            print("Date: {}, Title: {} \n\n".format(post['created_date'], post['title'], post['content']))
