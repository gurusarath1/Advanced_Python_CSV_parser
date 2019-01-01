# Created by Guru Sarath
# January 1 2019


import csv

'''
Use the parseCSV function in your code as shown in the example

file - File reference to the CSV file
CSV_ContainsHeader - if this flag is set to true, the first record of the CSV is treated as Header (all the data in first row will be treated as string)
DataTypeFrame - List containging the datatype of the columns in the csv file ()same order as the CSV flie
'''


class parsed_CSV:

	# Row 1 of the CSV file (if the CSV contains Header section)
	Header = None # List of column names

	# All the records of the CSV file
	parsed_CSV_records = None

	def __init__(self, DataTypeFrame = None, CSV_ContainsHeader = False, delimiterCSV = ',', Header= None, parsed_CSV_records = None):
		self.CSV_ContainsHeader = CSV_ContainsHeader
		self.delimiterCSV = delimiterCSV
		self.Header = Header
		self.parsed_CSV_records = parsed_CSV_records
		self.DataTypeFrame = DataTypeFrame

	# Returns a record from the CSV file (key th row)
	def __getitem__(self, key):
		return self.parsed_CSV_records[key]


def parseCSV(file, DataTypeFrame = None, CSV_ContainsHeader =  False, delimiterCSV = ','):

	with file as FP:
		Allrows = csv.reader(FP, delimiter = delimiterCSV)

		Final = []
		Header = []
		rowNum = 0
		for row in Allrows:

			i = 0

			if not CSV_ContainsHeader:
				row_reformatted = []
			else:
				row_reformatted = {}

			for element in row:

				# if the CSV contains column names (Row 0)
				# OR
				# Data types of the columns is not mentioned
				if (CSV_ContainsHeader and rowNum == 0) or not DataTypeFrame:
					dataTypeX = str

					if rowNum == 0:
						Header.append(dataTypeX(element).strip())
					else:
						row_reformatted.append(dataTypeX(element).strip())

				# if CSV_ContainsHeader store each record in a dictionary form
				elif CSV_ContainsHeader:
					dataTypeX = DataTypeFrame[i]
					if dataTypeX == str:
						row_reformatted[Header[i]] = dataTypeX(element).strip()
					else:
						row_reformatted[Header[i]] = dataTypeX(element)
				
				# if not CSV_ContainsHeader store each record in a list form
				else:
					dataTypeX = DataTypeFrame[i]

					if dataTypeX == str:
						row_reformatted.append(dataTypeX(element).strip())
					else:
						row_reformatted.append(dataTypeX(element))
				
				i += 1

			if Header and rowNum == 0:
				#Final.append(Header)
				pass
			else:
				Final.append(row_reformatted)

			rowNum += 1

		parsed_CSV_OBJECT = parsed_CSV(DataTypeFrame, CSV_ContainsHeader, delimiterCSV, Header, Final)

		#return Final
		return parsed_CSV_OBJECT
				


if __name__ == '__main__':

	fileP = open('Sample.csv', 'r')
	CSVFile = parseCSV(fileP, DataTypeFrame = [str,str,str,float, int, str], CSV_ContainsHeader = True)
	print(CSVFile, '\n')


	# Accessing elements of the CSV file when the CSV has a header:
	print(CSVFile[0]['First Name'], CSVFile[1]['Salary'])
	print('CSV Header - ', CSVFile.Header)
	print('CSV Records - ', CSVFile.parsed_CSV_records, '\n\n\n')


	print('--------------------------------------------------------------------------------------------------')

	fileP = open('Sample_2.csv', 'r')
	CSVFile = parseCSV(fileP, DataTypeFrame = [str,str,str,float, int, str], CSV_ContainsHeader = False)
	print(CSVFile, '\n')

	# Accessing elements of the CSV file when CSV does not have a header:
	print(CSVFile[1][0], CSVFile[1][4])
	print('CSV Header - ', CSVFile.Header)
	print('CSV Records - ', CSVFile.parsed_CSV_records, '\n\n\n')

	print('--------------------------------------------------------------------------------------------------')

	fileP = open('Sample_3.csv', 'r')
	CSVFile = parseCSV(fileP, CSV_ContainsHeader = False)
	print(CSVFile, '\n')

	# Accessing elements of the CSV file when CSV does not have a header and No data type mentioned:
	print(CSVFile[1][0], CSVFile[1][1])
	print('CSV Header - ', CSVFile.Header)
	print('CSV Records - ', CSVFile.parsed_CSV_records, '\n\n\n')