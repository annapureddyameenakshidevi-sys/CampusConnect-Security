p = 29
g = 2

a = 5
b = 12

A = pow(g, a, p)
B = pow(g, b, p)

alice_key = pow(B, a, p)
bob_key = pow(A, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)
print("Alice Shared Key:", alice_key)
print("Bob Shared Key:", bob_key)

if alice_key == bob_key:
    print("Shared keys match")
else:
    print("Shared keys do not match")
