import requests
import json
import urllib.request

#Reddit API guidelines: https://github.com/reddit-archive/reddit/wiki/API

#Change URL to the subreddit you wish to get your image from
URL = "https://www.reddit.com/r/EarthPorn/top/.json" #Note the .json at the end

#Change Header to follow the API guidelines listed above
headers = {
    'User-Agent': 'reddit-wallpaper-downloader-1.0'
}

r = requests.get(URL, headers = headers)

postTitle = r.json()['data']['children'][0]['data']['title']

imageURL = r.json()['data']['children'][0]['data']['url']

#Saves the image with the post title as the file name
urllib.request.urlretrieve(imageURL, postTitle + '.jpg')
