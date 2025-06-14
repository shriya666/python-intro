import random
base_budget= 10000
base_population= 500
population_capacity= 700
base_happiness= 23
tax= 0.5
average_income= 100
decisions= {
    "Build Park" : [-1000, random.randint(-5, 5), random.randint(-5, 5), random.randint(-1, 50), 0, random.randint(-5, 24)],
    "Better a school": [-1050, random.randint(10, 15), random.randint(15, 20), random.randint(-5, 75), 0, random.randint(22, 50) ], 
    "Build a factory": [100, random.randint(5, 30), random.randint(5, 35), random.randint(-10, 5), 0, random.randint(65, 70) ], 
    "Raise taxes": [0, random.randint(-15, -10), random.randint(-20, -15), random.randint(-15, 4), random.uniform(0.1, 0.7), random.randint(-5, 5) ], 
    "Lower taxes": [0, random.randint(15, 10), random.randint(20, 15), random.randint(15, 25), (random.uniform(0.1, 0.7))*(-1), random.randint(-5, 5)], 
    "Run a festival": [-300, random.randint(5, 10), random.randint(12, 15), random.randint(15, 35), random.randint(-5, 5)], 
    "Build housing": [-3000, random.randint(20, 55), random.randint(20, 75), random.randint(-5, 5), random.randint(45, 50) ], 
}

random_events= {
    "Your town got hijacked by bandits": [random.randint(-1500, -1000), random.randint(-25, 0), random.randint(-5, 5), random.randint(-41, 1), 0, random.randint(-15, -2)],
    " A storm destroyed everything!!!": [random.randint(-1500, -1000), random.randint(-25, 0), random.randint(-25, -4), random.randint(-20, 1), 0, random.randint(-15, -2)],
    " A tech boom increased productivity!!!!": [101, random.randint(5, 75), random.randint(10, 85), random.randint(21, 70), 0, random.randint(30, 75)],
    "Your town was chosen to be the set for  movie/tv show": [random.randint(15, 20), random.randint(15, 35), random.randint(10, 45), random.randint(21, 80), 0, random.randint(20, 45)],

}
while True:
    turndecisions= []
    print("stats: \n Budget: $", base_budget, "\n Population: ", base_population, "\n Population Capacity: ", population_capacity, "\n Happiness:" , base_population, "\n Taxes:", tax, "\n Average Income:",average_income )
    decision= input("Pick an action: \n A) Build Park: $1000 \n B) Better a school: $1050 \n C)Build a factory \n D)Raise taxes:  \n E)Lower Taxes: , \n F)Run a festival:  $300 \n G)Build housing: $3000. \n F) Or you could exit turn. ")
    while decision.lower() != "f":
        turndecisions.append(decision)
        decision= input("Pick an action: \n A) Build Park: $1000 \n B) Better a school: $1050 \n C)Build a factory \n D)Raise taxes:  \n E)Lower Taxes: , \n F)Run a festival:  $300 \n G)Build housing: $3000. \n F) Or you could exit turn. ")
    for d in turndecisions:
        d=d.lower()
        if d== "a":
            base_budget += decisions["Build Park"] [0]
        elif d=="b":
            base_budget += decisions["Better a School"]
        elif d== "c":
            base_budget += decisions["Build a Factory"]
        elif d=="d":
            base_budget += decisions["Raise Taxes"]
        elif d=="e":
            base_budget += decisions["Lower Taxes"]
        elif d=="f":
            