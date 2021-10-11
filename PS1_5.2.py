# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
def Find_expression(diction,value):
    keylist=[]
    for k,v in diction.items():
        if v==value:
            keylist.append(k)
    return keylist

def string_repeat(n_string,repeat_list):
    for s_index in range(0,len(n_string)):
        if (n_string[s_index]=="+") or (n_string[s_index]=="-"):
            repeat_list.append(s_index)
    return repeat_list


def make_dic(string_list,answer_list):
    formula_list=[]
    for i in string_list:
        new_string2=i.replace("a","")
        repeat_list2=string_repeat(new_string2,[])
        formula_list.append(new_string2)
        if len(repeat_list2) >0:
            answer=int(new_string2[:repeat_list2[0]])
            for j in range(0,len(repeat_list2)):
                if new_string2[repeat_list2[j]]=="+" and j< len(repeat_list2)-1:
                    answer=answer+int(new_string2[repeat_list2[j]+1:repeat_list2[j+1]])
                if new_string2[repeat_list2[j]]=="+" and j== len(repeat_list2)-1:
                    answer = answer + int(new_string2[repeat_list2[j] + 1:])
                if new_string2[repeat_list2[j]] == "-" and j< len(repeat_list2)-1:
                    answer = answer - int(new_string2[repeat_list2[j] + 1:repeat_list2[j + 1]])
                if new_string2[repeat_list2[j]] == "-" and j == len(repeat_list2) - 1:
                    answer = answer - int(new_string2[repeat_list2[j] + 1:])
            answer_list.append(answer)
        else:
            answer=123456789
            answer_list.append(answer)
    diction = dict(zip(formula_list, answer_list))
    return diction

def make_list():
    str_list = []
    for i in ['a', '-', '+']:
        for ii in ['a', '-', '+']:
            for iii in ['a', '-', '+']:
                for iiii in ['a', '-', '+']:
                    for iiiii in ['a', '-', '+']:
                        for iiiiii in ['a', '-', '+']:
                            for iiiiiii in ['a', '-', '+']:
                                for iiiiiiii in ['a', '-', '+']:
                                    str_list.append("1"+i +"2"+ ii+"3"+iii+"4"+iiii+"5"+iiiii+"6"+iiiiii+"7"+iiiiiii+"8"+iiiiiiii+"9")
    return str_list

string_list=make_list()
diction2=make_dic(string_list,[])
value_list=[]
solutions=[]
for value in range(1,101):
    solution = len(Find_expression(diction2,int(value)))
    value_list.append(value)
    solutions.append(solution)

total_solutions = dict(zip(value_list, solutions))
print(total_solutions)
max_list=[]
max_value=max(total_solutions.values())
for m,n in total_solutions.items():
    if n==max_value:
        max_list.append(m)
print(max_list)
min_list=[]
min_value=min(total_solutions.values())
for m,n in total_solutions.items():
    if n==min_value:
        min_list.append(m)
print(min_list)
x=value_list
y=solutions
plt.plot(x,y)
plt.show()