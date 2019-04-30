import tweepy	#twitter api
import time	#used for time interval posting
import schedule #used to post on specific times 

print("This is a twitter bot by Brittany Kraemer and Nathan Yee")

##################################################################################
# account keys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# OAuth process, using using the keys and token
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)



##################################################################################
# images and status'

#MONDAY 
imgMonday = "monday.jpg"
statusMonday = "Good Morning, happy Monday."

#TUESDAY
imgTuesday = "tuesday.jpg"
statusTuesday = "Good Morning, happy Tuesday." 

#WEDNESDAY
imgWednesday = "wednesday.png" 
statusWednesday = "Good Morning, happy Wednesday" 

#THURSDAY
imgThursday = "thursday.jpg"
statusThursday = "Good Morning, happy Thursday" 

#FRIDAY
imgFriday = "friday.jpg" 
statusFriday = "Good Morning, happy Friday"

#SATURDAY 
imgSaturday = "saturday.jpg"
statusSaturday = "Good Morning, happy Saturday" 

#SUNDAY
imgSunday = "sunday.jpg" 
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

def wednesdayTweet():
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

schedule.every().sunday.at("09:00").do(sundayTweet)

schedule.every().monday.at("09:00").do(mondayTweet)

schedule.every().tuesday.at("09:00").do(tuesdayTweet)

schedule.every().wednesday.at("09:00").do(wednesdayTweet)

schedule.every().thursday.at("09:00").do(thursdayTweet)

schedule.every().friday.at("09:00").do(fridayTweet)

schedule.every().saturday.at("09:00").do(saturdayTweet)



##################################################################################
# create infinite timer loop
while True:
	schedule.run_pending()
	time.sleep(1)
	
	
	
