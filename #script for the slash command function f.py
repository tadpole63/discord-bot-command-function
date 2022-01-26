#script for the slash command function for the discord bot
#will have multiple different slash commands
#might have activation feature?  Maybe a different script?

#update (16 December 2021) activation feature added

#update (17 December 2021) Puppy facts added ; /music fact added ; updated help URL ; end command works! ; 

#update (19 December 2021) selection structure for activation feature fixed ; while loop for break activation feature added

#view update log for further update documentation at https://docs.google.com/document/d/1cGz9gUvz7mhg5YD-kxP6HrPtlA8go3vwagf1qVlSNrA/edit


#import random module
import random
import time

#global trigger variables
user_slash = " "
user_mentioned = " "
bot_live = " "

#joke variables
joke_1 = "I used to work in an orange juice factory.  Yea, I got canned.  They really put the squeez on me."
joke_2 = "A ham sandwoch walks into a bar and orders a drink.  The bar tender says 'Sorry, we don't serve food here.'"
joke_3 = "Why did the Clydesdale give the pony a glass of water? Because he was a little horse."
joke_4 = "SUS"

#eight_ball variables
first = "no"
second = "yes"
third = "maybe"
fourth = "definetly"
fifth = "certianly not."

#random fact variables
fact_1 = "did you know, caffine is actually a drug?"
fact_2 = ("did you know, airplanes fly via a force called lift. Lift is generated when air travels faster over the top of an aircrafts' " +
"wings and lowers the pressure over the top of the wings.  The pressure difference lifts the aircraft by its wings into the air.")
fact_3 = "did you know dogs feel emotions?"

#puppy fact variables
pf_1 = "Puppies spend a majority of their day sleeping"
pf_2 = "The number of puppies in a litter depends on the breed"
pf_3 = "infant puppies cannot deficate"
pf_4 = "Puppies can be TWINS!!"
pf_5 = ("When newly born, puppies can only respond to warmth, tough and smell because their" + 
"eyes remain shut, and they don't develop hearing until 4 weekd after birth")
print("Enter the command 'start' to start")

#music fact variables
music_1 = "the notation layout is different from treble to bass cleff"
music_2 = "musicians are aliens"
music_3 = "the best instrument is the trumpet"
music_4 = "the piano is considered a percussion and string instrument"
music_5 = "a guitar is considered a plucked string instrument"

#aviation fact variables
av_f1 = ""
av_f2 = ""
av_f3 = ""
av_f4 = ""
av_f5 = ""

#command string variables
com_1 = "/afk"
com_2 = "/joke"
com_3 = "/help"
com_4 = "/8 ball"
com_5 = "/fact"
com_6 = "/puppy fact"
com_7 = "/music fact"
com_8 = "/aviation fact"
com_9 = "/commands"

#specific command information variables
afkInfo = ("the /afk slash command sets an afk message to be displayed when someone mentions you in your server." + 
"the command only sets an afk in the channel you make the command in.  We're working on making it apply to the entire server.")
jokeInfo = ("the /joke command initializes an algorythm that tells you a joke")
helpInfo = ("the /help command prints a URL you can go to for help")
eightBallInfo = ("the /8 ball command acts as an eight ball.  you can ask a question, and the program will provide a randomized response." + 
"there are some funny responses, some serious.  If tou would like to add a response, email your request to tadpierski63@gmail.com")
factInfo = ("the /fact command prints a random fact.  If you would like to add a fact, email your request to tadpierski63@gmail.com")
puppyFactInfo = ("the /puppy fact command prints a randomized puppy fact.  If you have addition sugestions, please email" + 
"tadpierski63@gmail.com")
musicFactInfo = ("")
aviationFactInfo = ("")
commandsInfo = ("")

#water fact variables
wf1 = "Water is made of Hydrogen and Oxygen!"
wf2 = "water is clear!"
wf2 = ("when preforming electrolysis on a container of water, you can decompose the water into oxygen and" +
" hydrogen gas!")
#affirmation message variable
affirmation = "you are great.  you are worth it."
affirmation_2 = "you are needed."
affirmation_3 = "you are loved."
affirmation_list = [affirmation, affirmation_2, affirmation_3]

bot_live = str(input(""))

while bot_live == "start":
    #start selection structure
    print("Enter a slash command") #have to have clear instructions for the user
    user_slash = str(input(""))
    #selection structure for slash commands
    if user_slash == "/afk":
        user_afk = str(input("Enter your AFK message:"))
        if user_mentioned == "yes":
            print(user_afk)
        else:
            print()
    elif user_slash == "/joke":
        joke = [joke_1, joke_2, joke_3, joke_4]
        tell_a_joke = random.choice(joke)
        print(tell_a_joke)
    elif user_slash == "/help":
        print("for assistance regarding commands go to")
    elif user_slash == "/8 ball":
        user_question = str(input("What would you like to know? "))
        eight_ball = [first, second, third, fourth, fifth]
        response = random.choice(eight_ball)
        print(response)
    elif user_slash == "/fact":
        random_fact = [fact_1, fact_2, fact_3]
        fact = random.choice(random_fact)
        print(fact)
    elif user_slash == "/puppy fact":
        puppy_fact = [pf_1, pf_2, pf_3, pf_4, pf_5] #actually put in facts later
        printed_fact = random.choice(puppy_fact) #chooses random in range (list)
        print(printed_fact) #prints random fact

    elif user_slash == "/music fact": #user music fact "/music fact"
        music_fact = [music_1, music_2, music_3, music_4, music_5]
        fact = random.choice(music_fact)
        print(fact)
    elif user_slash == "/aviation fact":
        aviation_fact = [av_f1, av_f2, av_f3, av_f4, av_f5]
        printed_aviation_fact = random.choice(aviation_fact)
        print(printed_aviation_fact)

    elif user_slash == "/commands":
        commands = [com_1, com_2, com_3, com_4, com_5, com_6, com_7, com_8, com_9]
        for elem in commands:
            print(elem)
            time.sleep(.5)
            #hopefully prints each on a different line
        specific_item = str(input("For more information on a specific command, enter that slash command. otherwise enter 'end'"))
        #com_# variable = command_# specified in variables list above
        if specific_item == com_1: #prints specific information on every command
            print(afkInfo)
        elif specific_item == com_2: 
            print(jokeInfo)
        elif specific_item == com_3:
            print(helpInfo)
        elif specific_item == com_4:
            print(eightBallInfo)
        elif specific_item == com_5:
            print(factInfo)
        elif specific_item == com_6:
            print(puppyFactInfo)
        elif specific_item == com_7:
            print(musicFactInfo)
        elif specific_item == com_8:
            print(aviationFactInfo)
        elif specific_item == com_9:
            print(commandsInfo)
        elif specific_item == "end":
            print()
        else:
            print("there was an error processing your entrance.")
            print("The most probable issue was invalid entrance syntax")
            print("If this error keeps occuring, please contact the script author at tadpierski63@gmail.com")
    
    elif user_slash == "/water fact":
        waterFact = [wf1, wf2]
        printWaterFact = random.choice(waterFact)
        print(printWaterFact)
    
    elif user_slash == "/affirmation":
        affirmation_print = random.choice(affirmation_list)
        print(affirmation_print)
    

    #print instructions for a reiteration of above selection structure
    print("To use the slash command feature again, please enter 'start' or 'end' to end.")
    bot_live = str(input(""))

    while bot_live != "start":
        break
    #if again entered, above will reiterate

if bot_live == "end":
    print("Thanks!")

#TabbyCat discord bot