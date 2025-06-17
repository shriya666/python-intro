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
    "Build a Factory": [100, random.randint(5, 30), random.randint(5, 35), random.randint(-10, 5), 0, random.randint(65, 70) ], 
    "Raise Taxes": [0, random.randint(-15, -10), random.randint(-20, -15), random.randint(-15, 4), random.uniform(0.1, 0.7), random.randint(-5, 5) ], 
    "Lower Taxes": [0, random.randint(10, 15), random.randint(15, 20), random.randint(15, 25), (random.uniform(0.1, 0.7))*(-1), random.randint(-5, 5)], 
    "Run a festival": [-300, random.randint(5, 10), random.randint(12, 15), random.randint(15, 35), random.randint(-5, 5), random.randint(-5, 24)], 
    "Build Housing": [-3000, random.randint(20, 55), random.randint(20, 75), random.randint(-5, 5), random.randint(45, 50), random.randint(-5, 24)], 
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
    decision= input("Pick an action: \n A) Build Park: $1000 \n B) Better a school: $1050 \n C)Build a factory \n D)Raise taxes:  \n E)Lower Taxes: , \n F)Run a festival:  $300 \n G)Build housing: $3000. \n H) Or you could exit turn. ")
    while decision.lower() != "h":
        turndecisions.append(decision)
        decision= input("Pick an action: \n A) Build Park: $1000 \n B) Better a school: $1050 \n C)Build a factory \n D)Raise taxes:  \n E)Lower Taxes: , \n F)Run a festival:  $300 \n G)Build housing: $3000. \n H) Or you could exit turn. ")
        for d in turndecisions:
            d=d.lower()
            if d== "a":
                base_budget += decisions["Build Park"] [0]
                base_population+= decisions["Build Park"] [1]
                population_capacity += decisions["Build Park"] [2]
                base_happiness += decisions["Build Park"] [3]
                tax += decisions["Build Park"] [4]
                average_income += decisions["Build Park"] [5]

            elif d=="b":
                base_budget += decisions["Better a school"] [0]
                base_population+= decisions["Better a school"] [1]
                population_capacity += decisions["Better a school"] [2]
                base_happiness += decisions["Better a school"] [3]
                tax += decisions["Better a school"] [4]
                average_income += decisions["Better a school"] [5]
            elif d== "c":
                base_budget += decisions["Build a Factory"] [0]
                base_population+= decisions["Build a Factory"] [1]
                population_capacity += decisions["Build a Factory"] [2]
                base_happiness += decisions["Build a Factory"] [3]
                tax += decisions["Build a Factory"] [4]
                average_income += decisions["Build a Factory"] [5]
            elif d=="d":
                base_budget += decisions["Raise Taxes"] [0]
                base_population+= decisions["Raise Taxes"] [1]
                population_capacity += decisions["Raise Taxes"] [2]
                base_happiness += decisions["Raise Taxes"] [3]
                tax += decisions["Raise Taxes"] [4]
                average_income += decisions["Raise Taxes"] [5]
            elif d=="e":
                base_budget += decisions["Lower Taxes"] [0]
                base_population+= decisions["Lower Taxes"] [1]
                population_capacity += decisions["Lower Taxes"] [2]
                base_happiness += decisions["Lower Taxes"] [3]
                tax += decisions["Lower Taxes"] [4]
                average_income += decisions["Lower Taxes"] [5]
            elif d=="f":
                base_budget += decisions["Run a festival"] [0]
                base_population+= decisions["Run a festival"] [1]
                population_capacity += decisions["Run a festival"] [2]
                base_happiness += decisions["Run a festival"] [3]
                tax += decisions["Run a festival"] [4]
                average_income += decisions["Run a festival"] [5]
            else:
                base_budget += decisions["Build Housing"] [0]
                base_population+= decisions["Build Housing"] [1]
                population_capacity += decisions["Build Housing"] [2]
                base_happiness += decisions["Build Housing"] [3]
                tax += decisions["Build Housing"] [4]
                average_income += decisions["Build Housing"] [5]

    random_event= random.randint(1, 100)
    if random_event>=80:
        event= random.choice(list(random_events.keys()))
        print("Random event: "+ event)
        base_budget += random_events[event] [0]
        base_population+= random_events[event] [1]
        population_capacity += random_events[event] [2]
        base_happiness += random_events[event] [3]
        tax += random_events[event] [4]
        average_income += random_events[event] [5]
    print("Turn is over.")
    if base_budget<=100 or base_happiness<=5:
        print("You lost. You were a terrible mayor. ")
        break 
    if base_budget>= 20000 and base_happiness<=1000:
        print(" You were amazing!!! You won.  Best mayor ever! ")
        break 