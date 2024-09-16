def checklogin(user):

    cur_user=input('Enter your username: ')
    cur_pass=input('Enter your password: ')
    check_login=0
    for i in range(0,len(user)):
        if user[i][0]==cur_user and user[i][1]==cur_pass:
            check_login=1
            break
        
    
    if check_login==1:
        print ('Login successful')
        return check_login

    else:
        print ('Failed to login')
        return check_login
