from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
import mysql.connector as mysql
def home(req):
      return HttpResponse("""
      <style>
               *{margin:0px}
               #header{height:10%;width:100%;background:black;}
               #title{height:100%;width:93%;background-image:url('https://cutewallpaper.org/21/vintage-musical-backgrounds/Music-background-with-rose-and-notes-Stock-image-Colourbox.jpg');background-repeat:no-repeat;background-size:cover;background-height:100%;float:right;color:white;}
               .dropbtn{height:100%;width:100%;font-size:6px;background-color: #000000;color:#666633;padding:17px;float:left;color:white;font-weight:bold;}
               .dropdown{position: relative;display: inline-block;}
               .dropdown-content{display: none;position: absolute;background-color: #999999;}
               .dropdown-content a{color: black;padding: 10px 20px;text-decoration: none;display: block;}
               .dropdown-content a :hover {background-color: #66CCFF;}
               .dropdown:hover  .dropdown-content {display: block;}
               .dropdown:hover  .dropbtn {background-color:#669966 ;}
               #player{height:90%;width:100%;background-image:url('https://i.pinimg.com/originals/7b/9e/f0/7b9ef0b3430c5f7ae348314c2d76cb81.jpg');background-repeat:no-repeat;background-size:100%;}
               #sec1{height:5%;width:100%;background-image:url('https://wallpaperaccess.com/full/2271516.jpg');background-repeat:no-repeat;background-size:100%;}
               #sec2{height:5%;width:100%;background-image:url('https://wallpaperaccess.com/full/2271516.jpg');background-repeat:no-repeat;background-size:100%;float:right;}
               #sec3{height:5%;width:100%;background-image:url('https://wallpaperaccess.com/full/2271516.jpg');background-repeat:no-repeat;background-size:100%;float:right;}
               #sec4{height:5%;width:100%;background-image:url('https://wallpaperaccess.com/full/2271516.jpg');background-repeat:no-repeat;background-size:100%;float:right;}
               #sec5{height:5%;width:100%;background-image:url('https://wallpaperaccess.com/full/2271516.jpg');background-repeat:no-repeat;background-size:100%;float:right;}
               #sec6{height:5%;width:100%;background-image:url('https://wallpaperaccess.com/full/2271516.jpg');background-repeat:no-repeat;background-size:100%;float:right;}
               #subsec1{height:30%;width:25%;background-image:url('https://c8.alamy.com/comp/DRPKHA/abstract-background-of-music-notes-DRPKHA.jpg');background-repeat:no-repeat;background-size:100%;float:left;}
               #subsec2{height:30%;width:25%;background:black;float:left;}
               #subsec3{height:30%;width:25%;background:yellow;float:left;}
               #subsec4{height:30%;width:25%;background:blue;float:left;}
               #subsec5{height:30%;width:25%;background:violet;float:left;}
               #contentimage{height:80%;width:100%;background:white;}
               #name{height:20%;width:100%;background:#c0c0c0;}
      </style>
      <body>
      
           <div id="header">
           
                    <div id="title">
                           <center><h2 style="font-family:red serif;font-style:normal;font-size:35px;font-weight:bold;letter-spacing:3px;">BEATS PLAYER</h2></center>
                   </div>
                    
                   <div class="dropdown">
                      <center><button class="dropbtn" ">MENU</button></center>
                      <div class="dropdown-content">
                             <a href="/login">Login</a>
                             <a href="/music/about">About us</a>
                             <a href="/music/version">Version</a>
                             <a href="/music/contact">Contact us</a>
                  </div>              
                                   
                  
                </div>
                  
           </div>
           
           <div>
                 <div id="player" >
                 
                       <div id="sec1"   ><h2 style="font-family:monospace;font-weight:bolt;">Top Stories</h2>
                       </div>
                       <div id="subsec1"  >
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/084/Attack-Hindi-2022-20220313112514-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/ik-tu-hai-%e2%9d%a4%ef%b8%8f/HiYTcll9eQQ">Ik Tu Hai</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec2">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/513/Classmates-Marathi-2014-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                      <center><h3 style="font-family:cursive;font-weight:bolt;"> <a href="https://www.jiosaavn.com/song/teri-meri-yaariyan/Ij8dVRdbAGw">Teri Meri Yaariyan </a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec3">
                                <div id="contentimage">
                                      <img src="https://c.saavncdn.com/752/Left-and-Right-Feat-Jung-Kook-of-BTS-English-2022-20220909020415-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/left-and-right-feat.-jung-kook-of-bts/JCUhBSZgT34">Left and Right</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec4">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/256/Shree-Hanuman-Chalisa-Hanuman-Ashtak-Hindi-2016-500x500.jpg

" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/album/shree-hanuman-chalisa-hanuman-ashtak/-nkzmBWD3rA_">Shree Hanuman Chalisa</a></h3></center>
                              </div>
                       </div>
                       
                       
                       
                       <div id="sec2" ><h2 style="font-family:monospace;font-weight:bolt;">Bollywood Songs</h2>
                       </div>
                       
                       <div id="subsec1">
                             <div id="contentimage">
                                      <img src="https://c.saavncdn.com/238/Shershaah-Original-Motion-Picture-Soundtrack--Hindi-2021-20210815181610-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://c.saavncdn.com/238/Shershaah-Original-Motion-Picture-Soundtrack--Hindi-2021-20210815181610-500x500.jpg">Raataan Lambiyan  </a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec2">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/633/Har-Har-Shambhu-Shiv-Mahadeva-Hindi-2022-20220502205548-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/har-har-shambhu-shiv-mahadeva-feat.-abhilipsa-panda/AF0xWxsDAR4">Har Har Shambhu Shiv Mahadeva</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec3">
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/768/Bas-Tum-Mere-Paas-Raho-Hindi-2022-20220125103321-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/bas-tum-mere-paas-raho/Pz8AWwdfDmI">Bas Tum Mere Paas Raho </a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec4">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/592/KGF-Chapter-2-Hindi-2022-20220415034804-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                      <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/falak-tu-garaj-tu/KQ0jeSwAc2s">Falak Tu Garaj Tu</a></h3></center>
                              </div>
                       </div>
                       
                       
                       
                       <div id="sec3"><h2 style="font-family:monospace;font-weight:bolt;">Artist</h2>
                       </div>
                       
                       <div id="subsec1">
                                <div id="contentimage">
                                      <img src="https://c.saavncdn.com/artists/Arijit_Singh_500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/artist/arijit-singh/LlRWpHzy3Hk_">| Arijit Singh |</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec2">
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/artists/Neha_Kakkar_006_20200822042626_500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/artist/neha-kakkar/EkEBV7JAU-I_">Neha Kakkar </a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec3">
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/artists/Justin_Bieber_005_20201127112218_500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/artist/justin-bieber/deJJWFd1ItE_">Justin Bieber</a></h3></center>
                              </div>     
                       </div>
                       
                       <div id="subsec4">
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/artists/Atif_Aslam_500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/artist/atif-aslam/MXn8bhT308U_">Atif Aslam</a></h3></center>
                              </div>
                       </div>
                       
                       
                       <div id="sec4"><h2 style="font-family:monospace;font-weight:bolt;">English Songs</h2>
                       </div>
                       
                       <div id="subsec1">
                                 <div id="contentimage">
                                      <img src="https://c.saavncdn.com/editorial/logo/TheAlanWalkerplaylist_20201110053647.jpg?bch=1665389839" height=100% width=100% >
                              </div>
                              <div id="name">
                                      <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/featured/lets-play---alan-walker/277qKJrlBTo_">Lets Play.....</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec2">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/070/Sorry-English-2021-20210125151204-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href=" https://www.jiosaavn.com/song/sorry/AiwueUxSe3s">Sorry --</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec3">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/624/Se-orita-English-2019-20190822022326-500x500.jpg

" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/senorita/I1sPdgJoZFE">Señorita</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec4">
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/896/Dusk-Till-Dawn-Radio-Edit--English-2017-20170905191749-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/dusk-till-dawn-radio-edit/IxAPfStmeQU">Dusk Till Dawn  </a><h3><center>
                              </div>
                       </div>
                       
                       
                       
                       <div id="sec5"><h2 style="font-family:monospace;font-weight:bolt;">Marathi Songs</h2>
                       </div>
                       
                       <div id="subsec1">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/116/Har-Har-Mahadev-Marathi-2022-20221007165606-500x500.jpg" height=100% width=100% >
                              </div>
                              
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/wah-re-shiva/LwtfBkJlD3Q">Wah Re Shiva</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec2">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/601/Boyz-3-Marathi-2022-20220809110359-500x500.jpg

" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/lagnalu-2.0/FBg5HD8BVFg">Lagnalu 2.0</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec3">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/771/Chandramukhi-Marathi-2022-20220428175059-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/chandra/ABJbUz97fEA">Chandra</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec4">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/994/Pawankhind-Marathi-2022-20220216231853-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/song/shwasat-raja-dhyasat-raja/B1EvUEddAX8">Shwasat Raja Dhyasat Raja</a></h3></center>
                              </div>
                              
                       </div>
                       
                                                               
                       <div id="sec6"><h2 style="font-family:monospace;font-weight:bolt;">Devotional Songs</h2>
                       </div>
                       
                       <div id="subsec1">
                              <div id="contentimage">
                                      <img src="https://c.saavncdn.com/editorial/logo/MTPOmNamahShivayhindiJaiShivShankar_20200611075405.jpg?bch=1665629560" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/featured/om-namah-shivay/jPV1FR8whUluOxiEGmm6lQ__">Om Namah Shivay</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec2">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/211/Shiv-Tandav-Stotram-Har-Har-Shiv-Shankar--Hindi-2021-20210709031001-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/album/shiv-tandav-stotram-har-har-shiv-shankar/ze4eTF8HXV0_">Shiv Tandav Stotram </a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec3">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/716/Radhe-Radhe-Hindi--Hindi-2020-20200911113300-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href="https://www.jiosaavn.com/album/radhe-radhe/4wDkHA,beys_">Radhe Radhe</a></h3></center>
                              </div>
                       </div>
                       
                       <div id="subsec4">
                               <div id="contentimage">
                                      <img src="https://c.saavncdn.com/610/Achyutam-Keshavam-Krishna-Damodaram-Zee-Music-Devotional-Hindi-2019-20190402064504-500x500.jpg" height=100% width=100% >
                              </div>
                              <div id="name">
                                       <center><h3 style="font-family:cursive;font-weight:bolt;"><a href=" https://www.jiosaavn.com/album/achyutam-keshavam-krishna-damodaram---zee-music-devotional/GY7aMeAzR6E_">Achyutam Keshavam Krishna Damodaram</a></h3></center>
                              </div>
                       </div>
                       
                       
                 
                 </div>
           </div>
                  
           
      </body>
""")

def about(req):  
           return render (req,'about.html',{ })
         
def version(req):  
           return render (req,'version.html',{ })
           
def contact(req):  
           return render (req,'contact.html',{ })
           
def contact_insert(req):
        name= req.GET.get("name")
        email= req.GET.get("Email")
        msg= req.GET.get("Message")
        
        
#Establish connection wd the database.
        conn =              mysql.connect(host="localhost",user="root",password="welcome123@",database="music")
        cr=conn.cursor()
        query="insert into contact values('{0}','{1}','{2}')".format(name,email,msg) 
        cr.execute(query)
        conn.commit()
        return redirect('/music/contact') 
        
