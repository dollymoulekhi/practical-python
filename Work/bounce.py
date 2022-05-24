# bounce.py
#
# Exercise 1.5
height=100 # in meters

# new_height=3/5* height # should be insie loop

# have to show the height of 1st 10 bounces

no_of_bounces=1

while no_of_bounces<=10:
    print('no_of_bounces',no_of_bounces)
    print('height of bounce',height)
    height=round(3* (height)/5.0,2)
    no_of_bounces=no_of_bounces+1
