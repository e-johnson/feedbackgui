This repository contains the sample code for extracting feedback metrics based on our most recent paper given data from IAGO. To run this code, you will need: 
1. Python 2.7
2. PyQt4 (should come with QT designer) 
3. matplotlib. 

You should be able to download and install required packages using python's pip. PyQT provides an easy to use tool for designing GUIs. PyQT designs can be imported into Python as objects with methods to import data. 

Here are some tutorial for designing interfaces using QT designer: 
1. http://www.cs.usfca.edu/~afedosov/qttut/
2. https://pythonspot.com/en/pyqt4-gui-tutorial/
3. https://pythonspot.com/en/pyqt4/

To do List: 
To this point, I have been able to create a gui based on the data from Iago that displays feedback using the metrics from our most recent AAMAS paper.The sample code is provided. Moving forward, we would like to provide feedback based on the conflict resolution agent. This requires extracting offer data from the user and agent. In order to captere the offer data from CRA, we will need two buttons on the wizard inteface which allows the wizard to log user offers and rejections.

We also need to output the data from CRA after each negotiation and write a script that processes the data and provide feedback based on how well the user did. The goal is to, first, determine how well the participants understands the agent's preferences before providing feedback. You can look at my example for more detail. 


