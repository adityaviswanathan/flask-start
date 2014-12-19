from rauth import OAuth1Service
 
twitter = OAuth1Service(
    name='twitter',
    consumer_key='Z9XGQMZuFNot3oXMu6nqTNurN',
    consumer_secret='xdFmRj6RRDl4Kwx1bXP4Ab3xTsuICvKUqPHy5vKYnamFGXQWxm',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    base_url='https://api.twitter.com/1.1/')
 
request_token, request_token_secret = twitter.get_request_token()
 
authorize_url = twitter.get_authorize_url(request_token)