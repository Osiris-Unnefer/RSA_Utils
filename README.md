Values :

Public Key Exponent (65537 Generally) = E

PUBLIC key Value = N

PRIVATE key Value = D

FACTOR 1 (prime1) = P

FACTOR 2 (prime2) = Q

(Fonction phi de Euler) INTERMEDIATE value PHI = φ

Ciphertext = C



Calculs :

p and q with N (when N is not that big for factoring attack) = https://factordb.com/

N = p*q
φ(n) = (p - 1) × (q - 1)
d × e ≡ 1 mod φ(n)
M = C^d modulo n
C = M^e modulo n
