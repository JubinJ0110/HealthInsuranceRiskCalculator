INTRODUCTION = '''
              \U0001F6E1 Health Insurance Risk Calculator\U0001F6E1            
\U0001F534*************************************************************\U0001F534
  Welcome to the Health Insurance Risk Calculator, where we'll 
  give you enough information to get an idea of how much you 
  owe us. We'll ask a series of basic question about your 
  personal information that will determine your risk level 
  and whether or not you are insurable.
\U0001F534*************************************************************\U0001F534
'''
print(INTRODUCTION + '\n\n' + 'Questions:')


def ValidNum(Response):
    if Response.isnumeric():
        return True
    else:
        print('This is not a number, try again!')
        return False

def ValidString(Response):
    if Response.isnumeric():
        print('This is a number, try again!')
        return False
    else:
        return True
       

TotPoints = 0

i = 1
while i < 2:
    i+=1
    UserR = input('\nWhat is your age?\n')
    age = UserR

    if ValidNum(UserR):
        i+=300000
        if int(UserR) < 30 and int(UserR) > 0:
            TotPoints += 0
        elif int(UserR) < 45:
            TotPoints += 10
        elif int(UserR) < 60:
            TotPoints += 20
        else:
            TotPoints += 30
    else:
        i-=1
        
i=1
while i<2:
    i+-1
    UserR = input('\nWhat is your height? Answer in typical 0\'0\" format.\n')
    UserHeight = UserR
    
    if UserR.find('\'') == 1 and UserR.endswith('\"'):
        feet = UserR.split('\'')
        ft = feet[0]

        inches = feet[1].split('\"')
        inch = inches[0]
        
        if ValidNum(ft) and ValidNum(inch):
            if int(ft) > 2 and int(ft) < 9 and int(inch) > -1 and int(inch) < 12:
                height = (float(ft)*12) + float(inch)
                i+=431745817387613
            else: 
                print('This is not a valid input, try again!')
                i-=1
        else:
            i-=1    
    else:
        print('This is not a valid input, try again!')
        i-=1



BMI = 0
i=1
while i<2:
    i+=1

    weight = input('''\nWhat is your weight in lbs?
(Only write the number, no \"lbs\" following it.)\n''')
    UserWeigth = weight

    if ValidNum(weight):
        if int(weight) > 5 and int(weight) < 750:
            i+=9232798
            BMI = (703.0*float(weight))/(float(height)*float(height))
        else:
            print('This is not a valid weight, try again!')
            i-=1
    else:
        i-=1

if BMI >= 18.5 and BMI <= 24.9:
    TotPoints +=0
elif BMI >= 25 and BMI <= 29.9:
    TotPoints += 30
elif BMI >= 30 and BMI <= 34.9:
    TotPoints += 75

BP = '''
                     ***BLOOD PRESSURE CATEGORIES***

BP Category                   Systopic                        Diastolic
                       | (mm Hg Upper Number) |         | (mm Hg Lower Number)
                       |                      |         |                
Normal                 |     Less than 120    |   and   |   Less than 80
                       |                      |         |               
Elevated               |       120-129        |   and   |   Less than 80
                       |                      |         |         
High BP                |       130-139        |   or    |       80-89
(Hypertension Stage 1) |                      |         |           
                       |                      |         |          
Hight BP               |    140 or higher     |   or    |   90 or higher
(Hypertension Stage 2) |                      |         |            
                       |                      |         |              
Hyptensive Crisis      |  Higher than 180     |  and/or |  Higher than 120
'''
print(BP)

i=1
while i<2:
    i+=1
    UserR = input('''\nWhat is your BP, input your answer as normal, elevated, 
stage 1, stage 2, or crisis? Select from the chart above.\n''')
    UserBP = UserR
    
    if ValidString(UserR):
        if str(UserR).lower() == 'normal':
            TotPoints += 0
        elif str(UserR).lower() == 'elevated':
            TotPoints += 15
        elif str(UserR).lower() == 'stage 1':
            TotPoints += 30
        elif str(UserR).lower() == 'stage 2':
            TotPoints += 75
        elif str(UserR).lower() == 'crisis':
            TotPoints += 100
        else:
            i-=1
            print('This is not a valid response, try again!')
    else:
        i-=1

i=1
while i<2:
    i+=1
    UserR = input('\nDoes Diabetes run in your family? Answer with a simple yes or no.\n')
    UserD = 'Does Diabetes run in the family - ' + UserR

    if ValidString(UserR):
        if UserR.lower() == 'yes':
            i+=18971
            TotPoints += 10
        elif UserR.lower() == 'no':
            i+=187237
        else:
            print('That\'s not a \"yes\" or \"no\" answer, try again!')
            i-=1
    else:
        i-=1

i=1
while i<2:
    i+=1
    UserR = input('\nDoes Cancer run in your family? Answer with a simple yes or no.\n')
    UserC = 'Does Cancer run in the family - ' + UserR

    if ValidString(UserR):
        if UserR.lower() == 'yes':
            i+=18971
            TotPoints += 10
        elif UserR.lower() == 'no':
            i+=187237
        else:
            print('That\'s not a \"yes\" or \"no\" answer, try again!')
            i-=1
    else:
        i-=1

i=1
while i<2:
    i+=1
    UserR = input('\nDoes Alzheimer\'s run in your family? Answer with a simple yes or no.\n')
    UserA = 'Does Alzhermer\'s run in the family - ' + UserR

    if ValidString(UserR):
        if UserR.lower() == 'yes':
            i+=18971
            TotPoints += 10
        elif UserR.lower() == 'no':
            i+=187237
        else:
            print('That\'s not a \"yes\" or \"no\" answer, try again!')
            i-=1
    else:
        i-=1


print('''\n***For the following questions you can enter \"done\" to 
immediately see you evaluation.***''')

isDone = False

UserR = input('\nIs there anything else you\'d like to tell us about your health?\n')

if UserR.lower() == 'done':
    isDone = True

if not isDone:
    UserR = input('\nHow\'s your day going?\n')
else:
    pass

if UserR.lower() == 'done':
    isDone = True

if not isDone:
    UserR = input('\nDo you have any suggestion for how we can improve?\n')
else:
    pass

print('\nAge: ' + age)
print('Height: ' + UserHeight)
print('Weight: ' + UserWeigth)
print('BMI: ' + str(BMI))
print(UserD)
print(UserC)
print(UserA)

print('\nTotal Risk Score(Higher = Worse): ' + str(TotPoints))
RiskC = ''

if TotPoints <= 20:
    RiskC = 'Low Risk'
elif TotPoints <= 50:
    RiskC = 'Moderate Risk'
elif TotPoints <= 75:
    RiskC = 'High Risk'
else:
    RiskC = 'Unisurable'

print('Your Risk Category: ' + RiskC + '\n')