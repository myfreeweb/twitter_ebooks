# twitter_ebooks

Twitter bot to have your own [_ebooks](https://twitter.com/#!/horse_ebooks).

Created by [Jaiden Mispy](https://github.com/mispy), updated to use hipster technology (Heroku & Redis) by [Greg V](https://github.com/myfreeweb). Powered by [NLTK](http://www.nltk.org/).

## Installation

```shell
git clone git://github.com/myfreeweb/twitter_ebooks.git
cd twitter_ebooks
heroku create --stack cedar
git push heroku master
heroku addons:add redistogo
heroku config:add EBOOKS_USERNAME=username EBOOKS_TARGET=username_ebooks EBOOKS_AUTH='{"consumer_key":"","consumer_secret":"","access_token_key":"","access_token_secret":""}'
heroku ps:scale worker=1
```

where `username` is, well, your username. Auth details are the ones you get from [dev.twitter.com](https://dev.twitter.com) (create an app with write permissions and an access token for it).