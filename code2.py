import csv

with open("allplatforms.csv", 'r') as File_Data : # To read our csv file data
	reader = csv.DictReader(File_Data) # To organize data easy for segregation
	for row in reader: # To segregate data
		id = row['ID']
		net = row['netflix']
		hulu = row['Hulu']
		prime = row['Prime Video']
		Disney = row['Disney+']
		net = net.replace('\n','')
		net=int(net)
		if(net==1):
			print(id,1) #for netflix the platform id is 1
		hulu = hulu.replace('\n','')
		hulu=int(hulu)
		if(hulu==1):
			print(id,2) #for hulu the platform id is 2
		prime = prime.replace('\n','')
		prime=int(prime)
		if(prime==1):
			print(id,3) #for prime the platform id is 3
		Disney = Disney.replace('\n','')
		Disney=int(Disney)
		if(Disney==1):
			print(id,4) #for Disney+ the platform id is 4
		

		