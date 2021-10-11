#  Search  for  lines  that  contain  ’From’
#  Sample code from:  http://www.py4e.com/code3/re01.py
#  Modified to run in 2021 Cyber conf environment
import  re
hand  =  open('email_log_small.txt')
for  line  in  hand:
    line  =  line.rstrip()
    if  re.search('From:',  line): print(line)


