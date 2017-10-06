"""
Combines all data entries from the same year 
	into a single csv file for future data processing.
"""


import os, xlrd, csv
from time import gmtime, strftime

# converts xlsx file into csv file and rename
def excel_to_csv(sheet_path, sheet_name, path_csv):
    workbook = xlrd.open_workbook(sheet_path + sheet_name)
    # sh = wb.sheet_by_name(sheet_name)
    sheet = workbook.sheet_by_index(0)

    csv_file = open(path_csv + sheet_name + '.csv', 'wb')
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sheet.nrows):
        writer.writerow(sheet.row_values(rownum))

    csv_file.close()

"""
adapted from 
https://stackoverflow.com/questions/20105118/
convert-xlsx-to-csv-correctly-using-python
"""

# combines csv files containing data from teh same year into one file and rename
def combineCsvs(path, from_year, to_year):
	print "Combining..."
	os.chdir(path) 		#change directory to the csv files' folder
	csv_name = str(from_year)+"-"+str(to_year)+" "+strftime("%m-%d %H:%M:%S", gmtime())
	output_file = open(path + csv_name + '.csv', 'a')

	for fn in os.listdir('.'):
		if (os.path.isfile(fn) & (fn != ".DS_Store") 
			& ((("EUAS " + str(from_year)) in fn) or (("EUAS " + str(to_year))) in fn)):
			print (fn)
			for line in open(fn):
				output_file.write(line)
	output_file.close()



#puts all csv files of certain years into the same folder
def integrate(from_year, to_year, in_path, out_path):
	print "integrating..."
	for year in xrange(from_year, to_year+1):
		tail_path = "EUAS " + str(year) + "/"  		# "EUAS 2003/"
		path = in_path + tail_path
		os.chdir(path) 		# change directory to certain year
		for fn in os.listdir('.'):
			if os.path.isfile(fn) & (fn != ".DS_Store"):
				print (fn)
				excel_to_csv(path, fn, out_path)



#____________________________________



in_path = "/Users/darcy/Desktop/WaterViz/EUAS/"
out_path = "/Users/darcy/Desktop/WaterViz/EUASCsv/"
final_path = out_path


# testing
# path_sheet_data_folder = "/Users/darcy/Desktop/WaterViz/EUAS/EUAS 2003/"
# path_project = "/Users/darcy/Desktop/WaterViz/"
# test_sheet_name = "Region 1 EUAS 2003"


# excel_to_csv(path_sheet_data_folder, test_sheet_name, path_csv_data_folder)



# shortcut of processing multiple years
def integrateDatabase(from_year, to_year, in_path, out_path, final_path):
	integrate(from_year, to_year, in_path, out_path)
	combineCsvs(final_path, from_year, to_year)


# integrateDatabase(2003, 2003, in_path, out_path, final_path)


def main():
	#integrate(2003, 2016, in_path, out_path) 
	for year in xrange(2003, 2016+1):
		print "Combining data from year " + str(year) 
		combineCsvs(final_path, year, year)





main()



# def path_leaf(path):
#     head, tail = ntpath.split(path)
#     return tail or ntpath.basename(head)
# https://stackoverflow.com/questions/8384737/
# extract-file-name-from-path-no-matter-what-the-os-path-format














