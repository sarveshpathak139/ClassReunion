from flask import Flask,session,request, url_for
from flask_pymongo import PyMongo
from first import First
from alumni import Alumni
from student import Student
from teacher import Teacher
from direct import Direct
from events import EventCreate
import pymongo
import os
from pymongo import MongoClient
from flask import request,jsonify,json,render_template,redirect
from mailhandler import Mailhandler





client=MongoClient('localhost', 27017)
app = Flask(__name__)


app.secret_key=os.urandom(24)
first=First() 
alma=Alumni()
stud=Student()
teach=Teacher()
di=Direct()
@app.route('/crash')
def main():
    raise Exception()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homelog')
def homelog():
    return render_template('login.html')


@app.route('/sign')
def signup():
    return render_template('sign.html')

@app.route('/getcolleges',methods=['GET'])
def getProducts():
    colleges=[]
    id=request.args['id']
    res=first.getCollegeByAttr("college_id",id)
    if (res==False):
        colleges.append("sorry no products found")
    else:    
        for i in res:   
            colleges.append({"college_id":i['college_id'],"college_name":i['college_name'],"eastablish_year":i['establish_year'],"email":i['email'],"location":i['location'],"website":i['website']})
    
    return jsonify({'result':colleges})

@app.route('/addcolleges',methods=['POST'])
def addCollege():
    colleges=[]
    id=request.form["clg_id"]
    name=request.form["clg_name"]
    esta_year=request.form["clg_esta_year"]
    email=request.form["clg_email"]
    password=request.form["clg_password"]
    website=request.form["clg_website"]
    location=request.form["clg_location"]
    college={"college_name":name,"college_id":id,"establish_year":esta_year,"email":email,"password":password,"website":website,"location":location}
    res=first.addNewCollege(college)
    if(res[1] == "true"):
        return render_template("login.html", uname = "Post Added Sucessfully")
    else:
        return render_template("sign.html")



@app.route('/addalumni',methods=['POST'])
def addAlumni():
    alumnies=[]
    id=request.form["alumni_id"]
    name=request.form["alumni_name"]
    join_year=request.form["alumni_join_year"]
    end_year=request.form["alumni_end_year"]
    email=request.form["alumni_email"]
    pnum=request.form["alumni_number"]
    password=request.form["alumni_password"]
    branch=request.form["alumni_branch"]
    desig=request.form["alumni_desig"]
    alma1={"alumni_name":name,"alumni_id":id,"alumni_join_year":join_year,"alumni_phone":pnum,"alumni_end_year":end_year,"alumni_email":email,"alumni_password":password,"alumni_branch":branch,"alumni_desig":desig}
    res=alma.addNewAlumni(alma1)

    if(res[1] == "true"):
        return render_template("login.html", uname = "Registration Sucess.. Please Login")
    else:
        return render_template("sign.html")



@app.route('/addstudent',methods=['POST'])
def addStudent():
    students=[]
    id=request.form["student_id"]
    name=request.form["student_name"]
    email=request.form["student_email"]
    password=request.form["student_password"]
    join_year=request.form["student_join_year"]

    end_year=request.form["student_end_year"]
   
    branch=request.form["student_branch"]
    college=request.form["student_college"]
    student={"student_name":name,"student_id":id,"student_join_year":join_year,"student_end_year":end_year,"stduent_password":password,"student_email":email,"student_branch":branch,"student_college":college}
    res=stud.addNewStudent1(student)

    if (len(res)<0):
        students.append("something went wrong ...student not added")
    else:    
        students.append(res)
    
    if(res[0] == "true"):
        return render_template("login.html", uname = "Register Sucessfully")
    else:
        return render_template("sign.html")


