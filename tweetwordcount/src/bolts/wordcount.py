from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

        #establish connection
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
       

    def process(self, tup):
        word = tup.values[0]
        cur = self.conn.cursor()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        
        # cur.execute("SELECT word, count from tweetwordcount WHERE word=%s", [word])
        # records = cur.fetchall()
        if self.counts[word] == 1:
            cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s)", (word, 1))
        else:
            newcount = self.counts[word]
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (newcount, word))

        #if len(records == 0):
        #    pass
            # cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s)", (word, 1))
        #else:
        #    pass

        #    newcount = records[0][1] + 1
        #    cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (newcount, word))

        self.conn.commit()


        # Increment the local count
        # self.counts[word] += 1
        # self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

