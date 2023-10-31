#!/usr/bin/env python3

import urllib.request
from PIL import Image
import requests
from utils import cli
from utils import api_calls

title,year = cli.get_titles()

url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/" + title

headers = {
	"X-RapidAPI-Key": "9107b39138mshe7b5211b39c1a05p1fd84ejsn5fc14360fcc3",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

querystring = {"exact": "false"}

# Make request
response = requests.request("GET", url, headers=headers, params=querystring)
id = api_calls.get_id(response, year)

url_ratings = "https://moviesdatabase.p.rapidapi.com/titles/" + id + "/ratings"
