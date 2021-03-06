#!/usr/bin/env python

import time, random, os
from Tkinter import Tk
from tkFileDialog import askdirectory
from subprocess import Popen

#This will hide the root Tkinter window
root = Tk()
root.withdraw()
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
root.update()

location = askdirectory(parent=root)
if not os.path.isdir(location):
  print "directory not found"
  exit()

time_per_song = raw_input("how long (in seconds) should each song play? (default is 1 minute)\n  >")
try:
  time_per_song = int(time_per_song)
except ValueError:
  time_per_song = 60
if time_per_song <= 0:
  time_per_song = 60

songs = [f for f in os.listdir(location) if (os.path.isfile(os.path.join(location, f)) and f[0]!='.')]
random.shuffle(songs)
print "playing %d songs for %d seconds each\n" % (len(songs), time_per_song)

for i in range(len(songs)):
  p = Popen(["afplay", os.path.join(location, songs[i])])
  print "playing song number %d" % i
  time.sleep(time_per_song)
  p.terminate()