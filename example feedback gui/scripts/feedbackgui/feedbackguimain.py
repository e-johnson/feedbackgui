from PyQt4.uic import loadUiType

from matplotlib.figure import Figure
import csv 
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas)
Ui_MainWindow, QMainWindow = loadUiType('mainwindow.ui')

class Main(QMainWindow, Ui_MainWindow):
		def __init__(self, ):
				super(Main, self).__init__()
				self.setupUi(self)

 		def addconcession(self, fig):
				self.canvas = FigureCanvas(fig)
				self.concess.addWidget(self.canvas)
				self.canvas.draw()

		def addknowledge(self, fig):
				self.canvas = FigureCanvas(fig)
				self.know.addWidget(self.canvas)
				self.canvas.draw()

		def addrejection(self, fig):
				self.canvas = FigureCanvas(fig)
				self.reject.addWidget(self.canvas)
 				self.canvas.draw()

 		def addtext(self, text):
 				#self.browser = QTextBroswer()
 				self.textBrowser.append(text)

if __name__ == '__main__':

	import sys
	from PyQt4 import QtGui
	participant_filepath = '../../data/iagostudystat.csv'


	def mergeconcessions(x1,x2,y1,y2): 
		print x1
		print y1
		print "seperate"
		print x2 
		print y2
		x1 = [int(i) for i in x1]
		x2 = [int(i) for i in x2]
		y1 = [int(i) for i in y1]
		y2 = [int(i) for i in y2]
		x1_new = [0]* ((len(x1)+ len(x2)) - 1 );
		x2_new = [0]* ((len(x1)+ len(x2)) - 1);
		y1_new = [0]* ((len(y1)+ len(y2)) - 1);
		y2_new = [0]* ((len(y1)+ len(y2)) - 1);
		output1 =[]
		#print "length of x1_new: %s x2_new: %s" % (len(x1_new), len(x2_new))
		if((len(x1) or len(x2)) < 1):
			return [[0],[0],[0],[0]]

		if(x2[0]< x1[0]): 
				x1_new[0] = x2[0]
				x2_new[0] = x2[0]
				y1_new[0] = 0
				y2_new[0] = y2[0]

		else: 
				x1_new[0] = x1[0]
				x2_new[0] = x1[0]
				y1_new[0] = y1[0]
				y2_new[0] = 0

		if(len(x1)> 1): 
				ix = 1
		else: 
				ix = 0

		if(len(x2)> 1): 
				jx = 1
		else: 
			jx = 0
		#print "length: x1:%s  x2: %s" % (x1, x2)
    

		#print "length of x1_new: %s " %len(x1_new)
		for i in range(1,((len(x1)+ len(x2) -1))):
		#		print "i: %s" %i
		#		print "jx: %s" % jx
		#		print "ix: %s" % ix
				if(i< (len(x1)+len(x2))-2):
						if(x1[ix]< x2[jx]):
								x1_new[i] = x1[ix]
								x2_new[i] = x1[ix]
								y1_new[i] = y1[ix]
								y2_new[i] = y2_new[jx -1]
								if (ix < (len(x1) -1 )):
										ix += 1
						elif(x2[jx]< x1[ix]):            
								x1_new[i] = x2[jx]
								x2_new[i] = x2[jx]
								y1_new[i] = y1_new[ix -1]
								y2_new[i] = y2[jx]
								if (jx < (len(x2) -1 )):
									jx += 1

						else: 

								x1_new[i] = x1[ix]
								x2_new[i] = x1[ix]
								y1_new[i] = y1[ix]
								y2_new[i] = y2[jx]
								if (ix < (len(x1) -1 )):
										ix += 1
								if (jx < (len(x2) -1 )):
										jx += 1
				else: 
						if(x1[ix]> x2[jx]):
								x1_new[i] = x1[ix]
								x2_new[i] = x1[ix]
								y1_new[i] = y1[ix]
								y2_new[i] = y2_new[jx -1]

						elif(x2[jx]> x1[ix]):            
								x1_new[i] = x2[jx]
								x2_new[i] = x2[jx]
								y1_new[i] = y1_new[ix -1]
								y2_new[i] = y2[jx]

						else: 

								x1_new[i] = x1[ix]
								x2_new[i] = x1[ix]
								y1_new[i] = y1[ix]
								y2_new[i] = y2[jx]

		output1.append(x1_new)
		output1.append(y1_new)
		output1.append(x2_new)
		output1.append(y2_new)
		output = [x1_new, y1_new, x2_new, y2_new]
		print "output: %s" %output1
		return output1 
	
	def feedback(data,id ): 
		duration = 0 
		avg_duration = 0.0
		total_participant_durations = 0.0
		avg_rejection = 0.0
		total_rejection = 0
		highest_initialcliam = 0
		lowest_initialclaim =100
		highest_userpoint= 0 
		claim_feedback_insert = ""
		output = []

		for x in data: 
			total_rejection =+ x[4]
			total_participant_durations =+ x[2]
			if (x[1] > highest_initialcliam): 
				highest_initialcliam = x[1]
			if ((x[1]) < lowest_initialclaim): 
				lowest_initialclaim = x[1]

			if (x[5] > highest_userpoint): 
				highest_userpoint = x[5]

		avg_duration = 354.23
		avg_rejection = 2
		found = 0
		iddata = ''
		for x in data: 
			if(x[0] == id): 
				iddata = x
				found = 1
				additionclaims = ""
				unclaimedvalue = x[8]
				unaskedquestionarray = x[9]
				unaskedquestion = ""
				for quest in unaskedquestionarray: 
					unaskedquestion = unaskedquestion +'\n'+ quest
				#print "unclaimedvalue: "
				#print unclaimedvalue
				#print unaskedquestionarray
				if(int(unclaimedvalue[0]) > 0):
					additionclaims  = additionclaims + "up to %s more shipments of spices," %unclaimedvalue[0]
				if(int(unclaimedvalue[1]) > 0):
					additionclaims  = additionclaims + "%s more shipments of bananass, " %unclaimedvalue[1]
				if(int(unclaimedvalue[2]) > 0):
					additionclaims  = additionclaims + "%s more bars of gold, " %unclaimedvalue[2]
				if(int(unclaimedvalue[3]) > 0):
					additionclaims  = additionclaims + " or %s more bars of iron" %unclaimedvalue[3]

				if (x[1] > 56): 
					claim_feedback_insert  = " a very high offer. worth %d out of 70 total points. That's a good start. To claim more value you could have asked for %s"%(x[1], additionclaims)
				elif(x[1]< 56 and x[1]> 28): 
					claim_feedback_insert  = " an average offer worth %d out of 70 total points. You should try to claim more value in the negotiation. To claim more value you could have asked for %s"%(x[1], additionclaims)
				else: 
					claim_feedback_insert  = " a very low offer. worth %d out of 70 total points.\n You need to review your strategy and make sure to claim more value in the negotiation. To claim more value you could have asked for %s"%(x[1], additionclaims)

				if(x[2] > (1.20 * avg_duration)):
					agreement_time_insert = " was much longer than most people"
				elif (x[2] < (1.20 * avg_duration) and x[2] > (.80 * avg_duration)):
					agreement_time_insert = " was close to the time most users negotiated"
				else: 
					agreement_time_insert = " was much shorter than most negotiation"

				if(x[4] > 3):
					rejection_feedback_insert = " That's a good strategy"
				else: 
					rejection_feedback_insert = " You may be accepting offers to early"

				initial_claim_feedback =" Initial Claim: \nYou began the negotiation with %s . Remember, the more you claim initially in a negotiation, the more likely you are to get what you want "%(claim_feedback_insert)
				agreement_time_feedback = " Length of Negotiation: \nThe length of your negotiation %s. You negotiated for %s seconds and the average is %d seconds. "%( agreement_time_insert, x[2], avg_duration)

				questionsasked_feedback = "Questions Asked: \nYou asked %d questions about your opponent's preference. Asking questions is vital because it helps you understand what your opponent wants.  In order to learn more about your opponent's preference, here are a few question(s) you could have asked:  %s"%(x[3], unaskedquestion)

				rejection_feedback = "Rejections: \nYou rejected %d of the agent's offers. %s. Rejection usually shows your opponent that you not are willing to accept subpar offers " %(x[4], rejection_feedback_insert)

				#print iddata
				#print initial_claim_feedback
				#print "\n"
				#print agreement_time_feedback
				#print "\n"
				#print questionsasked_feedback
				#print "\n"
				#print rejection_feedback

				# Pie chart
				labels = 'Asked', 'Unasked'

				objects = ('You', 'Avg')
				print "rejections: %d" % x[3]
				objvale =[x[4], avg_rejection]
				#print "average rejection %f" %avg_rejection
				val = ('Rej offers', 'total rej offers')
				y_pos = [0,1]
				sizes = [iddata[3], 13 - iddata[3] ]
				explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
				concessions = x[6]
				#print "time: concession value" 
				#x[7].append(x[1])
				#x[6].append(x[5])
				#fig1, ax1 = plt.subplots(2,2)
				fig1 = Figure()
				axarr = fig1.add_subplot(111)
				axarr.set_title('Concession Curve')
				axarr.set_xlabel('Time(sec)')
				axarr.set_ylabel('Points Claimed')
				#plotvalues = mergeconcessions(x[7],x[11], x[6], x[10])
				x1 = x[7]
				x2 = x[11]
				y1 = x[6]
				y2 = x[10]


				if (x1[-1] > x2[-1]): 
					x2.append(x1[-1])
					y2.append(y2[-1])

				if (x1[-1] < x2[-1]): 
					x1.append(x2[-1])
					y1.append(y1[-1])
					

				axarr.plot(x1, y1, 'bs-', x2, y2, 'rd-')
				axarr.legend(('User', 'Agent'),
           loc='upper left', shadow=True)
				
				colors = ['green', 'orangered']
				fig2 = Figure()
				axarr1 = fig2.add_subplot(111)
				axarr1.pie(sizes, explode=explode, labels=labels,colors = colors, autopct='%1.1f%%', shadow=True, startangle=90)
				axarr1.set_title('Percentage of total questions asked')


				fig3 = Figure()
				axarr2 = fig3.add_subplot(111)
				axarr2.barh(y_pos, objvale, align='center', alpha=0.5)
				axarr2.set_yticks(y_pos)
				axarr2.set_yticklabels( objects)
				axarr2.set_title('Your Rejected Offer vs Avg Rejected offers')
				axarr2.set_xlabel('Number of Rejected Offers')
				fig1.set_tight_layout(True)
				fig2.tight_layout(pad = 2)
				fig3.tight_layout(pad =2)
				output.append(fig1)
				output.append(fig2)
				output.append(fig3)
				output.append(initial_claim_feedback)
				output.append(agreement_time_feedback)
				output.append(questionsasked_feedback)
				output.append(rejection_feedback)



			else: 
				continue
		if (found ==0):
			print(" Participant not Found")
		return output

	
		 
	def convertcsv_to_listofparticipant(csv_f): 
		participants_data = []
		for row in csv_f:
			participants_data.append([int(row[0]),int(row[1]), int(row[2]), int(row[3]), int(row[4]),int(row[5]), list(row[6].split('-')),list(row[7].split('-')), list(row[8].split('-')), list(row[9].split('-')), list(row[10].split('-')), list(row[11].split('-'))] )
		print "participant data: "
		print participants_data[4]
		return participants_data

	file = open( participant_filepath, 'rb') 
	readindata = csv.reader(file)

	participants_data = convertcsv_to_listofparticipant(readindata)

	output = feedback(participants_data, 3)



	

outputtedtext = output[3] + '\n\n' + output[4] + '\n\n' + output[5] + '\n\n' + output[6]
#print outputtedtext
app = QtGui.QApplication(sys.argv)
main = Main()
main.addconcession(output[0])
main.addknowledge(output[1])
main.addrejection(output[2])
main.addtext(outputtedtext)
main.show()
sys.exit(app.exec_())