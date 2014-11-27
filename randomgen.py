#!/user/bin/python
import random

def generate_random(x,y):
    li=[]
    for i in range(150):
        li.append(round(random.uniform(x,y),1))

    return li

print generate_random(1.3,6.7)
print generate_random(1.2,7.9)
print generate_random(3.5,9.8)
print generate_random(2.4,8.7)
