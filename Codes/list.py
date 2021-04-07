countries = ["Australia","Austria","Belarus","Canada","Estonia"]
gold = [2,4,1,14,0]
silver= [1,6,1,7,1]
bronze = [0,6,1,5,0]

totals=[]
for i in range(len(countries)):
    medals = gold[i]+silver[i]+bronze[i]
    totals.append((medals,countries[i]))