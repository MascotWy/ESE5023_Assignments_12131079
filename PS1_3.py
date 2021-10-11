# -*- coding: utf-8 -*-
def Pascal_triangle(a):
    global b
    K=[1]
    if a >2:
        for i in range(0,a-1):
            if (i+1<a-1):
                K.append(Pascal_triangle(a-1)[i]+Pascal_triangle(a-1)[i+1])
            else:
                break
        K.append(1)
    elif a==1:
        K = [1]
    else:
        K=[1,1]
    if (len(K)==b):
        print(K)
    return (K)

a=10 # Change a to get Pascal_triangle(100) and Pascal_triangle(200)
b=a
Pascal_triangle(a)