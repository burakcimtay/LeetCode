def rom(num):

    str1 = ""
    rom_list = []
    if num==0:
        return str1
    while (num>=4):
        if(num>=1000):
            for i in range(num//1000):
                rom_list.append("M")
            num = num%1000
        elif(1000>num>=900):
            rom_list.append("CM")
            num = num-900
        elif(num>=500):
            for i in range(num//500):
                rom_list.append("D")
            num = num%500
        elif(500>num>=400):
            rom_list.append("CD")
            num = num-400
        elif(num>=100):
            for i in range(num//100):
                rom_list.append("C")
            num = num%100
        elif(100>num>=90):
            rom_list.append("XC")
            num = num-90
        elif(num>=50):
            for i in range(num//50):
                rom_list.append("L")
            num = num%50
        elif(50>num>=40):
            rom_list.append("XL")
            num = num-40
        elif(num>=10):
            for i in range(num//10):
                rom_list.append("X")
            num = num%10
        elif(num==9):
            rom_list.append("IX")
            break
        elif(num==4):
            rom_list.append("IV")
            break
        elif(num>=5):
            for i in range(num//5):
                rom_list.append("V")
            num = num%5

    if(num!=0 and num!=9 and num!=4):
        for i in range(num):
            rom_list.append("I")
            num = num-1

    return str1.join(rom_list)
while True:
    s = int(input())
    print(rom(s))

            