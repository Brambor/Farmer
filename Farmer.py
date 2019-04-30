import random
import time
import os

def help():
    print("Write number to go through.\nIf you want to go back write 'back'.\n")

print("_________________________\n*Welecome to The Farmer!*\n\nIf you need help write 'help'.\n")
time.sleep(0.8)
while True:
  menu0=input("1. Play\n2. About\n3. Exit game\n")
  if menu0=="1":
    while True:
        kontrola=open("existing saves.txt","r")
        kontrola1=kontrola.read()
        kontrola.close()
        print("1. New game")
        if kontrola1 != "":
            print("2. Load game\n3. Delete save")
        menu=input()
        breakit=False
        if menu=="help":
           help()
        elif menu == "1":
            place="Home"
            Day,Atime,Time1,Time2,Time3=[0]*5
            Time=480
            dum={}
            stanek={"Strawberry":7}
            plants=["StrawberryPlant.750.0","StrawberryPlant.750.0","StrawberryPlant.750.0","StrawberryPlant.750.0"]
            shanks=["StrawberryPlant.0.3.750","StrawberryPlant.0.3.750","StrawberryPlant.0.3.750","StrawberryPlant.0.3.750"]
            JidloKg={"bread":2,"jam":0.2}
            JidloKs={"Strawberry":1}
            Zakaznici=["Bugopaki.M.1-3.16-18.0.1020.50.0.10.Strawberry,5-10,6,4"]
            ZakazniciStanek={"Naxona.F.1-3.16-18.0.1020.50.0.10.Strawberry,5-10,6,4":5}
            Ceny={}
            penezenka=100.0
            saturation=700
            break
        elif menu == "2" and kontrola1 != "":
            savesS=open("existing saves.txt","r")
            saves=savesS.read().split(";")
            savesS.close()
            for i in range(len(saves)):
                print(str(i+1)+". "+saves[i])
            menu1=input()
            if menu1=="help":
                help()
            elif menu1.isdigit():
                soubor=saves[int(menu1)-1]
            elif menu1=="back":
                breakit=True
                break
            save=open("saves/"+soubor+".txt","r")
            radekPlace,radekTime,radekDum,radekStanek,radekFlowers,radekJidlo,radekZakaznici,radekCeny,radekPenezenka,radekSaturation=save.read().split("\n")
            save.close()
            place=radekPlace
            Day,Time,Atime,Time1,Time2,Time3=radekTime.split(";")
            Day,Time,Atime,Time1,Time2,Time3=int(Day),int(Time),int(Atime),int(Time1),int(Time2),int(Time3)
            dum={}
            if radekDum != "":
                ab=radekDum.split(";")
                for i in range(len(ab)):
                    abprvek=ab.pop(0)
                    a,b=abprvek.split(" ")
                    dum[a]=int(b)
            stanek={}
            ab=radekStanek.split(";")
            for i in range(len(ab)):
                abprvek=ab.pop(0)
                a,b=abprvek.split(" ")
                stanek[a]=int(b)
            ab2x=radekFlowers.split("<>")
            ab=ab2x.pop(0)
            plants=ab.split(";")
            ab=ab2x.pop(0)
            shanks=ab.split(";")
            JidloKg={}
            JidloKs={}
            abab2x=radekJidlo.split("<>")
            abab=abab2x.pop(0)
            abprvek=abab.split(";")
            for i in range(len(abprvek)):
                ab=abprvek.pop(0)
                a,b=ab.split(" ")
                JidloKg[a]=float(b)
            abab=abab2x.pop(0)
            abprvek=abab.split(";")
            for i in range(len(abprvek)):
                ab=abprvek.pop(0)
                a,b=ab.split(" ")
                JidloKs[a]=int(b)
            ab2x=radekZakaznici.split("<>")
            Zakaznici=[]
            ab=ab2x.pop(0)
            if ab =="":
                Zakaznici=[]
            else:
                Zakaznici=ab.split(";")
            ZakazniciStanek={}
            ab=ab2x.pop(0)
            if ab =="":
                ZakazniciStanek={}
            else:
                abprvek=ab.split(";")
                for i in abprvek:
                    a,b=i.split(" ")
                    ZakazniciStanek[a]=b
            Ceny={}
            if radekCeny=="":
                Ceny={}
            else:
                abab=radekCeny.split(";")
                for i in abab:
                    ab=abab.pop(0)
                    a,b=ab.split(" ")
                    Ceny[a]=int(b)
            penezenka=float(radekPenezenka)
            saturation=int(radekSaturation)
            if plants==[""]:
                plants=[]
            if shanks==[""]:
                shanks=[]
            
            break
        elif menu == "3" and kontrola1 != "":
            savesS=open("existing saves.txt","r")
            saves=savesS.read().split(";")
            savesS.close()
            for i in range(len(saves)):
                print(str(i+1)+". "+saves[i])
            menu1=input()
            if menu1=="help":
                help()
            elif menu1.isdigit():
                os.remove("saves/"+str(saves[int(menu1)-1])+".txt")
                del(saves[int(menu1)-1])
                savesS=open("existing saves.txt","w")
                savesS.write(";".join(saves))
                savesS.close()
            elif menu1=="back":
                breakit=True
                break
        elif menu == "back":
            breakit=True
            break

    while True:
        if breakit==True:
            break
        back,breakSaves=[False]*2
        menu=input("1.#Do\n2. Go to\n#3.Eat#\n4. Inventory\n#5.Stats#\n6. Menu\n")
        if menu=="help":
            help()
            print("Note: There is not place to go back.")
        elif menu == "1":
            if place=="Farm":
                if plants != [""]:
                  PrintPlant={}
                  FarmStrawberry=0
                  for i in range(len(plants)):
                    Flowers=plants[i]
                    flower,water,fruit=Flowers.split(".")
                    FarmStrawberry+=int(fruit)
                    if int(water)>=601:
                        stat=""
                    elif 600>=int(water)>=151:
                        stat="(sear)"
                    elif 150>=int(water)>1:
                        stat="(extremely sear)"
                    elif int(water)==0:
                        stat="(dead)"
                    plant=flower+stat
                    if plant in PrintPlant:
                        PrintPlant[str(plant)]+=1
                    elif plant not in PrintPlant:
                        PrintPlant[str(plant)]=1
                  for i in PrintPlant:
                    print(str(i)+" "+str(PrintPlant[i])+"x")
                  print(" Strawberry:"+str(FarmStrawberry))
                if shanks != [""]:
                  PrintPlant={}
                  for i in range(len(shanks)):
                    Flowers=shanks[i]
                    flower,stage,DaysToNextStage,water=Flowers.split(".")
                    if int(water)>=601:
                        stat=""
                    elif 600>=int(water)>=151:
                        stat="(sear)"
                    elif 150>=int(water)>1:
                        stat="(extremely sear)"
                    elif int(water)==0:
                        stat="(dead)"
                    if int(stage)==0:
                        PrintStage="-seed"
                    elif int(stage)==1:
                        PrintStage="-sproud"
                    elif int(stage)==2:
                        PrintStage="-first leaf"
                    elif int(stage)==3:
                        PrintStage="-early plant"
                    plant=flower+PrintStage+stat
                    if plant in PrintPlant:
                        PrintPlant[str(plant)]+=1
                    else:
                        PrintPlant[str(plant)]=1
                  for i in PrintPlant:
                    print(str(i)+" "+str(PrintPlant[i])+"x\n")
                while True:
                    menu1=input("1. Harvest fruits\n2. Water plants\n#3.Plant plant#\n#4.Plough field#\n")
                    if menu1=="help":
                        help()
                    elif menu1=="1":
                        Fruits=0
                        Products={}
                        for i in range(len(plants)):
                            Flowers=plants[i]
                            flower,water,fruit=Flowers.split(".")
                            product,nothing=flower.split("P")
                            if product in Products:
                                Products[product]+=int(fruit)
                            else:
                                Products[product]=int(fruit)
                        if Products[product] > 0:
                            Atime+=Products[product]*3
                            plants2=plants
                            plants=[]
                            for i in range(len(plants2)):
                                plant,water,fruit=plants2.pop(0).split(".")
                                plants.append(plant+"."+water+".0")
                            for i in Products:
                                while True:
                                    menu2=input("Where you want to store those fruits?\n"+i+" "+str(Products[i])+"\n1. Market\n2. Food\n")
                                    if menu2=="help":
                                        help()
                                        print("Note: You can not go back in this menu.\n")
                                    elif menu2=="1":
                                        if i in stanek:
                                            stanek[i]+=Products[i]
                                        else:
                                            stanek[i]=Products[i]
                                        Atime+=15
                                        place="Market"
                                        break
                                    elif menu2=="2":
                                        if i in JidloKs:
                                            jidlo[i]+=Products[i]
                                        else:
                                            jidlo[i]=Products[i]
                                        Atime+=3
                                        place="Home"
                                        break
                        else:
                            print("There are not fruits to harvest.\n")
                    elif menu1=="2":
                        Hwater=0
                        flowers=0
                        for i in range(len(plants)):
                            Flower=plants[i]
                            flower,water,fruit=Flower.split(".")
                            Hwater+=int(water)
                            flowers+=1
                        for i in range(len(shanks)):
                            Flower=shanks[i]
                            flower,stage,DaysToNextStage,water=Flower.split(".")
                            Hwater+=int(water)
                            flowers+=1
                        NeedetWater=flowers*750-Hwater
                        TimeToGetWater=int(NeedetWater/2000+1)
                        TimeToWaterPlants=85*int(NeedetWater/90+1)
                        Atime+=TimeToGetWater+TimeToWaterPlants
                        plants2=plants
                        plants=[]
                        for i in range(len(plants2)):
                            flower,water,fruit=plants2.pop(0).split(".")
                            plants.append(flower+".750."+fruit)
                        shanks2=shanks
                        shanks=[]
                        for i in range(len(shanks2)):
                            flower,stage,DaysToNextStage,water=shanks2.pop(0).split(".")
                            shanks.append(flower+"."+stage+"."+DaysToNextStage+".750")
                    elif menu1=="back":
                        break
            elif place == "Market":
                while True:
                    stale=True
                    while stale:
                        stale=False
                        for i in stanek:
                            if i not in Ceny:
                                while True:
                                    menu1=input("Set price of "+i+":")
                                    if menu1.replace(".","",1).isdigit():
                                        Ceny[i]=float(menu1)
                                        break
                                    else:
                                        print("Price is expressible only by numbers. Eventually with point('.')")
                                stale=True
                    x1=0
                    if ZakazniciStanek!={}:
                        x1=1
                        if len(ZakazniciStanek)==1:
                            print("There is one customer\n")
                        else:
                            print("There are "+str(len(ZakazniciStanek))+" customers.\n")
                        print(str(x1)+". Take a customer")
                    else:
                        print("There are no customers wating for you.")
                    menu1=input(str(x1+1)+". Change prices\n")
                    if menu1=="help":
                        help()
                    elif menu1==str(x1):
                        x2=1
                        while True:
                            if len(ZakazniciStanek) > 0:
                                if x2==1:
                                    print("1. Greet")
                                menu2=input(str(x2+1)+". Wait on customer\n")
                                if menu2=="help":
                                    help()
                                    print("'name' want:\n'product' 'quantity'\n'you have' 'your price'(You can change them in 'Change price')")
                                elif menu2==str(x2) and x2==1:
                                    print("You: Hi.\nCustomer: Hi.")
                                    Atime+=3
