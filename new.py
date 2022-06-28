#importing the modules 
import pandas as pd;
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#setting up firebse
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#reading a spread sheet data
data = pd.read_excel("pricelist.xlsx")
#size of data
rows,colums=data.shape
#looping througth the each row
for i in range(rows-1):
    onerow = data.loc[i]
    name = onerow[0]
    g250 = onerow[1]
    g500 = onerow[2]
    kg1 = onerow[3]
    kg10 = onerow[4]
    offer = onerow[5]
    gst = onerow[6]
    HSN = onerow[7]
    #creating a dict to send data to firestore
    datatosend = {"name":name,"250g":g250,"500g":g500,"1kg":kg1,"10kg":kg10,"offer":offer,"gst":gst,"HSN":HSN}
    db.collection("inventary").add(datatosend)

    print(datatosend)
   


