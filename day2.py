# Dictionaries & Sets
# Write a program that:
# Takes a string input.
# Counts frequency of each word using dictionary.
# Stores unique words in a set.
# Merge two dictionaries. If a key exists in both, add their values.
# Create a student dictionary (roll_no: marks). Print:
# Students with marks > 75.
# Student with highest marks.
# Given two sets of students (one in Python course, one in Networking):
# Find students enrolled in both.
# Find students only in Python.
# Find total unique students.
dict = {}
student_record = {1:90,2:90,3:80,4:65}
print(student_record)
for values in student_record:    
    if student_record[values] > 75:
        print(student_record[values])
        
python = {'s1','s2','s3'}
network = {'s1','s4','s5','s3'}
print(python.intersection(network))
print(python.difference(network))