#                                    spokojenost+
                                    x2=0
                                elif menu2==str(x2+1):
                                    for i in ZakazniciStanek:
                                        jmeno,pohlavi,Idny,Ihodiny,dny,hodiny,spokojenost,obsluhy,trpelivost,nakup=i.split(".")
                                        plod,Imnozstvi,mnozstvi,cena=nakup.split(",")
                                        cena,mnozstvi,obsluhy=int(cena),int(mnozstvi),int(obsluhy)
                                        while True:
                                            print(jmeno+" want:\n"+plod+" "+str(mnozstvi)+"ks")
                                            Atime+=5
                                            if plod in stanek:
                                                if Ceny[plod] <= cena:
                                                    mas,x3=1,1
                                                    print("You have:"+str(stanek[plod])+"ks for "+str(Ceny[plod]))
                                                    if cena <= stanek[plod]:
                                                        print("1. Sell")
                                                    else:
                                                        print("1. Sell what you have")
                                                else:
                                                    mas,x3=2,1
                                                    print(jmeno+": That is too expensive.\n\n1. Haggle about the price")
#                                                    spokojenost-
                                                    Atime+=5
                                            else:
                                                mas,x3=0,0
                                                print("You do not have this.")
#                                                spokojenost-
                                            leave=False
                                            menu3=input(str(x3+1)+". Throw out this customer\n")
                                            if menu3=="help":
                                                help()
                                            elif menu3==str(x3) and mas ==1:
                                                if stanek[plod] >= mnozstvi:
                                                    stanek[plod]-=mnozstvi
                                                    penezenka+=mnozstvi*Ceny[plod]
                                                    print(jmeno+": Thank you.",end=" ")
                                                    Atime+=2+mnozstvi*2
                                                    obsluhy+=1
