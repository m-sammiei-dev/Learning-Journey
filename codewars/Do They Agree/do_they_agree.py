def do_they_agree(alice, bob):
    new_alice = [i for i in alice if i in bob]
    new_bob = [i for i in bob if i in alice]
    return new_alice == new_bob
a = [8, 5, 4, 3]
b = [9, 8, 3, 1, 5]
print(do_they_agree(a, b))