from tkinter import *
import time, webbrowser, os, sys, subprocess


#--Home page pimping--
master = Tk()
master.wm_title("Home Menu")
master.geometry('700x500'.format(700, 500))

#-Clock stuff-
time1=''
timea = Label(master,font=("system", 100), height = 3)
timea.grid(row=0,column=0,columnspan=10)
def tick():
    global time1
    time2=time.strftime('%H:%M:%S')
    if time2 != time1:
        time1=time2
        timea.config(text=time2)
    timea.after(200, tick)

def search(h):
    i=""
    f=open('weirddata/test.txt','r')
    for x in f: 
        i=i+x
    f.close
    n= (i.find("p="))+2
    a=i[:n]+h+i[n:]
    e=open("weirddata/test.txt","w")
    e.write(a)
    e.close
    return

def select(k):
    i=""
    f=open('weirddata/test.txt','r')
    for x in f: 
        i=i+x
    f.close
    n= (i.find("?select="))+8
    a=i[:n]+k+i[n:]
    e=open("weirddata/test.txt","w")
    e.write(a)
    e.close
    return

def price(b,w):
    i=""
    f=open('weirddata/test.txt','r')
    for x in f: 
        i=i+x
    f.close
    n= (i.find("max="))+4
    j= (i.find("min="))+4
    a=i[:n]+w+i[n:]
    j=a[:j]+b+a[j:]
    e=open("weirddata/test.txt","w")
    e.write(a)
    e.close
    return

#htop
def htop():
    os.system("gnome-terminal -e 'bash -c \"htop\"'")
              
bhtop = Button(master, text="htop", font=("system", 30), width = 15, height = 4, command=htop)
bhtop.grid(row=1,column=2)

#Uni project

def uniproj():
    uniproj= Tk()
    uniproj.wm_title("Uni Project")
    uniproj.geometry('320x800'.format(320, 800))
    
    labelunipro=Label(uniproj,text="Uni Project",font=("system", 70,"bold"), height = 3)
    labelunipro.grid(row=0,column=0)
   
    def filezilla():
        os.system("gnome-terminal -e 'bash -c \"filezilla\"'")  
    bfilezilla = Button(uniproj, text="Filezilla", font=("system", 30), width = 15, height = 3, command=filezilla)
    bfilezilla.grid(row=2, column=0)
    
    def vmd():
        os.system("gnome-terminal -e 'bash -c \"vmd\"'")  
    bvmd = Button(uniproj, text="vmd", font=("system", 30), width = 15, height = 3, command=vmd)
    bvmd.grid(row=3, column=0)
    
    def kstrfile():
        os.system("gnome-terminal -e 'bash -c \"cd Desktop/Project/KstR \"'")  
    bvmd = Button(uniproj, text="KstR File", font=("system", 30), width = 15, height = 3, command=kstrfile)
    bvmd.grid(row=4, column=0)
    
    
b1 = Button(master, text="Uni Project", font=("system", 30), width = 15, height = 3, command=uniproj)
b1.grid(row=2,column=0)

#Admin button
def admin():
    admin= Tk()
    admin.wm_title("Administ")
    admin.geometry('320x800'.format(320, 800))
    
    labeladmin=Label(admin,text="Administ",font=("system", 70,"bold"), height = 3)
    labeladmin.grid(row=0,column=0)
    
    def outlookemail():
        webbrowser.open('https://outlook.live.com/owa/#wa=wsignin1.0')
    boutlookemail=Button(admin, text="Outlook", font=("system", 30), width = 15, height = 3, command=outlookemail)
    boutlookemail.grid(row=1, column=0)
    
    def studentemail():
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    bstudentemail=Button(admin, text="gmail", font=("system", 30), width = 15, height = 3, command=studentemail)
    bstudentemail.grid(row=2, column=0)
        
b2 = Button(master, text="Admin", font=("system", 30), width = 15, height = 3, command=admin)
b2.grid(row=2,column=1)

