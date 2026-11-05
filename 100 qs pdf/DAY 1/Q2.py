#extract all valid 10 digit indian mobile numbers (aptionally with +91)from a text>

import re
text = "call 9876543210 or +91-9123456780 . Invalid 12345 and 5555555555"
nums = re.findall(r"(?:\+91[-]?)?\b([6-9]\d{9})\b",text)
print (nums)