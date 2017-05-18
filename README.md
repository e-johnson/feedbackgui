This repository contains the code to run the feedback gui. To run this code, you willneed: 
1. Python 2.7
2. PyQt 4 ( should come with QT designer) 
3. matplotlib. 

Through these pacages, you should be able to run the eample code as well as create graphic user interfaces using python and the QT designer tool 

Here are some tutorial for designing interfaces using QT designer: 
1. http://www.cs.usfca.edu/~afedosov/qttut/
2. https://pythonspot.com/en/pyqt4-gui-tutorial/
3. https://pythonspot.com/en/pyqt4/

To do List; 
To this point, I have been able to create a gui based on the data from Iago that displays feedback using the metrics from our most recent AAMAS paper
this example code is provided. moving forward, we would ike to do the same based on the conflict resolution agent. In order to captere the offer data from CRA, we will need two buttons on the wizard inteface which allows the wizard to log when ever the user makes an offer. We also need to output the data from the wizard and write the script which takes the CRA data, process it and display based on how well participants understand the agent's preference. The goal is to first determine how well the participants understand what the agent wants before providing feedback. You can look at my example for more detail. 
