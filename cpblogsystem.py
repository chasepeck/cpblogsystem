import os
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
        <div class="blog" style="padding-left: 80px; padding-right: 80px; line-height: 44px;"><p>"""
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

def mainmenu():
    print("""cpblogsystem
    1. New post
    2. Delete post
    3. Edit post
    4. Quit""")
    _x = str(input("?"))
    if _x == "1":
        newpost(False)
    elif _x == "2":
        delpost()
    elif _x == "3":
        newpost(True)
    elif _x == "4":
        exit()

while True:
    mainmenu()