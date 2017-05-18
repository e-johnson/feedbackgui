import csv


iago_data_file_path = '../data/iagostudy.txt'
iagostudystat = '../data/iagostudystat.csv'
iago_study_data = open(iago_data_file_path,'r')
participants_sessions =[]
potentialquestion = ['what do you like the most?', 
'what do you like the least?', 
'Do you like shipments of spices more than shipments of bananas?',
'Do you like shipments of spices more than bars of gold?',
'Do you like shipments of spices more than bars of iron?',
'Do you like shipments of bananas more than shipments of spices?',
'Do you like shipments of bananas more than bars of gold?',
'Do you like shipments of bananas more than bars of iron?',
'Do you like bars of gold more than shipments of bananas?',
'Do you like bars of gold more than shipments of spices?',
'Do you like bars of gold more than bars of iron?',
'Do you like bars of iron more than shipments of bananas?',
'Do you like bars of iron more than bars of gold?', 'do you like bars of iron more than shipments of spices?']

	
def main(): 
	#userid = input('Which user\'s feedback would you like? ')
	i = 1
	count = 0
	participant_file = open('participantmsg%s.txt'% i, 'w' );
	for x in iago_study_data:
		if 'From:	Johnathan Mell' in x:  


			#print x
			#print "yes: %s" %i 
			participantfile = open('../data/participantmsg%s.txt'% i , 'w')
			if count == 1:
				participants_sessions.append(participant_session)
			participant_session = []

			#participantfile.write(x)
			#participant_session.append(x)

			i = i +1
		else: 
			 
			#participantfile.write(x)
			y = str(x)
			y = y.replace('\n','')
			y = y.replace('\r', '')
			participant_session.append(y)
		count =+ 1
	outputted_userdat =[]
	#print participants_sessions[1]
	userid = 1

	for participant_session in participants_sessions: 
		
		initialclaim =0
		initialunclaimed = [] 
		agreementtime = 0 
		questions = 0 
		numofrej = 0 
		userpoints = 0

		madefirstoffer = 0
		currenttime = 0
		timedout = 0
		claims = []
		opponentclaims = []
		timeofclaim = []
		opponenttimeofclaim = []
		questionsasked = []
		for data in participant_session: 
			data = data.split(',')
			if (data[0].lower() == 'TIME'.lower()):
				currenttime = int(data[1])
			elif (data[0].lower() == 'SEND_OFFER'.lower()) and (int(data[2]) == 1) : 
				
				initial = data[3:]
				#print "initial"
				stringinitial = ''.join(initial)
				
				stringinitial = stringinitial.strip(" ")
				#print stringinitial
				#print 'values: 1: %s, 2: %s, 3: %s, 4: %s, ' %(stringinitial[7], stringinitial[15], stringinitial[23], stringinitial[31])
				if(madefirstoffer ==0): 
					initialclaim = 1 * int(stringinitial[7]) + 2 * int(stringinitial[15]) + 3 * int(stringinitial[23]) + 4 * int(stringinitial[31])
					initialunclaimed.append(5 - (int(stringinitial[7])))
					initialunclaimed.append(5 - (int(stringinitial[15])))
					initialunclaimed.append(5 - (int(stringinitial[23])))
					initialunclaimed.append(5 - (int(stringinitial[31])))


					claims.append(initialclaim)
					timeofclaim.append(currenttime)
				else:    
					claims.append(1 * int(stringinitial[7]) + 2 * int(stringinitial[15]) + 3 * int(stringinitial[23]) + 4 * int(stringinitial[31]) )
					timeofclaim.append(currenttime)
				madefirstoffer = 1
			elif(data[0].lower().startswith('A'.lower())): 
				if(data[4].lower() == 'true'.lower()): 
					timedout = 1
			
				userpoints = data[2]
				#questions = data[7]
				#userid = data[0]
			elif (data[0].lower() == 'SEND_OFFER'.lower()) and (int(data[2]) == 0) : 
				opponentoffer = data[3:]
				stringoffer = ''.join(opponentoffer)
				print "opponent offer: " 
				print stringoffer 
				opponentclaims.append(4 * int(stringoffer[3]) + 3 * int(stringoffer[11]) + 2 * int(stringoffer[19]) + 1 * int(stringoffer[27]) )
				opponenttimeofclaim.append(currenttime)
				


			elif(data[0].lower() == 'FORMAL_ACCEPT'.lower()) : 
				agreementtime = currenttime
			elif( ('SEND_MESSAGE' in data[0] )  and ((data[3] == '1' )or ('1' in data[2]))):
				print data[1]
				if('No' in data[1]): 
					print "yes this is it"
					numofrej = numofrej + 1
				#print "got here"
				#print data[1]
				#print data[2] 
				
				for question in potentialquestion: 

					if ((question.lower() == data[1].lower()) ):
						#print "userid: %s" %(userid)
						#print questionsasked
						if(question not in questionsasked): 
							#print " got here for: %s " %(userid)
							questions = questions + 1
							questionsasked.append(question)
							if question == potentialquestion[2]: 
								questionsasked.append(potentialquestion[5])
							if question == potentialquestion[3]:
								questionsasked.append(potentialquestion[9])
							if question == potentialquestion[4]:
								questionsasked.append(potentialquestion[13])
							if question == potentialquestion[5]:
								questionsasked.append(potentialquestion[2])
							if question == potentialquestion[6]:
								questionsasked.append(potentialquestion[8])
							if question == potentialquestion[7]:
								questionsasked.append(potentialquestion[11])
							if question == potentialquestion[8]:
								questionsasked.append(potentialquestion[6])
							if question == potentialquestion[9]:
								questionsasked.append(potentialquestion[3])
							if question in potentialquestion[10]:
								questionsasked.append(potentialquestion[12])
							if question == potentialquestion[11]:
								questionsasked.append(potentialquestion[5])
							if question == potentialquestion[12]:
								questionsasked.append(potentialquestion[10])
							if question == potentialquestion[13]:
								questionsasked.append(potentialquestion[4])
							
							
		
								
							#print "question val: %d" % questions 
						#print data[1]

			else: 
				#print data
				continue
		outputtedclaims = '- '.join(str(x) for x in claims)
		outputtedtimeofclaim = '- '.join(str(x) for x in timeofclaim)
		opponent_outputtedclaims = '- '.join(str(x) for x in opponentclaims)
		opponent_outputtedtimeofclaim = '- '.join(str(x) for x in opponenttimeofclaim)
		outputtedinitialunclaimed = '- '.join(str(x) for x in initialunclaimed)
		qset = set(potentialquestion) 
		askedset = set(questionsasked)
		unaskedset = qset - askedset
		unasked = list(unaskedset)
		#print "questions asked: "
		#print unasked
		outputtedunasked = '- '.join(str(x) for x in unasked)
		participantdata = [userid, int(initialclaim),int(agreementtime), int(questions), numofrej,int(userpoints), outputtedclaims , outputtedtimeofclaim, outputtedinitialunclaimed, outputtedunasked, opponent_outputtedclaims, opponent_outputtedtimeofclaim]
		if(timedout ==0) and (initialclaim != 'none'.lower()): 
			outputted_userdat.append(participantdata)
		userid +=1
	#print outputted_userdat
	myfile = open(iagostudystat, 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	#label = ['UserId', 'Intial Claim', 'Agreement Time', 'Questions', 'Num of Rejection', 'User Points', 'Claims', 'Time of Claim', 'initially unclaimed']
	#wr.writerow(label)
	for data in outputted_userdat: 
		wr.writerow(data)
	myfile.close()
	#print "claims"
	#print claims
	
	#feedback(outputted_userdat,1)



main()
