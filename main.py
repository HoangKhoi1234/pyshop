import login

while True:
    menu = ['1: Xem sách', '2: Thêm sách','6: Đăng xuất']
    book = [['ABCE','Sách huyền bí','Mai Hoàng Khôi',2024],['XYZA','Sách toán chuyên','Mai Hoàng Khôi',1000]]
    user=[['khoi', '123']]
    print('SIGN UP')
    check=login.checklogin(user)
    while check ==1:
        print('YOUR OPTIONS:')
        for i in range(0,len(menu)):
            print(menu[i])
        option = int(input('CHOOSE OPTION: '))
        if option ==6:
            print('ĐĂNG XUẤT')
            break
        if option ==1:
            for i in range(0,len(book)):
                print(book[i])

        
    
            
        


