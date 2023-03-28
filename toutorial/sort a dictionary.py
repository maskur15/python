import  operator
d={1:3,2:1,4:4,5:22}
#sort a dictionary by descending order by value
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)