#Indie project button
def indieproj():
    indieproj= Tk()
    indieproj.wm_title("Indie Project")
    indieproj.geometry('400x1000'.format(400, 1000))
    
    labelindieproj=Label(indieproj,text="Indie Proj",font=("system", 70,"bold"), height = 3)
    labelindieproj.grid(row=0,column=0)

    def googlechrome():
        os.system("gnome-terminal -e 'bash -c \"google-chrome \"'")  
    bgeneralyahoosearch=Button(indieproj, text="Chrome", font=("system", 30), width = 15, height = 3, command=googlechrome)
    bgeneralyahoosearch.grid(row=1, column=0)
    
    def generalyahoosearch():
        webbrowser.open('http://www.stylezeitgeist.com/forums/showthread.php?3793-auctions-yahoo-co-jp-search-terms')
        webbrowser.open('http://auctions.yahoo.co.jp/')
        webbrowser.open('http://www.fromjapan.co.jp/en/')
    bgeneralyahoosearch=Button(indieproj, text="General Search", font=("system", 30), width = 15, height = 3, command=generalyahoosearch)
    bgeneralyahoosearch.grid(row=2, column=0)
    
    def specificyahoo():
        specificyahoopage=Tk()
        specificyahoopage.wm_title("Specific Yahoo Search")
        specificyahoopage.geometry('600x800'.format(600, 800))
        labeladmin=Label(specificyahoopage,text="Specific Yahoo",font=("system", 70,"bold"), height = 3)
        labeladmin.grid(row=1,column=0,columnspan=3)

        bannd=Button(specificyahoopage, text="AnnD", font=("system", 30), width = 15, height = 2, command=lambda: search("アンドゥムルメステール"))
        bannd.grid(row=2, column=0)

        bricko=Button(specificyahoopage, text="Rick", font=("system", 30), width = 15, height = 2, command=lambda: search("リックオウエンス"))
        bricko.grid(row=3, column=0)

        baltieri=Button(specificyahoopage, text="Altieri", font=("system", 30), width = 15, height = 2, command=lambda: search("アルティエリ"))
        baltieri.grid(row=4, column=0)

        bmargiela=Button(specificyahoopage, text="Margiela", font=("system", 30), width = 15, height = 2, command=lambda: search("マルジェラ"))
        bmargiela.grid(row=5, column=0)

        brafsi=Button(specificyahoopage, text="Raf", font=("system", 30), width = 15, height = 2, command=lambda: search("ラフシモンズ"))
        brafsi.grid(row=6, column=0)

        brafsi=Button(specificyahoopage, text="Nemeth", font=("system", 30), width = 15, height = 2, command=lambda: search("nemeth"))
        brafsi.grid(row=7, column=0)

        brafsi=Button(specificyahoopage, text="Damir", font=("system", 30), width = 15, height = 2, command=lambda: search("damir"))
        brafsi.grid(row=8, column=0)

        brafsi=Button(specificyahoopage, text="Yohji", font=("system", 30), width = 15, height = 2, command=lambda: search("ヨウジヤマモト"))
        brafsi.grid(row=9, column=0)

        brafsi=Button(specificyahoopage, text="Comme", font=("system", 30), width = 15, height = 2, command=lambda: search("ヨウジヤマモト"))
        brafsi.grid(row=10, column=0)

        brafsi=Button(specificyahoopage, text="Miyake", font=("system", 30), width = 15, height = 2, command=lambda: search("イッセイミヤケ"))
        brafsi.grid(row=11, column=0)

        brafsi=Button(specificyahoopage, text="Poell", font=("system", 30), width = 15, height = 2, command=lambda: search("キャロルクリスチャンポエル"))
        brafsi.grid(row=12, column=0)

        brafsi=Button(specificyahoopage, text="Dirk", font=("system", 30), width = 15, height = 2, command=lambda: search("dirk+bikkembergs"))
        brafsi.grid(row=13, column=0)

        brafsi=Button(specificyahoopage, text="Helmut", font=("system", 30), width = 15, height = 2, command=lambda: search("ヘルムートラング"))
        brafsi.grid(row=14, column=0)

        bannd=Button(specificyahoopage, text="Cheapest", font=("system", 30), width = 15, height = 2, command=lambda: select("01"))
        bannd.grid(row=2, column=1)

        baltieri=Button(specificyahoopage, text="Newest", font=("system", 30), width = 15, height = 2, command=lambda: select("22"))
        baltieri.grid(row=3, column=1)

        bannd=Button(specificyahoopage, text="Time", font=("system", 30), width = 15, height = 2, command=lambda: select("05"))
        bannd.grid(row=4, column=1)

        bricko=Button(specificyahoopage, text="10,000", font=("system", 30), width = 15, height = 2, command=lambda: price("0","10000"))
        bricko.grid(row=3, column=2)

        baltieri=Button(specificyahoopage, text="20,000", font=("system", 30), width = 15, height = 2, command=lambda: price("10000","20000"))
        baltieri.grid(row=4, column=2)

        bmargiela=Button(specificyahoopage, text="30,000", font=("system", 30), width = 15, height = 2, command=lambda: price("20000","30000"))
        bmargiela.grid(row=5, column=2)

        brafsi=Button(specificyahoopage, text="40,000", font=("system", 30), width = 15, height = 2, command=lambda: price("30000","40000"))
        brafsi.grid(row=6, column=2)

        brafsi=Button(specificyahoopage, text="50,000", font=("system", 30), width = 15, height = 2, command=lambda: price("40000","50000"))
        brafsi.grid(row=7, column=2)

        def reset():
            l=open("weirddata/test.txt","w")
            l.write("http://auctions.search.yahoo.co.jp/search?select=&p=&ei=UTF-8&oq=&auccat=0&select=22&slider=0&tab_ex=commerce&fixed=0&min=&max=&price_type=currentprice")
            l.close
        brafsi=Button(specificyahoopage, text="Reset", font=("system", 30), width = 15, height = 2, command=reset)
        brafsi.grid(row=10, column=2)

        def searcha():
            l=open("weirddata/test.txt","r")
            t=""
            for x in l:
                t=t+x
            webbrowser.open(t)
            l.close
        brafsi=Button(specificyahoopage, text="Search!", font=("system", 30), width = 15, height = 2, command=searcha)
        brafsi.grid(row=11, column=2)

    bspecificyahoopage=Button(indieproj, text="Specific search", font=("system", 30), width = 15, height = 3, command=specificyahoo)
    bspecificyahoopage.grid(row=3, column=0)
    
    def ehost():
        webbrowser.open('https://login.ehost.com/')
    behost=Button(indieproj, text="ehost login", font=("system", 30), width = 15, height = 3, command=ehost)
    behost.grid(row=4, column=0)    
	
