import re

# Opening the file ad reading all it's data
file=open("text.txt","r")
# Storeing the data in a variable.
information_of_file=file.read()
# This is the pattern used for email search.
pattern=re.compile("[a-zA-Z0-9]+\@+[a-zA-Z]+\.+[a-z]+")
result=pattern.findall(information_of_file)
print("The email found is :", result)

# Never forget to close the file.
file.close()