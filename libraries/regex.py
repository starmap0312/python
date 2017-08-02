import re

line = "pattern1 are pattern2 pattern3"

matchObj = re.match( r'(.*) arE (.*?) .*', line, re.M|re.I)
# re.M:
#   this makes $ match the end of a line and ^ match the start of any line
# re.I:
#   this erforms case-insensitive matching


if matchObj:
   print "matchObj.group() : ", matchObj.group()   # group(0): returns entire match, i.e. pattern1 are pattern2 pattern3
   print "matchObj.group(1) : ", matchObj.group(1) # group(1): returns matched pattern of the first subgroup enclosed by ()
   print "matchObj.group(2) : ", matchObj.group(2) # group(2): returns matched pattern of the second subgroup enclosed by ()
else:
   print "No match!!"
