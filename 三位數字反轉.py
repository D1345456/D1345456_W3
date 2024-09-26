A=int(input('輸入三位數字:'))
F=A//100
S=(A-F*100)//10
L=A-F*100-S*10
ans=L*100+S*10+F
print('結果：',ans)