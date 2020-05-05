# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:22:27 2020

@author: Ian
"""
import sys
sys.path.append(r"C:\Users\Ian\AnacondaProjects\GitHub\USAJobs")



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
    
    
reddit_bot.login(config.user, config.password)

