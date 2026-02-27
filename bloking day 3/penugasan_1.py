import turtle

t = turtle. Turtle()
t.speed(3)

def persegi_panjang(panjang, lebar):
    for i in range(2):
        t.forward(panjang)
        t.right(90)
        t.forward(lebar)
        t.right(90)

def segitiga(sisi):
    for i in range(3):
        t.forward(sisi)
        t.right(120)

def trapesium(a, b, tinggi):
    t.forward(a)
    t.right(90)
    t.forward(tinggi)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(tinggi)
    t.right(90)

def jajar_genjang(sisi, alas):
    t.forward(alas)
    t.right(60)
    t.forward(sisi)
    t.right(120)
    t.forward(alas)
    t.right(60)
    t.forward(sisi)

def belah_ketupat(sisi):
    for i in range(2):
        t.forward(sisi)
        t.right(60)
        t.forward(sisi)
        t.right(120)

persegi_panjang(150, 80)
t.penup()
t.goto(-200, 0)
t.pendown()
segitiga(100)

turtle.done()