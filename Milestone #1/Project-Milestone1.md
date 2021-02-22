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
* From a very-high levelpseudocode standpint, here is what I want to achieve

```sh
# input file in any format
# parse file => grab temporal and spacial 'measurements' & compare key words in requirements DB (this would require some manual work)
    # another implementation would be supervised learning
# determine if phrases are requirements
# use information surronding the requirement to generate a test case
# output info to a .csv or .txt
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
* I am also looking at __tf-idf__ as a way to further investigate an ML based approach to gathering requirements. Although the below code example is in JavaScript, note that this was from a previous course taken in Requirements Engineering. A simple JavaScript to Python conversion would not be difficult.
* Link to repo here: https://github.com/kevinstarmack/Requirements-Eng---Traceability
* Below is the main sample of code from the project:
```sh
//can take in any number of FRs in "inputs"
//after opening cmd line
//type cd requirements_eng
//node index.js
//output found in Atom under "requirements-3nfr-80fr.txt"
const jaccard = require('jaccard');
const nlp = require('compromise');
const glob = require('glob');
const keywords = require('keyword-extractor');
const fs = require('fs')

const INPUTS_FOLDER = './inputs/';
const OUTPUTS_FOLDER = './outputs/';
const SIMILARITY_CUTOFF = 0.08;
// Get all inputs
glob.sync(`${INPUTS_FOLDER}*.txt`).forEach(path => {
    let nfr = [];
    let fr = [];

    // Read the file
    fs.readFile(path, 'utf-8', (err, contents) => {
        let lines = contents.split(/\r?\n/);

        lines.forEach(line => {
            if (line.length == 0) {
                return;
            }
            // Split the requirement text from the type (FR/NFR)
            let typeEnd = line.indexOf(':');
            let type = line.substr(0, typeEnd);
            let reqText = line.substr(typeEnd);

            let words = keywords.extract(reqText, {
                language: 'english',
                remove_digits: true,
                return_changed_case: true,
                remove_duplicates: false,
            });
            // Extract singular and infinite forms of word if possible
            words = words.map(word => {
                let noun = nlp(word).nouns().toSingular().text();
                let verb = nlp(word).verbs().toInfinitive().text();

                if (noun.length > 0) {
                    return noun;
                }
                if (verb.length > 0) {
                    return verb;
                }
                return word;
            });

            // Push to either NFR of FR req array
            let reqStorage = type.indexOf('NFR') != -1 ? nfr : fr;
            reqStorage.push({
                id: type,
                req: reqText,
                topics: words
            });
        });

// Loop through FR and compute similarities with each NFR
        let outString = '';
        fr.forEach(frData => {
            let results = [];

            // Get the jaccard index of the NFR and FR keywords
            nfr.forEach(nfrData => {
                let index = jaccard.index(frData.topics, nfrData.topics);

                results.push(index);
            });


            // Based on the jaccard index and our cutoff, compute if the FR and NFR are related
            let r1 = results[0] > SIMILARITY_CUTOFF ? 1 : 0;
            let r2 = results[1] > SIMILARITY_CUTOFF ? 1 : 0;
            let r3 = results[2] > SIMILARITY_CUTOFF ? 1 : 0;

            outString += `${frData.id},${r1},${r2},${r3}\n`
        });

        // Get the filename
        let parts = path.split('/');
        let filename = parts[parts.length - 1];

        let outFilename = `trace-${filename}`;
        let outPath = `${OUTPUTS_FOLDER}${outFilename}`;

        // Write the entire result
        fs.writeFile(outPath, outString, (err) => {
            if (err) {
                console.error(err);
            } else {
                console.log(`Successfully saved output to ${outPath}`);
            }
        });
    });
});
```
__Updated Project Report__
* I will move away from testing educational and medical requirements documents to doing the same with software test cases.
* Here is an example of a test case:

    * Title: Login Page – Authenticate Successfully on gmail.com
    * Description: A registered user should be able to successfully login at gmail.com.
    * Precondition: the user must already be registered with an email address and password.
    * Assumption: a supported browser is being used.

* I will also be using and researching more the __NLTK__ and how that all ties back into Requirements Engineering.
* Here are some of the starting steps of downloading NLTK as well its applications,
__NLTK Documentation__: https://www.nltk.org/
###### NLTK Installation Steps
* Once you have Python installed, download and install NLTK:
```sh
pip install nltk
```
* Then install NLTK Data:
```sh
python -m nltk.downloader popular
```
* If you have lots of storage space and good bandwidth, you can also use ```python -m nltk.downloader all ```. See NLTK's installation page for help.
* There's also a user interface to select data to download, which you can start with the Python shell:
```sh
Python 3.8.2 ...
Type "help", ...

>>> import nltk
>>> nltk.download()
```
* ___Collocation refers to two (or more) words that tend to appear frequently together. Collocations help in understanding text formation and aid in text search and similarity comparison.___
* The above can be used specfically for temporal or logistical requirements by combining keywords for parsing. The first part of the 2 code blocks deals with the __Preprocessing__ (___tokenization, de-stopwording, and de-punctuating___)
```sh
# Tokenize
from nltk.tokenize import word_tokenize
text = word_tokenize(text)

# Remove stopwords
from nltk.corpus import stopwords
stops = stopwords.words('english')
# print(stops)
words = [word for word in text if word not in stops]

# Remove punctuations
import string
punctuations = list(string.punctuation)
# print(punctuations)

words = [word for word in words if word not in punctuations]
print("Without punctuations:", words)

Preprocessed: ['The', 'Project', 'Gutenberg', 'EBook', 'Pride', 'Prejudice', 'Jane', 'Austen']
```
* Trigrams and Bi-grams could be used extensively once a bit of work is done. Example of a trigram (3 words that appear together) in NLTK is:
```sh
# Trigrams
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
trigram_collocation = TrigramCollocationFinder.from_words(text)
# Top 10 most occurring collocations
print("Trigrams:", trigram_collocation.nbest(TrigramAssocMeasures.likelihood_ratio, 10))
```
### In Conclusion:
* This is what style of test cases I would like to be able to output in my final deliverable
___Example Test Steps___:

   1. Navigate to gmail.com
   2. In the ’email’ field, enter the email address of the registered user.
   3. Click the ‘Next’ button.
   4. Enter the password of the registered user
   5. Click ‘Sign In’

* Expected Result: A page displaying the gmail user’s inbox should load, showing any new message at the top of the page.