@app.route('/addstudentdata',methods=['POST'])
def addStudentdata():
    students=[]
    id=request.form["std_id"]
    name=request.form["std_name"]
    email=request.form["email"]
    pnumber=request.form["pnum"]
    join_year=request.form["admit_year"]
    end_year=request.form["passout_year"]
   
    branch=request.form["std_branch"]
    college=request.form["college"]
    student={"student_name":name,"student_id":id,"student_join_year":join_year,"student_email":email,"student_number":pnumber,"student_end_year":end_year,"student_branch":branch,"student_college":college}
    res=stud.addNewStudent(student)

    if (len(res)<0):
        students.append("something went wrong ...student not added")
    else:    
        students.append(res)
    
    db = client.alumni
    data = db.students
    friendsList = data.find()
           
    if(res[0] == "true"):
        return render_template("college/adminpanel_user.html",lp=friendsList, uname = "Register Sucessfully")
    else:
        return render_template("college/adminpanel_user.html",uname="Beacuse of some error Not added")



@app.route('/addteacher',methods=['POST'])
def addTeacher():
    teachers=[]
    id=request.form["teacher_id"]
    name=request.form["teacher_name"]
    email=request.form["teacher_email"]
    password=request.form["teacher_password"]
    branch=request.form["teacher_branch"]
    college=request.form["teacher_college"]
    teacher={"teacher_name":name,"teacher_id":id,"teacher_email":email,"teacher_password":password,"teacher_branch":branch,"teacher_college":college}
    res=teach.addNewTeacher(teacher)

    if(res[1] == "true"):
        return render_template("login.html", uname = "Post Added Sucessfully")
    else:
        return render_template("sign.html")


# @app.route('/adddirect',methods=['POST'])
# def addDirect():
#     directs=[]
#     id=request.form["direct_id"]
#     name=request.form["direct_name"]
#     email=request.form["direct_email"]
#     password=request.form["direct_password"]
#     branch=request.form["direct_branch"]
#     college=request.form["direct_college"]
#     direct={"direct_name":name,"direct_id":id,"direct_email":email,"direct_password":password,"direct_branch":branch,"direct_college":college}
#     res=di.addNewDirect(direct)


#     if(res[1] == "true"):
#         return render_template("login.html", uname = "Post Added Sucessfully")
#     else:
#         return render_template("sign.html")


@app.route('/login',methods=['POST'])
def login():
    
    db=client.alumni
    role=request.form['role']
    username=request.form['username']
    password=request.form['password']
    results=[]
    if(role=='student'):
        
        if (db.users.find({ '$and': [ { 'student_name':username }, { 'stduent_password': password } ] }).count() > 0):
            results.append('login successfully')
            db.session.insert({'user':username})
            session["user"]=request.form['username']
            if(results[0] == "login successfully"):
                db = client.alumni
                data = db.posts
                friendsList = data.find() 

                db = client.alumni
                datas = db.notice
                friends = datas.find()

                return render_template('student/index2.html', name = "Sucessfully Added",lp = friendsList,np=friends)
        else:
            results.append('login not successfully')

    if(role=='direct'):
        if db.directs.find({ '$and': [ { 'direct_name':username }, { 'direct_password': password } ] }).count() > 0:
            results.append('login successfully')
            db.session.insert({'user':username})
            session["user"]=request.form['username']
            if(results[0] == "login successfully"):
                return render_template('directorate/adminpanel.html', name = "Sucessfully Added")

        else:
            results.append('login not successfully')

        
    if(role=='teacher'):
        if db.teachers.find({ '$and': [ { 'teacher_name':username }, { 'teacher_password': password } ] }).count() > 0:
            results.append('login successfully')
            db.session.insert({'user':username})
            session["user"]=request.form['username']
            if(results[0] == "login successfully"):
                db = client.alumni
                data = db.posts
                friendsList = data.find()    
                return render_template('teacher/index2.html', name = "Sucessfully Added",lp = friendsList)
        else:
            results.append('login not successfully')

        
    if(role=='alumni'):
        if db.alumnies.find({ '$and': [ { 'alumni_name':username }, { 'alumni_password': password } ] }).count() > 0:
            results.append('login successfully')
            db.session.insert({'user':username})
            session["user"]=request.form['username']
            if(results[0] == "login successfully"):
                db = client.alumni
                data = db.posts
                friendsList = data.find()
                return render_template('alumni/index2.html', name = "Sucessfully Added",lp=friendsList)
        else:
            results.append('login not successfully')

    if(role=='college'):
        if db.colleges.find({ '$and': [ { 'college_name':username }, { 'password': password } ] }).count() > 0:
            results.append('login successfully')
            db.session.insert({'user':username})
            session["user"]=request.form['username']

            if(results[0] == "login successfully"):
                db = client.alumni
                data = db.posts
                friendsList = data.find()

                data1 = db.notice
                friendsList1 = data1.find()
                return render_template('college/collegedashbord.html', name = "Sucessfully Added",lp = friendsList,np=friendsList1)
            else:
                results.append('login not successfully')

    return jsonify({'results':results})

    
    
    

