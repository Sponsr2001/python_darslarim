#son = -54
#if son<0:
#    print("manfiy son")
#else:
#    print('musbat son')

#yosh = int(input('Yoshingiz nechchida>>> '))
#if yosh<=4:
#    print('Sizga kirish bepul.')
#elif yosh<=12:
#    print('sizga kirish 5000 ming so\'m.')
#else:
#    print('sizga kirish 120000 ming so\'m.')

#kun = input("Bugun kun nima>>> ")
#if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    print("Bugun dam olish kuni.")
#else:
#    print("Bugun ish kuni.")

#kun = input("Bugun kun nima>>> ")
#harorat = float(input("Havo harorati qanday>>> "))
#if kun.lower() == 'yakshanba' and harorat>=30:
#    print('Cho\'milgani kettik ')
#elif kun.lower() == 'yakshanba' and harorat<30:
#    print("Uyda dam olamiz.")

#narx = 15000
#choy = True
#salat = True
#if choy and salat:
#    narx = narx + 10000
#elif choy or salat:
#    narx = narx + 5000

#print( narx)

#narx = 20000
#choy = 1
#salat = 0
#non = 1
#kampot = 0
#assorti = 1

#if choy:
#    print("Mijoz choy oldi")
#    narx = narx + 1000

#if salat:
#    print("Mijoz salat oldi")
#    narx = narx + 3000

#if non:
#    print("Mijoz non oldi")
#    narx = narx + 5000

#if kampot:
#    print("Mijoz kampot oldi")
#    narx = narx + 1000


#if assorti:
#    print("Mijoz Assorti oldi")
#    narx = narx + 7000

#print(f"Jami {narx}")

#menu = ['somsa ','osh', 'shashlik', 'norin']
#'manti' in menu
#ovqat = input("Nima ovqat yeysiz>>> ")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi.")
#else:
#    print("Bizda bunday ovqat yo'q.")

#menu = ['osh', 'shashlik', 'norin', 'kabob', 'somsa']
#buyurtmalar = ["osh","shashlik"]
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
#else:
#     print("Hech narsa harid qilmadingiz")

#      Uyga vazifa!!!

#son = int(input("Juft son kiriting>>> "))
#if son%2 == 0:
#    print("Raxmat.")
#else:
#    print("Bu juft son emas.")

#yosh = int(input("Yoshingizni kiriting>>> "))
#if yosh<=4 or yosh>=60:
#    print("Sizga kirish bepul. ")
#elif yosh<18:
#    print("Sizga kirish 10000 so'm. ")
#else:
#    print("Sizga kirish 20000 so'm ")

#son1 = float(input("Birinchi sonni kiriting>>> "))
#son2 = float(input("Ikkinchi sonni kiriting>>> "))
#if son1<son2:
#    print(f'{son1}<{son2}')
#elif son1>son2:
#    print(f'{son1}>{son2}')
#elif son1==son2:
#   print(f'{son1}={son2}')

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
#   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)
#if mavjud_emas:
#  print("Do'konimizda quyidagi mahsulotlar yo'q:")
#  for mahsulot in mavjud_emas:
#    print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
  #             'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)
#if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q")
#    for mah in mavjud_emas:
#        print(mah)
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
        
#login = ['anvar','javohir','husan','hasan','akobir']
#new = input("login kiriting: ")
#if new in login:
#       print("Yangi login kiriting.")
#else:
#       print("Xush kelibsiz.")

son = int(input("Istalgan butun sonni kiriting: "))
for n in range(2,11):
    if son % n == 0:
        print(f"{son} ni {n} ga qoldiqsiz bo'linadi.")
    
   
       





        
        
        

