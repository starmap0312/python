import configparser

parser = configparser.ConfigParser()
parser._interpolation = configparser.ExtendedInterpolation()
parser.read("example.ini")

print(parser.sections())                     # ['SectionOne', 'SectionTwo', 'SectionThree'] 
print(parser.get('SectionOne', 'Param1'))    # Hello
print(parser.get('SectionOne', 'Param2'))    # World
#print(parser.get('SectionOne', 'Param3'))   # NoOptionError: No option 'param3' in section: 'SectionOne'
print(parser.get('SectionTwo', 'Param1'))    # Hello World
print(parser.get('SectionThree', 'Charlie')) # One Mississippi
