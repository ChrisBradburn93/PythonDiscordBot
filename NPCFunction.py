import json
from msilib.schema import Class
import random
import os
from tarfile import GNUTYPE_LONGLINK

CL = [ "Artificer",
        "Barbarian",
        "Bard",
        "Blood Hunter",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard"
     ]
Gender = ["Male", "Female"]
Race =  [ "Dragonborn",
          "Elf"
        ]

def NPCCall():

    with open('NPC.json') as n:
        data = json.load(n)
    DBMale_FN = data["Dragonborn_Male_Fname"]
    DBFemale_FN = data["Dragonborn_Female_Fname"]
    DBLN = data["Dragonborn_Lname"]

    HMMale_FN = data["Human_Male_Fname"]
    HMFemale_FN = data[ "Human_Female_Fname"]
    HMLN = data["Human_Lname"]

    ELMale_FN = data[ "Elf_Male_Fname"]
    ELFemale_FN = data["Elf_Female_Fname"]
    ELLN = data["Elf_Lname"]

    DWMale_FN = data["Dwarf_Male_Fname"]
    DWFemale_FN = data["Dwarf_Female_Fname"]
    DWLN = data["Dwarf_Lname"]

    GNMale_FN = data["Gnome_Male_Fname"]
    GNFemale_FN = data["Gnome_Female_Fname"]
    GNLN = data["Gnome_Lname"]

    HFMale_FN = data["Halfling_Male_Fname"]
    HFFemale_FN = data["Halfling_Female_Fname"]
    HFLN = data["Halfling_Lname"]

    HELMale_FN = data["Half-Elf_Male_Fname"]
    HELFemale_FN = data["Half-Elf_Female_Fname"]
    HELLN = data["Half-Elf_Lname"]

    if random.choice(Gender)=="Male" and  random.choice(Race)=="Dragonborn":
     return (random.choice(DBMale_FN)+" "+ (random.choice(DBLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) == "Dragonborn":
         return (random.choice(DBFemale_FN)+" "+ (random.choice(DBLN)+" is a female "+(random.choice(CL))))

    if random.choice(Gender)=="Male" and  random.choice(Race)=="Human":
         return (random.choice(HMMale_FN)+" "+ (random.choice(HMLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) == "Human":
         return (random.choice(HMFemale_FN)+" "+ (random.choice(HMLN)+" is a female "+(random.choice(CL))))

    if random.choice(Gender)=="Male" and  random.choice(Race)=="Elf":
     return (random.choice(ELMale_FN)+" "+ (random.choice(ELLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) =="Elf":
     return (random.choice(ELFemale_FN)+" "+ (random.choice(ELLN)+" is a female "+(random.choice(CL))))
         
    if random.choice(Gender)=="Male" and  random.choice(Race)=="Dwarf":
         return (random.choice(DWMale_FN)+" "+ (random.choice(DWLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) == "Dwarf":
         return (random.choice(DWFemale_FN)+" "+ (random.choice(DWLN)+" is a female "+(random.choice(CL))))    

    if random.choice(Gender)=="Male" and  random.choice(Race)=="Gnome":
         return (random.choice(GNMale_FN)+" "+ (random.choice(GNLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) == "Gnome":
         return (random.choice(GNFemale_FN)+" "+ (random.choice(GNLN)+" is a female "+(random.choice(CL))))    

    if random.choice(Gender)=="Male" and  random.choice(Race)=="Halfling":
         return (random.choice(HFMale_FN)+" "+ (random.choice(HFLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) == "Halfling":
         return (random.choice(HFFemale_FN)+" "+ (random.choice(HFLN)+" is a female "+(random.choice(CL))))    

    if random.choice(Gender)=="Male" and  random.choice(Race)=="Half-Elf":
         return (random.choice(HELMale_FN)+" "+ (random.choice(HELLN)+" is a male "+(random.choice(CL))))

    if random.choice(Gender) =="Female" and random.choice(Race) == "Half-Elf":
         return (random.choice(HELFemale_FN)+" "+ (random.choice(HELLN)+" is a female "+(random.choice(CL))))    
    else:
         return "Try again motherfucker"


