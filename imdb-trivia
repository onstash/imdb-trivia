import requests
import json
import os
import urllib2

print "\n\n\tWelcome to the MOVIE POSTER and TRIVIA downloader v0.01a"
print "\n\n**ENTER MOVIE NAME WITH SPACES**"
movie_name = raw_input('Enter the movie name:')
movie_json_file = movie_name.replace(' ','_') + str('.json')

#JSON download
if not os.path.exists(movie_json_file):
	print "\n\t Saving JSON File..\n"	
	r = requests.get('http://www.omdbapi.com/?t='+str(movie_name))
	movie_json_data = r.json()
	with open(movie_json_file,'w') as json_outfile:
		json.dump(movie_json_data, json_outfile, sort_keys = True, indent = 4)
	print "\n\t JSON file \"" + str(movie_json_file) + "\" saved successfully!"

#JSON Parsing
movie_info = json.loads(open(str(movie_json_file)).read())

#URL Definitions
imdbURL = "http://www.imdb.com/title/" + str(movie_info["imdbID"])
posterURL = movie_info["Poster"]
triviaURL = imdbURL + "/trivia?ref_=tt_trv_trv"
quotesURL = imdbURL + "/trivia?tab=qt&ref_=tt_trv_qu"

#Printing Details
print "\n" + ("-" * 80)
print "\n\t Title \t\t-\t" + movie_info["Title"]
print "\n\t Year \t\t-\t" + movie_info["Year"]
print "\n\t Released \t-\t" + movie_info["Released"]
print "\n\t Director \t-\t" + movie_info["Director"]
print "\n\t Actors \t-\t" + movie_info["Actors"]
print "\n\t Genre \t\t-\t" + movie_info["Genre"]
print "\n\t imdbURL \t-\t" + imdbURL
print "\n\t Rating \t-\t" + movie_info["imdbRating"]
print "\n\t Rated \t\t-\t" + movie_info["Rated"]
print "\n\t Runtime \t-\t" + movie_info["Runtime"]
print "\n\t Language \t-\t" + movie_info["Language"]
print "\n\t Plot \t\t-\t" + movie_info["Plot"]
print "\n\t Poster \t-\t" + movie_info["Poster"]
print "\n\t TriviaURL \t-\t" + triviaURL
print "\n\t QuotesURL \t-\t" + quotesURL
print "\n" + ("-" * 80)

#Download Trivia of the movie
triviaHTML = movie_name.replace(' ','_') + "-TRIVIA.html"

if not os.path.exists(triviaHTML):
	print "\n\t Downloading TRIVIA related to \"" + movie_name + "\".."
	response = urllib2.urlopen(triviaURL)
	trivia_content = response.read()	
	trivia_file = open(str(triviaHTML),'w')
	trivia_file.write(trivia_content)
	trivia_file.close()
	print "\n\n\tFile \""+str(triviaHTML)+"\" saved succesfully!!"

#Download Poster of the movie
poster_file = movie_name.replace(' ','_') + "-POSTER" + posterURL[-4:]
if not os.path.exists(poster_file):
	print "\n\t Downloading POSTER related to \"" + movie_name + "\".."
	response = urllib2.urlopen(posterURL)
	poster_content = response.read()
	poster_image = open(str(poster_file),'w')
	poster_image.write(poster_content)
	poster_image.close()
	print "\n\n\tPoster \""+str(poster_file)+"\" saved succesfully!!"	
	
