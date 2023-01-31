#In a file called extensions.py, implement a program that
#  prompts the user for the name of a file and then outputs 
# that file’s media type if the file’s name ends, case-insensitively, 
# in any of these suffixes:
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
#If the file’s name ends with some other suffix or has no suffix at all,
#  output application/octet-stream instead, which is a common default.


def files_name ():
    answer =str(input("File's name: ").lower())
    if answer.endswith(".gif"):
        print("image/gif")
    elif answer.endswith(".jpeg"):
        print("image/jpeg")
    elif answer.endswith("jpg"):
        print ("image/jpeg")
    elif answer.endswith(".png"):
        print("image/png")
    elif answer.endswith(".pdf"):
        print("application/pdf")
    elif answer.endswith(".txt"):
        print("text/plain")
    elif answer.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

files_name()