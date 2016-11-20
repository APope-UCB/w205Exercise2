# plot-top-tweets.py
# Andrea Pope
# w205
# Display histogram of top N tweets, based on input (20 by default)


# standard python library tools
import psycopg2
import sys    # command line arguments
import pandas as pd
import matplotlib



# general outline:
# create connection to dB
# Capture # of  bars
# select all words and their count, ordered by count, and then word, between 2 values
# fetch all records
# display records

# could add more checking for valid intgers, etc..

# main program
try:
    
    # connect to dB
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    # set up cursor
    cur = conn.cursor()
    # bars = 20

    bars = sys.argv[1]
    bars = bars.decode('utf-8')
    if bars.isnumeric():
        bars = int(bars)
    else:
        bars = 20


    sql_str = "SELECT word, count FROM tweetwordcount ORDER BY count desc, word asc LIMIT " + str(bars)

    cur.execute(sql_str)
    records = cur.fetchall()
    df = pd.DataFrame(records)
    bar_chart = df.plot(kind='bar')
    fig = bar_chart.get_figure()
    fig.savefig('TopTweets.png')
    print("See local directly for TopTweets.png bar chart.")

    conn.close()

except:
    print("Please try again and enter 1 valid integer greater than 0.")

    

