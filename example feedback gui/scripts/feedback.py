import csv 
import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure

participant_filepath = '../data/iagostudystat.csv'

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
			if (x[5] > 56): 
				claim_feedback_insert  = " a very high offer. worth %d out of 70 total points. \nThat's a good start. To claim more value you could have asked for %s"%(x[5], additionclaims)
			elif(x[5]< 56 and x[5]> 28): 
				claim_feedback_insert  = " an average offer worth %d out of 70 total points. \nYou should try to claim more value in the negotiation. \nTo claim more value you could have asked for %s"%(x[5], additionclaims)
			else: 
				claim_feedback_insert  = " a very low offer. worth %d out of 70 total points.\n You need to review your strategy and make sure to claim more value in the negotiation. To claim more value you could have asked for %s"%(x[5], additionclaims)

			if(x[2] > (1.20 * avg_duration)):
				agreement_time_insert = " was much longer than most people"
			elif (x[2] < (1.20 * avg_duration) and x[2] > (.80 * avg_duration)):
				agreement_time_insert = " was the length people typically negotiated"
			else: 
				agreement_time_insert = " was much shorter than most negotiation"

			if(x[4] > 3):
				rejection_feedback_insert = " That's a good strategy"
			else: 
				rejection_feedback_insert = " You may be accepting offers too early"

			initial_claim_feedback =" You began the negotiation with %s . \nRemember, the more you claim initially in a negotiation, the more likely you are to get what you want "%(claim_feedback_insert)
			agreement_time_feedback = "The length of your negotiation %s. \nYou negotiated for %s seconds and the average is %d seconds. "%( agreement_time_insert, x[1], avg_duration)

			questionsasked_feedback = "You asked %d questions about your opponent's preference. \nAsking questions is vital because it helps you understand what your opponent wants."%(x[3])

			rejection_feedback = "You rejected %d of the agent's offers. %s. \nRejection usually shows your opponent that you not are willing to accept subpar offers" %(x[4], rejection_feedback_insert)

			#print iddata
			print initial_claim_feedback
			print "\n"
			print agreement_time_feedback
			print "\n"
			print questionsasked_feedback
			print "\n"
			print rejection_feedback

			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'Asked Questions', 'Unasked Questions'

			objects = ['Rej offers', 'AvgNumOfReject']

			objvale =[x[3], avg_rejection]
			#print "average rejection %f" %avg_rejection
			y_pos = [0,1]
			sizes = [iddata[3], 10 - iddata[3] ]
			explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
			concessions = x[6]
			#print "time: concession value" 
			x[7].append(x[1])
			x[6].append(x[5])
			#fig1, ax1 = plt.subplots(2,2)
			fig1 = Figure()
			axarr = fig1.add_subplot(111)
			axarr.set_title('Concession Curve')
			axarr.set_xlabel('Time(sec)')
			axarr.set_ylabel('Points Claimed')
			axarr.plot(x[7], x[6])
			

			fig2 = Figure()
			axarr1 = fig2.add_subplot(111)
			axarr1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
			axarr1.set_title('Knowledge of Opponent\'s Preference')


			fig3 = Figure()
			axarr2 = fig3.add_subplot(111)
			axarr2.barh(y_pos, objvale, align='center', alpha=0.5)
			axarr2.set_yticklabels( objects)
			axarr2.set_title('Number of Rejection')
			axarr2.set_xlabel('Rejected Offers')
			output.append(fig1)
			output.append(fig2)
			output.append(fig3)
			output.append(initial_claim_feedback)
			output.append(agreement_time_feedback)
			output.append(questionsasked_feedback)
			output.append(rejection_feedback)

			#axarr[1, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
			#axarr[1, 1].set_title('Axis [1,1]')
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
			#plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
			#plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

			#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
			#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
			#plt.show()
			axarr.annotate('initial claim: (%s)'%x[1], xy=(190, x[1]), xytext=(190-60, x[1]+1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ) 
			#plt.tight_layout()
			#plt.show()

		else: 
			continue
	if (found ==0):
		print(" Participant not Found")
	return output

def start(): 
	participants_data = []
	file = open( participant_filepath, 'rb') 
	csv_f = csv.reader(file)
	print csv_f

	for row in csv_f:
		participants_data.append([int(row[0]),int(row[1]), int(row[2]), int(row[3]), int(row[4]),int(row[5]), list(row[6].split('-')),list(row[7].split('-'))] )
		print row 
		feedback(participants_data, 4)



start() 