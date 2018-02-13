import datetime

CURRENT_YEAR = datetime.datetime.now().year  #get the current year

'''
	Method checks whether zip code is valid
'''
def validZip(zip_code):
    if (zip_code == ''): return False
    if (len(zip_code) != 5 and len(zip_code) != 9): return False
    if (zip_code.isdigit() == False): return False
    return True

'''
    Method checks whether the date field is valid. MMDDYYYY = valid field date.
    It is assumed that the year cannot be greater then current year + 1
    It is assumed that the year cannot be less then 1975, that is when the standards began. 
'''
def validDate(date):
    if (date == ''): return False
    if (len(date) != 8): return False
    if (date.isdigit() == False): return False

    year = int(date[4:8])
    if (year > (CURRENT_YEAR + 1)): return False
    if (year < 1776): return False

    day = int(date[2:4])
    month = int(date[0:2])
    try: 
        datetime.datetime(year,month,day)     #checks whether the given day, month can work with the given year
    except ValueError:
        return False

    return True


'''
	This method read the string in PercentileFile and checks whether the number is valid
	returns a string converted to a float
'''
def readPercentileString(input_string):
    try:
        PERCENTILE_number = float(input_string)/100.0
    except ValueError:
        print 'The value in the percentile.txt file is not correct\n'
        print 'value = ' + input_string
    
    if PERCENTILE_number < 0 or PERCENTILE_number > 100:
        raise ValueError('The value in the percentile.txt file is not correct  value = ' + input_string)

    
    return PERCENTILE_number


'''
	This method checks if the name is valid, it is assumed to consist of two parts separated by a comma
	Neither one empty
'''
def validName(name):
    name_array = name.split(',')
    if(len(name_array) != 2): return False
    first_name = name_array[1]
    last_name = name_array[0]
    if(first_name == '' or last_name == ''): return False
    return True



'''
	This method checks whether the donation amount is valid, it should be able to be converted to a float and cannot be negative
'''
def validAmount(amount):
    if(amount == ''): return False
    number = 0
    try:
        number = float(amount)
    except ValueError:
        return False

    if(number < 0): return False

    return True
