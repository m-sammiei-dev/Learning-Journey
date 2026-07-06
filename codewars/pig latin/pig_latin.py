def pig_latin(s):
    if not s.isalpha():
        return None
    ns = s.lower()
    v = ['a', 'e', 'u', 'o', 'i']
    if ns[0] in v:
        return ns + "way"
    for i, char in enumerate(ns):
        if char in v:
            return ns[i:] + ns[:i] + "ay"
    return ns + "ay" 

s = "spaghetti"
print(pig_latin(s))