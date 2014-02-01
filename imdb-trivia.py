"""
	TO DO:
		Use webbrowser module to open the triviaHTML after it is saved.
"""

import sys
import json
import urllib2
import os
import webbrowser as browser

def open_trivia(triviaHTML):
	print "\n\t\t Opening TRIVIA page..."
	try:
		browser.open_new(triviaHTML)
	except:
		browser.error

def get_movie():
	print "\n\n**ENTER MOVIE NAME WITH SPACES**"
	movie_name = raw_input('Enter the movie name:')
	return movie_name

def get_info(movie_name):
	"""
		This method takes the string 'movie_name' as an argument and returns a json file.
	"""
	print "\n\t Fetching required JSON File..\n"
	movie_search = movie_name.replace(" ","+")
	url = "http://www.omdbapi.com/?t="+str(movie_search)
	response = urllib2.urlopen(url)
	movie_info = json.load(response)
	return (movie_info)

def get_links(movie_info):
	"""
		This method takes the json 'movie_info' as an argument, checks if the "Response" is "True" i.e. checks if the 'movie_name' exists in imDB or not and returns three links : imdbURL,triviaURL,posterURL.
	"""
	#URL Definitions
	if movie_info["Response"] == "True":
		imdbURL = "http://www.imdb.com/title/" + str(movie_info["imdbID"])
		posterURL = movie_info["Poster"]
		triviaURL = imdbURL + "/trivia?ref_=tt_trv_trv"
		quotesURL = imdbURL + "/trivia?tab=qt&ref_=tt_trv_qu"
		return (imdbURL,triviaURL,posterURL)
	else:
		print "\n\t\t Error fetching imdb data. The required movie does not exist in the database!"
		return (None,None,None)

def print_details(movie_info, imdbURL, triviaURL, posterURL):
	"""
		This method takes 4 arguments : a json file movie_info, imbdURL, triviaURL, posterURL and prints detials regarding the movie_name. 
	"""
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
	print "\n\t Poster \t-\t" + posterURL
	print "\n\t TriviaURL \t-\t" + triviaURL
	print "\n" + ("-" * 80)

def get_trivia(triviaURL, triviaHTML):
	#Local Download Trivia of the movie
	"""
		This method takes 2 arguments : triviaURL, triviaHTML and saves a local copy of the trivia page related to the movie_name.
	"""
	if not os.path.exists(triviaHTML):
		print "\n\t Downloading TRIVIA..."
		response = urllib2.urlopen(triviaURL)
		trivia_content = response.read()	
		trivia_file = open(str(triviaHTML),'w')
		trivia_file.write(trivia_content)
		trivia_file.close()
		print "\n\n\tFile \""+str(triviaHTML)+"\" saved succesfully!!"
	else:
		print "\n\n\tSkipping TRIVIA because \""+str(triviaHTML)+"\" already exists!"

def get_poster(posterURL, poster_file):
	#Download Poster of the movie
	"""
		This method takes 2 arguments : posterURL, poster_file and saves a local copy of the poster image related to the movie_name.
	"""
	if not os.path.exists(poster_file):
		print "\n\t Downloading POSTER..."
		response = urllib2.urlopen(posterURL)
		poster_content = response.read()
		poster_image = open(str(poster_file),'w')
		poster_image.write(poster_content)
		poster_image.close()
		print "\n\n\tPoster \""+str(poster_file)+"\" saved succesfully!!"	
	else:
		print "\n\n\tSkipping POSTER because \""+str(poster_file)+"\" already exists!"

def user_choice():
	choice = 0
	print "\n\t Press -\n"
	print "\n\t\t 1.Trivia(only)"
	print "\n\t\t 2.Poster(only)"
	print "\n\t\t 0.For both Trivia and Poster"
	choice = int(raw_input("\n\tEnter your choice : "))
	return choice

def main():
	print "\n\n\tWelcome to the MOVIE POSTER and TRIVIA downloader v0.2a"
	movie_name = str(sys.argv[1])
	
	#movie_name = get_movie()
	if "_" in movie_name:
		movie_name = movie_name.replace("_"," ")
		
	movie_data = get_info(movie_name)
	
	imdbURL,triviaURL,posterURL = get_links(movie_data)
	poster_ext = posterURL[-4:]

	if not imdbURL == None:
		triviaHTML = movie_name.replace(' ','_') + "-TRIVIA.html"
		#print triviaHTML
		
		poster_file = movie_name.replace(' ','_') + "-POSTER" + poster_ext
		#print poster_file
	
		choice = user_choice()
		if choice == 0:
			get_poster(posterURL, poster_file)
			get_trivia(triviaURL, triviaHTML)
		elif choice == 1:
			get_trivia(triviaURL)
		elif choice == 2:
			get_poster(posterURL)
	
		print_details(movie_data, imdbURL, triviaURL, posterURL)

if __name__ == '__main__':
	main()

