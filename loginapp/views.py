from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import mysql.connector as mysql

# Create your views here.
def  login(req):
      return render (req,'login.html',{ })   


def  Regi(req):
      return render (req,'regi.html',{ })

def  logintask(req):
       
        email=req.GET.get("Email")
        password=req.GET.get("Password")
        
        conn =              mysql.connect(host="localhost",user="root",password="welcome123@",database="music")
        cr= conn.cursor()
        cr.execute("select * from user")
        
        
        while True:
            row=cr.fetchone()
            print(row)
            
            if row is None:
                 break;
            elif row[1]==email and row[2]==password:
                 return  redirect('/msg')
        return redirect('/login')
      
def msg(req):
        return HttpResponse("""
        <body style="background-image:url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlf_K781m4pyPb1qEiur9ht8LTUC9rtE9NaKoOPS1cQvjbL_6COaEwQTJPoj6P9uka4tY&usqp=CAU');background-repeat:no-repeat;background-size:cover;">
        <h4><a href="music/home"><-Back To Home</a></h4>
        <center><h2>Login Successful !</h2></center>     
         </body>
         """) 
def insert(req):
        name= req.GET.get("name")
        email= req.GET.get("Email")
        password= req.GET.get("Password")
        repassword=req.GET.get("RePassword")
        numbers= req.GET.get("Mobile")
        
#Establish connection wd the database.
        conn =              mysql.connect(host="localhost",user="root",password="welcome123@",database="music")
        cr=conn.cursor()
        query="insert into user values('{0}','{1}','{2}','{3}',{4})".format(name,email,password,repassword,numbers) 
        cr.execute(query)
        conn.commit()
        return redirect('/login')  
      

