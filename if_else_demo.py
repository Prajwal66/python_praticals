import sys

if (len(sys.argv) < 2):
    print("please rerun and Enter arguments")
    sys.exit(1)


type = sys.argv[1]

if type == "t2.micro":
    print("we will creating a instance of type t2.micro")

elif type == "finder":
    print("enter a value to find even or odd")
    num = int(input("Number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")
else:
    print("free tier is not eligible ")
