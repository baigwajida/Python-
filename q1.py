import re
import logging
LOG_FILENAME = "example.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.debug('This message should go to the log file')
logger1 = logging.getLogger('package1.module1')
s = raw_input("Enter the password: ")
def validate(s):
	for i in s.split():
		if(s.isalpha()):
			if(s.isupper()):
				return 1
			elif(s.islower()):
				return 1 	
		elif(s.isdigit()):
			return 1
	
		elif(s.match("[$#@]")):
 			return 1
		elif(len(s) >= 6 and len(s) <= 12):
			return 1
def main():
	if(validate(s)):
		print("Valid")
		logger1.warning('This message comes from one module')
	else:
		print("Not Valid")
				