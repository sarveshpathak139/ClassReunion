import pymongo
from pymongo import MongoClient
class Direct():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
        
    
    def getDirectByAttr(self,attr,attrvalue):
        attrvalue=int(attrvalue)
        print(type(attrvalue))
        directs=[]
        for d in self.db.directs.find({attr:attrvalue}):
            directs.append(d)
        print(directs)
         
        if len(directs) > 0:
            return directs
        else:
            return False


    def addNewDirect(self,data):
        
        
        results=[]
        if self.db.directs.find({"direct_name":data['direct_name']}).count() > 0:
            
            results.append("hey! This directorate name is already taken..plz choose another one")
            results.append("false")
        elif self.db.directs.find({"direct_id":data['direct_id']}).count() > 0:
            
            results.append("hey! This directs id is already taken..plz choose another one")
            results.append("false")
        else:       
            res=self.db.directs.insert(data)
            results.append("Directorate successfully added")
            results.append("true")
        return results    

    def deleteDirectByAttr(self,attr,attrvalue):
        if(attr=='direct_name'):
            res=self.db.teachers.delete_many({"direct_name":attrvalue})
        else:
            res=self.db.colleges.delete_one({attr:attrvalue})
        
        return res
        
    def updateDirectByAttr(self,attr,prevval,newval):
        res=self.db.directs.update({attr:prevval},{'$set':{attr:newval}})
        return res

        
