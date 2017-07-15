import datetime

today=datetime.date.today()

target=today+datetime.timedelta(days=7)

bday={'Bavs':'13-07-17','Okvya':'15-07-17','ishu':'14-07-17','divs':'14-02-17','rams':'20-07-17','shans':'28-07-17',
'ragz':'09-07-17','dp':'18-07-17','neha':'20-07-17','Poori':'03-02-17'}

flag=0

for i,j in bday.items():

	j=datetime.datetime.strptime(j, '%d-%m-%y').date()	
	
if j>=today and j<=target:
		
	print i+" birthday is on "+str(j)
		
	flag=1

if flag==0:
	
	print("No birthday in this week")

