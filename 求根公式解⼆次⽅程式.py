import math
A=int(input('輸入係數a:'))
B=int(input('輸入係數b:'))
C=int(input('輸入係數c:'))
D=~B+1
F=(D+(B**2-4*A*C)**0.5)/(2*A)
S=(D-(B**2-4*A*C)**0.5)/(2*A)
print('方程式的根為:X1=',F,'X2=',S)