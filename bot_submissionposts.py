import praw
import time


reddit = praw.Reddit('BottyMcThotty')

subred = reddit.subreddit("conservative").top(limit=250)
for post in subred:
    print('post title=',post.title)
    reddit.subreddit("BotTown2").submit(title=post.title, url=post.url)
    time.sleep(15)