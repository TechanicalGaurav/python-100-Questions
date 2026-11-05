#validate a list of email address using a regular expression

import re
pattern = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")
emails = ["a@b.com","bad@","john.doe+@gmail.co.in","no at.com"]
emails.append("sanjaylohani697@gmail.com")
for e in emails:
    print(e,bool(pattern.match(e)))
