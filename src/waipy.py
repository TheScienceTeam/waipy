#!/usr/bin/env python3

import json
import functools
from pathlib import Path
from urllib.parse import urlparse

import praw
from faker import Faker


def read_file(file):
    with open(file, encoding = 'utf-8', mode = 'r') as file:
        return file.read()

def read_json(file):
    return json.loads(read_file(file))

def get_credentials(file):
    return read_json(file)['bots']

def new_bot(file, count = 1):
    source = read_json(file)
    
    if int(source['count']) < count:
        raise ValueError(f"Insufficient bot credentials defined in '{file}'.")
    
    for account in range(count):
        yield praw.Reddit(
            client_id = source['bots'][account]['client_id'],
            client_secret = source['bots'][account]['client_secret'],
            user_agent = Faker().user_agent()
        )

def browser(file, bot_count, limit):
    for reddit in new_bot(file, bot_count):
        subreddit = reddit.subreddit('animewallpaper')

        for submission in subreddit.top(limit):
            if not submission.stickied:
                url = urlparse(submission.url)
                if url.netloc == "i.redd.it":
                    print(submission.url)

def main(file, bot_count, limit):
    browser(file, bot_count, limit)

if __name__ == '__main__':
    main('credentials.json', bot_count = 1, limit = 10)