@app.route('/showloggedin')
def showloggedin():
    return jsonify(session['user'])

@app.route('/createpost',methods=['POST'])
def cratepost():

        from Posting import Posting

        p=Posting()
        posts=[]
        name=session['user']

        post=request.form["userpost"]
      
        
        post1={"username":name,"post":post}
        res=p.addNewPost(post1)

        if (len(res)<0):
            posts.append("something went wrong ...post not added")
        else:    
            posts.append(res)
        if(res[1] == "true"):
            db = client.alumni
            data = db.posts
            friendsList = data.find()    
            return render_template("alumni/index2.html", uname = "Post Added Sucessfully",lp = friendsList)
        else:
            return render_template("alumni/index2.html",lp = friendsList)


@app.route('/collegecreatepost',methods=['POST'])
def collegecratepost():

        from Posting import Posting

        p=Posting()
        posts=[]
        name=session['user']

        post=request.form["userpost"]
      
        
        post1={"username":name,"post":post}
        res=p.addNewPost(post1)

        if (len(res)<0):
            posts.append("something went wrong ...post not added")
        else:    
            posts.append(res)
        if(res[1] == "true"):
            db = client.alumni
            data = db.posts
            friendsList = data.find()    
            return render_template("college/collegedashbord.html", uname = "Post Added Sucessfully",lp = friendsList)
        else:
            return render_template("college/collegedashbord.html",lp = friendsList)



@app.route('/searchpeoples',methods=['POST'])
def searchPeoples():
    from search import Search

    s=Search()
    searches=[]
    
    
    name=request.form["name"]
    
    

    res=s.searchbyName(name)

    if (len(res)<0):
        searches.append("students not found")
    else:    
        searches.append(res)
    
    
    return render_template('college/search.html',result=res)



@app.route('/searchpeoplessss',methods=['POST'])
def searchPeoplesssss():
    from search import Search

    s=Search()
    searches=[]
    
    name=request.form["name"]
    
    res=s.searchbyName(name)

    if (len(res)<0):
        searches.append("students not found")
    else:    
        searches.append(res)
    
    
    return render_template('teacher/search.html',result=res)


@app.route('/searchpeoplesss',methods=['POST'])
def searchPeoplesss():
    from search import Search

    s=Search()
    searches=[]
    
    
    name=request.form["name"]
    
    

    res=s.searchbyName(name)

    if (len(res)<0):
        searches.append("students not found")
    else:    
        searches.append(res)
    
    
    return render_template('student/search.html',result=res)



@app.route('/searchpeopless',methods=['POST'])
def searchPeopless():
    from search import Search

    s=Search()
    searches=[]
    
    name=request.form["name"]
    
    
    res=s.searchbyName(name)

    if (len(res)<0):
        searches.append("students not found")
    else:    
        searches.append(res)
    
    
    return render_template('alumni/alumni_search.html',result=res)
 


# Teachercreate job start Here
@app.route('/createjob',methods=['POST'])
def cratejob():
        from Posting import Posting
        p=Posting()
        jobposts=[]
        name=session['user']
        jobtitle = request.form["jobtitle"]
        jobposition = request.form["jobposition"] 
        jobexp = request.form["jobexp"] 
        jobsalary = request.form["salary"]
        joblocation = request.form["location"]
        url = request.form["url"]
        description = request.form["description"]
      
        
        post1={"username":name,"companyname":jobtitle,"jobposition":jobposition,"jobexperience":jobexp,"jobsalary":jobsalary,"joblocation":joblocation,"url":url,"description":description}
        res=p.addNewjobPost(post1)

        if (len(res)<0):
            jobposts.append("something went wrong ...post not added")
        else:    
            jobposts.append(res)
        if(res[1] == "true"):
            db = client.alumni
            data = db.jobposts
            friendsList = data.find()    
            return render_template("alumni/alumni_job.html", uname = "Post Added Sucessfully",lp = friendsList)
        else:
            return render_template("alumni/alumni_job.html",lp = friendsList)



