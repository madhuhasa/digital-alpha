# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:41:20 2018

@author: Madhuhasa
"""
import pickle
import pandas as pd
userItemData = pd.read_excel('C:\\Users\\user\\Desktop\\newdataset.xlsx')
#userItemData = userItemData[:]
userItemData.head()

#Getting list of Unique Items
#itemListt = userItemData["ProductName"].unique().tolist()
itemList = pickle.load(open("4yrsBMW.p", "rb"))
uniqueproducts = userItemData['ProductName'].unique()
itemListt=[]
for i in range(0,370):
    itemListt.append(itemList["d_product"][i])
#Getting list of Unique Users
usersList = userItemData["Customer ID"].unique().tolist()
userCount=len(set(userItemData["ProductName"].tolist()))

#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount=0
#itemAffinity['item2'] = uniqueproducts
lenData = len(itemAffinity['item2'])
lengData = len(itemAffinity['item1'])
#For each item in the list, compare with other items.
for ind1 in range(len(itemListt)):
    #Get list of users who bought this item 1.
    item1Users = userItemData[userItemData.ProductName==itemListt[ind1]]["Customer ID"].tolist()
    #print("Item 1 ", item1Users)
    #Get item 2 - items that are not item 1 or those that are not analyzed already.
    for ind2 in range(ind1, len(itemListt)):
        
        if ( ind1 == ind2):
            continue
        #Get list of users who bought item 2
        item2Users=userItemData[userItemData.ProductName==itemListt[ind2]]["Customer ID"].tolist()
        #print("Item 2",item2Users)
        #Find score. Find the common list of users and divide it by the total users.
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=commonUsers / userCount

        #Add a score for item 1, item 2
        itemAffinity.loc[rowCount] = [itemListt[ind1],itemListt[ind2],score]
        rowCount +=1
        #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
        itemAffinity.loc[rowCount] = [itemListt[ind2],itemListt[ind1],score]
        rowCount +=1
        
#Check final result
itemAffinity.head()

for i in itemListt:
    Recommendations=[]
    searchItem= i 
    recoList=itemAffinity[itemAffinity.item1==searchItem]\
            [["item2","score"]]\
            .sort_values("score", ascending=[0])
    recoList=recoList.reset_index(drop=True)        
    for i in range(len(recoList)):
        if (recoList['score'][i] > 0):
            Recommendations.append(recoList['item2'][i])
    print("\n\n Recommendations for",itemListt[i]," \n",Recommendations[:5])