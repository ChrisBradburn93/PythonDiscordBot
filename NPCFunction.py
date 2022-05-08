import json
from msilib.schema import Class
import random



def NPCCall():

    with open('NPC.json') as n:
        data = json.load(n)
    Male_FN = data["Dragonborn_Male_Fname"]
    Female_FN = data["Dragonborn_Female_Fname"]
    LN = data["Dragonborn_Lname"]
    CL = data["Class"]

    return (random.choice(Male_FN)+" "+ (random.choice(LN)+" is a "+(random.choice(CL))))
 
