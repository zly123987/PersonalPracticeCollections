import csv,math,json

#Non-lemmatization
def similarity(str1,str2):
	str1 = str1.split()
	str2 = str2.split()
	#remove duplicate
	set1 = list(set(str1))
	set2 = list(set(str2))
	
	#dict with word frequency
	dict1 = dict()
	dict2 = dict()
	for i in set1:
		dict1[i] = str1.count(i)
	for i in set2:
		dict2[i] = str2.count(i)
	
	#L2 normalize
	sum= 0
	for i in set1:
		sum = sum + dict1[i]*dict1[i]
	L2_1 = math.sqrt(sum)
	for i in set1:
		dict1[i]=dict1[i]/L2_1
	
	sum= 0
	for i in set2:
		sum = sum + dict2[i]*dict2[i]
	L2_2 = math.sqrt(sum)
	for i in set2:
		dict2[i]=dict2[i]/L2_2
	

	
	#cosine calculate
	sum=0
	for i in set1:
		for j in set2:
			if i==j:
				sum=sum+dict1[i]*dict2[j]
	return sum



	
with open('IdNotFound.csv','w+') as fw: 
	notfoundlist = csv.writer(fw,delimiter=',',lineterminator = '\n')
	
	
	y=list()
	x=list()
	threshold = 0.9
	step =1
	buf=0
	while threshold<=1:
		notfound = list()
		with open('javascript_bugs.csv','r') as f1:
			bugs = f1.read().split('\n')
			bug = csv.reader(bugs,delimiter=",")
			for row in bug:
				
				flag = 0
				with open('javascript_bugs2.csv','r') as f2:
					dbs = f2.read().split('\n')
					db = csv.reader(dbs,delimiter=",")
					for row2 in db:
						try:
							if row[1] ==row2[0]:
								if buf!=row2[4]:
							
									if similarity(row[2],row2[4])>threshold:
										
										flag =1
										break
									buf = row2[4]
							
								
								
						except Exception as e:
							pass
							
				if flag ==0 and len(row)>0:
					notfound.append(row[0])
		
	
	
