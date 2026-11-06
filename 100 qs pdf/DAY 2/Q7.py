'''Write a function that checks whether a password is strong (min 8 chars, upper, lower,
digit, special character).'''

import re 
def is_strong(p):
    rules = [r"[A-Z]",r"[a-z]",r"\d",r"[^\w\s]"]
    return len(p) >=8 and all (re.search(r,p) for r in rules)
for p in ["abc","Passw0rd!","password123"]:
    print(p,is_strong(p))  