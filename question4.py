import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
file=open("question4.json","w")
json.dump(a,file,sort_keys=True)
file.close()
