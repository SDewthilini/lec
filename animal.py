import sys

def cat():
    print("Baw")

def default():
    print('I am an Dog')

def main():
    if sys.argv[1] == 'dog':
        cat()
    else:
        default()

if __name__ == '_main_':
    main()