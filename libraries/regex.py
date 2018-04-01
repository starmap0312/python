import re

pattern = r'(.*) arE (.*?) .*'
text = "pattern1 are pattern2 pattern3"

matchObj = re.match(pattern, text, re.M|re.I)
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


# replace all non-word characters
print re.sub(r'\W+', ' ', 'hello;`1`23~!#world') # hello 1 23 word


# replace a set of keywords, ex. keyword -> <b>keyword</b>
keywords = ['hello', 'world']
pattern = re.compile("|".join(keywords)) # "hello|world"
print pattern.sub(lambda m: '<b>{0}</b>'.format(re.escape(m.group(0))), "Hi, helloxxxmyworld!") # Hi, <b>hello</b>xxxmy<b>world</b>!
