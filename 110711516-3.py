mon=int(input("請輸入月份:"))
if (mon>=13):
    print("不再月份內") 
elif(mon>=10):
    print("冬天")
elif (mon>=7):
    print("秋天")
elif (mon>=4):
    print("夏天")
else :
    print("春天")

