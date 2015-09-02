# -*- coding: utf-8-*-
import logging
import re
import urllib2
import time


WORDS = ["HOT", "COLD", "COOL", "WARM"]

PRIORITY = 4

def handle(text, mic, profile):
    """
        Handle garage events based on user input
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    def on_connect(client, userdata, flags, rc):
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("<status_topic>")

    

    logger = logging.getLogger(__name__)
    logger.debug("Garage: got text=" + text)

    if re.search(r'\bhot\b', text, re.IGNORECASE):
        logger.debug("Turning on cooler <cmd_topic>")
        mic.say("So take off all your clothes")
        time.sleep(5)
        mic.say("Just kidding, turning on the cooler now.")
        url_response = urllib2.urlopen('http://192.168.0.231/cgi-bin/relay.cgi?on')
    if re.search(r'\bcold\b', text, re.IGNORECASE):
        logger.debug("Turning off cooler <cmd_topic>")
        url_response = urllib2.urlopen('http://192.168.0.231/cgi-bin/relay.cgi?off')
        mic.say("Gosh, put on a sweater!")
   

def isValid(text):
    """
        Returns True if the text is related to the cooler

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(weathers?|hot|' +
                          r'cold|freezing|)\b', text, re.IGNORECASE)