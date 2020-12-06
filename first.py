import pymongo
from pymongo import MongoClient
class First():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
        
    
    def getCollegeByAttr(self,attr,attrvalue):
        attrvalue=int(attrvalue)
        print(type(attrvalue))
        colleges=[]
        for d in self.db.colleges.find({attr:attrvalue}):
            colleges.append(d)
        print(colleges)
         
        if len(colleges) > 0:
            return colleges
        else:
            return False


    def addNewCollege(self,data):
        
        
        results=[]
        if self.db.colleges.find({"college_name":data['college_name']}).count() > 0:
            
            results.append("hey! This college name is already taken..plz choose another one")
            results.append("false")
        elif self.db.colleges.find({"college_id":data['college_id']}).count() > 0:
            
            results.append("hey! This college id is already taken..plz choose another one")
            results.append("false")
        else:       
            res=self.db.colleges.insert(data)
            results.append("College successfully added")
            results.append("true")
        return results    

    def deleteCollegeByAttr(self,attr,attrvalue):
        if(attr=='collegename'):
            res=self.db.colleges.delete_many({"collegename":attrvalue})
        else:
            res=self.db.colleges.delete_one({attr:attrvalue})
        
        return res
        
    def updateCollegeByAttr(self,attr,prevval,newval):
        res=self.db.colleges.update({attr:prevval},{'$set':{attr:newval}})
        return res

        
