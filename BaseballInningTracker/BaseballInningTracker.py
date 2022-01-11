
#creates dictionaries to hold home team (team1) and visiting team (team 2) scores
team_1_innings = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
team_2_innings = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}


#if a file holding the scores for each team already exists, the scores from those files are loaded into the dictionaries
try:
    #loads scores into dictionary for home team
    f = open('./testH.txt')
    
    #list holds values from score files to then populate dictionary
    test = []
    count = 0
    for line in f:
        v = line
        #because the first line of the score file stores the name of the team, we dont want to add that to the dictionary.
        #This count variable ensures first line (team name) isn't added to the dictionary
        count += 1
        if count == 1:
            test.append(v)
            continue
        #converts score from list to int in order to remove the \n
        v = int(v)
        test.append(v)
        
        t = str(test[0])
        
    
    f.close()
    home = test[0]
    #actually populates dictionary with scores from file for home team
    for i in range(1,len(test)):
        team_1_innings[str(i)] = str(test[i])

    #loads scores into dictionary for visiting team
    f = open('./testV.txt')
    
    #list holds values from score files to then populate dictionary
    test = []
    count = 0
    for line in f:
        v = line
        #because the first line of the score file stores the name of the team, we dont want to add that to the dictionary. 
        #This count variable ensures first line (team name) isn't added to the dictionary
        count += 1
        if count == 1:
            test.append(v)
            continue
        #converts score from list to int in order to remove the \n
        v = int(v)
        test.append(v)
        t = str(test[0])
        
    f.close()
    visitor = test[0]
    #actually populates dictionary with scores from file for visiting team
    for i in range(1,len(test)):
        team_2_innings[str(i)] = str(test[i])

    
#if this is the user's first time using this program, new files to store scores and team names are created are created
except Exception:
    #file with home team name and scores
    f1 = open("./testH.txt",'w')
    f1.close()
    #file with visiting team name and scores
    f2 = open("./testV.txt",'w')
    f2.close()
    

#function to determine whether or not every inning has a score
def complete_inning_check():
    count = 0
    for i in team_1_innings.values():
        if len(i) > 0:
            count += 1
    if count == 9:
        return True
    else:
        return False

       
#checks the inning the user wants to add a score to is valid and returns the current inning of the game (to prevent user from putting in innings that already exist or skipping innings)
def inning_check(selection):
    #ensures inning selection is valid (1-9) and ensures every score has not yet been input
    if selection in team_1_innings.keys() and complete_inning_check() == False:
        for i in range(1, 10):
            if len(team_1_innings[str(i)]) > 0:
                continue
            else:
                return str(i)
    #if they select an inning larger than 9 or put in anything else (like a string) the inning_check function will return "invalid inning"
    elif selection not in team_1_innings.keys():
        return ('invalid inning')
    elif complete_inning_check() == True:
        return('all already entered')
    #fail safe (shouldn't trigger)
    else:
        return 'something has gone wrong'
    
    
#function to add scores to dictionaries 
def inning_selection():
    total1 = 0
    total2 = 0
    
    
    l = ['1','2','3','4','5','6','7','8','9']
    selection = input('enter inning')
    
    #stores current inning or error message depending on what inning the user input in the inning_check() function
    check = inning_check(selection)
    
    #checks whether the inning selection is valid or an error message
    if check in l:
        #if the check is a valid inning, the current inning and and selected inning are converted to integers so they can be compared numerically
        intselect = int(selection)
        intcheck = int(check)
    else:
        #if the check is an error message, the check variable remains a string
        intselect = selection
        intcheck = check
    
    if check != 'invalid inning':
        
        #if the inning 
        if selection == check:
            
            #if the inning they selected and the current inning (check variable) are the user is asked to input the scores for that inning
            score1 = input('enter score for home team')
            score2 = input('enter score for visiting team')
            
            #ensures scores are numerical values before adding them to the dictionary
            if score1.isdigit() and score2.isdigit() and len(score1) < 5 and len(score2) < 5:
                team_1_innings[selection] = score1
                team_2_innings[selection] = score2
            else:
                return 'invalid score. please enter scores for inning',selection,'again'
            
            #calculates total scores for each team
            for i in range(1,int(selection) + 1):
                if len(team_1_innings[selection]) > 0:
                    total1 += int(team_1_innings[str(i)])
                    total2 += int(team_2_innings[str(i)])
            
            #converts totals back to strings so they can be added to the table
            total1 = str(total1)
            total2 = str(total2)
            
            #table file is opened
            f = open("./test.txt",'a')
            
            #table is updated with new scores
            f.write("{0} | {1} | {2}| {3} | {4}\n".format(selection.ljust(len("inning"), " "),team_1_innings[selection].ljust(len(home), " "),team_2_innings[selection].ljust(len(visitor), " "),total1.ljust(len("Home")," "),total2.ljust(len("Visiting")," ")))
            f.close()
            
            #scores are saved to score files in case user wants to exit the game and come back without resetting their game
            f = open("./testH.txt",'a')
            f.write(team_1_innings[selection]+'\n')
            f.close()
            f = open("./testV.txt",'a')
            f.write(team_2_innings[selection]+'\n')
            f.close()
            
        #if the inning they selected is greater than the current inning, this error message pops up
        elif intselect > intcheck:
            return 'inning',check,'must be added first'
        
        #if they already added the inning they are trying to add to, this error message pops up
        elif intselect < intcheck:
            return selection,'has already been added.'
        
        #if all scores have been added, this error pops up
        elif check == 'all already added':
            return ('all already added')
        #fail safe error message (shouldn't trigger but we put it here just in case)
        else:
            return 'something has gone wrong'
    else:
        return 'invalid inning'


#menu
option = 0
while option != '4':
    #prints menu with options
    option = input("""enter option:
    
            1: New Game (this will reset your game)
            2: Enter Scores
            3: Print Game Info
            4: Exit""")
    
    #wipes dictionaries and score files and asks user for the new names. The new names are stored in the file
    if option == '1':
        team_1_innings = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'',}
        team_2_innings = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'',}
        home = input('enter hometeam name')
        visitor = input('enter visitor name')
        f = open("./testH.txt",'w')
        f.write(home+'\n')
        f.close()
        f = open("./testV.txt",'w')
        f.write(visitor+'\n')
        f.close()
        f = open('./test.txt','w')
        f.write("{0} | {1} | {2} | {3} | {4}\n".format("inning".ljust(len("inning"), " "),home.ljust(len(home), " "),visitor.ljust(len(visitor), " "),"Home".ljust(len("Home")," "),"Visiting".ljust(len("Visiting")," ")))
        f.write("{0}-+-{1}-+-{2}-+-{3}-+-{4}\n".format("".ljust(len("inning"), "-"),"".ljust(len(home), "-"),"".ljust(len(visitor), "-"),"".ljust(len("Home"),"-"),"".ljust(len("Visiting"),"-")))
        f.close()
    
    #runs inning_selection function as long as a game and score files already exists. The ValueError exception also guarantees the input score is valid
    elif option == '2':
        try:
            print(inning_selection())
        except(NameError):
            print('game must be created first')
        except(ValueError):
            print('at least one of your scores is invalid. please enter scores again')
        
        
    #prints table file
    elif option == '3':
        try:
            f = open("./test.txt",'r')
            table = f.read()
            f.close()
            print(table)
        #if a game has not been created yet, this message is displayed
        except:
            print('you must create game first')
    #exit option
    elif option == '4':
        print('thanks for playing')
    #prevents user from inputting an invalid menu option
    else:
        print('invalid choice')
