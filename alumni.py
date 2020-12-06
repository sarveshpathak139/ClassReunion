import pymongo
from pymongo import MongoClient
class Alumni():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
        
    
    def getAlumniByAttr(self,attr,attrvalue):
        attrvalue=int(attrvalue)
        print(type(attrvalue))
        alumies=[]
        for d in self.db.alumnies.find({attr:attrvalue}):
            alumnies.append(d)
        print(alumies)
         
        if len(alumies) > 0:
            return alumies
        else:
            return False


    def addNewAlumni(self,data):
        
        
        results=[]
        if self.db.alumnies.find({"alumni_name":data['alumni_name']}).count() > 0:
            
            results.append("hey! This alumni name is already taken..plz choose another one")
            results.append("false")
        elif self.db.alumnies.find({"alumni_id":data['alumni_id']}).count() > 0:
            
            results.append("hey! This alumni id is already taken..plz choose another one")
            results.append("false")
        else:       
            res=self.db.alumnies.insert(data)
            results.append("Alumni successfully added")
            results.append("true")
        return results    



    def deleteAlumniByAttr(self,attr,attrvalue):
        if(attr=='alumniname'):
            res=self.db.alumnies.delete_many({"alumniname":attrvalue})
        else:
            res=self.db.colleges.delete_one({attr:attrvalue})
        
        return res
        
    def updateAlumniByAttr(self,attr,prevval,newval):
        res=self.db.alumies.update({attr:prevval},{'$set':{attr:newval}})
        return res

        
