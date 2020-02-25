import tweepy
import geocoder
import folium
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')
consumer_key = 'DSpVC1xYyL1W3Npr3xzWYbI39'
consumer_secret = 'kgvxBslDg55gBxOnz88djgw3HFYanDa6fPAtHZ3VreXMr7P50U'
access_token = '1230809857244176384-ZKNaMge9zyxP9DzEeMzcPJJD1ZnhBo'
access_token_secret = '7hMnkW1Gl1yVCshNuIv0XZmjFYKtRfQyZg0vEHqzEfcxX'


def getting_location(consumer_key, consumer_secret, access_token, access_token_secret, name):
    '''
    str, str, str, str, str -> dict
    Function returns the dict where
    key is friend's name and value is
    friend's location
    '''
    friends_location = {}

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    user = api.get_user(name)

    for friends in user.friends(count=user.friends_count):
        if friends.location:
            friends_location[friends.name] = friends.location

    return friends_location


def lat_lon_location(friends_location):
    '''
    dict -> dict
    Function returns the dict where key is
    friend's name and value is friend's
    latitude-longitude location
    '''

    for friend in friends_location:
        location = geocoder.osm(friend)
        friends_location[friend] = location.latlng

    return friends_location


def map_generating(friends_location):
    '''
    dict -> None
    Function generates map with icons
    of user's friends
    '''
    map = folium.Map(location=[49.817930, 24.022602], zoom_start=3)

    for friend in friends_location:
        if friends_location[friend] is not None:
            map.add_child(folium.Marker(location=[float(friends_location[friend][0]),
                                                  float(friends_location[friend][1])],
                                        icon=folium.Icon(color='black'),
                                        popup=friend))

    map.save('templates/map.html')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def map_generated():
    name = request.form['text']
    try:
        map_generating(lat_lon_location(getting_location(consumer_key,
                                                         consumer_secret,
                                                         access_token,
                                                         access_token_secret,
                                                         name)))
    except tweepy.error.TweepError:  # Exception in case there is no such a twitter username
        return main()

    return render_template('map.html')


if __name__ == '__main__':
    app.run(host='localhost', debug=True)