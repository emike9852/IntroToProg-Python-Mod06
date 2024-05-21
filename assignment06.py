# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Mike Espinoza, 05/19/2024,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Defining constants
FILE_NAME: str = 'Enrollments.json'
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
    '''

# Defining variables
students: list = []
menu_choice = ''

# Defining classes and functions
class ProcessFileData:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when reading the file!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!",e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_current_data(student_data: list):
        print('='*40)
        for item in student_data:
            print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, CourseName: {item['CourseName']}")
        print('='*40, end='\n\n')  

    @staticmethod
    def output_menu(menu: str):
        print(menu,end='\n\n')  

    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  
                raise Exception("You must choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  
        return choice

    @staticmethod
    def input_data_to_table(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Enter the course: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_data.append({"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name})
        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)  
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)
        return student_data

student_table = ProcessFileData.read_data_from_file(
                    file_name=FILE_NAME, student_data=students)

# Input from user
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

# Enrolling a student for a course
    if menu_choice == "1":
        student_table = IO.input_data_to_table(student_data=students)
        print("\n Here is the current list of data")
        IO.output_current_data(student_data=student_table)
        continue

# Showing user the current data
    if menu_choice == "2":
        IO.output_current_data(student_data=students)
        continue

# Saving the data to the .json file
    elif menu_choice == "3":
        ProcessFileData.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

# Exiting the program
    elif menu_choice == "4":
        break  