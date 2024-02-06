from User import User
from Secretary import Secretary

def main():
    s = Secretary()
    s.create_test_users()
    print (str(s.users))



if __name__ == '__main__':
    main()