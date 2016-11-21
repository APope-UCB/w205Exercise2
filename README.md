w205Exercise2


To Run Application:

1.	Start instance, and ensure postgres is running

2.	Clone project directory (from root directory)
git clone https://github.com/APope-UCB/w205Exercise2.git

3.	Navigate to project folder:
cd /root/w205Exercise2/

4.	Ensure permissions on the script
chmod +x Ex2-APope.sh

5.	Run script
./Ex2-APope.sh

Notes on the script file:
Requires specific packages are installed
 - If not already installed on local instance, uncomment lines from script file
   Includes: psycopg2, tweepy, pandas, matplotlib
 - Script Executes the Following:
	Creates Steamparse Project
	Moves files from git directory into steamparse project
	Creates dB for tweets to be stored
	Streams tweets for a specific period of time
	Runs analysis

To run specific analysis(in addition to what is included in script), the following can also be run
1.	Ensure in project directory:
	cd /root/w205Exercise2/

2. 	Analysis files to choose from
	python finalresults.py happy # returns count for 1 word (happy)
	python finalresults.py # returns count for all words
	python histogram.py 13 15
	python plot-top-tweets.py



Submission Overview:
1. Complete and fully functional twitter application - complete, see instructrions above to run

2. Architecture.pdf -included here

3. See screenshots directory (storm components, streaming tweets, 3 analysis pics)

4. This file

5. Plot.png  - included here (note, also within the screenshots directory)
