import json
import random



def NPCCall():

    with open('NPC.json') as n:
        data = json.load(n)
    FN = data["FName"]
    LN = data["LName"]

    return (random.choice(FN)+" "+ (random.choice(LN)+" is a NPC "))