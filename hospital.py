class Doctor:
    def __init__(self, name, type, start):
        self.name= name
        self.type= type
        self.start=start
        self.times=[]
        for i in range(8):
            if start+i>12:
                self.times.append(start+i-12)
            else:
                self.times.append(start+i)

Susan= Doctor("Dr. Susan", "Primary Care Physician",7 )
Susana= Doctor("Dr. Susana", "Primary Care Physician",7 )
Kevin= Doctor("Dr. Kevin","Pediatrician", 12 )
Kyla= Doctor("Dr. Kyla", "Cardiologists", 9)
Kayla= Doctor("Dr. Kayla", "Cardiologists", 10)
Kevina= Doctor("Dr. Kevina","Pediatrician", 1)
Kyle= Doctor("Dr. Kyle", "Pediatrician", 5)
Georgina= Doctor("Dr. Georgina", "Pediatrician", 8)
George= Doctor("Dr. George", "Primary care Physician", 11)


Pediatricians= [Georgina, Kevina, Kyle, Kevin ]
Cardiolgist= [Kyla, Kayla]
Pcp= [George, Susan, Susana]

doctors=[Susan, Susana, Kevin, Kevina, Kyla, Kayla, Kyle, George, Georgina]

name=input("What is your name? ")
intro= "I am a chatbot. My name is Dr. Princessa, and I am devoted to helping you. I love helping! :)\n. I can help you \n 1. Book an appointment(include 'appointment' in the comand, appointments, are by the hour, so no 7:30, only 7.) \n 2. Bring you information about the doctors "
