from sys import argv
import os
script, postdate, postname = argv
overwriting = False
headertext = """
<!DOCTYPE html>
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
    <div class="blog" style="padding-left: 80px; padding-right: 80px; line-height: 44px;"><p>
"""
footertext = """
</p>
</div>
</body>
</html>
"""
if os.path.exists("blog/"+postdate+".html"):
    print("WARNING! Blog post already exists. Are you sure you want to overwrite it? y/n")
    _x = input()
    overwriting = True
    if not "y" in _x:
        raise Exception("Cancelled")
blogfile=open("blog/"+postdate+".html","w")
blogtable=open("blog/blogtable.txt","a")
print("Type your HTML post:")
content = input()
towrite = headertext+content+footertext
blogfile.write(towrite)
if overwriting == False:
    blogtable.write("\n"+postdate+"_"+postname)