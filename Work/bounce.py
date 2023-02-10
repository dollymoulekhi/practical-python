# Exercise 1.5: The Bouncing Ball
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
#  it bounces back up to 3/5 the height it fell. Write a program bounce.py 
# that prints a table showing the height of the first 10 bounces.

initial_height=100
# get 10 bounces height

for i in range(10):
    h_new=3/5*(initial_height)
    initial_height=h_new
    print('Height after every bounce',round(h_new,2))


