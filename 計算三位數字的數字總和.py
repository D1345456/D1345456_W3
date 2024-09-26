A=int(input('請輸入一個三位數:'))
F=A//100
S=(A-F*100)//10
L=A-F*100-S*10
ans=F+S+L
print('每位數字的總和：',ans)