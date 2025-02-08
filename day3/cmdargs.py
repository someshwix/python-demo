import sys
# Working with command line arguments
# Usage: python cmdargs.py murthy 

if len(sys.argv) > 1:
    print("You have passed the following arguments:")
    for index, argval in enumerate(sys.argv):
        print(f"arg{index}: {argval}")
    print(f"Your argument value is: {sys.argv[1]}")
else:
    print("Sorry, please pass arguments; Usage: python file.py args...")