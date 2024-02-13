print('Hello')
asosiy = 10
qoshish = 10
hech = asosiy * qoshish
print(hech)
def yulduz_shakli(hajm):
     for i in range(hajm):
        print("*" * (i + 1))

if __name__ == "__main__":
    hajm = int(input("Yulduz shaklini hajmini kiriting: "))
    yulduz_shakli(hajm)
