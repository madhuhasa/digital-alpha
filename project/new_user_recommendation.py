import pickle
import pandas as pd
from collections import defaultdict

bestList = pickle.load(open("C:\\Users\\user\\Desktop\\4yrsBMW.p", "rb"))
recommendedList = pickle.load(open("C:\\Users\\user\\Desktop\\Product_Recommendation.p","rb"))


data = pd.read_excel('C:\\Users\\user\\Desktop\\newdataset.xlsx')

bestList = (bestList['d_product'])
bestList = bestList[:370]

final_dict =defaultdict(list)

customer_dict=defaultdict(list)
customers = data["Customer ID"].unique().tolist()
for i in range(len(data)):
    
    customer_dict[data['Customer ID'][i]].append(data['ProductName'][i])
 
new_list = list(customer_dict.keys())
for i in range(0,len(new_list)): 
    
    pn=(customer_dict[new_list[i]])
    pn1 = list(set(pn))
#    print("\n \nRecommended items for the customer ",new_list[i], " : ")
                
                
    S1 = set(pn1)
    S2 = set(bestList)
    S3 = list(S2.intersection(S1))
                
    final_recommendation=[]
        
    product_list = list(recommendedList.keys())
# =============================================================================
#     for i in range(0,len(product_list)):
#         for j in range(0,len(S3)):
#             if S3[j]==product_list[i]:
# =============================================================================
    #print(recommendedList[product_list[i]][:5], "\n")
                #print("The recommended Products for ", S3[j], " are ",(recommendedList[product_list[i]][:5]))
# =============================================================================
#     for i in range(0,5):
#         item= str(recommendedList[product_list[i]][i:i+1])
#                     
#         final_recommendation.append(item)
# =============================================================================
    print("The recommended products for user ",new_list[i])
    for j in range(0, len(S3)):
        
        for k in range(0,5):
            #recommendedList[S3[j]][:5]['item2'][k]
            final_dict[new_list[i]].append(recommendedList[S3[j]][:5])
            print(recommendedList[S3[j]][:5]['item2'][k], "\n")
            
#    final_dict['item2'].unique()
   
# =============================================================================
#     final_list = list(final_dict.values())
#     
#     
#     final_List = final_dict.items()
#     for key,value in final_dict.items():
#         final_List.append([key,value])
#     
# =============================================================================
    #final_recommendation = list(set(final_recommendation))
    #final_dict[new_list[i]].append(recommendedList[product_list[i]][:5])
    
        
    