#                                                    spokojenost+
                                                    leave=True
                                                else:
                                                    mnozstvi-=stanek[plod]
                                                    penezenka+=stanek[plod]*Ceny[plod]
                                                    print(jmeno+": Thank you.")
                                                    Atime+=2+stanek[plod]*2
#                                                    spokojenost+-
                                            elif menu3==str(x3) and mas ==2:
                                                while True:
                                                    if Ceny[plod] > cena:
                                                        menu4=input("Your offer is:\n"+plod+" for "+str(Ceny[plod])+"\n\n1. Reduce price\n2. Throw out this customer\n")
                                                        if menu4==help:
                                                            help()
                                                        elif menu4=="1":
                                                            while True:
                                                                menu5=input("Set new price for "+plod+": ")
                                                                if menu5=="help":
                                                                    help()
                                                                elif menu5.replace(".","",1).isdigit():
                                                                    if float(menu5) < Ceny[plod]:
                                                                        Ceny[plod]=float(menu5)
                                                                        if Ceny[plod] <= cena:
                                                                            print(jmeno+": That is better.\n")
#                                                                            spokojenost+
                                                                            Atime+=3
                                                                            break
                                                                        else:
                                                                            print(jmeno+": That is still too expensive.")
#                                                                            spokojenost-
                                                                            Atime+=4
                                                                    else:
                                                                        print("You choose 'reducte price' so you have to set lower price.")
                                                                elif menu5=="back":
                                                                    break
                                                                else:
                                                                    print("Price is expressible only by numbers. Eventually with point('.')")
                                                        elif menu4=="2":
                                                            leave=True
                                                        elif menu4=="back":
                                                            break
                                                        if leave:
                                                            break
                                                    else:
                                                        break
                                            elif menu3==str(x3+1):
                                                leave=True
