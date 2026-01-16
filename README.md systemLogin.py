# this is the simple program in if , else condition 

email = input('Enter the email : ')
password = input('Enter the password : ')
# uses if . else and elif condition
# which are making nested if condition

if email == 'shivamofficer@gmail.com' and password == '1234':
    print(" Welcome! ")
elif email == 'shivamofficer@gmail.com' and password  != '1234':
    password = input('Enter again password : ')
    if password  == '1234':
        print(" WELCOME,FINALLY ")
    else :
        print('Beta tumsa nahi ho paayga ')
else :
    print("Not correct ")

