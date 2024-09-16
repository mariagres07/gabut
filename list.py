kata = []
abjad = "j"
while abjad != "":
    abjad = str(input("Masukkan kata (Berhenti jika ENTER saja sbg input) = "))
    
    if abjad != "":
        kata.append(abjad)      

New = list(set(kata))
for y in New:
    print(y)