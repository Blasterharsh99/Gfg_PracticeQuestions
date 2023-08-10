import pandas as pd
data = {'cars': ["BMW", "Volvo", "Ford"],' passings ': [3, 7, 2]}
var = pd.DataFrame(data)
print(var)

#a = [2,1,8,0]
#b=pd.Series(a,index= ["B","C","E","S"])
#print(b)

#d ={'b':2,'c':1,'e':8,'s':0}
#e = pd.Series(d,index= ['b','c','e'])
#print(e)

#print(var.loc[[0,1]])

pd.options.display.max_rows = 999
print(pd.options.display.max_rows)