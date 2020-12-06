import pymongo
from flask import *
from bson import json_util, ObjectId
import json
from pymongo import MongoClient
class Search():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni

    def searchbyName(self,name):
        name=name
        results=[]
        
        if self.db.teachers.find({"teacher_name":name}).count() > 0:
            for d in self.db.teachers.find({"teacher_name":name}):
                results.append(d)
                print(d)
        if self.db.students.find({"student_name":name}).count() > 0:
            for d in self.db.students.find({"student_name":name}):
                results.append(d)
                print(d)
        if self.db.alumnies.find({"alumni_name":name}).count() > 0:
            for d in self.db.alumnies.find({"alumni_name":name}):
                results.append(d)
                print(d)
            
        
        page_sanitized = json.loads(json_util.dumps(results))
        return page_sanitized


    def searchStudentByAttr(self,attr,attrvalue):
        results=[]
        
        if self.db.students.find({attr:attrvalue}).count() > 0:
            for d in self.db.students.find({attr:attrvalue}):
                results.append(d)
                print(d)

        else:
            results.append("not found")
        
        page_sanitized = json.loads(json_util.dumps(results))

        return page_sanitized
        
