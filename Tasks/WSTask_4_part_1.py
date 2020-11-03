import pdb
students = int(input("Enter the number of students: "))
books = int(input("Enter the number of books: "))
distribution = books//students
remainder = books % students 
print("Every student will have",distribution,"books each and there will be",remainder," books left.")
