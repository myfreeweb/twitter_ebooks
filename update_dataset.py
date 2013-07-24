#!/usr/bin/env python

import time
import tweepy
from traceback import print_exc

def update_dataset(username, auth, since_id):
    """Fetches as many tweets as possible for the given user since
    since_id. Returns a tuple of the texts and the since_id for the next invocation."""

    _auth = tweepy.OAuthHandler(auth['consumer_key'], auth['consumer_secret'])
    _auth.set_access_token(auth['access_token_key'], auth['access_token_secret'])
    api = tweepy.API(_auth)

    page = 1
    statuses = []
    while True:
        try:
            new = api.user_timeline(username, since_id=since_id, count=200, page=page)
            if len(new) == 0: break
            statuses += new
            print "Received %d tweets..." % len(statuses)
            page += 1
        except tweepy.TweepError:
            print_exc()
            print "Retrying in 5 seconds..."
            time.sleep(5)

    if len(statuses) == 0:
        print "No new tweets."
        return

    texts = [s.text.replace("\n", " ") for s in statuses]

    return ("\n".join(texts), statuses[0].id)
