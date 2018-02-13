from validation import *
import bisect
import math
import sys


'''
	This method reads the single line in the itcont.txt file and returns False if the entry is invalid
	returns list of values if the entry is valid
'''
def read(line):
    line_array = line.split('|')     
    if(len(line_array) != 21): return False

    OTHER_ID = line_array[15]
    if(OTHER_ID != ''): return False


    TRANSACTION_DT = line_array[13]
    if not validDate(TRANSACTION_DT): return False
    transaction_year = TRANSACTION_DT[4:8] #in the challenge we need only the year, not any other part of the date

    CMTE_ID = line_array[0]
    if (CMTE_ID == ''): return False

    if(validZip(line_array[10]) == False): return False
    ZIP_CODE = line_array[10][0:5]

    transaction_amount_string = line_array[14]
    if(validAmount(transaction_amount_string) == False): return False
    TRANSACTION_AMT = float(transaction_amount_string)

    NAME = line_array[7]
    if(validName(NAME) == False): return False

    return (CMTE_ID, NAME, ZIP_CODE, transaction_year, TRANSACTION_AMT)


'''
	The main algorithm
'''

#I used dictionaries instead of arrays for hashing concerns



'''
	The dictionary where all the donors are stored
	key = (NAME, ZIP_CODE)
	value = None or 1, if the key does not exist it is 'None', otherwise it is 1 indicating that this donor has already donated
	                   and is in the dictionary. 
'''
all_donors = {}




'''
	The dictionary where all the repeat donors are stored
	key = (CMTE_ID, ZIP_CODE, transaction_year)   here TRANSACTION_DT has been truncated to just the year. 
	value = ( [array of all donations to this candidate from repeat donors], total sum of donations)
'''
repeat_donors = {}  #Repeat donors are stored in this dictionary

input_file = open(sys.argv[1], 'r')
percentile_file = open(sys.argv[2], 'r')
output_file = open(sys.argv[3], 'w')


PERCENTILE_string = percentile_file.read()
PERCENTILE_number = readPercentileString(PERCENTILE_string)/100.0


for line in input_file:
	value = read(line)
	if value == False:  #checks if the entry is valid, if it is not the loop continues. 
		continue
	
	CMTE_ID, NAME, ZIP_CODE, transaction_year, TRANSACTION_AMT = value
	multiple_donor = all_donors.get((NAME, ZIP_CODE))
	
	
	
	#first time donors are processed
	if multiple_donor == None:        #if there are no donors by this name and zip code, a new donor entry is created. 
		all_donors[(NAME, ZIP_CODE)] = 1
	
	#repeat donors are processed
	else:                             #if a donor entry exists, this means it is a repeat donor.                            
		repeat = repeat_donors.get((CMTE_ID, ZIP_CODE, transaction_year))
		if repeat == None:            #if no entry for this repeat donor exists, a new entry is created
			repeat_donors[(CMTE_ID, ZIP_CODE, transaction_year)] = [[TRANSACTION_AMT], TRANSACTION_AMT]
			
			output_file.write(CMTE_ID + '|' + ZIP_CODE + '|' + transaction_year + '|' + str(int(round(TRANSACTION_AMT))) + '|' + 
																							str(int(round(TRANSACTION_AMT))) + '|' + '1\n')
		
		else:
			'''
				donation_array = stores all donations from repeat donors with a given tuple = (CMTE_ID, ZIP_CODE, transaction_year)
				total_amount = sum of the donation array
			'''
			donation_array, total_amount = repeat_donors[(CMTE_ID, ZIP_CODE, transaction_year)]
			total_amount += TRANSACTION_AMT                  #total amount of money donated is increased by the next donation
			
			bisect.insort(donation_array, TRANSACTION_AMT)      #a new value is inserted and the array is sorted again. 
			repeat_donors[(CMTE_ID, ZIP_CODE, transaction_year)] = [donation_array, total_amount]
			
			percentile =  donation_array[int(math.ceil(PERCENTILE_number*len(donation_array))) - 1]  #percentile value is calculated 
			output_file.write(CMTE_ID + '|' + ZIP_CODE + '|' + transaction_year + '|' + str(int(round(percentile))) + '|' +  
																			str(int(round(total_amount))) + '|' +  str(len(donation_array)) + '\n')
input_file.close()
output_file.close()


