A=int(input('輸入一個五位數:'))
M1=A//10000
M2=(A-M1*10000)//1000
M3=(A-M1*10000-M2*1000)//100
M4=(A-M1*10000-M2*1000-M3*100)//10
M5=A-M1*10000-M2*1000-M3*100-M4*10
print(M1)
print(M2)
print(M3)
print(M4)
print(M5)