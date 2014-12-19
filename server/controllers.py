from pprint import pprint
from . import app
from flask import render_template, make_response, flash, url_for, session, request, redirect, jsonify
from server.login import twitter
from rauth.utils import parse_utf8_qsl
from server.db import api_manager, db_entry
from server.models import *

for model_name in app.config['API_MODELS']:
    model_class = app.config['API_MODELS'][model_name]
    api_manager.create_api(model_class, methods=['GET', 'POST']) 

@app.route('/<path:path>')
@app.route('/')
def index(path=None):
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)    

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# @app.route('/user')
# def user():
#     # show the user profile for that user
#     return render_template('user.html', str=request.args.get('user'))  

@app.route('/login')
def login():
    oauth_callback = url_for('authorized', _external=True)
    params = {'oauth_callback': oauth_callback}

    r = twitter.get_raw_request_token(params=params)
    data = parse_utf8_qsl(r.content)

    session['twitter_oauth'] = (data['oauth_token'],
                                data['oauth_token_secret'])
    return redirect(twitter.get_authorize_url(data['oauth_token'], **params))  

@app.route('/authorized')
def authorized():
    request_token, request_token_secret = session.pop('twitter_oauth')

    # check to make sure the user authorized the request
    if not 'oauth_token' in request.args:
        flash('You did not authorize the request')
        return redirect(url_for('index'))

    try:
        creds = {'request_token': request_token,
                'request_token_secret': request_token_secret}
        params = {'oauth_verifier': request.args['oauth_verifier']}
        sess = twitter.get_auth_session(params=params, **creds)
    except Exception, e:
        flash('There was a problem logging into Twitter: ' + str(e))
        return redirect(url_for('index'))

    verify = sess.get('account/verify_credentials.json',
                    params={'format':'json'}).json()

    user_payload = {
        'name': verify['name'],
        'twitter_handle': verify['screen_name'],
        'photo': verify['profile_image_url'],
        'email': None
    }
    
    response = User.get_or_create(user_payload)
    print response
    # data = jsonify(response.serialize())
    # print data
    print 'LOGGED IN AS ' + verify['name']
    # pprint(verify)    
    return redirect('user') # calling angularjs router to serve partial
    return redirect(url_for('user', user=response))