# teacher end Here

@app.route('/teachercreatejob',methods=['POST'])
def teachercratejob():
        from Posting import Posting
        p=Posting()
        jobposts=[]
        name=session['user']
        jobtitle = request.form["jobtitle"]
        jobposition = request.form["jobposition"] 
        jobexp = request.form["jobexp"] 
        jobsalary = request.form["salary"]
        joblocation = request.form["location"]
        url = request.form["url"]
        description = request.form["description"]
      
        
        post1={"username":name,"companyname":jobtitle,"jobposition":jobposition,"jobexperience":jobexp,"jobsalary":jobsalary,"joblocation":joblocation,"url":url,"description":description}
        res=p.addNewjobPost(post1)

        if (len(res)<0):
            jobposts.append("something went wrong ...post not added")
        else:    
            jobposts.append(res)
        if(res[1] == "true"):
            db = client.alumni
            data = db.jobposts
            friendsList = data.find()    
            return render_template("college/job.html", uname = "Post Added Sucessfully",lp = friendsList)
        else:
            return render_template("college/job.html",lp = friendsList)




# Publish Notice Code here
@app.route('/publishnotice',methods=['POST'])
def cratenotice():
        from Posting import Posting
        p=Posting()
        notice=[]
        jobtitle = request.form["description"]
      
        
        post1={"Message":jobtitle}
        res=p.addNewnotice(post1)
        m=Mailhandler()
        m.send_mail_notice(post1)

        

        if (len(res)<0):
            notice.append("something went wrong ...post not added")
        else:    
            notice.append(res)
        if(res[1] == "true"):
            db = client.alumni
            data = db.notice
            friendsList = data.find()    
            return render_template("college/admin_createevent.html", uname = "Post Added Sucessfully",lp = friendsList)
        else:
            return render_template("college/admin_createevent.html",lp = friendsList)

# Publish notice code end here
 
@app.route('/sendMail',methods=['GET'])

def sendMail():
    m=Mailhandler()
    m.py_mail_confirm()    
    


    return "Email Sent"



@app.route('/show')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


@app.route('/adminpanel')
def adminpanel():
    return render_template('college/adminpanel.html')

@app.route('/adminuser')
def adminuser():

    db = client.alumni
    data = db.students
    friendsList = data.find()
    return render_template('college/adminpanel_user.html',lp=friendsList)

@app.route('/sendmessages',methods=['POST'])
def sendmessages():
    number=request.form['receiver']
    message=request.form['message']
    message_details={"phone":number,"message":message}
    print(number)
    print(message)

    m=Mailhandler()
    m.send_message(message_details)
    
    db = client.alumni
    data = db.students
    friendsList = data.find()
    
    return render_template('college/adminpanel_user.html',lp=friendsList)


@app.route('/sendmailmodule',methods=['POST'])
def sendmailmodule():
    mail=request.form['receiver']
    subject=request.form['subject']
    message=request.form['message']
    mail_details={"mail":mail,"subject":subject,"message":message}
    print(mail_details)

    m=Mailhandler()
    m.sendmailmodule(mail_details)

    db = client.alumni
    data = db.students
    friendsList = data.find()
   
    return render_template('college/adminpanel_user.html',lp=friendsList,uname="Mail Send Sucessfully")




@app.route('/admincreateevent')
def admincreateevent():
    return render_template('college/admin_createevent.html')


@app.route('/adminaddevent',methods=['POST'])
def adminaddevent():
    eventtitle=request.form['eventtitle']
    location=request.form['location']
    event_description=request.form['event_description']
    date=request.form['date']
    print(eventtitle)
    print(location)
    print(event_description)
    print(date)
    events=[]
    event_details={"event_title":eventtitle,"location":location,"event_description":event_description,"date":date}
    ec=EventCreate()
    res=ec.Create_Event(event_details)
    
    m=Mailhandler()
    m.send_mail_event_details(event_details)
    m.send_message_alumni(event_details)
    if (len(res)<0):
        events.append("something went wrong ...event not added")
    else:    
        events.append(res)
    
    
    return render_template('college/admin_createevent.html')
    

    

