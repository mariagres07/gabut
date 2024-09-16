data = str(input("Masukkan sebuah kata : "))

kata = set()

for y in data:
    kata.add(y)

kata = len(kata)

print("kata", data, "terdiri dari",kata, "karakter unik")