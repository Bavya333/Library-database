m=[{'Name':'Bavya','ID':3,'Visit count':0},
{'Name':'kaya','ID':1,'Visit count':0},
{'Name':'Divya','ID':5,'Visit count':0},
{'Name':'Ramya','ID':7,'Visit count':0},
{'Name':'Sandhya','ID':11,'Visit count':0},
{'Name':'Ishu','ID':13,'Visit count':0},
{'Name':'Diya','ID':33,'Visit count':0},
{'Name':'Shanthi','ID':43,'Visit count':0},
{'Name':'Mayoora','ID':34,'Visit count':0}]

print("Enter -1 to exit and 5 to enter:")

a=raw_input("hh")


while int(a)==5:
	
 print("Enter your ID:")

	id=input()
	
flag=1
	
for i in m:
		
	if id==i['ID']:
			
		i['Visit count']+=1
			
		print i
			
		flag=0
                      
	  	break
        	
		
	
	if flag==1:
		
		print("Your good name:")
		
		nam=raw_input()
		
		m=m+[{'Name':nam,'ID':id,'Visit count':1}]
   		
		print("Database updated")
	
		print("Enter 5...exit -1:")
	
		a=raw_input()

for i in m:
   
   	print i








