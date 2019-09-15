print('Operator Aritmetika')
print(21+22) # 43
print(34-14) # 20
print(2*3) # 6
print(21/2) # 10.5
print(21.00/2.00) # 10.5
print(21%2) # 1
print(21.00//2.00) # 10.0
print(4**3) # 4 pangkat 3
print('Operator Relasional / Perbandingan')
print(3>22) # False
print(3<22) # True
print(4<=4) # True
print(4>=4) # True
print(5==5.0) # True
print(1!=1.0) # False
print('Operator Bitwise')
x = 25 # nilai awal
# 25 = 0001 1001
print(x >> 2) # 0000 0110 = 6
print(x << 2) # 0001 1000 = 24
a = 3 # 0000 0011
b = 6 # 0000 0110
# AND
print (a & b) # jika bit di dua operand sama, diaktifkan di hasil
              # 0000 0010 = 2
# OR
print (a | b) # jika bit ada di salah satu atau kedua operand, 
              # diaktifkan di hasil:
              # 0000 0111 = 7
# XOR
print (a ^ b) # jika bit ada di salah satu operand tapi tdk di keduanya,
              # diaktifkan di hasil:
              # 0000 0101 = 5
# Negasi / Not
print (-a) 
print('Operator Penugasan / Assignment')
x = 50
print(x) # 50
x+=5
print(x) # x = x lama + 5 = 50 + 5 =  55
x-=2
print(x) # x = x lama - 2 = 55 - 2 = 53
x*=2
print(x) # x = x lama * 2 = 53 * 2 = 106
x/=2
print(x) # x = x lama / 2 = 106 / 2 = 53
x%=3
print(x) # x = x lama modulo 3 = 53 modulo 3 = 2.0 
         # (karena pembagian terakhir berhenti di 51)
x = 55
x//=2
print(x) # x = x lama / 2, hasil dibulatkan ke bawah = 27.5
         # dibulatkan 27
x**=2
print(x) # x = x lama pangkat 2 = 27 pangkat 2 = 729
x = 7
x&=2
print(x) # x = x lama AND 2 = 7 and 2
         # 7 = 0000 0111
         # 2 = 0000 0010
         # bit hidup jika di kedua operand hidup
         # 0000 0010 = 2
x = 7
x|=2
print(x) # x = x lama OR 2 = 7 or 2
         # 7 = 0000 0111
         # 2 = 0000 0010
         # bit hidup jika di salah satu operand hidup
         # 0000 0111 = 7
x = 7
x^=2
print(x) # x = x lama XOR 2 = 7 xor 2
         # 7 = 0000 0111
         # 2 = 0000 0010
         # bit hidup jika di salah satu operand hidup, 
         # tapi tidak di keduanya
         # 0000 0101 = 5
x = 7
x>>=2
print(x) # x = x lama >> 2 = 7 >> 2
         # 7 = 0000 0111
         # 0000 0001 = 1
x = 7
x<<=2
print(x) # x = x lama << 2 = 7 << 2
         # 7 = 0000 0111
         # 0001 1100 = 28
print('Operator Logika')
x = 3 > 1 and 2 < 19 # jika kedua sisi true -> true
print(x)
x = 3 > 4 or 2 < 10 # jika salah satu sisi benar -> true
print(x)
x = not(3 > 4) # not -> negasi
print(x)
print('Operator Keanggotaan / Membership')
x = (2,5,9,8,1,9,7,2)
print(9 in x)
print(10 in x)
print(10 not in x)
print('Operator Identitas / Identity')
x = 7
print(x is 7)
print(x is not 7)
