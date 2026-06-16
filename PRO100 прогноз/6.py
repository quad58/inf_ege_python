import turtle as t
t.tracer(0)
t.screensize(3000, 3000)
r = 30

for i in range(3):
    t.forward(7*r); t.right(90); t.forward(12*r); t.right(90)
t.up()
t.forward(4*r); t.right(90); t.forward(6*r); t.left(90)
t.down()
for i in range(4):
    t.forward(83*r); t.right(90); t.forward(77*r); t.right(90)
t.up()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x*r, y*r); t.dot(3)

print(8*13 - 4*7 + 84*78)
t.done()