#                                                spokojenost-
                                                print(jmeno,end=" ")
                                            elif menu3=="back":
                                                break
                                            if leave:
                                                break
                                        if leave:
                                            a,b=Idny.split("-")
                                            a,b=int(a),int(b)
                                            dny=ranndom.randint(a,b)
                                            a,b=Ihodiny.split("-")
                                            a,b=int(a)*60,int(b)*60
                                            hodiny=ranndom.randint(a,b)
                                            a,b=Imnozstvi.split("-")
                                            a,b=int(a),int(b)
                                            mnozstvi=random.randint(a,b)
                                            Zakaznici.append(jmeno+"."+pohlavi+"."+Idny+"."+Ihodiny+"."+str(dny)+"."+str(hodiny)+"."+spokojenost+"."+str(obsluhy)+"."+trpelivost+"."+plod+","+Imnozstvi+","+str(mnozstvi)+","+str(cena))
                                            del ZakazniciStanek[i]
                                            print("Bye.")
                                            Atime+=7
                                            break
                                elif menu2=="back":
                                    break
                            else:
                                break
                    elif menu1==str(x1+1):
                        while True:
                            print("What price do you want to change?")
                            for q in range(len(Ceny)):
                                for i in Ceny:
                                    print(str(q+1)+". "+i+" for "+str(Ceny[i]))
                            menu2=input() 
                            if menu2=="help":
                                help()
                            elif menu2.isdigit():
                                while True:
                                    menu3=input("Set the price of "+list(Ceny)[int(menu2)-1]+": ")
                                    if menu3.replace(".","",1).isdigit():
                                        Ceny[list(Ceny)[int(menu2)-1]]=float(menu3)
                                        break
                                    else:
                                        print("Price is expressible only by numbers. Eventually with point('.')")
                            elif menu2=="back":
                                break
                    elif menu1=="back":
                        break
        elif menu == "2":
            for i in range(3): # lze smazat?
                places=["Home","Market","Farm","Shop"]
                places.remove(place)
            for i in range(3):
                print(str(i+1)+". "+places[i])
            menu1=input()
            BackPlace=True
            if menu1=="help":
                help()
            elif menu1=="1":
                Oplace=place
                place=places[0]
            elif menu1=="2":
                Oplace=place
                place=places[1]
            elif menu1=="3":
                Oplace=place
                place=places[2]
            elif menu1=="back":
                BackPlace=False
            if BackPlace==True:
                if (place=="Farm" and Oplace=="Home") or (place=="Home" and Oplace=="Farm"):
                    Atime+=3
                elif (place=="Farm" and Oplace=="Market") or (place=="Market" and Oplace=="Farm"):
                    Atime+=15
                elif (place=="Farm" and Oplace=="Shop") or (place=="Shop" and Oplace=="Farm"):
                    Atime+=124
                elif (place=="Home" and Oplace=="Market") or (place=="Market" and Oplace=="Home"):
                    Atime+=9
                elif (place=="Home" and Oplace=="Shop") or (place=="Shop" and Oplace=="Home"):
                    Atime+=118
                elif (place=="Market" and Oplace=="Shop") or (place=="Shop" and Oplace=="Market"):
                    Atime+=124
