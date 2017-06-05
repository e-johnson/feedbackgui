This repository contains the code for extracting feedback metrics based on our most recent paper(provided in the repository)given data from IAGO. To run this code, you will need: 
1. Python 2.7
2. PyQt4 (should come with QT designer) 
3. matplotlib. 

You should be able to download and install required packages using python's pip. PyQT provides an easy to use tool for designing GUIs. PyQT designs can be imported into Python as objects with methods to import data. 

To run the code, navigate to the examplefeedbackgui/scripts/feedbackgui and run the feedbackguimain.py script. 

Here are some tutorial for designing interfaces using QT designer: 
1. http://www.cs.usfca.edu/~afedosov/qttut/
2. https://pythonspot.com/en/pyqt4-gui-tutorial/
3. https://pythonspot.com/en/pyqt4/

To do List: 
To this point, I have been able to create a gui based on the data from Iago.  Moving forward, we would like to provide feedback based on data from the conflict resolution agentd. This requires extracting offer data from the user and agent. In order to captere the offer data,  we will need two buttons on the wizard inteface which allows the wizard to log user and agent offers .

We also need to output the data from CRA after each negotiation,  processes that data and provide feedback based on how well the user did. The goal is to, first, determine how well the participants understood the agent's preferences before providing feedback. You can look at my example for more detail. 


