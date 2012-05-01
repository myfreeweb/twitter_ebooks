#!/usr/bin/env python

import os
import time
import json
import redis
import twitter
import urlparse
from generator import Generator
from update_dataset import update_dataset

capitalize = os.environ.get("EBOOKS_CAPITALIZE", False) != False
interval   = int(os.environ.get("EBOOKS_INTERVAL", "14400"))
username   = os.environ["EBOOKS_USERNAME"]
target     = os.environ["EBOOKS_TARGET"]

auth = json.loads(os.environ["EBOOKS_AUTH"])
api = twitter.Api(**auth)

if os.environ.has_key("REDISTOGO_URL"):
    urlparse.uses_netloc.append("redis")
    url = urlparse.urlparse(os.environ["REDISTOGO_URL"])
    db = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
else:
    db = redis.Redis()

while "they're taking the hobbits to Isengard":
    update = update_dataset(username, auth, db.get("last_id"))
    if update:
        (data, last_id) = update
        db.append("data", data)
        db.set("last_id", last_id)
    gen = Generator(db.get("data"), capitalize)
    tweet = gen.tweetworthy()
    api.PostUpdate(tweet)
    time.sleep(interval)
