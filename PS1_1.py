# -*- coding: utf-8 -*-
# #Q1
import random
a=random.random()*100
b=random.random()*100
c=random.random()*100
if (a>b):
	if (b>c):
		print(a,b,c)
	elif (a>c):
		print(a,c,b)
	else:
		print(c,a,b)
elif (b>c):
	if (a>c):
		print(b,a,c)
	else:
		print(b,c,a)
else:
	print(c,b,a)