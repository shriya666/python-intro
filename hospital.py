import random
import ast
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
        

Susan= Doctor("Susan", "Primary Care Physician",7 )
Susana= Doctor("Susana", "Primary Care Physician",7 )
Kevin= Doctor("Kevin","Pediatrician", 12 )
Kyla= Doctor("Kyla", "Cardiologists", 9)
Kayla= Doctor("Kayla", "Cardiologists", 10)
Kevina= Doctor("Kevina","Pediatrician", 1)
Kyle= Doctor("Kyle", "Pediatrician", 5)
Georgina= Doctor("Georgina", "Pediatrician", 8)
George= Doctor("George", "Primary care Physician", 11)

print(Kayla.times)

Pediatricians= [Georgina, Kevina, Kyle, Kevin ]
Cardiolgist= [Kyla, Kayla]
Pcp= [George, Susan, Susana]

doctors=[Susan, Susana, Kevin, Kevina, Kyla, Kayla, Kyle, George, Georgina]

intro= "I am a chatbot. My name is Dr. Princessa, and I am devoted to helping you. I love helping! :)\n. I can help you \n 1. Book an appointment(include 'appointment' in the comand, appointments, are by the hour, so no 7:30, only 7.) \n 2. Bring you information about the doctors (type 2 or 'information') \n 3. Suggest a doctor if you are facing any kind of symptoms. If this is an emergency, call 911!!!. Type 'exit' to stop talking with me :(( "

def random_response():
    responses= [
        "I'm sorry, can you repeat that in a differnt way?",
        "Pardon me? What?",
        "I'm confused. Stop making me confused. Please repeat in a clear and concise manner.",
        "Excuse me? "
    ]
    return random.choice(responses)


