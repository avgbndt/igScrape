# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 09:12:39 2019

@author: avgbndt
"""
#%%
import requests
import json
from time import sleep
from random import randint
#%%

class Instagram_Scrape(object):

    def __init__(self):
        self.profiles = {}
        self.posts = {}

    def add_profile(self, profile):
        self.profiles[profile] = False

    def add_profiles(self, profile_list):
        for profile in profile_list:
            self.profiles[profile] = False

    def add_post(self, post):
        self.posts[post] = False

    def add_posts(self, post_list):
        for post in post_list:
            self.posts[post] = False

    def gather_posts(self):
        for profile in self.profiles.keys():
            sleep(randint(3, 5))
            try:
                print(f"Requesting {profile}")
                response = requests.get(f"https://www.instagram.com/{profile}/?__a=1")
                parsed_json = json.loads(response.text)
                shortcodes = [i["node"]["shortcode"] for i in parsed_json["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]]
                self.profiles[profile] = True
                with open('posts.csv', 'a') as f:
                    f.write(f'\"User\",\"Post\",\"Status\"\n')
                    for i in shortcodes:
                        f.write(f'\"{profile}\",\"{i}\",\"{False}\"\n')
            except:
                self.profiles[profile] = False
                raise "Failed attempt"
