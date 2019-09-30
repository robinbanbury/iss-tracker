#!/usr/bin/env python3

import twitter
from credentials import consumer_key, consumer_secret, access_token, access_secret

api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token,
    access_token_secret=access_secret
)


def post_tweet(message):
    status = api.PostUpdate(message)
    print(status.text)
