import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms - Use a unique hashtag here eg. '#ISSoverheadMyStreet'
TERMS = '#ISSoverhead'


# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)



# GPIO pin number of LED
LED = 36

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)



# Twitter application authentication
APP_KEY = pUw6yPihbG4TVAYcjVsPxRNPo
APP_SECRET = JRkIwZ87RzmZ5bYvFMRw9wATV1zd3oIHG5snn3TDZR8yUolmnP
OAUTH_TOKEN = 975697105-Xj5TUCM7leIgjhEKnDJpgo83e3VS96HUFfVbrPRY
OAUTH_TOKEN_SECRET = djrU87A40unPdkYN8GPSIuHpjpxfGtF4gYz6l4MRTYzxl

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        i=0
                        while i < 20:
                        	GPIO.output(LED,1)
                         	time.sleep(0.5)
                         	GPIO.output(LED,0)
                         	time.sleep(0.5)
                         	i = i + 1




# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

