'''
Isn't it great that i have to write code to write my code?
No, everything needs to be redone.

Creates function calls with list of tutor spreadsheets inputs. Whenever a new tutor is added
their name can be added to the csv list and the new functions can be created that include their
name.

Example outputs:
=INCOME({'Name1'!A$11:A, 'Name2'!A$11:A},{'Name1'!B$11:B, 'Name2'!B$11:B}, TutorList!B$3:B$NUMBER_OF_TUTORS_PLUS_2,{'Name1'!E$11:E, 'Name2'!E$11:E},A3, B3)

=PAIDOUT({'Name1'!A$11:A, 'Name2'!A$11:A},{'Name1'!B$11:B, 'Name2'!B$11:B}, TutorList!B$3:B$NUMBER_OF_TUTORS_PLUS_2,{'Name1'!E$11:E, 'Name2'!E$11:E},{'Name1'!F$11:F,'Name2'!F$11:F},A3, B3)
'''
import csv

names = []

def create_name_list(names, before, after, divider):
	'''
	Given a list of names, creates a string that is a list with properties defined by the parameters
	before: before every name
	after: after each name
	divider: between each item, not at beginig of list or end
	'''
	string = ""
	for index, name in enumerate(names):
		string += before + name + after
		if index != (len(names)-1):
			string += divider
	return string

# Get names from csv file
with open('tutors.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		names.append(row[0])
		print(row[0])

# Create output strings
total_in_string = "=INCOME"
total_out_string = "=PAIDOUT"

shared_string = "({"
shared_string += create_name_list(names, "'", "'!A$11:A", ", ")
shared_string += "},{"
shared_string += create_name_list(names, "'", "'!B$11:B", ", ")
shared_string +="}, TutorList!B$3:B$" + str(len(names)+2)

total_in_string += shared_string 
total_in_string += ",{"
total_in_string += create_name_list(names, "'", "'!E$11:E", ", ")
total_in_string += "},A3, B3)"

total_out_string += shared_string
total_out_string +=",TutorList!C$3:C$" + str(len(names)+2)
total_out_string += ",{"
total_out_string += create_name_list(names, "'", "'!E$11:E", ", ")
total_out_string += "},{"
total_out_string += create_name_list(names, "'", "'!F$11:F", ", ")
total_out_string += "},A3, B3)"

# Output strings to terminal and save to files
print("\n\nTotal In function:\n\n")
print(total_in_string)

with open('total_in.txt', 'w') as file:
    file.write(total_in_string)

print("\n\nTotal out function:\n\n")
print(total_out_string)

with open('total_out.txt', 'w') as file:
    file.write(total_out_string)