#        elif menu == "3":
#            menu1=input
        elif menu == "4":
            while True:
                menu1=input("1. Home\n2. Market\n3. Food\n4. Money\n")
                if menu1=="help":
                    help()
                elif menu1=="1":
                    print("Home:")
                    home=list(set(dum))
                    for i in range(len(dum)):
                        print(home[i]+" "+str(dum[home[i]])+"ks")
                elif menu1=="2":
                    print("Market:")
                    market=list(set(stanek))
                    for i in range(len(stanek)):
                        print(market[i]+" "+str(stanek[market[i]])+"ks")
                elif menu1=="3":
                    print("Food:")
                    food=list(set(JidloKg))
                    for i in range(len(food)):
                        print(food[i]+" "+str(JidloKg[food[i]])+"kg")
                    print()
                    food=list(set(JidloKs))
                    for i in range(len(food)):
                        print(food[i]+" "+str(JidloKs[food[i]])+"ks")
                elif menu1=="4":
                    print("Money:\n"+str(penezenka)+" CZE")
                elif menu1=="back":
                    break
                else: # nejsem si jist?
                    print()
#        elif menu == "5":
#            menu1=input("")
        elif menu == "6":
            menu1=input("1. Save game\n2. Quit\n")
            if menu1=="help":
                help()
                print("Note: In this menu you can go back by writing anything else that 'help' or '1' or '2'.")
            elif menu1=="1":
                savesS=open("existing saves.txt","r")
                saves=savesS.read().split(";")
                savesS.close()
                while True:
                    if saves != [""]:
                        for i in range(len(saves)):
                            print(str(i+1)+". "+saves[i])
                        print(str(i+2)+". "+"New slot")
                    else:
                        print("1.New slot")
                    menu2=input()
                    if menu2=="help":
                        help()
                        print("Note: You can not name your save 'help' or 'back'.\n      P.S: Do not try it.")
                    elif menu2.isdigit():
                        if saves == [""] and menu2 == "1":
                            soubor=input("Name your slot:\n")
                        elif int(menu2)<(i+2):
                            soubor=saves[int(menu2)-1]
                        elif int(menu2)==(i+2):
                            soubor=input("Name your slot:\n")
                            LOS=open("existing saves.txt","r")
                            los=LOS.read()
                            LOS.close()
                            KontrolaSaves=los.split(";")
                            while soubor in KontrolaSaves:
                                if soubor == "help":
                                    help()
                                    print("Note: You can not go back in this menu.")
                                soubor=input("Choose another name for your slot.\nThese has been taken:\n"+", ".join(KontrolaSaves)+"\nName your slot:\n")
                        print("saving...\n")
                        breakSaves=True
                        save=open("saves/"+soubor+".txt","w")
                        LOS=open("existing saves.txt","r")
                        los=LOS.read()
                        KontrolaSaves=los.split(";")
                        LOS.close()
                        LOS=open("existing saves.txt","a")
                        if los == "":
                            LOS.write(soubor)
                        elif soubor in KontrolaSaves: # nejsem si jist?
                            print()
                        else:
                            LOS.write(";"+soubor)
                        LOS.close()
                        SaveHome=[]
                        home=list(set(dum))
                        for i in range(len(dum)):
                            SaveHome.append(home[i]+" "+str(dum[home[i]]))
                        SaveMarket=[]
                        market=list(set(stanek))
                        for i in range(len(stanek)):
                            SaveMarket.append(market[i]+" "+str(stanek[market[i]]))
                        SaveFoodKg=[]
                        food=list(set(JidloKg))
                        for i in range(len(food)):
                            SaveFoodKg.append(food[i]+" "+str(JidloKg[food[i]]))
                        SaveFoodKs=[]
                        food=list(set(JidloKs))
                        for i in range(len(food)):
                            SaveFoodKs.append(food[i]+" "+str(JidloKs[food[i]]))
                        SaveZakazniciStanek=[]
                        customers=list(ZakazniciStanek)
                        for i in customers:
                            SaveZakazniciStanek.append(i+" "+str(ZakazniciStanek[i]))
                        SaveCeny=[]
                        prices=list(Ceny)
                        for i in prices:
                            SaveCeny.append(i+" "+str(Ceny[i]))
                        save.write(place+"\n"+str(Day)+";"+str(Time)+";"+str(Atime)+";"+str(Time1)+";"+str(Time2)+";"+str(Time3)+"\n"+";".join(SaveHome)+"\n"+";".join(SaveMarket)+"\n"+";".join(plants)+"<>"+";".join(shanks)+"\n"+";".join(SaveFoodKg)+"<>"+";".join(SaveFoodKs)+"\n"+";".join(Zakaznici)+"<>"+";".join(SaveZakazniciStanek)+"\n"+";".join(SaveCeny)+"\n"+str(penezenka)+"\n"+str(saturation))
                        save.close()
                        break
                    elif menu2=="back":
                        break
            elif menu1=="2":
                exit=str(random.randint(2,99))
                menu2=input("All content that wasn't saved will be lost.\n1. Continue\n"+exit+". Exit game\n")
                if menu2=="help":
                    help()
                    print("Note: In this menu you can go back by writing anything else that 'help' or the exit number (now it was '"+str(exit)+"').")
                elif menu2==exit:
                    breakit=True
                    break
                    
        while Atime > 0:
            if Atime >= 60:
                Time1,Time2,Time3=Time1+60,Time2+60,Time3+60
                Atime-=60
            else:
                Time1,Time2,Time3=Time1+Atime,Time2+Atime,Time3+Atime
                Atime=0
            while Time1 >= 864:
                saturation-=1
                Time1-=864
            while Time2 >= 60:
                #for i in Zakaznici: # NEDOKONčENO
                #    jmeno,pohlavi,Idny,Ihodiny,dny,hodiny,spokojenost,obsluhy,trpelivost,nakup=i.split(".") # NEDOKONčENO
                Time+=1
                while Time >= 1440:
                    Time-=1440
                    Day+=1
                    shanks2=shanks
                    shanks=[]
                    for i in range(len(shanks)):
                        Flower=shanks2[i]
                        flower,stage,DaysToNextStage,water=Flower.split(".")
                        stage,DaysToNextStage=int(stage),int(DaysToNextStage)
                        if DaysToNextStage == 0:
                            if stage == 3:
                                plants.append(flower+"."+water+".0")
                            else:
                                stage+=1
                            DaysToNextStage=random.randint(2,4)
                        else:
                            DaysToNextStage-=1
                        if stage != 3:
                            shanks.append(flower+"."+str(stage)+"."+str(DaysToNextStage)+"."+water)
                Time2-=60
            while Time3 >= 576:
                plants2,shanks2=plants,shanks
                plants,shanks=[[]]*2
                for i in range(len(shanks)):
                    Flower=shanks2[i]
                    flower,stage,DaysToNextStage,water=Flower.split(".")
                    water=str(int(water)-1)
                    shanks.append(flower+"."+stage+"."+DaysToNextStage+"."+water)
                for i in range(len(plants)):
                    Flower=plants2[i]
                    flower,water,fruit=Flower.split(".")
                    water=str(int(water)-1)
                    plants.append(flower+"."+water+"."+fruit)
                Time3-=576

  elif menu0=="2":
    Otitulky=open("subtitles.txt","r")
    for i in range(50):
        print()
    titulky=Otitulky.read().split("\n")
    time.sleep(1)
    for row in titulky:
        for char in row:
            print(char, end="", flush=True)
            time.sleep(0.07)
        time.sleep(0.2)
        print()
        time.sleep(0.2)
    Otitulky.close()
  elif menu0=="3":
    print("Thanks for playing!")
    time.sleep(2.4)
    break
  elif menu0=="help":
      help()
