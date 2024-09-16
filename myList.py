mylist = ["apa", "bagaimana"]

kata = str(input("masukkan kata yang ingin dicari = "))
if kata in mylist:
    print("ada", kata)
else:
    print("tidak ada", kata)
    mylist.append(kata)
    print(mylist)

mylist.remove("apa")
print(mylist)

del mylist[0]

#tuple
tuple = ("apple", "banana", "cherry")
print(tuple)

#set
myset = {"apple", "banana", "cherry"}
print(myset)

#dictionary
thisdictionary = {
    "nim" : "235314094",
    "nama" : "maria gresia",
    "mata kuliah" : "alpro",
}
print(thisdictionary)