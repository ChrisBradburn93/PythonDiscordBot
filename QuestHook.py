import json
import random

with open('places.json') as d:
        data = json.load(d)
P = data["Place"]
AT = data["AdjectiveTense"]
AO = data["AdjectiveOwner"]
EP = data["EnemyPrefix"]
ET = data["EnemyType"]

print ("You are tasked with seeking out the disturbance at the " + (random.choice(AO)+" "+(random.choice(AT)+" "+(random.choice(P)+". There have been rumours that a "+(random.choice(EP)+" "+(random.choice(ET))+ " has been spotted in the area.")))))