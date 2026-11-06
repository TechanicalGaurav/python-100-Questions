'''Create an SEO-friendly URL slug from a blog title (handle accents, symbols and extra
spaces).'''

import re,unicodedata
def slugify(title):
    t = unicodedata.normalize("NFKD",title).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")
print(slugify("Cafe\u0301:Python & AI in 2025!"))
print(slugify("Hello, World!!"))
