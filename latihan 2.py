print("\nkonversi suhu\n")


celcius = float(input("Masukkan suhu dalam Celcius = "))
print("Suhu (Celcius)        = ",celcius)
cr = (4/5)*celcius
cf = ((9/5)*celcius) + 32
ck = 273 + celcius
print("celcius ke reamur     = ", cr)
print("celcius ke fahrenheit = ",cf)
print("celcius ke kelvin     = ",ck)

print("")
reamur = float(input("Masukkan suhu dalam Reamur = "))
print("Suhu (Reamur)        = ",reamur)
rc = (5/4)*reamur
rf = ((9/4)*reamur)+32
rk = rc+273
print("reamur ke celcius    = ", rc)
print("reamur ke fahrenheit = ", rf)
print("reamur ke kelvin     = ", rk)

print("")
fahrenheit = float(input("Masukkan suhu dalam fahrenheit = "))
print("Suhu (fahrenheit)     = ",fahrenheit)
fc = (5/9)*(fahrenheit-32)
fr = (9/4)*(fahrenheit-32)
fk = fc+273
print("fahrenheit ke celcius = ", fc)
print("fahrenheit ke reamur  = ", fr)
print("fahrenheit ke kelvin  = ", fk)

print("")
kelvin= float(input("Masukkan suhu dalam kelvin = "))
print("Suhu (kelvin)        = ",kelvin)
kc = kelvin-273
kr = (4/5)*kc
kf = ((9/5)*kc)+32
print("kelvin ke celcius    = ", kc)
print("kelvin ke reamur     = ", kr)
print("kelvin ke fahrenheit = ", kf)

