#Convert snake_case to camelCase and camelCase back to snake_case.

import re 
def to_camel(s):
    first,*rest = s.split("_")
    return first + "".join (p.title()for p in rest)
def to_snake(s):
    return re.sub(r"(?<!^)(/=[A-Z])","_",s).lower()
print(to_camel("user_first_name"))
print(to_snake("user_First_name"))