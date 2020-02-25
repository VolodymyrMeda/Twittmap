# Twittmap
JSON navigation and TwittMap modules, labs task 2 and 3 


JSON Navigator (Lab №3, task 2):
- File name: json_navigator.py

- Description: The program navigates you in the JSON file I got from Twitter API (json_api.json in the repositore for example), 
               you can use it for any JSON, actually. Program gives you a choice of all posible keys you can use, when you go 
               to the next stage in the file it will again offer you all the possible keys you may enter. If you reached
               the last stage you can go to the beginning or quit. You may quit or go to the beginning at any stage though.

- Functions:
   - reading_json(file) - function reads JSON file and returns dictionary, where 'file' is JSON file name
   - json_navigation(json_read) - function navigates user in JSON dictionary, where 'json_read' is JSON dictionary
  
- Modules imported: json


Twitter API Map (Lab №3 task 3):
- File name:
  - twittmap_app.py - main module
  - templates - folder with html files (used in flask)
  - static - folder with folder images (used for setting background image in html/css)
  
- Description: Web application created with Flask framework, firstly, user has to enter his Twitter nickname, then he gets the
                map with icons that show the location of user's friends (if they added it in their profile). Twitter API was 
                used to implement the task.
- Functions: 
  - getting_location(consumer_key, consumer_secret, access_token, access_token_secret, name) - function returns the dict where 
                key is friend's name and value friend's location, function takes keys for getting an API and user's name
  - lat_lon_location(friends_location) - function returns the dict where key is friend's name and value is friend's 
                latitude-longitude location, function takes dictionary with names and locations
  - map_generating(friends_location) - function generates map with icons of user's friends, takes dict with names and 
                lat-lon location
                
- Modules imported: 
  - tweepy - getting API from keys
  - geocoder - getting lat-lon location
  - folium - map generating
  - flask - creating web application

Application: meda.pythonanywhere.com
  
