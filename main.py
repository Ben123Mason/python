score=0
# ask the user their name and store it
name =input("What is your name?")
#greet the user and introduce the quiz
print("Welcome to this quiz",name)
print("This quiz is about capital citys of the world")
#ask the user a question
question_format= "{}\nA.{} \n B.{} \n C.{} \n D.{} \n"
question= "What is the capital city of New Zealand?"
A="wellington"
B="Auckland"
C="Queenstown"
D="Russel"
answer= input(question_format.format(question, A, B, C, D )).lower()
#check the user's answer and give feedback
if answer== "wellington" or answer== "A".lower():
    print ("correct")
    score+=5
elif answer== "":
    print ("Try Harder next time ")
else:
   print("WRONG") 
print("The answer is Wellington")
#end the quiz
print("thank you for playing {} your score is {}".format(name,score))
