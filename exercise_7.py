# Write a Python program that accepts a filename from the user 
# and prints the extension of the file.
# Sample filename : abc.java
# Output : java

filename = input("Input filename: ")
file_type = filename.split('.')
print(f'File type is {file_type[-1]}.')