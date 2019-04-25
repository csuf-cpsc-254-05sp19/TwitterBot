import tweepy	#twitter api
import time	#used for time interval posting
import schedule #used to post on specific times 

print("This is a twitter bot by Brittany Kraemer and Nathan Yee")

##################################################################################
# account keys

CONSUMER_KEY = 'IlZxyXCp00qJdejPPCwFLLrDH'
CONSUMER_SECRET = 'Rtcy2SMqhnTLHdenPxO6MruHyppQ8HpDiqk1XJRPBRR6BhLajg'
ACCESS_KEY = '1116377589545701376-4Eua8JN4olk5f8zpSMs3hUUgbt6H31'
ACCESS_SECRET = '4tc2TcxavgWUEFpMPnEFjmjpyW8xDcEVj2hqFwsU1l4yA'

# OAuth process, using using the keys and token
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)



##################################################################################
# images and status'

#MONDAY 
imgMonday = "/pics/monday.JPG"
statusMonday = "Good Morning, happy Monday."

#TUESDAY
imgTuesday = "/pics/tuesday.JPG"
statusTuesday = "Good Morning, happy Tuesday." 

#WEDNESDAY
imgWednesday = "/pics/wednesday.png" 
statusWednesday = "Good Morning, happy Wednesday" 

#THURSDAY
imgThursday = "/pics/thursday.JPG" 
statusThursday = "Good Morning, happy Thursday" 

#FRIDAY
imgFriday = "/pics/friday.JPG" 
statusFriday = "Good Morning, happy Friday"

#SATURDAY 
imgSaturday = "/pics/Saturday.jpg"
statusFriday = "Good Morning, happy Saturday" 

#SUNDAY
imgSunday = "/pics/sunday.JPG" 
statusSunday = "Good Morning, happy Sunday"



##################################################################################
# Define functions for weekdays

def sundayTweet():
	api.update_with_media(imgSunday, statusSunday)
	print("Tweet has been posted")

def mondayTweet():
	api.update_with_media(imgMonday, statusMonday)
	print("Tweet has been posted")

def tuesdayTweet():
	api.update_with_media(imgTuesday, statusTuesday)
	print("Tweet has been posted")

def weddayTweet():
	api.update_with_media(imgWednesday, statusWednesday)
	print("Tweet has been posted")

def thursdayTweet():
	api.update_with_media(imgThursday, statusThursday)
	print("Tweet has been posted")

def fridayTweet():
	api.update_with_media(imgFriday, statusFriday)
	print("Tweet has been posted")

def saturdayTweet():
	api.update_with_media(imgSaturday, statusSaturday)
	print("Tweet has been posted")



##################################################################################
# Test tweet using schedule

schedule.every().sunday.at("9:00").do(thursdayTweet)

schedule.every().monday.at("9:00").do(thursdayTweet)

schedule.every().tuesday.at("9:00").do(thursdayTweet)

schedule.every().wednesday.at("9:00").do(thursdayTweet)

schedule.every().thursday.at("9:00").do(thursdayTweet)

schedule.every().friday.at("9:00").do(thursdayTweet)

schedule.every().saturday.at("9:00").do(thursdayTweet)



##################################################################################
# create infinite timer loop
while True:
	schedule.run_pending()
	time.sleep(1)
	
	
	
