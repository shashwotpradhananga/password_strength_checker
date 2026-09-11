
#So this is my initial project, I am developing a password strength checker 
#This a version 1, As the versions of AI, It's version will also keep on developing as I keep learning

password = input("Enter your password")

#Modern cybersecurity standards recommend a minimun length of 16 character for a password to be considered strong, with 12 serving as bare minimun

length = len(password)
if length >= 12:
    
    print(" Your password in strong")
else:
    print(" Your password in weak")
    print(" Try another password")

