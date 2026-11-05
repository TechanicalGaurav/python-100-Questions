#Mask sensitive data: show only the last 4 digits of a card number and hide most of an
email username.

def mask_card(n):
    n=n.replace(" "," ")
    return "*" * (len(n)-4) + n[-4:]
def mask_email(e):
    user,domain = e.split("@")
    return user[0] + "*" * (len(user)-1) + "@" + domain
print(mask_card("1234 5678 9012 3456"))
print(mask_email("lohanigaurav538@gmail.com"))