b3 = Button(master, text="Indie Project", font=("system", 30), width = 15, height = 3, command=indieproj)
b3.grid(row=2,column=2)    
    
#Rereational button
def recreational():
    recreational= Tk()
    recreational.wm_title("Recreational")
    recreational.geometry('400x800'.format(400, 800))
	
    labelrecreational=Label(recreational,text="Recreational",font=("system", 70,"bold"), height = 3)
    labelrecreational.grid(row=1,column=0)
	
    def gimp():
        os.system("gnome-terminal -e 'bash -c \"gimp \"'")  
    bgeneralyahoosearch=Button(recreational, text="GIMP", font=("system", 30), width = 15, height = 3, command=gimp)
    bgeneralyahoosearch.grid(row=2, column=0)

    def notepadqqo():
        os.system("gnome-terminal -e 'bash -c \"notepadqq \"'")  
    bgeneralyahoosearch=Button(recreational, text="Notepadqq", font=("system", 30), width = 15, height = 3, command=notepadqqo)
    bgeneralyahoosearch.grid(row=3, column=0)

    def shuttero():
        os.system("gnome-terminal -e 'bash -c \"shutter \"'")  
    bgeneralyahoosearch=Button(recreational, text="Shutter", font=("system", 30), width = 15, height = 3, command=shuttero)
    bgeneralyahoosearch.grid(row=4, column=0)
b4 = Button(master, text="Recreational", font=("system", 30), width = 15, height = 3, command=recreational)
b4.grid(row=2,column=3)

def updateme():
    os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
              
bupdate = Button(master, text="Update", font=("system", 30), width = 15, height = 4, command=updateme)
bupdate.grid(row=4,column=1)

def terminalopen():
    os.system("gnome-terminal")   

btermin = Button(master, text="Terminal", font=("system", 30), width = 15, height = 4, command=terminalopen)
btermin.grid(row=4,column=2)





tick()
master.mainloop()
