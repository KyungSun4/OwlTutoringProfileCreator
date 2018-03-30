
# coding: utf-8

# In[114]:


import pandas as pd
import re

# Read submissions file
applications = pd.read_csv("submissions.csv")

# Create dataframe to store profiles
profiles = pd.DataFrame(columns = ["name", "contact", "bio", "subjects", "days", "form_name"])


# In[115]:



# Get rid of done applications
applications = applications[applications["Unnamed: 11"].isin(["done"])==False]

# Fill in basic parts of profiles: Name and Submission Form name
profiles["form_name"] = applications["Name"]+" Submision Form"
profiles["name"] = applications["Name"]

# Use names as indeces
profiles = profiles.set_index("name")
applications = applications.set_index("Name")


# In[116]:


# List generation functions
def get_availabilty_list(string):
    ''' Givena comma seperated list of days, return a vertical
        list of days
    '''
    days = [x for x in string.split(", ") if x != ", "]
    return_string = ""
    for i, day in enumerate(days):
        return_string += day
        if i < len(days)-1:
            return_string += "\n"
    return return_string

def get_subject_list(string):
    ''' Givena a comma seperated list of subjects and levels, 
        return a vertical list of subjects
    ''' 
    subjects = [x for x in string.split(", ") if " Level Subjects" not in x and x != ", "]
    
    return_string = ""
    for i, subject in enumerate(subjects):
        return_string += subject
        if i < len(subjects)-1:
            return_string += "\n"
    return return_string
        


# In[117]:


# String parseing functions
def get_grade(string):
    ''' Given a string that the tutor inputed as their grade,
        figure out what grade is and return a clean consistent
        string of this grade. Return error if unexpected input
    '''
    for i in ["11", "junior"]:
        if re.search(i, string, re.IGNORECASE):
            return "Junior"
    for i in ["12", "Senior"]:
        if re.search(i, string, re.IGNORECASE):
            return "Senior"
    for i in ["10", "sophomore"]:
        if re.search(i, string, re.IGNORECASE):
            return "Sophomore"
    for i in ["9", "Freshman"]:
        if re.search(i, string, re.IGNORECASE):
            return "Freshman"
    return "ERROR"

def get_school(string):
    ''' Given the input string of the tutors school, check for
        trigger words and output the formated name of that school
    '''
    schools = {"libertyville": "Libertyville High School", "stevenson":"Stevenson High School", "vernon hills":"Vernon Hills High School", "carmel":"Carmel Catholic High School", "mundelein":"Mundelein High School", "naperville central":"Naperville Central High School", "neuqua":"Neuqua Valley High School", "waubonsie":"Waubonsie Valley High School"}
    for key in schools:
        if re.search(key, string,re.IGNORECASE):
            return schools[key]
    return "ERROR"

def get_subjects(string):
    ''' Given a string of subjects and grades fromsubmission form, 
        return a formated list of subjects
    '''
    subjects = string.split(", ")
    subjects = [x for x in subjects if " Level Subjects" not in x and x != ", "]
    
    return_string = ""
    for i, subject in enumerate(subjects):
        if i == len(subjects)-1 and i != 0:
            return_string += "and "
        return_string += subject
        if i != len(subjects)-1:
            return_string += ", "
    return return_string

def get_grades(string):
    ''' Given a list of grades and subjects from submission form
        return a formated list of grades
    '''
    grades = string.split(", ")
    grades = [x for x in grades if " Level Subjects" in x and x != ", "]
    
    return_string = ""
    for i, grade in enumerate(grades):
        grade = grade.split(" Level Subjects")[0]
        if i == len(grades)-1 and i != 0:
            return_string += "and "
        return_string += grade
        if i != len(grades)-1:
            return_string += ", "
    return_string += " Level Subjects"
    return return_string

def get_availability(string):
    ''' Given a string of days from submission form, 
        return a formated list of days
    '''
    days = [x for x in string.split(", ") if x != ", "]
    
    return_string = ""
    for i, day in enumerate(days):
        if i == len(days)-1 and i != 0:
            return_string += "and "
        return_string += day
        if i != len(days)-1:
            return_string += ", "
    return return_string



# In[119]:


# For every application
for index, row in applications.iterrows():
    
    '''
    Grade: Junior

    Highest Education: High School

    Email: student@students.d100.org

    Phone: (123) 123-1234

    Tutoring Experience: 0 years
    '''
    # Create basic contact info
    profiles.loc[index,"contact"] = "Grade: " + get_grade(row.Grade) + "\n"         + "School: " + get_school(row.School) + "\n"         + "Email: " + row["Email Address"] + "\n"         + "Phone: " + row.Phone + "\n"         + "Tutor Experience: DONT_FORGET_THIS_IRONIC_I_FORGOT_IT years\n"     
    '''
    Subjects I Teach: Science, Math and English

    Grades I Teach: Elementary School Level Subjects and Junior High Level Subjects

    Availability: Sunday, Thursday and Saturday

    Bio:  this is a bio. bios are usually longer
    '''
    # Create additional info paragraph
    profiles.loc[index,"bio"] = "Subjects I Teach: " + get_subjects(row.Subjects) + "\n"         + "Grades I Teach: " + get_grades(row.Subjects) +"\n"         + "Availability: " + get_availability(row.Availability) + "\n"         + "Bio: " + row.Biography
    profiles.loc[index,"days"] = get_availabilty_list(row.Availability)
    profiles.loc[index,"subjects"] = get_subject_list(row.Subjects)
    


# In[122]:



# Save profiles in csv
out_name = input("Enter output file name, should be csv: ")
profiles.to_csv(out_name)


# In[ ]:




