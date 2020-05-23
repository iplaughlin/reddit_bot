# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:18:55 2020

@author: Ian
"""

import sys
sys.path.append(r"C:\Users\Ian\AnacondaProjects\GitHub\USAJobs")

import praw
from requests import Session
from config_file import config

session = Session()
reddit = praw.Reddit(client_id = config['clientId'],
                     client_secret = None,
                     password = config['password'],
                     requestor_kwargs = {'session':session},
                     user_agent = 'testBot by /u/iaalaughlin',
                     username = config['user'])

config
