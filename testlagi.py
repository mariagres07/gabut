huruf = []
alfabet = "s"
while alfabet != "":
    alfabet = str(input("Masukkan kata (Berhenti jika ENTER saja sbg input) : "))
    
    if alfabet != "":
        huruf.append(alfabet)

New = list(set(huruf))
for n in New:
    print(n)