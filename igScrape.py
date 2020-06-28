# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 09:12:39 2019

@author: avgbndt
"""
#%%
import requests
import pandas as pd
from datetime import datetime
from sys import argv
#%%


def getComments(user):
    """
    Parameters
    ----------
    user : String
        Instagram user handle(without @).

    Returns
    -------
    None.

    """
    now = datetime.now()
    current_time = now.strftime("%H%M%S")

    try:
        userposts = requests.get(f'https://www.instagram.com/{user}/?__a=1')
        lastpost = userposts.json()
        lastpostid = lastpost['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']

        output = {'author': [],
                  'post_id': [],
                  'contents': [],
                  'created_at': []}

        try:
            result = requests.get(
                f'https://www.instagram.com/p/{lastpostid}/?__a=1')
            whole = result.json()
            comments = whole['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']

            for comment in comments:
                output['author'].append(comment['node']['owner']['username'])
                output['post_id'].append(comment['node']['id'])
                output['contents'].append(comment['node']['text'])
                output['created_at'].append(comment['node']['created_at'])

            df = pd.DataFrame(output)
            df.to_csv(f'{user}-{lastpostid}-{current_time}.csv')
            print(
                f'File ({user}-{lastpostid}-{current_time}.csv) created at local directory')

        except:
            print('No comments currently found.')

    except:
        print("Something happened, please check the spelling for the user handle.")

    print('Done!')


try:
    user_input = str(argv[1])
    getComments(user_input)
except:
    print('Execute the script with an Instagram Handle as the parameter e.g: \n\
          $ python3 igScrape userhandle')
