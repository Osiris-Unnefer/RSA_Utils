import time

e = 65537;p = 0;q = 0;m = 0;d = 0;phi = 0;d =0;c=0;stop=0
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n   Created by Osiris_Unnefer \n\nhttps://github.com/Osiris-Unnefer\n")

e = int(input("e -> " ))
p = int(input("p -> " ))
q = int(input(" q -> " ))


#calculs
m =  p * q 
def  egcd(a, b): #fonction egcd
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b// a) * y, y
            
def modinv(a, m): # fonction modinv
    g, x, y = egcd(a, m)
    if g !=1:
             Exception ('D est incalculable')
    else:
        return x % m
phi = (p - 1) * (q - 1)
d = modinv(e, phi)


#affichage
print("\nm = ",m)
print("\np = ",p)
print("\nq = ",q)
print("\nphi = ",phi)
print("\ne = ",e )
print("\nd = ",d)
time.sleep(1)
