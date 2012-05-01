#!/usr/bin/env python

import time
import twitter
from traceback import print_exc

def update_dataset(username, auth, since_id):
    """Fetches as many tweets as possible for the given user since
    since_id. Returns a tuple of the texts and the since_id for the next invocation."""

    api = twitter.Api(**auth)

    page = 1
    statuses = []
    while True:
        try:
            new = api.GetUserTimeline(username, since_id=since_id, count=200,
                                      include_rts=False, page=page)
            if len(new) == 0: break
            statuses += new
            print "Received %d tweets..." % len(statuses)
            page += 1
        except twitter.TwitterError:
            print_exc()
            print "Retrying in 5 seconds..."
            time.sleep(5)

    if len(statuses) == 0:
        print "No new tweets."
        return

    texts = [s.text.replace("\n", " ") for s in statuses]

    return ("\n".join(texts), statuses[0].id)
