import json
dic={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
 }
file=open("question6.json","w")
json.dump(dic,file,indent=2)
file.close()
