# https://istinye.blackboard.com/ultra/courses/_8635_1/outline <<< Programlama ve Temel Algoritma dersinin eski uygulama pdflerine baktım.
# https://translate.google.com/?hl=tr <<< İngilizcemin yetmediği bazı yerleri çevirmek için kullandım.
# https://www.programiz.com/python-programming/if-elif-else <<< if-elif-else koşullu ifadelere baktım.
# https://www.w3schools.com/python/python_functions.asp <<< Fonksiyonlara baktım.
# https://www.w3resource.com/python-exercises/python-basic-exercise-3.php <<< Python datetime güncel zaman ve tarih çikarmaya baktım.


import datetime  

now = datetime.datetime.now() #güncel zaman için.

admin = ['Ibrahim', '1122']             #istenilen kullanıcılar ve hesap bilgileri.
users = [['Ahmet', '1234'], ['Zeynep', '4321'], ['Alberto', '4422']]
everything = [['Ahmet', '1234', 500, [], [], []], ['Zeynep', '4321', 700, [], [], []],
              ['Alberto', '4422', 1200, [], [], []]]


def loginScreen():
    print("   ------------------")
    print(" /       İSTANBUL      \ ")   #ana giriş ekranında karşılıyan şekil saat ve istanbul yazısı.
    print()
    y = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"|   {y}   |")
    print()
    print(" \                    /")
    print("   ------------------ ")
    print('--- Welcome to İSTİNYE Bank (v.0.1) ---')
    print('1. Login')
    print('2. Exit')
    x = (input('>>>'))   #giriş veya çıkış için tuş kodlaması. 
    if(x=='1'): 
        login()
    elif(x=='2'):
        print('Good bye you logged out.')
    else:
        print("Please enter a valid value")
        loginScreen()



def login():
    print("What do you want to login as:") #kullanıcı giriş veya admin giriş bölümü.
    print('1. Admin')
    print('2. User')
    print('3. Go Back')
    y = input("Yapacaginiz islemi secin: ")
    if(y=='1'): #admin giriş.
        AdminLogin()
    elif (y == '2'): #kullanıcı giriş.
        print('User Name: ')
        username = input('') #kullanıcı adı şifre yazdırma kodu.
        print('Password: ')
        password = input('')
        for x in users:
            if (x[0] == username and x[1] == password): #kullanıcı adı şifre onaylatma kodu.
                operations(username)
        else:
            print("Username or password is wrong please try again.")
            login()

    elif (y == '3'): #çıkış.
        loginScreen()
    else:
        print("Please enter a number that is a valid input")
        login()


def operations(username):  
    print(f"{username} Welcome to Sehir Bank") #kullanıcı girişi yapıldıktan sonraki seçim ekranı.
    print('Please enter the number of the service')
    print('1. Withdraw Money') #kullanıcının kullanabileceği özellikler.
    print('2. Deposit Money')
    print('3. Transfer Money')
    print('4. My Account Information')
    print('5. Logout')
    y = input('>>>') #kullanıcının seçeceği bölüme aktaran kod.
    if (y == '1'):  
        withdraw(username)
    elif (y == '2'):
        deposit(username)
    elif (y == '3'):
        transaction(username)
    elif(y== '4'):
        accountInfo(username)
    elif(y==str(5)):
        logout(username)
    else: #verilen numaralar dışında farklı numara yazarsa alacağı uyarı
        print(
            'Please enter a value between 1 and 5')  
        operations(username)


def withdraw(username):  #withdraw menüsü.
    print('Please enter the amount you want to withdraw:')
    withdraw = int(input('')) #girilecek sayı kodlaması.
    for x in everything:
        if (x[0]) == username:
            if (x[2] >= withdraw):
                x[2] -= withdraw
                y = now.strftime("%Y-%m-%d %H:%M:%S") #zaman
                x[3].append([y,withdraw," TL"])
                print(f"{withdraw} TL withdrawn from your account")
                print('Going back to main menu...')
                operations(username)

    else: #geçersiz miktar girerse uyarı.
        print(
            f"You don't have {withdraw} TL in your account")  
        print('Going back to main menu...')
        operations(username)

def deposit(username):  #deposit menüsü.
    print('Please enter the amount you want to deposit: ')
    deposit = int(input('')) # girilecek sayı kodlaması.
    for x in everything:
        if (x[0]) == username:
            x[2] += deposit
            y = now.strftime("%Y-%m-%d %H:%M:%S") #zaman
            x[4].append([y, deposit, " TL"])
            print(f"{deposit} TL added to your account")
            print('Going back to main menu...')
            operations(username)

def transaction(username):  #transfer menü.
    print('Warning: If you want to abort the transfer please enter abort ') #transfer öncesi uyarı.
    transfer_name = input("Please enter the name of the user you want transfer money to:") #transfer için girilecek isim.
    transactionControl(username, transfer_name)
    for x in everything:
        if(x[0]==transfer_name):
            transactionControl(username,transfer_name)
        else:
            transactionNameControl(username,transfer_name)

def transactionNameControl(username,transfer_name):
    if(transfer_name == "abort"):
        print('Going back to main menu...')
        operations(username)

    else: #yanlış isim girerse uyarı.
        print("User deos not exist !")
        transaction(username)

