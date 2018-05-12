# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:36:44 2018

@author: user
"""
import pickle
import pandas as pd
bestList = pickle.load(open("C:\\Users\\user\\Desktop\\4yrsBMW.p", "rb"))
recommendedList = pickle.load(open("C:\\Users\\user\\Desktop\\Product_Recommendation.p","rb"))
customers = data["Customer ID"].unique().tolist()
data = pd.read_excel('C:\\Users\\user\\Desktop\\newdataset.xlsx')
pn = []
for i in range(len(data)):
    if data['Customer ID'][i] in customers:
        pn.append(data['ProductName'][i]) 
        
pn1 = list(set(pn))
bestList = bestList.iloc[:370,:]
bestList = list(bestList['d_product'])

S1 = set(pn1)
S2 = set(bestList)
S3 = list(S2.intersection(S1))

for i in range(0,2):
    if S3[i] in 
    


customersList = data["Customer ID"].unique().tolist()
customersCount=len(set(data["ProductName"].tolist()))

productScore= pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount=0
lenData = len(productScore['item2'])
lengData = len(productScore['item1'])
for ind1 in range(len(S3)):
    item1Users = data[data.ProductName==S3[ind1]]["Customer ID"].tolist()
    for ind2 in range(ind1, len(S3)):
        if ( ind1 == ind2):
            continue
        item2Users=data[data.ProductName==S3[ind2]]["Customer ID"].tolist()
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=commonUsers / customersCount
        productScore.loc[rowCount] = [S3[ind1],S3[ind2],score]
        rowCount +=1
        productScore.loc[rowCount] = [S3[ind2],S3[ind1],score]
        rowCount +=1        
productScore.head()
search="Eaton Premium Continuous-Feed Paper, 25% Cotton, Letter Size, White, 1000 Shts/Box"
recoList=productScore[productScore.item1==search]\
        [["item2","score"]]\
        .sort_values("score", ascending=[0])      
print("Recommendations for item 1st product\n", recoList)


