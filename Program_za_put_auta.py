v1 = 1
v2 = 3

l102 = 2*v1*60
v1 += 2
l124 = 2*v1*60
v1 *= 3
l146 = 2*v1 * 60
v1 -= 2
l168 = 2*v1 * 60

l1 = l102 + l124 + l146 + l168

print(l1)




v1 = float(input("Unesi pocetnu brzinu autica 1: "))
v2 = float(input("Unesi pocetnu brzinu autica 2: "))
l1 = 2*v1*60 + 2*(v1+2)*60 + 2*(3*(v1+2)*60) + 2*(3*(v1+2)-2)*60
l1 = round(l1, 3)
l2 = 2*60*v2 + 2*60*(v2+1) + 2*60*(2*(v2+1)) + 2*60*((v2+1)*2-1)2
l2 = round(l2, 3)
print("Auto 1 ce preci put od " + str(l1) + " metara.")
print("Auto 2 ce preci put od " + str(l2) + " metara.")

if l1 < l2:
	print ("Auto 2 je presao veci put od auta 1")
elif l1==l2:
	print("autici su prosli isti put")
else:
	print("Auto 1 jepresao veci put od auta 2")
print("Kraj programa.")
