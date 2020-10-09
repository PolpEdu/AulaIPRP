from turtle import *

# forward()
# left()
# backward()

color('red', 'yellow')
begin_fill()
while True:
    print(heading())  # degrees
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
