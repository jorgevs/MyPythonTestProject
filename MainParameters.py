import sys

def myFuntion(param):
    print ("This is my function")

    try:
        print (sys.argv[1])
    except IndexError:
        print ("IndexError")
    finally:
        print ("Finally")

    return "The received parameter is: " + param


print (sys.argv[0])
if __name__ == "__main__":   # This will only be true if the script is called as the main program
    print ("Hi")
    x = myFuntion("XX")
    print (x)




