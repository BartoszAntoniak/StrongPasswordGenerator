import random, re, pyperclip

Characters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=']
StrongPassword1 = re.compile("[QWERTYUIOPASDFGHJKLZXCVBNM]")
StrongPassword2 = re.compile("[qwertyuiopasdfghjklzxcvbnm]")
StrongPassword3 = re.compile("\d")
StrongPassword4 = re.compile("[$&+,:;=?@#|'<>.-^*()%!]")

def ListToString(list):
    PasswordString = ''
    for character in list:
        PasswordString += str(character) 

    if StrongPassword1.findall(PasswordString)!= []:
        if StrongPassword2.findall(PasswordString) != []:
            if StrongPassword3.findall(PasswordString) != []:
                if StrongPassword4.findall(PasswordString) != []:
                    pyperclip.copy(PasswordString) 
                    print(PasswordString)
                else:
                    PasswordGenerator()
            else:
                PasswordGenerator()
        else:
            PasswordGenerator()
    else:
        PasswordGenerator()
    return

def PasswordGenerator():
    PasswordList = []
    i=1

    while i <= 10:
        PasswordList.append(Characters[random.randrange(74)])
        i=i+1
    ListToString(PasswordList)
    return

print('Randomly generated strong password for you is:')
PasswordGenerator()
print('This password was just copied to your clipboard')
end = input()

