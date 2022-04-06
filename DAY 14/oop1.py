# ad,soyad,email
# Istifadəçilərimi bir yerə yığmaq üçün bir baza təyin etdim
from glob import glob
from os import remove


users=[]
# İstifadəçi istehsal etmək üçün bir qəlib təyin etdim
class User:
    def __init__(self,_ad,_soyad,_email):
        self.Ad=_ad
        self.Soyad=_soyad
        self.Email=_email
    def getUserData(self):
        return f'{self.Ad} | {self.Soyad} | {self.Email}'
# İstifadəçiləri qeydiyata alan funksiya təyin etdim   
def UserRegistration():
    daxilEdilenAd=input('Zəhmət olmasa adınızı daxil edin:')
    daxilEdilenSoyad=input('Zəhmət olmasa soyadınızı daxil edin:')
    daxilEdilenEmail=input('Zəhmət olmasa email adresinizi daxil edin:')
    daxilEdilenuserad=input('Silmek istediyiniz userin adin daxil edin:')
    user=User(daxilEdilenAd,daxilEdilenSoyad,daxilEdilenEmail)
    users.append(user)
# İstifadəçi məlumatlarını ekranda göstərmək üçün funksiya təyin etdim
def ShowAllUser():
    for user in users:
        print(user.getUserData())
        
def Userisilmek():
    users.remove('User')


while True:
    programMenyusu="""
    - Qeydiyyat üçün 1 yaz
    - İstifadəçiləri görmək üçün 2 yaz
    - Programdan çıxmaq üçün 3 yaz
    - Istifadecini silmek ucun 4 yaz
    """
    print(programMenyusu)
    istifadəçininQerarı=input('Hansı əməlyatı yerinə yetirmək istəyirsən? : ')
    if istifadəçininQerarı=="1":
        UserRegistration()
    elif istifadəçininQerarı=="2":
        ShowAllUser()
    elif istifadəçininQerarı=="3":
        break
    elif istifadəçininQerarı=="4":
        Userisilmek()
        
    else:
        print('Qərarınızı anlaşılmayan qərardır.Təkrar cəhd edin')
