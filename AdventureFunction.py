import json
import random



def AdventureCall():

    with open('Adventure.json') as a:
        data = json.load(a)
    P = data["Place"]
    AT = data["AdjectiveTense"]
    AO = data["AdjectiveOwner"]
    EP = data["EnemyPrefix"]
    ET = data["EnemyType"]
    C = data["Crime"]
    V = data["Victims"]
    EA = data["EventAdjective"]

    return "You are tasked with seeking out the "+(random.choice(EA)+" at the " + (random.choice(AO)+" "+(random.choice(AT)+" "+(random.choice(P)+". There have been rumours that a "+(random.choice(EP)+" "+(random.choice(ET))+ " has been "+(random.choice(C))+" "+(random.choice(V))+".")))))
