# FILE NAME - compliment_02.py

# NAME: Jared Thibado
# DATE: 02/25/2026
# BRIEF DESCRIPTION: a program that gives a compliment if "yes" is input, but will say 'no compliment for you' for any other input.  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def compliment_question():

    user_question = input("Would you like a compliment? ")
    if user_question == "yes":
        print("You have wonderful eyes.")
        print("Thank you for playing.")
    elif user_question != "yes":
        print("No compliment for you!")
        print("Thank you for playing.")
    
compliment_question()








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? Yes
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? y
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? no
No compliment for you!
Thank you for playing.
'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you struggle with this lab (YES/NO)?
NO






'''
