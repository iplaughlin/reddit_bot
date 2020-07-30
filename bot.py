# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:22:27 2020

@author: Ian
"""
import praw

#%%

def submit_to_reddit(bot_to_use, sub_to_post_to, title = '', posting_text = ''):
    reddit_bot = praw.Reddit(bot_to_use)
    subreddit = reddit_bot.subreddit(sub_to_post_to)
    for item in subreddit.new(limit = 5):
        if item.title == title:
            return item.url
        else:
            subreddit.submit(title, selftext = posting_text)
            for item in subreddit.new(limit = 5):
                if item.title == title:
                    return item.url
                else:
                    return False

def post_to_reddit(bot_to_use, submission_url, posting_text):
    reddit_bot = praw.Reddit(bot_to_use)
    submission = reddit_bot.submission(url = submission_url)
    submission.reply(posting_text)


