import turtle as t
t.screensize(3000, 3000)
r = 30

t.right(315)
for i in range(12):
    t.forward(11*r); t.right(45)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*r, y*r); t.dot(5);

t.done()
# 88