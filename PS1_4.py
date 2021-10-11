# -*- coding: utf-8 -*-
import math
import random
def Least_moves(a,step):
    if (a!=1):
        if (math.ceil(a / 2) == (a / 2)):
            step += 1
            Least_moves(a / 2,step)
        else:
            step += 1
            Least_moves(a - 1,step)
    else:
        print("least step:"+str(step))
a=int(random.random()*100)
print("RMB:"+str(a))
step=0
Least_moves(a,step)