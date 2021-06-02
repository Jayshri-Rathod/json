import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"] 
key=["name","designation","age","salary"]
# Dictionary={}
emp1={}
i=0
a=[]
while i<len(list1):
    m=key[i],list1[i]
    i+=1
    a.append(m)
emp1.update(a)
# print(emp1)
emp2={}
j=0
b=[]
while j<len(list2):
    p=key[j],list2[j]
    j+=1
    b.append(p)
emp2.update(b)
# print(emp2)
emp3={}
k=0
c=[]
while k<len(list3):
    n=key[k],list3[k]
    k+=1
    c.append(n)
emp3.update(c)
# print(emp3)
emp4={}
l=0
d=[]
while l<len(list4):
    o=key[l],list4[l]
    l+=1
    d.append(o)
emp4.update(d)
# print(emp4)
Dictionary={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
with open("question8.json","w") as f:
    json.dump(Dictionary,f,indent=2)
f.close()











# i=0
# while i<len(list1):
#     emp1.update({key[i]:list1[i]})
#     i+=1
# j=0
# while j<len(list2):
#     emp2.update({key[j]:list2[j]})
#     j+=1
# k=0
# while k<len(list3):
#     emp3.update({key[k]:list3[k]})
#     k+=1
# l=0
# while l<len(list4):
#     emp4.update({key[l]:list4[l]})
#     l+=1
# with open("question8.json","w") as f:
#     json.dump(Dictionary,f,indent=2)
# f.close()


