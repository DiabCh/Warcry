import random


names={
    "fname": [
         "Mihai",
         "Radu",
         "Diab",
         "Teo",
         "Irina",
         "Bogdan",
         "Goerge",
         "Stefan",
         "Paul",
         "Vasile",
         "Ovidiu",
         "Florin",
         "Cornel",
         "Matei",
         "Robik",
         "Romeo",
         "Costel",
         "Marinica",
         "Leana",
         "Atimut",
         "Chad",
         "Jamal",
         "Putifric",

    ],

    "lname":[
        "Giosan",
        "Stancu",
        "Chraif",
        "Popa",
        "Botez",
        "Paladi",
        "Bombardieru",
        "Dumitru",
        "Ionesc",
        "Ciobanu",
        "Florea",
        "Nagy",
        "Constantinescu",
        "Cojocaru",
        "Fantastik",
        "Abagiu",
        "Whisperwind",
        "Stormrage",
        "Thunderwrath",
        "Truthseeker",
        "Lights bane",
        "Slayer of the meek",
        "Poxbringer",
        "cronescovici"

     ],
    "nickname":[
        "\"the Faceless One\"",
        "\"the Insane\"",
        "\"Predator\"",
        "\"Blood Champion\"",
        "\"Crusader\"",
        "\"The Immortal\"",
        "\"Trashmaster\"",
        "\"One man klan\"",
        "\"Salty\"",
        "\"Bloodsail Admiral\"",
        "\"Archdruid\"",
        "\"Kebab shishkebab\"",
        "\"Captain\"",
        "\"Servant of Nzoth\"",
        "\"The proven healer\"",
        "\"The Patient\"",
        "\"Starcaller\"",
        "\"The dreamer\"",
        "\"Adventuring instructor\"",
        "\"the Truck\"",
        "\"Ten-ton terror of Tal'ador\""


    ]

}
races=["orc", "human", "elf", "undead"]


def get_name():
    fname = random.choice(names["fname"])
    lname = random.choice(names["lname"])
    return f"{fname} {lname}"


def get_nickname():
    return random.choice(names["nickname"])


def get_random_race():
    return random.choice(races)

