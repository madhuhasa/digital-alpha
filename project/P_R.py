# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:41:20 2018
@author: Madhuhasa
"""
# -- Import Libraries -- #
import pickle
import pandas as pd

# --- Read Data --- #
userItemData = pd.read_excel('C:\\Users\\Swathi\\Desktop\\store-dataset1.xlsx')
userItemData.head() #printing top 5 elements of data

# -- Getting list of Unique Products -- #
BMWList = pickle.load(open("C:\\Users\\Swathi\\Desktop\\4yrsBMW.p", "rb"))#Loading 4Years best, moderate and worst products Pickle file
uniqueproducts = userItemData['ProductName'].unique()
productList=[]

for i in range(0,370):
    productList.append(BMWList["d_product"][i])

#Getting list of Unique Users
usersList = userItemData["Customer ID"].unique().tolist()
userCount=len(set(userItemData["ProductName"].tolist()))

#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('Product1', 'Product2', 'SCORE'))
rowCount=0

lenData = len(itemAffinity['Product2'])
lengData = len(itemAffinity['Product1'])

#For each PRODUCT in the list, compare with other PRODUCTS.
for ind1 in range(len(productList)):
    #Get list of users who bought this product1.
    Product1Users = userItemData[userItemData.ProductName==productList[ind1]]["Customer ID"].tolist()
    #print("Item 1 ", Product1Users)
    
    #Get item 2 - items that are not item 1 or those that are not analyzed already.
    for ind2 in range(ind1, len(productList)):
        if ( ind1 == ind2):
            continue
        
        #Get list of users who bought item 2
        Product2Users=userItemData[userItemData.ProductName==productList[ind2]]["Customer ID"].tolist()
        #print("Item 2",Product2Users)
        
        #Find SCORE. Find the common list of users and divide it by the total users.
        commonUsers= len(set(Product1Users).intersection(set(Product2Users)))
        SCORE=commonUsers / userCount

        #Add a SCORE for item 1, item 2
        itemAffinity.loc[rowCount] = [productList[ind1],productList[ind2],SCORE]
        rowCount +=1
        
        #Add a SCORE for Product2, item 1. The same SCORE would apply irrespective of the sequence.
        itemAffinity.loc[rowCount] = [productList[ind2],productList[ind1],SCORE]
        rowCount +=1
        
#Check final result
itemAffinity.head()
RECList = []

for j in productList:
    Recommendations=[]
    searchItem= j
    recoList=itemAffinity[itemAffinity.Product1==searchItem][["Product2","SCORE"]].sort_values("SCORE", ascending=[0])
    recoList=recoList.reset_index(drop=True)  
    RECList.append(recoList)    
    for i in range(len(RECList)):
        Recommendations=[]
        for u in range(len(RECList[i])):
            if (RECList[i]['SCORE'][u] >= 0.0005405405405405405):
                Recommendations.append(RECList[i]['Product2'][u])
        print("\n\n Recommendations for",productList[i]," \n",Recommendations[:5])

#creating pickle file for final output.
pickle_out = open("Product_Recommendation.p","wb")
pickle.dump(RECList,pickle_out)
pickle_out.close()
pickle_in = open("Product_Recommendation.p","rb")
pickle.load(pickle_in)