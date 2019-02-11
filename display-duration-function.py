'''

This script retrieves the list of all available subway turnstile data files 
from the New York MTA web site, and saves the files to a local folder.

The page where the files are listed is http://web.mta.info/developers/turnstile.html

The file names from the page do not include the first two digits for 
the year, the missing digits are added to the file name when the file 
is saved. Didn't they live through Y2K?

In their defense, the available files go back to 2010 (as I write this),
so there is no risk of confusion.

Note: I use the requests library instead of urllib2 because I prefer writing
   r = requests.get(myurl)
instead of 
   r = urllib2.urlopen(myurl)
It saves me 3 characters. Otherwise functionality is the same for this simple case.

'''

import requests
from bs4 import BeautifulSoup as BS4
import re
from timeit import default_timer as timer

# initialize URL and folder, record start time
urlroot = r'http://web.mta.info/developers/'
path = r'e:\python\utilities\turnstile_20'
starttime = timer()


# The DisplayDuration function is used to correctly display the completion
# time of a function or program in hours, minutes and seconds, including
# the correct spelling of 'hour(s)', 'minute(s)' and 'second(s)'.
# The output is "Completed in xx hour xx minutes xx seconds."
def DisplayDuration(starttime, endtime):

	m, s = divmod(int(endtime - starttime), 60)
	h, m = divmod(m, 60)

	duration = 'Completed in '

	if h > 0:
		if h > 1:
			duration = duration + str(h) + ' hours '
		else:
			duration = duration + str(h) + ' hour '
	if m > 0:
		if m > 1:
			duration = duration + str(m) + ' minutes '
		else:
			duration = duration + str(m) + ' minute '
	if s > 0:
		if s > 1:
			duration = duration + str(s) + ' seconds.'
		else:
			duration = duration + str(s) + ' second.'
	
	print(duration)


# read the page html and use BeautifulSoup to extract the list of data files
r = requests.get(urlroot + 'turnstile.html')
soup = BS4(r.content, features = 'html.parser')
files = soup.find('div', {'id': 'contentbox'}).find('div', {'class': 'container'}).find('div', {'class': 'span-84 last'}).findAll('a', attrs={'href': re.compile("^data/nyct/turnstile/")})

# iterate through the list of files, retrieve the data for each file, and save file to the local folder
#for file in files:
print('Saving file turnstile_20' + str(files[0])[39:49])
datafile = requests.get(urlroot + str(files[0])[9:49])
with open(path + str(files[0])[39:49], 'w') as outf:
	for line in datafile.text:
	      outf.writelines(line)

print('Saving file turnstile_20' + str(files[1])[39:49])
datafile = requests.get(urlroot + str(files[1])[9:49])
with open(path + str(files[1])[39:49], 'w') as outf:
	for line in datafile.text:
	      outf.writelines(line)

print('Saving file turnstile_20' + str(files[2])[39:49])
datafile = requests.get(urlroot + str(files[2])[9:49])
with open(path + str(files[2])[39:49], 'w') as outf:
	for line in datafile.text:
	      outf.writelines(line)

print('Saving file turnstile_20' + str(files[3])[39:49])
datafile = requests.get(urlroot + str(files[3])[9:49])
with open(path + str(files[3])[39:49], 'w') as outf:
	for line in datafile.text:
	      outf.writelines(line)		  

# record completion time and display duration
endtime = timer()
DisplayDuration(starttime, endtime)
