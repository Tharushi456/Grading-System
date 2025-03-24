# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solution.
# Student ID: 20232322
# Date: 14/12/2023


from graphics import *    #import the graphics.py module

#Variables
creditList = [0, 20, 40, 60, 80, 100, 120]
progressionList = [] 
progress_students = 0
trailer_students = 0
exclude_students = 0
retriever_students = 0
programExit = "y"
firstTime = True
total_outcomes = 0

#user defined functions
def CreditValidation(pass_credits, defer_credits, fail_credits):  #Defining a function to check the progression
    global progress_students
    global trailer_students
    global exclude_students
    global retriever_students

    if pass_credits == 120:
        progress_students += 1
        progressionList.append("Progress")  # Adding "progress" to the progressionList
        progressionList.extend([pass_credits, defer_credits, fail_credits])  # Adding the credits to the progressionList
        print("Progress\n")
    elif pass_credits == 100:
        trailer_students += 1
        progressionList.append("Progress (module trailer)")  # Adding "module trailer" to the progressionList
        progressionList.extend([pass_credits, defer_credits, fail_credits])  #Adding the credits to the progressionList
        print("Progress(Module Trailer)\n")
    elif pass_credits <= 40 and defer_credits <= 40 and fail_credits >= 80:
        exclude_students += 1
        progressionList.append("Exclude")  #Adding "Exclude" to the progressionList
        progressionList.extend([pass_credits, defer_credits, fail_credits])  #Adding the credits to the progressionList
        print("Exclude\n")
    else:
        retriever_students += 1
        progressionList.append("Module retriever")  #Adding "Module retriever" to the progressionList 
        progressionList.extend([pass_credits, defer_credits, fail_credits])  #Adding the credits to the progressionList
        print("Module retriever\n")


def GettingCredits():     #Defining a function to input credits
    global total_outcomes
    
    while True:
        try:  #Checking the data type
            pass_credits = int(input("\nEnter your total PASS credits:"))
            if pass_credits not in creditList:    #Checking the range of pass credits
                print("Out of range\n")
                continue
            defer_credits = int(input("Enter your total DEFER credits:"))
            if defer_credits not in creditList:    #Checking the range of defer credits
                print("Out of range\n")
                continue
            fail_credits = int(input("Enter your total Fail credits:"))
            if fail_credits not in creditList:     #Checking the range of fail credits
                print("Out of range\n")
                continue
            if (pass_credits + defer_credits + fail_credits) == 120:     #Checking the total 
                CreditValidation(pass_credits, defer_credits, fail_credits)      #Checking the progression
                total_outcomes += 1
                break
            else:
                print("Total Incorrect\n")  #Display "Total incorrect" if the total is incorrect
        except ValueError:
            print("Integer required\n") #Display "Integer required" if wrong data type is entered



            


category = str(input("Enter category [student/staff]: "))  #input the category of the user ("student" or "staff")

while category.lower() != "student" and  category.lower() != "staff":   #Checking whether the input is valid ("student" or "staff")
    print("\nInvalid input.Please try again.")  #getting the input again if the input is invalid
    category = str(input("Enter category [student/staff]: "))
    
if category.lower() == "student":     #getting the credits once if the user is a student
    GettingCredits()
    
