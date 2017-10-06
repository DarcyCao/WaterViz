import csv
import textract
import copy
from random import randint



def importData(path):
	with open(path, 'rb') as csvfile:
	    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
	    index = 0;
	    for row in reader:
	    	print row
	    	#if row[1] != '':
	    	#splited =  row[0].split('. ')
	    	#print len(splited)
	    	#first.append(splited[0])
	    	#print splited[0]
	    	#print splited[1]
	    	#titles[splited[1]] = index
	    	#index+=1

	return 1


def importBase(path, titles):
	text = textract.process(path)
	splited = text.split('\n')
	set_base = set()
	for i in splited:
		set_base.add(i)
	#print len(set_base)
	print "------------------------splited------------------------"
	crosses = copy.deepcopy(titles)
	for title in titles:
		#print item
		# print type(set_splited)
		crosses[title] = -1
		for sentence in set_base:
			#print sentence
			#print title
			if title in sentence:
				print "Ha!"
				crosses[title] = titles[title]
				break



	#print crosses
	return crosses




def writeToNewFile(crosses): #convert dictionary data to csv
    path = '/Users/darcy/Downloads/' + str("crosses") + str(randint(0, 9))+'.csv'
    with open(path, 'w+') as csvfile:
        #print (resultList)
        for item in crosses:
        	new = [item, crosses[item]]
            	writer = csv.writer(csvfile, delimiter=',')
            	writer.writerow(new)
    return








#data source: http://data.unhcr.org/syrianrefugees/regional.php
def main():
	date, total, dire = importData(path)
	date, timeTotal, timeDire = cleanData(date, total, dire)






path_sheet_data_folder = "/Users/darcy/Desktop/WaterViz/EUAS/"
path_csv_data_folder = "/Users/darcy/Desktop/WaterViz/EUASCsv/"

path_project = "/Users/darcy/Desktop/WaterViz/"



importData("/Users/darcy/Desktop/WaterViz/EUAS/EUAS 2016/Region 1 EUAS 2016.xlsx")



# c = importBase(path1, s)
# writeToNewFile(c)
# writeToNewFile(s)
#main()





'''

Process:
[0] conversing all xlsx diles into csv and rename for better future reference
[1] reference different data folders in a single program
[2] filter out the buildings without water data entries
[3] write different functions of organizing the filtered data
	[3.1] for each building, data entry according to time from 2003 to 2016
	[3.2] for each year, all the buildings with all their data
	[3.3] for each state, all the buildings and all the data



final data stucture:

(building properties)
building id,
the state the building is in,
sqft,

(building data)
Time (month since October, year)
electricity * 2,
gas * 2,
water * 2,

(objective data)
Monthly average temperatures across the US 

Organize the data according to each building, put together all the data for each building

JSON file??? Is it a good idea?







'''









# s1 = "Daylighting Impacts on Retail Sales Performance. Journal of the Illuminating Engineering Society, 31:2, pp. 21-25."






# s2 = "(2002) Daylighting Impacts on Retail Sales Performance"

# print (s2 in s1)