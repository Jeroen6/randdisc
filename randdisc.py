#!/usr/bin/env python

"""RandDisc.py: Randomize a playlist to a collection of folders."""

# Author: Jeroen Lodder (https://github.com/Jeroen6/randdisc)
# License: Public domain
# Version: 0.1
#
# How does it work?
#
# 0. Note: it moves files. (see simulate)
#
# 1. Set "source",  "destination", "tracks" and "discs" as you please.
# An example could be:
# Takes files from "/playlist", move them to "collection/"
# with "10" tracks per disc with a maximum of "20" discs.
#
# 2. Run it.
# The script will take a random file from source,
# and move it to a folder named CD## with a track number prepended.
# Thats it!

import os, shutil
import random
import sys

# Settings:
# Source file directory (no folders!), must end with /
source = "playlist/"
# Desination directory, must end with /
destination = "USB/"
# maximum tracks per disc folder
tracks = 99
# maximum disc folders
discs = 99
# Simulate (set to 1 to no move any files)
sim = 0

# Program:
# Get list of all files in source
files = os.listdir(source)
files.sort()

# Loop until reached max discs
d = 1
while (d <= discs):
	t = 1
	# Loop until reached max tracks on disc
	while (t <= tracks):
                # Loop until out of source file
                if (len(files) == 0):
                        sys.exit('Done! Out of files!')
		# Pick randomg file from list
		item = random.choice(files)
		files.remove(item)
		# Debug: Output the filename with disc and track number
		#print str(d) + " - " + str(t) + " - " + item
		#
		# The moving part
		# Compile the destination part (destination/CD##/file)
		destdir = destination + "CD" + str(d).zfill(len(str(discs))) + "/"
		# Prepend track number
		filename = str(t).zfill(len(str(tracks))) + " - " + item 
		# Make the destination directory
		if not os.path.exists(os.path.dirname(destdir)):
                        os.makedirs(os.path.dirname(destdir))
                # Move the file                        
		src = source + item
		dst = destdir + filename
		if not sim:
                        shutil.move(src,dst)
		print src + "; " + dst
		# Increment track counter
		t = t + 1
	# Increment disc counter
	d = d + 1

# It also lets you know you have selected too much files.
if (len(files) > 0):
        if not (d <= discs):
                sys.exit('Reached disc limit!')         
sys.exit('Done')
