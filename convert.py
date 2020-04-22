import re;




#numeric_const_pattern = '([-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?)'
#rx = re.compile(numeric_const_pattern, re.VERBOSE)
#print rx.findall("55435345.6554 Some example: Jr. it. was .23 between 2.3 and 42.31 seconds")


numeric_const_pattern = '(^(0[X|x][A-F|a-f|0-9]{4,})$)|(^([A-Z|a-z|0-9|\_|\+|\-|\S]{1,})$)|(^([0-9]{1,})$)'
rx = re.compile(numeric_const_pattern, re.VERBOSE)
print rx.findall("545")

