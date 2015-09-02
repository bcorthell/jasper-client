# -*- coding: utf-8-*-
import urllib2
import random
import re

WORDS = ["HOT", "COLD"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("So take off all your clothes")
    url_response = urllib2.urlopen('http://192.168.0.231/cgi-bin/relay.cgi?on')


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bhot\b', text, re.IGNORECASE))