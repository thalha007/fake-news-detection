from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pymysql


db=pymysql.connect(host="localhost",user="root",password="",database="dbfakenewsdetection")
c=db.cursor()

######################################################################
#
#
#                           COMMON
#
#
######################################################################
######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data=loadcategory()
    return render(request,"index.html",{"data":data})

######################################################################
#                           LOGIN
######################################################################
def login(request):
    """ 
        The function to load login page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="localbody"):
                        s="select * from tbllocalbody where lEmail='"+email+"'"
                        c.execute(s)
                        i=c.fetchone()
                        request.session['id']=i[0]
                        request.session['name']=i[1]
                        return HttpResponseRedirect("/lbodyhome")
                    elif(i[2]=="user"):
                        s="select * from tbluser where uEmail='"+email+"'"
                        c.execute(s)
                        i=c.fetchone()
                        request.session['id']=i[0]
                        request.session['name']=i[1]
                        return HttpResponseRedirect("/userhome")
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"login.html",{"msg":msg})
######################################################################
#                     USER REGISTRATION
######################################################################
def registration(request):
    """ 
        The function to register user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """

    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        email=request.POST["txtEmail"]
        phone=request.POST["txtContact"]
        pwd=request.POST["txtPassword"]

        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Email already registered"
        else:
            s="insert into tbluser (uName,uContact,uEmail,uAddress) values('"+str(name)+"','"+str(phone)+"','"+str(email)+"','"+str(address)+"')"
            try:
                c.execute(s)
            except:
                msg=s
            else:
                s="insert into tbllogin (username,password,usertype,status) values('"+email+"','"+pwd+"','user','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login process error"
                else:
                    msg="Registered successfully."

    return render(request,"registration.html",{"msg":msg})

######################################################################
#
#
#                           ADMIN
#
#
######################################################################
######################################################################
#                        LOAD ADMIN HOME PAGE
######################################################################
def adminhome(request):
    """ 
        The function to load home page of the admin. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")
######################################################################
#                        LOAD LOCATION PAGE
######################################################################
def admincategory(request):
    """ 
        The function to load, add and view category. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if request.POST:
        location=request.POST['txtCategory']
        s=f"select count(*) from tblcategory where category='{location}' and status='1'"
        c.execute(s)
        d=c.fetchone()
        if d[0]>0:
            msg="Already exist"
        else:
            s=f"insert into tblcategory(category,status) values('{location}','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Category added"
    data=loadcategory()
    return render(request,"admincategory.html",{"data":data,"msg":msg})
######################################################################
#                        LOAD CATEGORY PAGE
######################################################################
def loadcategory():
    """ 
        The function to load category. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblcategory where status='1'"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                        LOAD CATEGORY PAGE
######################################################################
def adminuser(request):
    """ 
        The function to load user page for admin. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tbluser where uEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminuser.html",{"data":data})
######################################################################
#
#
#                        LOCAL BODY
#
#
######################################################################
######################################################################
#                    LOAD LOCAL BODY HOME PAGE
######################################################################

######################################################################
#                    LOAD NEWS PAGE
######################################################################

######################################################################
#
#
#                            USER
#
#
######################################################################
######################################################################
#                    LOAD USER HOME PAGE
######################################################################
def userhome(request):
    """ 
        The function to load home page of the user. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    qry="select * from tblcategory"
    c.execute(qry)
    category=c.fetchall()
    qry="select * from tblnews order by ndate desc"
    c.execute(qry)
    latest=c.fetchall()[:1]
    if request.POST:
        cat=request.POST['txtCategory']
        date=request.POST['txtDate']
        qry=f"select * from tblnews where catId='{cat}' and cast(ndate as date)=cast('{date}' as date)"
        c.execute(qry)
        latest=c.fetchall()
    qry="select * from tblnews order by ndate desc"
    c.execute(qry)
    popular=c.fetchall()[:10]
    
    return render(request,"userhome.html",{"latest":latest,"popular":popular,"category":category})
######################################################################
#                    LOAD USER HOME PAGE
######################################################################
