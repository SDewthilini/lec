import sys

def cat():
    print("Mewo")

def default():
    print('I am an animal')

def main():
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '_main_':
    main()