elif category.lower() == "staff":      #getting the credits multiple times if the user is a staff member
    while (programExit == "y"):
        if firstTime == True:
            GettingCredits() #input credits and checking the progression in the first attempt
            firstTime = False
            #asking the user input "y" or "q" from the second attempt

        print("Would you like to enter another set of data?") #asking whether to quit or continue to input data
        programExit = input("Enter 'y' for yes or 'q' to quit and view results:")
        
        while programExit != "y" and programExit != "q":  #Checking whether the input is valid ("y" or "q")
            print("\nInvalid input.Please try again.")  #getting the input again if the input is invalid
            programExit = input("Enter 'y' for yes or 'q' to quit and view results:")

        if programExit.lower() == "y": #input another set of data if user input "y"
            GettingCredits() #input credits and checking the progression
            
        elif programExit.lower() == "q":  #quit the program and display the histogram if user input "q"

            def main():
                # open the window
                win = GraphWin("Histogram", 750, 700)
                win.setBackground("white")
                # Drawing a line
                aLine = Line(Point(50, 500), Point(700, 500))
                aLine.draw(win)
                # Drawing rectangle for "Progress"
                ProgressRectangle = Rectangle(Point(100, 500 - (progress_students * 20)), Point(200, 500))
                ProgressRectangle.setFill(color_rgb(204, 235, 197))
                ProgressRectangle.draw(win)
                #Drawing rectangle for "Module trailer"
                TrailerRectangle = Rectangle(Point(250, 500 - (trailer_students * 20)), Point(350, 500))
                TrailerRectangle.setFill(color_rgb(141, 186, 127))
                TrailerRectangle.draw(win)
                #Drawing rectangle for "Module retriever"
                RetrieverRectangle = Rectangle(Point(400, 500 - (retriever_students * 20)), Point(500, 500))
                RetrieverRectangle.setFill(color_rgb(230, 245, 226))
                RetrieverRectangle.draw(win)
                #Drawing rectangle for "Exclude"
                ExcludeRectangle = Rectangle(Point(550, 500 - (exclude_students * 20)), Point(650, 500))
                ExcludeRectangle.setFill(color_rgb(185, 204, 179))
                ExcludeRectangle.draw(win)
                # Display "histogram results" on top
                histogram_results = Text(Point(150, 50), "Histogram Results")
                histogram_results.setSize(25)
                histogram_results.setTextColor(color_rgb(63, 128, 70))
                histogram_results.draw(win)
                # Display the outcome "Progress"
                progress_title = Text(Point(150, 520), "Progress")
                progress_title.draw(win)
                #Display the outcome "Trailer"
                Trailer_title = Text(Point(300, 520), "Trailer")
                Trailer_title.draw(win)
                #Display the outcome "Retriever"
                Retriever_title = Text(Point(450, 520), "Retriever")
                Retriever_title.draw(win)
                #Display the outcome "Exclude"
                Exclude_title = Text(Point(600, 520), "Exclude")
                Exclude_title.draw(win)
                #Display number of total outcomes at the bottom
                Total_outcomes_title = Text(Point(150, 575), f"{total_outcomes} outcomes in total")
                Total_outcomes_title.setSize(21)
                Total_outcomes_title.setTextColor(color_rgb(63, 128, 70))
                Total_outcomes_title.draw(win)
                #Diplay number of students for "Progress"
                ProgressTotal = Text(Point(150, 490 - (progress_students * 20)), progress_students)
                ProgressTotal.draw(win)
                #Display number of students for "Trailer" 
                TrailerTotal = Text(Point(300, 490 - (trailer_students * 20)), trailer_students)
                TrailerTotal.draw(win)
                #Display number of students for "Retriever"
                RetrieverTotal = Text(Point(450, 490 - (retriever_students * 20)), retriever_students)
                RetrieverTotal.draw(win)
                #Display number of students for "Exclude"
                ExcludeTotal = Text(Point(600, 490 - (exclude_students * 20)), exclude_students)
                ExcludeTotal.draw(win)

                win.getMouse()
                win.close()

            main()

            # Part 2
            count = 0  
            num_students = int(len(progressionList) / 4) #getting the number of total students 
            for i in range(0, num_students):
                #printing outcome and credits of each student
                print(f"{progressionList[count]} - {progressionList[count + 1]} , {progressionList[count + 2]} , {progressionList[count + 3]}")
                count += 4  #adding 4 to access the credits of the next student

            # Part 3

            file = open("creditfile.txt", 'w') #opening a text file to write the credits of students
            count = 0
            for i in range(0, num_students):
                #writing outcome and credits of each students in the text file
                file.write(f"{progressionList[count]} - {progressionList[count + 1]} , {progressionList[count + 2]} , {progressionList[count + 3]}\n")
                count += 4  #adding 4 to access the credits of the next student
            file.close()   






    
