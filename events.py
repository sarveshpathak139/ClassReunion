import pymongo
from flask import Flask,session,request, url_for
from pymongo import MongoClient
import json

class EventCreate():
        def __init__(self):
            self.client=MongoClient('localhost', 27017)
            self.db=self.client.alumni

        def Create_Event(self,data):
            results=[]
            res=self.db.events.insert(data)
            results.append("Alumni successfully added")
            results.append("true")
            return results    
                
        def Show_Event(self):
            results=[]
            res=self.db.events.find()
            return res   

        def Create_Fundraising(self,data):
            results=[]
            res=self.db.fund_raising.insert(data)
            return res   