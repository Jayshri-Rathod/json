import json
dic={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
# with open("question9.json","w") as f:
#     json.dump(dic,f,indent=2)
# f.close()
# item=input("konsa item kharidna chahte ho")
# quntity=int(input("enter kitana kharidna chahte ho"))
for i in dic:
    print(i)
    # if item in dic:
    #     print(int(dic[i])-quntity)