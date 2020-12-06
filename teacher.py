import pymongo
from pymongo import MongoClient
class Teacher():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
        
    
    def getTeacherByAttr(self,attr,attrvalue):
        attrvalue=int(attrvalue)
        print(type(attrvalue))
        teachers=[]
        for d in self.db.teachers.find({attr:attrvalue}):
            teachers.append(d)
        print(teachers)
         
        if len(teachers) > 0:
            return teachers
        else:
            return False


    def addNewTeacher(self,data):
        
        
        results=[]
        if self.db.teachers.find({"teacher_name":data['teacher_name']}).count() > 0:
            
            results.append("hey! This teacher name is already taken..plz choose another one")
            results.append("false")
        elif self.db.teachers.find({"teacher_id":data['teacher_id']}).count() > 0:
            
            results.append("hey! This teacher id is already taken..plz choose another one")
            results.append("false")
        else:       
            res=self.db.teachers.insert(data)
            results.append("teacher successfully added")
            results.append("true")
        return results    

    def deleteTeacherByAttr(self,attr,attrvalue):
        if(attr=='teacher_name'):
            res=self.db.teachers.delete_many({"teacher_name":attrvalue})
        else:
            res=self.db.colleges.delete_one({attr:attrvalue})
        
        return res
        
    def updateTeacherByAttr(self,attr,prevval,newval):
        res=self.db.teachers.update({attr:prevval},{'$set':{attr:newval}})
        return res

        
