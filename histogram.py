# histogram.py
# Andrea Pope
#w205
# Display results (2) of streaming tweets into postgres dB
# Gets word as an argument and returns the total number of word occurences in the stream

# standard python library tools
import psycopg2
import sys    # command line arguments



# general outline:
# create connection to dB
# select all words and their count, ordered by count, and then word, between 2 values
# fetch all records
# display records

# could add more checking for valid integers, etc..

# main program
try:
    
    # connect to dB
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    # set up cursor
    cur = conn.cursor()

    k1 = sys.argv[1]
    k2 = sys.argv[2]

    
    # if not valid integers, defaulting to 10 and 11
    k1 = k1.decode('utf-8')

    if k1.isnumeric():
        k1 = int(k1)
    else:
        k1 = '10'
        k2 = '11'


    k2 = k2.decode('utf-8')
    if k2.isnumeric():
        k2 = int(k2)
    else:
        k1 = '10'
        k2 = '11'

    
    #sql_str = "SELECT word, count FROM tweetwordcount WHERE count between " + str(k1) + " and " + str(k2) +  " ORDER BY count desc, word asc"

    sql_str = "SELECT word, count FROM tweetwordcount WHERE count between " + str(k1) + " and " + str(k2) +  " ORDER BY count desc, word asc"

    cur.execute(sql_str)
    records = cur.fetchall()
    for rec in records:
        result = rec[0] + ": " + str(rec[1]) + "\n"
        #print rec[0]
        #print ":", rec[1], "\n"
        print result



    conn.close()

except:
    print("Please try again and enter 2 valid integers greater than 0.")

    

