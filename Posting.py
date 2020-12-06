import pymongo
from pymongo import MongoClient
class Posting():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
        
    
    def getPostByAttr(self,attr,attrvalue):
        attrvalue=int(attrvalue)
        print(type(attrvalue))
        directs=[]
        for d in self.db.posts.find({attr:attrvalue}):
            posts.append(d)
        print(posts)
         
        if len(posts) > 0:
            return posts
        else:
            return False


    def addNewPost(self,data):
        
        
        results=[]
              
        res=self.db.posts.insert(data)
        results.append("posts successfully added")
        results.append("true")
        return results

    
    def addNewjobPost(self,data):
        
        results=[]
        res=self.db.jobposts.insert(data)
        results.append("posts successfully added")
        results.append("true")
        return results    

    def addNewnotice(self,data):
        
        results=[]
        res=self.db.notice.insert(data)
        results.append("posts successfully added")
        results.append("true")
        return results    

        
