# finalresults.py
# Andrea Pope
#w205
# Display results (1) of streaming tweets into postgres dB
# Gets word as an argument and returns the total number of word occurences in the stream

# standard python library tools
import sys    # command line arguments
import string    # string ascii
import psycopg2   


# general outlines
# get word from command line (alt display all)
# change to lower case (storing words as lowercase)
# check for occurence in postgres

# helper functions

def valid_char(x):
    # validate if string or wild card
    if x in string.ascii_lowercase:
        return True
    else:
        return False

def check_entry(word):
	#validates entered value is made of ascii characters
	valid = False
	for let in word:
		if valid_char(let):
			valid = True
		else:
			valid = False
			break
	return valid




# main program
try:
    
	# connect to dB
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	# set up cursor
	cur = conn.cursor()

	all_words = True
	# 1st system variable is python file name
	if len(sys.argv) < 2:
		all_words = False
		#print("No Argument")
		cur.execute("SELECT word, count from tweetwordcount order by word")
		records = cur.fetchall()
		for rec in records:
			result = "(" + rec[0] + ", " + str(rec[1]) + ")\n"
			#print rec[0]
			#print ":", rec[1], "\n"
			print result
    
	else:
		entry = sys.argv[1]
		while check_entry(entry) == False:
			
			message = "\n You attenpted to enter a word to seach for, " \
					  "but it does not contain valid characters. \n" \
					  "Please enter a word using ASCII characters. " \
					  "New Word: "
			entry = input(message)
		else:
			#switch to lowercase
			entry = entry.lower()
			#print(entry)
			#print("Execute check for word")
			cur.execute("SELECT word, count from tweetwordcount WHERE word=%s", [entry])
			records = cur.fetchall()
			if len(records) > 0:
				resultstring = "Total number of occurences of \'" + records[0][0] + "\': " + str(records[0][1]) + "."
			else:
				resultstring =  "There are no occurences of \'" + entry + "\'."
			print resultstring

		
	conn.close()

except:
	print("Please try again.")

