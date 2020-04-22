import re;





#numeric_const_pattern = '([-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?)'
#rx = re.compile(numeric_const_pattern, re.VERBOSE)
#print rx.findall("55435345.6554 Some example: Jr. it. was .23 between 2.3 and 42.31 seconds")


numeric_const_pattern = '(?:^([A-Za-z]{1,1}[A-Za-z0-9_.]+)) |(?:^(0[X|x][A-F|a-f|0-9]{4,})$)  |  (?:^([-+]?[0-9]{1,}$))  |   ([-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?)'

rx = re.compile(numeric_const_pattern, re.VERBOSE)
a= rx.findall('asa')
print a


val=''
eval_map={}

eval_map[0]="str(val)"
eval_map[1]="int(val, 16)"
eval_map[2]="int(val)"
eval_map[3]="float(val)"

#print a[0][0],'  ',a[0][1],'   ',a[0][2]


#s = re.search(r'(?:^(0[X|x][A-F|a-f|0-9]{4,})$)|(?:^([-+]?[0-9]{1,}$))', "123")
#if s:
   # print(s.group())


i=0
for match in range(0,4):
    if(a[0][i]!=''):
	val=a[0][i]
	break 
    else:
	print "non matched index=",i
    i+=1



print eval(eval_map[i])
print "matched index=",i







