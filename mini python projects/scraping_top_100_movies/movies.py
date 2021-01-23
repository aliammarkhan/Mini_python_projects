from bs4 import BeautifulSoup
import requests
#script to get the names of top 100 movies from empire online
url = "https://www.empireonline.com/movies/features/best-movies-2/"

#get the html from the url
response = requests.get(url)

#create soup object
soup = BeautifulSoup(response.text,"html.parser")

#find all the h3 tages with class = title

tags = soup.find_all(name = "h3",class_= "title")
movies = []
#loop through each tag
for tag in tags:
    #append each movie name in the list
    movies.append(tag.getText())
#reverse the list
movies.reverse()
#save the movies in the file
with open("movies.txt","w",encoding="utf-8") as f:
    for movie in movies:
        f.write(f"{movie}\n")
        
    f.close()
