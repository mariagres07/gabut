angka = []
data = 2
while data != 0:
    data = int(input("Masukkan data (Berhenti jika 0) = "))
    
    if data != 0:
        angka.append(data)      

angka.sort()
for y in angka:
    print(y)
   