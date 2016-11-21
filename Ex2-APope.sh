# Ex2-APope.sh
# Andrea Pope
# w205

# Objective: move files from copied git folder into steamparse project and run steamparse project

# assumptions:
# postgres is running
# python is installed (several packages listed below to add if not already on/installed)


# pip install psycopg2
# pip install pandas
# pip install tweepy

# matplotlib is used for saving final png locally
# standard install, did not work, due to Tkinter
# need to manually install, and change the library
# pip install matplotlib

# git clone git://github.com/matplotlib/matplotlib.git
# cd matplotlib
# python setup.py install

# change liibary manually if see Tkinter errors later
# vi /usr/lib64/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc
# update to make: backend:  agg
# Press Esc
# :wq! (to write and save file)

# copy Streamparse project from git
# git also includes additional python files to run

# ensure git folder has moved over

# ensure at root
cd /root/

sparse quickstart tweetwordcount

# add spouts/bolts/toplogies from git folder
#topology
cd /root/tweetwordcount/topologies
rm wordcount.clj
cd /root/w205Exercise2/tweetwordcount/topologies/
mv tweetwordcount.clj /root/tweetwordcount/topologies

# spout
cd /root/tweetwordcount/src/spouts
rm words.py
cd /root/w205Exercise2/tweetwordcount/src/spouts/
mv tweets.py /root/tweetwordcount/src/spouts


# bolts
cd /root/tweetwordcount/src/bolts
rm wordcount.py
cd /root/w205Exercise2/tweetwordcount/src/bolts
mv parse.py /root/tweetwordcount/src/bolts
mv wordcount.py /root/tweetwordcount/src/bolts

# move to file with supporting programs
cd /root/w205Exercise2/

#create tweetcount dB (where tweets are stored)
python create-tweetcount-db.py

# a good check point to make sure dB is set up

# move into tweetwordcount (from root)
cd /root/tweetwordcount/

# run
sparse run -t 120

cd /root/w205Exercise2

python finalresults.py happy
python histogram.py 13 15
python plot-top-tweets.py 20

# following code will move png file back to git
# git add .
# git commit -m "Top Tweets image"
# git push origin master


