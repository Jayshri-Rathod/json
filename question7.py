import json
file="text.txt"
dic={}
f=open(file)
for i in f:
    key,dictonry=i.split(None,1)
    dic[key]=dictonry.strip()
new_file=open("question.json","w")
json.dump(dic,new_file,indent=3)
new_file.close()

