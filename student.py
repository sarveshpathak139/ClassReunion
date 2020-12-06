import pymongo
from pymongo import MongoClient
class Student():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
        
    
    def getStudentByAttr(self,attr,attrvalue):
        attrvalue=int(attrvalue)
        print(type(attrvalue))
        alumies=[]
        for d in self.db.students.find({attr:attrvalue}):
            students.append(d)
        print(students)
         
        if len(students) > 0:
            return students
        else:
            return False


    def addNewStudent(self,data):
        results=[]
        
        
        if (self.db.students.find({"student_id":data['student_id']}).count() == 0):
            
            results.append("true")   
            res=self.db.students.insert(data)
            results.append("Student added")
            results.append("true")
        else:
            results.append("Student founded ")
            results.append("true")

        return results 



    def addNewStudent1(self,data):
        
        if (self.db.students.find({ '$and': [ { 'student_name':data["student_name"]}, { 'student_id': data["student_id"] },{"student_branch":data["student_branch"]},{"student_college":data["student_college"]},{"student_join_year":data["student_join_year"],"student_end_year":data["student_end_year"]} ] }).count()==1):
            results=[]
            results.append("true")
        

            if (self.db.users.find({"student_id":data['student_id']}).count() == 0):
           
                res=self.db.users.insert(data)
                results.append("NOW VERIFIED AND SIGNED UP ")
               
            else:
                results.append("ALEREADY SIGNED UP ")

        else:
            results=[]
             
            
            results.append("alumni not verified ")
            results.append("false")

            

        return results    



    def deleteStudentByAttr(self,attr,attrvalue):
        if(attr=='student_name'):
            res=self.db.alumnies.delete_many({"alumniname":attrvalue})
        else:
            res=self.db.colleges.delete_one({attr:attrvalue})
        
        return res
        
    def updateStudentByAttr(self,attr,prevval,newval):
        res=self.db.alumies.update({attr:prevval},{'$set':{attr:newval}})
        return res

        