@app.route('/alumnidirectory')
def alumnidirectory():
    db = client.alumni
    data = db.alumnies
    friendsList = data.find()
   
    return render_template('college/alumni_directory.html',lp=friendsList)

@app.route('/adminsetting')
def adminsetting():
    return render_template('college/adminsetting.html')

@app.route('/collegedashbord')
def collegedashbord():
    db = client.alumni
    data = db.posts
    friendsList = data.find()

    data1 = db.notice
    friendsList1 = data1.find()
            
    return render_template('college/collegedashbord.html',lp=friendsList,np=friendsList1)

@app.route('/adminfundraise')
def adminfundraise():
    return render_template('college/admin_fundraise.html')


@app.route('/adminaddfundcompaings',methods=['POST'])
def adminaddfundcompaings():
    eventtitle=request.form['eventtitle']
    location=request.form['location']
    event_description=request.form['event_description']
    date=request.form['date']
    Amount=request.form['rupees']
    print(eventtitle)
    print(location)
    print(event_description)
    print(date)
    events=[]
    fundcompaign_details={"event_title":eventtitle,"location":location,"event_description":event_description,"date":date,"Amount":Amount}
    ec=EventCreate()
    res=ec.Create_Fundraising(fundcompaign_details)
    
    m=Mailhandler()
    m.send_mail_fundraising_details(fundcompaign_details)
    
    
    
    return render_template('college/admin_createevent.html')
    


@app.route('/adminseeevent')
def adminseeevent():
    ec=EventCreate()
    res=ec.Show_Event()
    return render_template('college/admin_seeevent.html',events=res)

@app.route('/search')
def search():
    db=client.alumni
    res=db.alumnies.find()
    
    data1 = db.notice
    friendsList1 = data1.find()
  
    return render_template('college/search.html',result=res,np=friendsList1)

@app.route('/job')
def job():
    db = client.alumni
    data = db.jobposts
    friendsList = data.find() 

    data1 = db.notice
    friendsList1 = data1.find()       
    return render_template('college/job.html',lp=friendsList,np=friendsList1)

@app.route('/chat')
def chat():
    return render_template('college/chat.html')

@app.route('/friendmap')
def friendmap():
    return render_template('college/friendmap.html')

@app.route('/groupchat')
def groupchat():
    return render_template('chat.html')

# Alumni render Files
@app.route('/profile')
def myprofil():

    db = client.alumni
    datas = db.notice
    friends = datas.find()  
    return render_template('alumni/alumni_profile.html',np=friends)


@app.route('/donation')
def donation():
    db = client.alumni
    data = db.fund_raising
    friendsList = data.find()

    db = client.alumni
    datas = db.notice
    friends = datas.find() 
    return render_template('alumni/user_donation.html',lp=friendsList,np=friends)

@app.route('/home')
def home():
    db = client.alumni
    data = db.posts
    friendsList = data.find()    

    db = client.alumni
    datas = db.notice
    friends = datas.find()      
    return render_template('alumni/index2.html',lp = friendsList,np=friends)


@app.route('/usersearch')
def usersearch():
    db=client.alumni
    res=db.alumnies.find()
   
    db = client.alumni
    datas = db.notice
    friends = datas.find() 
    return render_template('alumni/alumni_search.html',result=res,np=friends)


@app.route('/userjob')
def userjob():
    db = client.alumni
    data = db.jobposts
    friendsList = data.find()  

    db = client.alumni
    datas = db.notice
    friends = datas.find()         
    return render_template('alumni/alumni_job.html',lp=friendsList,np=friends)


@app.route('/userchat')
def userchat():
    return render_template('alumni/alumni_chat.html')

@app.route('/usermap')
def usermap():
    return render_template('alumni/alma_friendmap.html')

# Render for the logout
@app.route('/logout')
def logout():
    return render_template('login.html')

