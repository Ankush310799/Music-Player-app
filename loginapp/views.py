from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import mysql.connector as mysql

# Create your views here.
def  login(req):
      return render (req,'login.html',{ })   


def  Regi(req):
      return HttpResponse("""
      
      <center><h4>New Registration</h4></center>
      <body style="background:#f5f5dc;"><center><form action="insert">
      <table>
      <tr>
            <td>Name </td>
            <td><input type="text"  name="name"><br></td>
            
       </tr>
       
       <tr>
            <td>Email</td>
            <td><input type="email"  name="Email"><br></td>
            
       </tr>
       <tr>     
            <td>Password</td>
            <td><input type="text" name="Password"><br></td>
       </tr>
       <tr>     
            <td>Mobile Number</td>
            <td><input type="number" name="mobile"><br></td>
       </tr>
       
       
       <tr>
             <td><input type="submit" value="Registration"></td>
       </tr>
       
      
      </table>
      </form></center>
      </body>
      
""")

def  logintask(req):
       
        email=req.GET.get("Email")
        password=req.GET.get("Password")
        
        conn =              mysql.connect(host="localhost",user="root",password="welcome123@",database="music")
        cr= conn.cursor()
        cr.execute("select * from uservalues")
        
        
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
        <body style="background:#8EE8EE;">
        <h5><a href="music/home"><-Back To Home</a></h5>
        <center><h4>Login Successful !</h4></center>     
         </body>
         """) 
def insert(req):
        name= req.GET.get("name")
        email= req.GET.get("Email")
        password= req.GET.get("Password")
        numbers= req.GET.get("mobile")
        
#Establish connection wd the database.
        conn =              mysql.connect(host="localhost",user="root",password="welcome123@",database="music")
        cr=conn.cursor()
        query="insert into uservalues values('{0}','{1}','{2}',{3})".format(name,email,password,numbers) 
        cr.execute(query)
        conn.commit()
        return redirect('/login')  
      

