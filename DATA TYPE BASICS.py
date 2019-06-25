# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:29:33 2019

@author: HAI
"""
     'NUMERIC'
     
e=12
print(e)
print(int(e))
print(float(e))




     'STRING'
     
a='srikrishna'
print(id(a))
print(type(a))
print(len(a))
print(a[2])
print(a[-2])
print(id(a[-2]))
print(id(a[2]))






     'STRING'
     
ss='1234567as'
print(type(ss))
print(len(ss))
print(ss[3])
print(id(ss))
print(id(ss[3]))
print(a[-4])
print(ss)



         'LIST'
q=[12,13,'as',132,12.3,[12,13]]
print(q[0])
print(q[-1])
print(q[-1][0])
q[-1][0]=121212
print(q)
q[-1]='sri krishna'
print(q)
print(len(q))
print(id(q[3]))
print(id(q[4]))
print(type(q))
print(q[0],q[1])




         'TUPLE'
ee=(11,1,1,1,1,1,1,1,[1,1],1,1,1,'asd','aaaaa')
print(ee[6])
print(type(ee))
print(len(ee))
print(id(ee))
print(id(ee[8]))
print(ee[8])
ee[8][0]=11
print(ee)
print(type(ee))
print(len(ee))






    'DICTIONARY'
dd={12:'ps',7:'fy',5:'er',44:[23,33],12:(12,11)}
print(dd[7])
dd[7]=123
print(dd)
dd[44][0]=11
print(dd)
print(dd[12])
dd[44]=(12,13)
print(dd)
dd[44]=11
print(dd)
dd[12]='srikrishna'
print(dd)
oo='sri krishna'
print(oo[3])
print(oo[2])




      'SET BY USING OPERATORS'
dd={12,12,13,14}
ss={12,'as',34}
print(dd|ss)
print(dd&ss)
print(dd-ss)
print(ss-dd)


    'DIFFERENT DATA TYPE BY USING THE DIFFERENT DATA TYPES WITH OPERATORS '
x=12
y='ac'
e={12:111,'as':12}
l=[12,13]
print(x*y)
print('BULIT IN FUNCTIONS')
cc=12
print(cc)
print(id(cc))
print(type(cc))
print(int(cc))   
print(float(cc))
