#!/usr/bin/env python3

import functools
from pathlib import Path
from urllib.parse import urlparse

import gentools as gen

import praw
from faker import Faker
from tqdm import tqdm
from colorama import Fore

class Bot(object):
    def __init__(self, filename = "credentials.json", count = 1):
        self.configuration = filename
        self.bot = next(self.new_bot(count))

    def new_bot(self, count):
        config = gen.read_json(self.configuration)
        
        if int(config['count']) < count:
            raise ValueError(f"{self.configuration}でご提示いただいた認証情報は物足りなくありません.")
        
        for account in range(count):
            yield praw.Reddit(
                client_id = config['bots'][account]['client_id'],
                client_secret = config['bots'][account]['client_secret'],
                user_agent = Faker().user_agent()
            )

    def scrap(self, subreddit, target_directory, limit = 10, min_score = 10):
        subreddit = self.bot.subreddit(subreddit)

        for submission in tqdm(subreddit.top(limit = limit), unit = '画像', desc = 'ダウンロード中', bar_format = "{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET), ascii = True, total = limit):
            url = urlparse(submission.url)
            image = target_directory.joinpath(url.path[1:])

            if url.netloc == "i.redd.it" and submission.score >= min_score and not image.exists():              
                gen.download(submission.url, image)


if __name__ == '__main__': 
    pass
    
    
        
