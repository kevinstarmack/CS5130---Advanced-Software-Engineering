## Project Milestone 1
__For Milestone #1, the objectives are to:__
* Know what techniques to use / Consolidate research approach
* Start writing code
* Updated Project Report
* Complete data set, which in my case are appropraite software requirements

__In regards to knowing which techniques to use and consolidating my project approach__
* In the grand scheme, I plan on using Python to create a method of automating extraction of requirements from documents, how-to guides, tutorials, etc.
* For the first steps, I always like to start with the happy path, a route which should encounter no errors or exceptions. It can cover a large portion of the workflow, and if it doesn’t work smoothly, the rest of your testing may be blocked. In this example, the happy path would be something like this:

    1. Purchase items from general search
    2. Click order history from accounts page
    3. Verify that previously ordered items are displayed
    4. Add items to cart from the previously ordered list
    5. Complete purchase of previously ordered items

When the code is delivered to me for testing, this would be the first test case to execute.

__Code__
* From a pseudocode standpint, here is what I want to achieve

```sh
$ --add-modules java.se.ee
$ java -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -file input.txt
```

* However, this is at the point I am now:
* I have written a few examples of parsing an input file in Python, and will be looking to how I can tie in the __Natural Language Tool-kit (NLTK)__ into my code further.
```sh
# function for parsing the data
def data_parser(text, dic):
for i, j in dic.iteritems():
    text = text.replace(i,j)
return text

inputfile = open('test.dat')
outputfile = open('test.csv', 'w')

# sample text string, just for demonstration to let you know how the data looks like
# my_text = '"2012-06-23 03:09:13.23",4323584,-1.911224,-0.4657288,-0.1166382,-0.24823,0.256485,"NAN",-0.3489428,-0.130449,-0.2440527,-0.2942413,0.04944348,0.4337797,-1.105218,-1.201882,-0.5962594,-0.586636'

# dictionary definition 0-, 1- etc. are there to parse the date block delimited with dashes, and make sure the negative numbers are not effected
reps = {'"NAN"':'NAN', '"':'', '0-':'0,','1-':'1,','2-':'2,','3-':'3,','4-':'4,','5-':'5,','6-':'6,','7-':'7,','8-':'8,','9-':'9,', ' ':',', ':':',' }

for i in range(4): inputfile.next() # skip first four lines
for line in inputfile:
    outputfile.writelines(data_parser(line, reps))

inputfile.close()
outputfile.close()
#
#### a more conventional method below
#
import sys
import os
import re

def readFile( fileName ):
    try:
      file myFile = open( fileName, "r")
    except IOError:
      print "There was an error reading file"
      sys.exit()
    file_text = myFile.read()
    myFile.close()
    return file_text

def writeFile( fileName, fileContent ):
    ret = 1
    try:
        file myFile = open(fileName, "w")
    except IOError:
        print "There was an error writing to", fileName
        sys.exit()
    myFile.write(fileContent)
    myFile.close()
    return ret

str     textContents  = readFile("./myfile.txt")
list    textLineList = textContents.splitlines()

for textLine in textLineList:
    if re.match("(?:word1|word2|word3)*", textLine, re.I ):
        print textLine
```

__Updated Project Report__
* I will move away from testing educational and medical requirements documents to doing the same with software test cases.
* Here is an example of a test case:

    * Title: Login Page – Authenticate Successfully on gmail.com
    * Description: A registered user should be able to successfully login at gmail.com.
    * Precondition: the user must already be registered with an email address and password.
    * Assumption: a supported browser is being used.

* I will also be using and researching more the __NLTK__ and how that all ties back into Requirements Engineering.

___Example Test Steps___:

   1. Navigate to gmail.com
   2. In the ’email’ field, enter the email address of the registered user.
   3. Click the ‘Next’ button.
   4. Enter the password of the registered user
   5. Click ‘Sign In’

* _Expected Result: A page displaying the gmail user’s inbox should load, showing any new message at the top of the page.
