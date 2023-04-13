# School Report GUI


This is a beginner project. Any suggestions on how to improve it or PRs as well as criticism is warmly welcome.

To use the app,
* First read the README 
* Clone the repo
* Install the requirement
* Run the script (For a quick test, you can reduce the number of students in the file: students_file.csv.
    Else, the app will require you to calculater for ALL students.)


How the app works

To begin, the user must select a menu from the Menu list. If the Calculate records menu is selected, the
following steps are valid:

    Step 1 : To begin, the user must first press the "Next" button below. Then the first student is selected.

    Step 2 :The user must then manually enter the scores for each subject under a section. For each section,that is, Quiz Score,
            home work,class attendance,exam, there are entries for four subjects:chemistry,biology,physics and maths. After entering
            each score, the user must press the "calculate" button to get the average scores,gpa,grade and status for that student.

    Step 3 : Then the user must press the "Next student" button to proceed to the next available student.

    Step 4 : Repeat steps 2 and 3 until all students data has been generated.
    Step 5 : When the last student's scores has been calculated, a "save" button pops up. Then a dialog opens for the user to
             choose a directory to store the generated students' record files. The default file extension is .csv.


    Note:  Please note that the calculate button does not perform any calculations until all entries are filled and a valid student
    is selected and the "Next student" button does not function until the current selected student's values have been calculated.
    This means that to proceed to the next student, you must first enter all scores and press the calculate button.

    Also, if the user enters a score more than the total score for a section(this can be found in the grade components file in the repo), the app does not perform a calculation.

    If a successful calculation is performed, the average score for each subject,the total average score of all subjects,
    the GPA, grade and status is shown to the user.

    If no calculation is performed, please check that a valid student is shown in the "Student Name" and "ID" columns.Check
    that an entry is filled and it is not more than the total score for that section.

    If pressing the "Next student" button does not take you to the next student page, ensure that a successful calculation
    of the current student scores has been executed.

else if the user selects the Perform search menu, the following steps are valid:

     Steps : First, choose a search filter by clicking the filter arrows.
              In the full performance filter, the user gets the full performance of a student by entering a student's
              name or ID.

              In the Subject performance filter, the user gets the total average of a student in a particular subject. The
              requirements are: the user must type in a student's name or ID and a subject(bio,chem,phy or math) in the
              respective entries.

              In the Grades filter, the user gets all students that attain a certain grade. The requirement is that the
              user must type in a grade (a,b,c,d,e or f) in the provided entry

              In the Grades filter, the user gets all students that attain a certain status(pass,fail or retake).
              The requirement is that the user must type in a grade (pass,fail or retake) in the provided entry

else if the user selects the Exit menu, the application ends.

To execute the python script, run the main.py file.