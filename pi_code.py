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
APP_KEY = 'wlyCCU4dMANfqr1S4DnXSyV4D'
APP_SECRET = 'AaqQltLh6qFza66qkB5rvMSyjRpL3MGf0caolZdPahZM2cAl7P'
OAUTH_TOKEN = '276163658-9fEYQ6DgcygTpotzl9DFOdTvrCydgg85U8tU3HoR'
OAUTH_TOKEN_SECRET = 'vXwDl18SjbMjYUe40OCsYqCfGa4N0OT8pgklRQssm1pTA'

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

