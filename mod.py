import calendar
import math
# print(calendar.isleap(2002))
# print(math.pi)
from random import *
from math import *
print(randint(1,6))
print(sqrt(4))
print(cos(4))

from art import art,text2art
print(art('random',number=2))
print(text2art("art",font='block',chr_ignore=True))
from textblob import TextBlob

text = 'I love you'

blob = TextBlob(text)

print(blob.sentiment)

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()