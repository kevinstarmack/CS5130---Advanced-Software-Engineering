# Final Report

## Introduction 
* Tell us the problem you are addressing:
	* Requirements are defined as the needs and desires of the stakeholder. Requirements Engineering is the process of defining, documenting, and maintaining requirements in the engineering design process. It is a common role in both systems engineering and software engineering.
	* The problem I am addressing is the ambiguity of temporal requirements in software engineering, how they are important, and well as generating test cases for them
* Why is the problem important?
	* Temporal Software Requirements are very key in the field of not only Requirements Engineering but also in Software Engineering. Temporal Requirements are usually the most important from a schedule standpoint in the development process

* __Basic Research Questions__
	1. Can text classification and part of speech tagging be the key to bridging the gap between formal and natural languages?
	2. Is it possible to implement this in an automated fashion?
	3. How difficult will it be generating test cases for temporal requirements?

## Motivation 
* Tell us the motivation of your approach/study:
	* I chose to pick this topic because it is very relevant in the field of Requirements Engineering, a field of Computer Science I discovered this year and found very interesting
	* My primary motivation stems from curiosity in the subject of requirements engineering, and the lack of literature and hard data to back up exactly what I was exploring.
* Limitations of existing work
	* Existing work is inconclusive if there is actually a good way of determining temporal logic or not. There has been 1 paper about creating test cases through temporal logic, however it was a research paper with no public repository of code. I wanted to see if I could imitate their results. The paper explores the __TestMEReq__ tool. I will be showing this during my project.
	
## Background  
* Technical background needed to understand your approach:
	* A background in Natural Language Processing (NLP), knowledge of text classifiers, machine learning as well as terminology used in the field of Requirements Engineering
	* In the initial stages of development, I was using the Jupyter notebook alongside Python to create a classifier. Jupyter was new to me.
	* In my final approach to attempting to solve the problem, I used a software called "Node-RED." It did a lot of the work for me, however it required a switch-up in which programming language I used, shifiting from Python to JavaScript
	* It would be helpful to know what Node-RED is before looking at my actual implementation. Node-RED is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices, APIs and online services as part of the Internet of Things. It is very user friendly.
	* Node-RED provides a web browser-based flow editor, which can be used to create JavaScript functions. Elements of applications can be saved or shared for re-use. The runtime is built on Node.js. The flows created in Node-RED are stored using JSON.
	* From a technological standpoint, to emulate my project, one needs a background in either Python or JavaScript. Initially I was going to use Python, but instead opted to use JavaScript.
	* Other background needed would be: the knowledge of Part of Speech tagging (POS tagging) and its correlation to Temporal Requirements, knowing what a test case is, and how to generate a test case based off of a requirement, temporal or non-temporal
	
## Approach 
* Overview, detailed technical material, examples, implementation
	* There was a lot of manual work done for this project. Such as manually determining which requirements are temporal or not based so that I could generate the proper training data for a supervised learning algorithm.
	* I wanted to use a large dataset of circa 100 requirements and have the classifier determine which were temporal and which were not.
	* I had began implementing an iPython notebook classifier using a neural network, as I thought this was my best bet
	* Part of Speech tagging and creating a dictionary would be a large step in aiding said classifier
	* It is also very important to know what a test case is and what features determine whether a requirement can be tested.
	* Another approach was to create an Excel sheet from these ~100 phrases that show us the pre-processing: Stemmed and stop word removal and removed punctuations First 200 words + 200 pos tags. From there the iPython notebook classifier can be used.
	* The contents of the excel sheet showed: The word frequency and PoS tags of the 111 requirements listed under the folder 'Requirements Documents' of the main branch. This was required to be done before any classification could be done
	* Ideally, this would have lead to an output that leads to ideal training data
	* For the sake of having a deliverable, I was forced to use Node-RED for an easy to demonstrate execution of my ideal results
	* Final implementation of the demo software itself was via Node-RED.
.
## Results
* Results and analysis of the results
	* The scale of the project is no where close to where I wanted it to be. Instead of having an ML solution, I had to create a makeshift application to try and display what I wanted to convey. However I believe I have laid good groundwork in an area that previously did not much physical work into itself. It is only able to process 1 requirement at a time with via a .txt file-input.
* Insights and take-home messages
	* The largest takeaway was to pick your battles and don’t jump around from idea to idea too much in a short term development process.
	* Although this was a largly test-case application project, there is a lot of work to do when working with NLP. It is best to only try to tackle 1 thing at a time versus attempting to try 2 things at once
	
## Limitations 
* Technical limitations 
	* Technical limitations were large, in the fact that this is still a theoretical topic without much documentation to back it up. I wanted to have a challenge. I lacked the proper background knowledge going into the project.
* What you should have done if you had more time
	* If I had more time (perhaps another semester), I would have liked to be able to test out other software or read other papers. Most importantly, I would want to have a trained classifier

* __Basic Research Questions - Answered__
	1. Can text classification and part of speech tagging be the key to bridging the gap between formal and natural languages?
		* Yes, it does appear that these 2 technologies can be used in conjunction in order to do so. Based off of studying and learning the subject, it is very possible.
	2. Is it possible to implement this in an automated fashion?
		* Papers have shown that automated Requirements tools are possible, and I was close to implementing a classifier for specifically temporal requirements. I believe with more time and study this could have been achieved.
	3. How difficult will it be generating test cases for temporal requirements?
		* This part was difficult for me. In fact I was not really able to make much headway on that as I was very pre-occupied with the text classifier aspect of the project.
	
## Discussion 
* Future work
	* If I were to continue this in the future, I would still like to try to use Node-RED, as it is a very friendly tool as well as supporting npm packages with documentation as to how to create and train a classifier, which would therefore allow for scalability in the project. After all, a few weeks messing with Pandas, and I should have a good grasp on it. I simply ran out of time to find a proper solution. However perhaps that is not the best method of going about this. I could also create a classifier in Python that could just as easily do the trick.

* What have you learned from the project?
* As I said before: __The largest takeaway was to pick your battles and don’t jump around from idea to idea too much in a short term development process.__
	* I was never really given a foothold or a good place to start. I hit a lot of dead ends. This has happened in industry to myself and colleagues working in R&D projects.
	* However, through this project, I have learned a lot about different software tools in ML.
	* The intertwining of NLP and ML cannot be understressed. Without ML, there wouldn't be NLP. ML is the true workhorse of the modern computing age. 
