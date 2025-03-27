# 7.1. File Reading and Writing

# Python allows us to read and write data to external files. We can open files in different modes, such as read ("r"), write ("w"), or append ("a"), and perform read and write operations.

# Reading files
# To read the contents of a file, we must first open it using the open() function in read mode ("r"). Then, we can read the file's contents using methods like read() or readlines().

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# In this example, the file "data.txt" is opened in read mode using open(). Then, the entire content of the file is read using the read() method and stored in the content variable. Finally, the content is displayed on the screen, and the file is closed using the close() method.

# Writing files
# To write data to a file, we open it in write mode ("w") using the open() function. If the file does not exist, it will be created automatically. If the file already exists, its content will be overwritten.

file = open("data.txt", "w")
file.write("Hello, world!")
file.close()
# In this example, the file "data.txt" is opened in write mode using open(). Then, the string "Hello, world!" is written to the file using the write() method. Finally, the file is closed using the close() method.

# You can also use the with statement to handle opening and closing files automatically.

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# In this case, the file is opened using the with statement and is automatically closed once the with block is exited, even if an exception occurs.

# Input and output in Python offers great flexibility for interacting with the user and manipulating external files. We can request information from the user, display results on the screen, and read or write data to text files. Always remember to handle file opening and closing properly and consider possible exceptions that may occur during input/output operations.