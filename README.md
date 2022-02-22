# movieAPI
Scraps the latest list of movies in the IMDB database and saves them in a seperate JSON file. Data can be used from the JSON response. Example: movie name,poster,cast,release date,rating,votes etc.


#### REQUIRES AN API KEY
#### if you want your own API KEY then request it from the TMDB website/API<hr>

```python
import requests
import json
API_KEY = #drop your requested API key here
URL = # drop the url and add your api key and end point routes correctly
response = requests.get(url).json()
if response['success']:
    # can manipulate your data

```

#### SHORT--PROJECT--OVERVIEW


https://user-images.githubusercontent.com/73898320/155100710-eb3e5b3a-1652-4c11-8973-ede570a35a6a.mp4

