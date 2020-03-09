agirlik = int (input("Lütfen ağırlığınızı giriniz(kg):"))

boy = int (input("Lütfen boyunuzu giriniz (cm):"))

boy = boy/100

bki = agirlik/(boy*boy)

print("Beden Kütle İndeksi: {}".format(round(bki)))

print ("BKİ: ", bki)



if  bki < 18.5 :

    print("Zayıfsınız")

    print("{} Kilo Almanız Gerekiyor.".format(round(25*(boy*boy) - agirlik)))

elif bki < 25 :

    print("Normal Kilodasınız.")

elif bki < 30:

    print("Fazla Kilolusunuz.")

    print("{} Kilo Vermeniz Gerekiyor.".format(agirlik - round(25*(boy*boy) )))

elif bki < 35:

    print("1. Derece Obezsiniz.")

    print("{} Kilo Vermeniz Gerekiyor.".format(agirlik - round(25*(boy*boy) )))

elif bki < 40:

    print("2. Derece Obezsiniz.")

    print("{} Kilo Vermeniz Gerekiyor.".format(agirlik - round(25*(boy*boy) )))

elif bki < 45:

    print("3. Derece Obezsiniz.")

    print("{} Kilo Vermeniz Gerekiyor.".format(agirlik - round(25*(boy*boy) )))