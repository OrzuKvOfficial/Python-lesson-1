import time

while True:
    # Joriy vaqt bilan sanani olish
    joriy_vaqt = time.localtime()

    sana = time.strftime("%Y-%m-%d", joriy_vaqt)

    soat = time.strftime("%H:%M:%S", joriy_vaqt)

    daqiqalar = time.strftime("%M", joriy_vaqt)

    print("Sana:", sana, "Soat", soat, "Daqiqalar",daqiqalar)

    time.sleep(60)
    
def yulduz_shakli(hajm):
     for i in range(hajm):
        print("*" * (i + 1))

if __name__ == "__main__":
    hajm = int(input("Yulduz shaklini hajmini kiriting: "))
    yulduz_shakli(hajm)

