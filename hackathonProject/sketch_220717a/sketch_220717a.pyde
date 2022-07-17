import time
import json
from subprocess import Popen

def setup():
    global bg, tlt, tb, articles
    articles = []
    products = []
    size(800, 600)
    
    #loading assets
    bg = loadImage("gradient.png")
    tlt = loadImage("amazon_title.PNG")
    textFont(createFont("AmazonEmber_Lt.ttf", 24))
    
    #configuring loaded assets
    s = 200
    tlt.resize(s, (336/800) * s)
    
    #instantiate objects/classes
    tb = textbox(240, 25, 500, 25)
    
    x, y = 20, 120
    for i in range(10):
        articles.append(article(x, y ,"product", "price"))
        y += 45
        
def readfile(dir):
    f = open(dir, "r")
    raw = f.readlines()
    f.close()
    
    return raw

def writefile(dir, c):
    f = open(dir, "w")
    raw = f.write(str(c))
    f.close()
    
    return raw

def run(dir):
    return launch(dir)

def executebot():
    global articles, tb, time
    writefile("C:/Users/mikep/workspace_python/amazon_scrapper_bot/cmds.txt", tb.txt)
    run("C:/Users/mikep/workspace_python/amazon_scrapper_bot/main.exe")
    time.sleep(5)
    try:
        data = readfile("C:/Users/mikep/workspace_python/amazon_scrapper_bot/product_profiles.txt")
        for i in range(10):
            t = data[i].strip(")(\n")[1:].split("',")[0]
            p = data[i].strip(")(\n")[1:].split("',")[1]
            if len(t) > 70: 
                articles[i].title = t[:70] + " . . ."
            else: 
                articles[i].title = t
            articles[i].price = p
    except:
        exit()

        
def draw():
    image(bg, 0, 0)
    image(tlt, 0, 0)
    tb.show()
    for i in articles:
        i.show()

class textbox():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.txt = ""
        self.selector = ""
        self.active = False
        self.curTime = time.time()

    def show(self):
        textAlign(LEFT, CENTER)
        textSize(24)

        fill(255)
        if self.active:
            pass
            
        if self.txt == "":
            text("search" + self.selector, self.x, self.y)
        else:
            text(self.txt  + self.selector, self.x, self.y)
        
        stroke(255)    
        line(self.x - 5, self.y + self.h/2 + 10, self.x + self.w + 5, self.y + self.h/2 + 10)
        
        noFill()
        ellipse(self.x + self.w - 10, self.y + 2, 10, 10)
        line(self.x + self.w - 6, self.y + 6, self.x + self.w, self.y + 12)
        
        if self.active:
            blink = 0.5
            elaTime = time.time() - self.curTime
            
            if elaTime > blink:
                self.curTime = time.time()
                if self.selector == "":
                    self.selector = "|"
                else:
                    self.selector = ""
        else:
            self.selector = ""
            
    def toggle_active(self, mx, my):
        if (mx > self.x and mx < self.x + self.w) and (my > self.y and my < self.y + self.h):
            self.active = True
        else:
            self.active = False

    def type_txt(self, k, kc):
        self.curTime = time.time()
        if self.active == True:
            if kc == 10:
                executebot()
            elif kc == 8:
                self.txt = self.txt[:len(self.txt)- 1]
            else:
                if len(self.txt) < 45:
                    self.txt += str(k)
                    
    def selected(self):
        if self.active == True:
            pass
            
class article():
    
    def __init__(self, x, y, title, price):
        self.x = x
        self.y = y
        self.w = 725
        self.h = 25
        self.title = title
        self.price = price
        
    def show(self):
        textAlign(LEFT, CENTER)
        textSize(18)
        
        fill(105)
        text(self.title, self.x, self.y)
        
        textAlign(RIGHT, CENTER)
        
        text(self.price, self.x + self.w, self.y)
        
        stroke(105)
        line(self.x - 5, self.y + self.h/2 + 10, self.x + self.w + 5, self.y + self.h/2 + 10) 
            
def mouseClicked():
    global tb
    tb.toggle_active(mouseX, mouseY)

def keyPressed():
    global tb
    tb.type_txt(key, keyCode)
