import csv

list = [] #dictinct value of the column
File_Data = open('langu.csv', 'r') # To read our csv file data
Data = File_Data.readlines()
#used this for language,genre
for line in Data: # To segregate data

	item = line.split(",")
	for eachitem in item:
		eachitem = eachitem.replace('"','')
		eachitem = eachitem.replace('\n','')

		if eachitem in list :
			continue

		else : #Add distinct values to the list
			if len(eachitem) > 0  :
				list.append(eachitem)
				#print(eachitem)
				#print(len(list))

i = 1
#used this for languagerel,genrerel
for line in Data : # To segregate data

	item = line.split(",")

	for eachitem in item:
		eachitem = eachitem.replace('"','')
		eachitem = eachitem.replace('\n','')
		if len(eachitem)==0:
			itemid = ""
		else:
			itemid = list.index(eachitem) + 1
		
		#print(i, itemid)

	i +=1