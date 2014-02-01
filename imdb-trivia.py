"""
	TO DO:
		Use webbrowser module to open the triviaHTML after it is saved.
"""

import json
import urllib2

def get_movie():
	print "\n\n\tWelcome to the MOVIE POSTER and TRIVIA downloader v0.01a"
	print "\n\n**ENTER MOVIE NAME WITH SPACES**"
	movie_name = raw_input('Enter the movie name:')
	return movie_name

def get_info(movie_name):
	print "\n\t Fetching required JSON File..\n"	
	response = urllib2.urlopen('http://www.omdbapi.com/?t='+str(movie_name))
	movie_info = json.load(response)
	return movie_info
	
def get_links(movie_info):
	
	#URL Definitions
	if movie_info["Response"] == "True":
		imdbURL = "http://www.imdb.com/title/" + str(movie_info["imdbID"])
		posterURL = movie_info["Poster"]
		triviaURL = imdbURL + "/trivia?ref_=tt_trv_trv"
		quotesURL = imdbURL + "/trivia?tab=qt&ref_=tt_trv_qu"
		return (imdbURL,posterURL,triviaURL)
	else:
		print "\n\t\t Error fetching imdb data. The required movie does not exist in the database!"
		return (None,None,None)

def print_details(movie_info):
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

def get_trivia(triviaURL):
	#Local Download Trivia of the movie
	triviaHTML = movie_name.replace(' ','_') + "-TRIVIA.html"

	if not os.path.exists(triviaHTML):
		print "\n\t Downloading TRIVIA related to \"" + movie_name + "\".."
		response = urllib2.urlopen(triviaURL)
		trivia_content = response.read()	
		trivia_file = open(str(triviaHTML),'w')
		trivia_file.write(trivia_content)
		trivia_file.close()
		print "\n\n\tFile \""+str(triviaHTML)+"\" saved succesfully!!"
	else:
		print "\n\n\tSkipping TRIVIA because \""+str(trivaHTML)+"\" already exists!"
	
def get_poster(posterURL):
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
	movie_name = get_movie()
	movie_info = get_info(movie_name)
	imdbURL,triviaURL,posterURL = get_links(movie_info)
	
	choice = user_choice()
	if choice == 0:
		poster_file = get_poster(posterURL)
		triviaHTML = get_trivia(triviaURL)
	elif choice == 1:
		triviaHTML = get_trivia(triviaURL)
	elif choice == 2:
		poster_file = get_poster(posterURL)
		
	print_details(movie_info)
	

if __name__ == '__main__':
	main()
