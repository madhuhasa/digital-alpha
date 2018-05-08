# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:41:20 2018

@author: Madhuhasa
"""
import pandas as pd
userItemData = pd.read_excel('C:\\Users\\user\\Desktop\\newdataset.xlsx')
userItemData.head()

#Getting list of Unique Items
itemList = userItemData["ProductID"].unique().tolist()
#Getting list of Unique Users
usersList = userItemData["Customer ID"].unique().tolist()
userCount=len(set(userItemData["ProductID"].tolist()))

#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount=0

#For each item in the list, compare with other items.
for ind1 in range(len(itemList)):
    #Get list of users who bought this item 1.
    item1Users = userItemData[userItemData.ProductID==itemList[ind1]]["Customer ID"].tolist()
    #print("Item 1 ", item1Users)
    #Get item 2 - items that are not item 1 or those that are not analyzed already.
    for ind2 in range(ind1, len(itemList)):
        
        if ( ind1 == ind2):
            continue
        #Get list of users who bought item 2
        item2Users=userItemData[userItemData.ProductID==itemList[ind2]]["Customer ID"].tolist()
        #print("Item 2",item2Users)
        #Find score. Find the common list of users and divide it by the total users.
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=commonUsers / userCount

        #Add a score for item 1, item 2
        itemAffinity.loc[rowCount] = [itemList[ind1],itemList[ind2],score]
        rowCount +=1
        #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
        itemAffinity.loc[rowCount] = [itemList[ind2],itemList[ind1],score]
        rowCount +=1
        
#Check final result
itemAffinity.head()