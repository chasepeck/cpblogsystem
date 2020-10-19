import os
from graphics import *

window = GraphWin("cpblogsystem", 500, 500)
menustate = "mainmenu"

def newpost(override_overwriting):
    postdate = input("Enter date of post: ")
    postname = input("Enter name of post: ")
    overwriting = override_overwriting
    headertext = """<!DOCTYPE html>
    <html>
        <head>
            <title>your blog ("""+postdate+""")</title>
            <meta charset="UTF-8">
            <style>
                body {
                    background-color: blue;
                }
            </style>
        </head><body>
        <div class="blog" style="padding-left: 80px; padding-right: 80px;"><p>"""
    footertext = """</p>
    </div>
    </body>
    </html>"""
    if os.path.exists("blog/"+postname+".html") and override_overwriting == False:
        print("WARNING! Blog post already exists. Are you sure you want to overwrite it? y/n")
        _x = input()
        overwriting = True
        if not "y" in _x:
            return
    elif not os.path.exists("blog/"+postname+".html") and override_overwriting == True:
        print("Post does not exist!")
        return
    blogfile=open("blog/"+postname+".html","w")
    blogtable=open("blog/blogtable.txt","a")
    print("Type your HTML post:")
    content = input()
    towrite = headertext+content+footertext
    blogfile.write(towrite)
    if overwriting == False:
        blogtable.write("\n"+postdate+"_"+postname)
    if override_overwriting:
        print("Edited post!")
    else:
        print("Created post!")
    blogfile.close()
    blogtable.close()

def delpost():
    postdate = input("Enter date of post to delete: ")
    postname = input("Enter name of post to delete: ")
    os.remove("blog/"+postname+".html")
    blogtable=open("blog/blogtable.txt","r")
    btlines = blogtable.readlines()
    blogtable.close()
    blogtable=open("blog/blogtable.txt","w+")
    output=[]
    for line in btlines:
        if line!=str(postdate+"_"+postname):
            output.append(line)
    blogtable.writelines(output)
    print("Deleted!")
    blogtable.close()

def drawmenu():
    global menustate
    if menustate=="mainmenu":
        text = Text(Point(250,250),"""1. New Post
2. Delete Post
3. Edit Post
4. Quit""")
        text.draw(window)
        while True:
            key = window.getKey()
            if key == "1":
                menustate="newpost"
                text.undraw()
                drawmenu()
            elif key == "2":
                menustate="delpost"
                text.undraw()
                drawmenu()
            elif key == "3":
                menustate="editpost"
                text.undraw()
                drawmenu()
            elif key == "4":
                break
    if menustate=="newpost":
        text = Text(Point(100,250),"""Name of post:
Date of post: """)
        text.draw(window)

        box1 = Entry(Point(250,250),10)
        box1.draw(window)
        box2 = Entry(Point(250,300),10)
        box2.draw(window)
        submitbox = Rectangle(Point(125,350),Point(375,450))
        submitbox.draw(window)
        submitbox.setFill("blue")
        submittext = Text(Point(250,400),"Submit")
        submittext.draw(window)
        submittext.setTextColor("white")
        while True:
            mouseclick = window.getMouse()
            if mouseclick.getY() > 350:
                box1text = box1.getText()
                box2text = box2.getText()
                print(str(box1text)+str(box2text))
                text.undraw()
                box1.undraw()
                box2.undraw()
                submitbox.undraw()
                submittext.undraw()
                menustate="mainmenu"
                drawmenu()
                break
drawmenu()