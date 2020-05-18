# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:22:27 2020

@author: Ian
"""
import sys
sys.path.append(r"C:\Users\Ian\AnacondaProjects\GitHub\USAJobs")

from urllib.parse import quote_plus


import praw
import pdb
import re
import os
#import your secrets file
from config_file import config
#%%

reddit_bot = praw.Reddit(client_id = config['clientId'],
                         client_secret = config['secret'], 
                         password = config['password'], 
                         user_agent = 'computer:testBot:v0.1 (by u/iaalaughlin)',
                         username = config['user'])
    
subreddit = reddit_bot.subreddit("EmergencyManagement")
for submission in subreddit.stream.submissions():
    if re.search(r'(Jobs Roundup Thread)', submission.title, re.IGNORECASE):
        print(submission.title)

reply_template = '[let me google that for you](https://lmgtfy.com/q={})'
url_title = quote_plus()

