# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:22:27 2020

@author: Ian
"""
from urllib.parse import quote_plus
import praw
import pdb
import re
import os
import datetime

#%%
today = datetime.datetime.today()
month = today.strftime('%B')
year = today.year

title = f'{month} {year} Jobs Roundup Thread'
posting_test = """Please put each new job posting in a reply to the top-level post (i.e., this one);
 include a link; say where the job is located; and provide an optional short summary of the duties and pay scale (if known).
 One job per response, please, so we can clearly thread any subsequent discussion.
All sectors are welcome; most of my own postings are likely to be in my own sector, higher education.

Disclaimer: Unless otherwise specified, users who post jobs have no connection to any position or organization listed here,
so please don't ask for referrals or gouge. This thread is intended as a clearinghouse only."""

reddit_bot = praw.Reddit('EMJobsBot')

subreddit = reddit_bot.subreddit("EmergencyManagement")

subreddit.submit(title, selftext = posting_text)

# for submission in subreddit.stream.submissions():
#     if re.search(r'(Jobs Roundup Thread)', submission.title, re.IGNORECASE):
#         if submission.title == 'May 2020 Jobs Roundup Thread':
#             submission.reply(reply_text)

# reply_template = '[let me google that for you](https://lmgtfy.com/q={})'
# url_title = quote_plus()

