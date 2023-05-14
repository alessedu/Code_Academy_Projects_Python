#Importinghte 'datetime' module
from datetime import datetime

#Create a date using year, month day hour minute and seconds arguments
birthday = datetime(1997, 2, 24, 4, 25, 12)

birthday.year
birthday.month
birthday.day
birthday.hour
birthday.weekday()

#Create a date using datetime.now()
datetime.now()

#subtract them, cnnot +, / or *
datetime(2018, 1, 1) - datetime(2017, 1, 1)
datetime.now() - datetime(2018, 1, 1)

#Parsing a date usng strptime, using format characters
parsed_date = datetime.strptime('Jan 15, 2018', '%b %, %Y')

#Rendering a date as a string
date_string = datetime.stringftime(datetime.now(), '%b %d, %Y')