# Render for the Directorate Here
@app.route('/directorhome')
def directorhome():
    return render_template('directorate/adminpanel.html')

@app.route('/directorsearch')
def directorsearch():
    return render_template('directorate/search.html')

@app.route('/directoruser')
def directoruser():
    return render_template('directorate/adminpanel_user.html')

@app.route('/directordirect')
def directordirect():
    return render_template('directorate/alumni_directory.html')


# Student Route Start Here
@app.route('/studenthome')
def studenthome():
    db = client.alumni
    data = db.posts
    friendsList = data.find()    

    db = client.alumni
    datas = db.notice
    friends = datas.find()      
    
    return render_template('student/index2.html',lp = friendsList,np=friends)

@app.route('/studentprofile')
def studentprofile():
    db = client.alumni
    datas = db.notice
    friends = datas.find()      
    
    
    datas = db.notice
    friends = datas.find() 
    return render_template('student/myprofile.html',p=friends,np=friends)

@app.route('/studentsearch')
def studentsearch():

    db=client.alumni
    res=db.alumnies.find()
    
    datas = db.notice
    friends = datas.find() 
    return render_template('student/search.html',result=res,np=friends)



@app.route('/studentjob')
def studentjob():
    db = client.alumni
    data = db.jobposts
    friendsList = data.find()  
    
    datas = db.notice
    friends = datas.find()         
    
    return render_template('student/job.html',lp=friendsList,np=friends)

@app.route('/studentchat')
def studentchat():
    return render_template('student/chat.html')

@app.route('/studentmap')
def studentmap():
    return render_template('student/friendmap.html')


# Teacher Render Start Here

@app.route('/teacherhome')
def teacherhome():
    db = client.alumni
    data = db.posts
    friendsList = data.find()    
                
    return render_template('teacher/index2.html',lp = friendsList)

@app.route('/teacherprofile')
def teacherprofile():
    return render_template('teacher/myprofile.html')

@app.route('/teachersearch')
def teachersearch():
    db=client.alumni
    res=db.alumnies.find()
    
    return render_template('teacher/search.html',result=res)

@app.route('/teacherchat')
def teacherchat():
    return render_template('teacher/chat.html')

@app.route('/teacherjob')
def teacherjob():
    db = client.alumni
    data = db.jobposts
    friendsList = data.find()          
    
    return render_template('teacher/job.html',lp=friendsList)

@app.route('/teacherdonation')
def teacherdonation():
    db = client.alumni
    data = db.fund_raising
    friendsList = data.find()
    
    return render_template('teacher/user_donation.html',lp=friendsList)

@app.route('/teachermap')
def teachermap():
    return render_template('teacher/friendmap.html')


@app.route('/carddemo')
def carddemo():
    
    db = client.alumni
    data = db.posts
    friendsList = data.find()
    return render_template('alumni/verify_student.html', lp = friendsList)




# Code for upload the Image
# @app.route('/upload')
# def uploadimage():
#     return render_template('alumni/afterlogin.html')

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# @app.route('/uploadimage',methods=['POST'])
# def uploadp():
#     target = os.path.join(APP_ROOT,'images/')
#     print(target)

#     if not os.path.isdir(target):
#         os.mkdir(target)

#     else:
#         print("Couldn't create upload directory:{}".format(target))
#     print(request.files.getlist("file"))        

#     for upload in request.files.getlist("file"):
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#         destination = "".join([target, "temp.jpg"])
#         print("Accept incoming file:", filename)
#         print("Save it to:",destination)
#         upload.save(destination)

#     return render_template("alumni/complete.html")    

# Code for Upload Image End Here



# 2nd Approch
# Code for the Image Upload Secound
@app.route('/upload')
def upload():
    return render_template("alumni/afterlogin.html")    
   

@app.route('/uploadimage',methods=['POST'])
def uploadp():
    if 'file' in request.files:
        profile_image = request.files['file']
        db=client.img
        # db.save_file(profile_image.filename,profile_image)
        db.insert({'username' : request.form.get('username'), 'profile_image' : profile_image.filename})

    return 'Done!'
# Code for the Image Upload End Here






# Event and Other Code by Kedar p





# Event and Other Code end here


    
app.run(debug=True)


