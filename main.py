import requests
import json

API_KEY = "77898adead85b505390dd8deaabba714"
url = (f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&page=1&language=en-US&include_video=true")
response = requests.get(url).json()
#with open('spiderman.json','w') as file:
#    file.write(json.dumps(response))
for j in range(1,10):
    url = (f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&page={j}&language=en-US&include_video=true")
    response = requests.get(url).json()
    with open(f'page{j}.json','w') as file:
        file.write(json.dumps(response))
        file.close()
    for i in range(len(response['results'])):
        
        movieName = response['results'][i]['original_title']
        movieRating = response['results'][i]['vote_average']
        movieRelease = response['results'][i]['release_date']
        print(f"MOVIE NAME: {movieName}  \nMOVIE RATING: {movieRating}\nRELEASE DATE: {movieRelease}\n")
    
    



    
