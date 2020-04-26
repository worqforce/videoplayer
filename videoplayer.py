print("Loading plugin videoplayer.py...")
import os
from tkinter import *

print("Starting videoplayer")
if not os.path.isdir("./video/"):
    os.system("mkdir video")
    print("CREATED VIDEO FOLDER")
if not os.path.isdir("./server/videoplayercache"):
    os.system("mkdir ./server/videoplayercache")
    print("CREATED VIDEOPLAYERCACHE FOLDER")

def status(stext):
    openedfile=open("./server/stat.set", "w+")
    openedfile.write(stext)
    openedfile.close()

def generatevideopage():
    if os.path.isfile("./server/videoplayercache/setup.html"):
        os.system("rm ./server.html")
        os.system("cp ./server/videoplayercache/setup.html ./setup.html")
    status("Generating video Page...")
    os.system("rm -rf ./video/.DS_Store")
    os.system("rm -r ./videohtml")
    os.system("mkdir ./videohtml")
    dircontent=os.listdir("./video")
    print(dircontent)
    numdircontent=len(dircontent)
    index=0
    openedfile=open("./videoin.html", "w+")
    openedfile.write("""<style>
    body { background-color: clear;}
</style>
<head>
    <link rel="stylesheet" href="./ui/css/video.css">
</head>\n
<script>document.addEventListener('contextmenu', event => event.preventDefault());</script>
<div class="noclassinf"><h1>Your Videos</h1>""")
    while True:
        selectedfile=dircontent[index]
        selectedfileedit=selectedfile
        selectedfileedit=selectedfileedit.replace(".mp3", "")
        selectedfileedit=selectedfileedit.replace(".wav", "")
        selectedfileedit=selectedfileedit.replace(".mp4", "")
        selectedfileedit=selectedfileedit.replace(".ogg", "")
        selectedfileedit=selectedfileedit.replace(".png", "")
        selectedfileedit=selectedfileedit.replace(".jpeg", "")
        selectedfileedit=selectedfileedit.replace(".jpg", "")
        selectedfile=selectedfile.replace("'", "´")
        selectedfile=selectedfile.replace('"', "´´")
        openedfile.write("""<button onclick="location.href='./videohtml/""" + selectedfileedit +""".html'" type="button" frameBorder="2">""" + selectedfileedit +"""</button>\n""")
        index=index + 1
        if index == numdircontent:
            break
    openedfile.write("</div>")
    openedfile.close()
    index=0
    while True:
        selectedfile=dircontent[index]
        selectedfileedit=selectedfile
        selectedfileedit=selectedfileedit.replace(".mp3", "")
        selectedfileedit=selectedfileedit.replace(".wav", "")
        selectedfileedit=selectedfileedit.replace(".mp4", "")
        selectedfileedit=selectedfileedit.replace(".ogg", "")
        selectedfileedit=selectedfileedit.replace(".png", "")
        selectedfileedit=selectedfileedit.replace(".jpeg", "")
        selectedfileedit=selectedfileedit.replace(".jpg", "")
        selectedfile=selectedfile.replace("'", "´")
        selectedfile=selectedfile.replace('"', "´´")
        openedfile=open("./videohtml/" + selectedfileedit + ".html", "w+")
        openedfile.write("""<style>
    body { background-color: clear;}
</style>
<script>document.addEventListener('contextmenu', event => event.preventDefault());</script>
""")
        openedfile.write("""<video\n
 controls controlsList='nodownload' width="100%" height="100%" autoplay\n
src= '../video/""" + selectedfile + """'
Your browser does not support SONX.>
</video>""")
        openedfile.close()
        index=index + 1
        if index == numdircontent:
            break
    
    os.system("cp ./setup.html ./server/videoplayercache/setup.html")
    setupfile=open("./setup.html", "r")
    setupfilecont=setupfile.read()
    setupfile.close()
    setupfile=open("./setup.html", "w+")
    setupfile.write(setupfilecont)
    setupfile.write("""\n
    <a href="./video.html"><h1>Your Videos</h1></a>""")
    setupfile.close()
    videopage=open("./video.html", "w+")
    videopage.write("""<head>
    <link rel="stylesheet" href="./ui/css/index.css">
</head>
<script>document.addEventListener('contextmenu', event => event.preventDefault());</script>
<body>
<link rel="stylesheet" href="./ui/css/index.css">
<title>SONX</title>
    <a href="./index.html"><div class="menu"><img alt="Home" src="./ui/sonx.png" width=100" height="70"></img></div></a>
    <a href="./support.html"><div class="sup"><img alt="Support SONX" src="./ui/support.png" width=100" height="70"></img></div></a>
    <a href="./setup.html"><div class="set"><img alt="Setup" src="./ui/setup.png" width=100" height="70"></img></div></a>
    <a href="./about.html"><div class="abb"><img alt="About" src="./ui/about.png" width=100" height="70"></img></div></a>
<div class="frm">
<iframe src="./videoin.html" width=100% height="100%" frameBorder="0"></iframe>
</div>
</body>
""")
    
def statusreport():
    openedfile=open("./server/stat.set", "r")
    openedfileread=openedfile.read()
    openedfile.close()
    if openedfileread==("OFF"):
        videopl.destroy()
    videopl.after(1000, statusreport)


videopl=Tk()
videopl.title("videoplayer plugin for SONX")
infotext=Label(videopl, text="videoplayer plugin for SONX\nPress 'Generate' to generate a new video page.")
genbutton=Button(videopl, text="Generate", command=generatevideopage)

infotext.pack()
genbutton.pack()
statusreport()
videopl.mainloop()