def transactionControl(username, transfer_name):

    for h in everything:
        if (h[0] == transfer_name):
            print(transfer_name)
            print("Please enter the amount you want to transfer: ") #yazılan isim doğru ise miktar girme. 
            transfer_money = int(input('')) #miktar yazma yeri.
            for z in everything:
                if (z[0] == username):
                    if (z[2] >= transfer_money): #seçilen tutar kadar parasının olup olmadığını kontrol etme.
                        z[2] -= transfer_money #yeterliyse parayı aktarır.
                        y = now.strftime("%Y-%m-%d %H:%M:%S") #zaman.
                        z[5].append([y,f"Transferred to {transfer_name}",transfer_money," TL"])

                        for x in everything:
                            if (x[0] == transfer_name):
                                x[2] += transfer_money #gönderilen parayı ekler. 
                                r= now.strftime("%Y-%m-%d %H:%M:%S") #zaman
                                x[5].append([r,f"Transferred to me from {username}",transfer_money," TL"]) #başarı ekranı.

                                print("Money transferred succesfully!") #para transferi başarılı olursa.
                                print('Going back to main menu...')
                                operations(username)
                    else:
                        print("Sorry! you don't have the entered amount.") #para transferi başarısız olursa.
                        print('1. Going back to main menu') #deneme seçenekleri veya çıkış.
                        print('2. Transfer again')
                        t = input("") #seçenek alan kod.
                        if (t == '1'): #tekrar deneme.
                            operations(username)
                        elif (t == '2'): #menü dönme.
                            operations(transaction(username))
                        else:
                            transactionControl(username, transfer_name)

def AdminLogin(): #ilk kullanıcı girişinde admin girişi.
    print('User Name: ') #admin isim.
    username = input('') #yazılan yer.
    print('Password: ') #admin şifre.
    password = input('') #yazılan yer.
    if(admin[0]==username and admin[1]==password): #admin giriş doğrulama.
        AdminPage(username)
    else: #hatalı giriş yönlendrime.
        print("Password or username is wrong. Try Again") #hatalı giriş ekranı.
        AdminLogin() #tekrardan giriş yönlendirme.

def AdminPage(username): #başarılı giriş sonrası admin seçenekleri.
    print(f"Welcome {username}")
    print("-----  Admin Menu -----")
    print("Please enter a number of the settings operations supported:")
    print("1. Add User") #kullanıcı ekleme.
    print("2. Remove User") #kullanıcı silme.
    print("3. Display All Users") #tüm kullanıcıları silme.
    print("4. Exit Admin Menu") #admin menü çıkış.
    y=input(">>> ") #istenilen seçeneğin girildiği yer.

    if (y == '1'):  #seçenekelere yönlendirme.
        AdminAddUser(username)
    elif (y == '2'):
        AdminRemoveUser(username)
    elif (y == '3'):
        AdminShowUser(username)
    elif(y== '4'):
        login()
    else:
        print(
            'Please enter a value between 1 and 4')  #farklı seçenek girerse alınan uyarı.
        AdminPage(username)

def AdminAddUser(username): #kullanıcı ekleme ekranı.
    print("Access granted")
    print("Enter the new username:") #isim.
    user=input(">>> ") #yazılan yer.
    print("Enter the new user passwordu:") #şifre.
    password = input(">>> ") #yazılan yer.
    users.append([user,password]) #yazılan kullanıcıyı users kullanıcı listesine .append ile ekleme.
    print(users)
    everything.append([user,password,0,[],[],[]]) #açılan kullanıcının bilgileri isim,şifre,para vb.
    print(everything)
    print(f"{user} was added as an user.") #başarılı ekranı.
    AdminPage(username)

def AdminRemoveUser(username): #kullanıcı silme.
    print("Access granted")
    print("Enter the username:") #isim.
    deluser=input(">>> ")#yazılan yer.
    for x in everything:
        if(x[0]==deluser):
            everything.remove(x) #kullanıcı silinen yer remove veya pop kullanarak.
            print(f"{deluser} was removed as an user to İSTİNYE Bank") #başarılı ekranı.
            AdminPage(username)
        else:
            print(f"{deluser} does not exist as an user to İSTİNYE Bank") #yanlış isim girilirse uyarı.
            AdminPage(username)

def AdminShowUser(username): #tüm kullanıcıların bilgilerini görme.
    print("Access granted")
    sayi=0

    print(f"There are {sayi} users using İSTİNYE Bank")
    print("    Name & Password:")
    for x in users:
        sayi+=1
        print(f"{sayi}. {x}")
    AdminPage(username)

def accountInfo(username):     #kullanıcı hesap geçmişi ve bilgileri.                    
    print("   ------------------")
    print(" /       İSTANBUL      \ ")
    print()
    y = now.strftime("%Y-%m-%d %H:%M:%S") #zaman.
    print(f"|   {y}   |")
    print()
    print(" \                    /")
    print("   ------------------ ")
    for x in everything:
        if(x[0]==username):
            print(f"Your Name:{x[0]} ")       #hesap bilgileri.     
            print(f"Your Password: {x[1]}")
            print(f"Your Amount (TL): {x[2]}")
            print('----------------')
            print("User Activities Report :")

            print("Your Withdrawals: ")
            for t in x[3]:
                print(t)
            print("Your Deposits:")
            for j in x[4]:
                print(j)
            print("Your Transfers:")
            print("Time Person Amount")
            for a in x[5]:
                print(a)
            operations(username)

def logout(username):  #en son çıkış.                            
    print(f"{username} logged out")
    login()


loginScreen()  # < En baştaki giriş ekranına yolladığım son ve bitiş kodum.