def respond(user_response):
    user_response=user_response.lower()
    if "appointment" in user_response:
        print("Type the type of doctor ")
        for i in range(len(doctors)):

            if doctors[i].name.lower() in user_response.lower():
                print("aa")
                for j in user_response.split():
                    print(user_response.split())
                    # if ast.literal_eval(i) in doctors[i].times:
                    #     print("Good job! You booked an appointment with "+doctors[i].name+ "at "+i+". ")
                    #     return
                    print(i)
                    print(doctors[i].name)
                    print(str(doctors[i].times[0]))
                    print(doctors[i].name+" is available " + str(doctors[i].times[0]) + " to " + str(doctors[i].times[7])+ ". Please pick a time when "+ doctors[i].name +" is available" )
                    return 
            elif "cardiologist" in user_response:
                print("Our cardiologists are:" )
                #print(Cardiolgist)
                for c in Cardiolgist:
                    print(c.name, "available times: ", str(c.times[0]) + " to " + str(c.times[len(c.times)-1]))
                pickdoctor=input("Type which doctor you want ")
                pickdoctor=pickdoctor.lower()
                if "kyla" in pickdoctor:
                    picktime= input("Pick a time ")
                    if "9" or "10" or "11" or "12" or "1" or "2" or "3" or "4" in picktime:
                        picktime1=int(picktime)
                        if picktime1 in Kyla.times:
                            for i in Kyla.times:
                                if i==picktime1:
                                    Kyla.times.remove(i)
                                    print(Kyla.times)
                                    print("Appointment booked. Type exit to exit. ")

                        else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return 
                elif "kayla" in pickdoctor:
                        picktime= input("Pick a time ")
                        if "10" or "11" or "12" or "1" or "2" or "3" or "4" or "5" in picktime:
                            picktime1=int(picktime)
                            if picktime1 in Kayla.times:
                                for i in Kayla.times:
                                    if i==picktime1:
                                        Kayla.times.remove(i)
                                        print(Kayla.times)
                                        print("Appointment booked. Type exit to exit. ")

                            else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return 

                return
            elif "pediatrician" in user_response:
                print("Our pediatricians are:" )
                for p in Pediatricians:
                    print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[len(p.times)-1]))
                pickdoctor=input("Type which doctor you want ")
                pickdoctor=pickdoctor.lower()
                if "georgina" in pickdoctor:
                    picktime= input("Pick a time ")
                    if "8" or "9" or "10" or "11" or "12" or "1" or "2" or "3" in picktime:
                        picktime1=int(picktime)
                        if picktime1 in Georgina.times:
                            for i in Georgina.times:
                                if i==picktime1:
                                    Georgina.times.remove(i)
                                    print(Georgina.times)
                                    print("Appointment booked. Type exit to exit. ")

                        else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return 
                elif "kevina" in pickdoctor:
                        picktime= input("Pick a time ")
                        if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" in picktime:
                            picktime1=int(picktime)
                            if picktime1 in Kevina.times:
                                for i in Kevina.times:
                                    if i==picktime1:
                                        Kevina.times.remove(i)
                                        print(Kevina.times)
                                        print("Appointment booked. Type exit to exit. ")
                            else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return
                elif "kyle" in pickdoctor:
                        picktime= input("Pick a time ")
                        if "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" in picktime:
                            picktime1=int(picktime)
                            if picktime1 in Kyle.times:
                                for i in Kyle.times:
                                    if i==picktime1:
                                        Kyle.times.remove(i)
                                        print(Kyla.times)
                                        print("Appointment booked. Type exit to exit. ")
                            else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return
                elif "kevin" in pickdoctor:
                        picktime= input("Pick a time ")
                        if "12" or "1" or "2" or "3" or "4" or "5" or "6" or "7" in picktime:
                            picktime1=int(picktime)
                            if picktime1 in Kevin.times:
                                for i in Kevin.times:
                                    if i==picktime1:
                                        Kevin.times.remove(i)
                                        print(Kevin.times)
                                        print("Appointment booked. Type exit to exit. ")
                            else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return
                
                return
            elif "primary" in user_response:
                print("Our Primary Care Physicians are:" )
                for p in Pcp:
                    print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[len(p.times)-1]))
                pickdoctor=input("Type which doctor you want ")
                pickdoctor=pickdoctor.lower()
                if "george" in pickdoctor:
                    picktime= input("Pick a time ")
                    if "11" or "12" or "1" or "2" or "3" or "4" or "5" or "6" in picktime:
                        picktime1=int(picktime)
                        if picktime1 in George.times:
                            for i in George.times:
                                if i==picktime1:
                                    George.times.remove(i)
                                    print(George.times)
                                    print("Appointment booked. Type exit to exit. ")

                        else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return 
                elif "susan" in pickdoctor:
                        picktime= input("Pick a time ")
                        if "7" or "8" or "9" or "10" or "11" or "12" or "1" or "2" in picktime:
                            picktime1=int(picktime)
                            if picktime1 in Susan.times:
                                for i in Susan.times:
                                    if i==picktime1:
                                        Susan.times.remove(i)
                                        print(Susan.times)
                                        print("Appointment booked. Type exit to exit. ")

                            else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return 
                elif "susana" in pickdoctor:
                        picktime= input("Pick a time ")
                        if "7" or "8" or "9" or "10" or "11" or "12" or "1" or "2" in picktime:
                            picktime1=int(picktime)
                            if picktime1 in Susana.times:
                                for i in Susana.times:
                                    if i==picktime1:
                                        Susana.times.remove(i)
                                        print(Susana.times)
                                        print("Appointment booked. Type exit to exit. ")

                            else:
                                print("Appointment already booked. Try again. Click enter. ")
                                return
                return
            # else:
            #     print("Please pick a doctor, or type of doctor SUCH AS: Cardiologist, Pediatrician, or Primary care")
        return 

    elif "child" in user_response or "son" in user_response or "daughter" in user_response or "kid" in user_response or "baby" in user_response or "pediatrician" in user_response:
        print("I recommend that you see one of our wonderful pediatricians! Here is their info!!")
        for p in Pediatricians:
            print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
        pickdoctor=input("Type which doctor you want ")
        pickdoctor=pickdoctor.lower()
        if "georgina" in pickdoctor:
            picktime= input("Pick a time ")
            if "8" or "9" or "10" or "11" or "12" or "1" or "2" or "3" in picktime:
                picktime1=int(picktime)
                if picktime1 in Georgina.times:
                    for i in Georgina.times:
                        if i==picktime1:
                            Georgina.times.remove(i)
                            print(Georgina.times)
                            print("Appointment booked. Type exit to exit. ")

                else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return 
        elif "kevina" in pickdoctor:
                picktime= input("Pick a time ")
                if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" in picktime:
                    picktime1=int(picktime)
                    if picktime1 in Kevina.times:
                        for i in Kevina.times:
                            if i==picktime1:
                                Kevina.times.remove(i)
                                print(Kevina.times)
                                print("Appointment booked. Type exit to exit. ")
                    else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return
        elif "kyle" in pickdoctor:
                picktime= input("Pick a time ")
                if "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" in picktime:
                    picktime1=int(picktime)
                    if picktime1 in Kyle.times:
                        for i in Kyle.times:
                            if i==picktime1:
                                Kyle.times.remove(i)
                                print(Kyla.times)
                                print("Appointment booked. Type exit to exit. ")
                    else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return
        elif "kevin" in pickdoctor:
                picktime= input("Pick a time ")
                if "12" or "1" or "2" or "3" or "4" or "5" or "6" or "7" in picktime:
                    picktime1=int(picktime)
                    if picktime1 in Kevin.times:
                        for i in Kevin.times:
                            if i==picktime1:
                                Kevin.times.remove(i)
                                print(Kevin.times)
                                print("Appointment booked. Type exit to exit. ")
                    else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return
        return
    elif "chest" in user_response or "dizzy" in user_response or "heart" in user_response or "cardiologist" in user_response:
        print("That sounds serious! You should see one of our cardiologists. Here is their info ")
        for c in Cardiolgist:
            print(c.name, "available times: ", str(c.times[0]) + " to " + str(c.times[7]))
        pickdoctor=input("Type which doctor you want ")
            pickdoctor=pickdoctor.lower()
            if "kyla" in pickdoctor:
                picktime= input("Pick a time ")
                if "9" or "10" or "11" or "12" or "1" or "2" or "3" or "4" in picktime:
                    picktime1=int(picktime)
                    if picktime1 in Kyla.times:
                        for i in Kyla.times:
                            if i==picktime1:
                                Kyla.times.remove(i)
                                print(Kyla.times)
                                print("Appointment booked. Type exit to exit. ")

                    else:
                            print("Appointment already booked. Try again. Click enter. ")
                            return 
            elif "kayla" in pickdoctor:
                    picktime= input("Pick a time ")
                    if "10" or "11" or "12" or "1" or "2" or "3" or "4" or "5" in picktime:
                        picktime1=int(picktime)
                        if picktime1 in Kayla.times:
                            for i in Kayla.times:
                                if i==picktime1:
                                    Kayla.times.remove(i)
                                    print(Kayla.times)
                                    print("Appointment booked. Type exit to exit. ")

                        else:
                            print("Appointment already booked. Try again. Click enter. ")
                            return
        return
    elif "sick" in user_response or "illness" in user_response or "ill" in user_response or "illnesses" in user_response or "hurt" in user_response or "hurts" in user_response or "ache" in user_response or "aches" in user_response or "Primary Care Physician" in user_response or "Primary Care" in user_response:
        print("See a general primary care physician!!! Here is their info!!")
        for p in Pcp:
            print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
        pickdoctor=input("Type which doctor you want ")
        pickdoctor=pickdoctor.lower()
        if "george" in pickdoctor:
            picktime= input("Pick a time ")
            if "11" or "12" or "1" or "2" or "3" or "4" or "5" or "6" in picktime:
                picktime1=int(picktime)
                if picktime1 in George.times:
                    for i in George.times:
                        if i==picktime1:
                            George.times.remove(i)
                            print(George.times)
                            print("Appointment booked. Type exit to exit. ")

                else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return 
        elif "susan" in pickdoctor:
                picktime= input("Pick a time ")
                if "7" or "8" or "9" or "10" or "11" or "12" or "1" or "2" in picktime:
                    picktime1=int(picktime)
                    if picktime1 in Susan.times:
                        for i in Susan.times:
                            if i==picktime1:
                                Susan.times.remove(i)
                                print(Susan.times)
                                print("Appointment booked. Type exit to exit. ")

                    else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return 
        elif "susana" in pickdoctor:
                picktime= input("Pick a time ")
                if "7" or "8" or "9" or "10" or "11" or "12" or "1" or "2" in picktime:
                    picktime1=int(picktime)
                    if picktime1 in Susana.times:
                        for i in Susana.times:
                            if i==picktime1:
                                Susana.times.remove(i)
                                print(Susana.times)
                                print("Appointment booked. Type exit to exit. ")

                    else:
                        print("Appointment already booked. Try again. Click enter. ")
                        return   
        return
    elif "info" in user_response or "what" in user_response or "type" in user_response or "doctors" in user_response or "help" in user_response:
        print("Our pediatricians are: ")
        for p in Pediatricians:
            print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
        print("Our cardiologists are: ")
        for p in Cardiolgist:
            print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
        print("Our Primary Care Physicians are: ")
        for p in Pcp:
            print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
        return 

    elif "2" in user_response or "information" in user_response:
        answer= int(input("type 1 for cardiologists, type 2 for pediatricians, or type 3 for primary care physicians. "))
        if answer==1:
            for c in Cardiolgist:
                print(c.name, "available times: ", str(c.times[0]) + " to " + str(c.times[7]))
            return
        elif answer==2:
            for p in Pediatricians:
                print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
            return
        elif answer==3:
            for p in Pcp:
                print(p.name, "available times: ", str(p.times[0]) + " to " + str(p.times[7]))
            return
        else:
            while user_response.lower() != "exit":
                respond(user_response)
                user_response=input()
    else:
        for p in doctors:
            if p.name in user_response:
                print(p.name, "is available from ", str(p.times[0]) + " to " + str(p.times[7]))
                return
            print(random_response())
            return
        return

        
print(intro)
user_response=input()
while user_response.lower() != "exit":
    respond(user_response)
    user_response+=" "+input()
    print(user_response)