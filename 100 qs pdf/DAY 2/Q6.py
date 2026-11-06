'''Parse server log lines and count how many entries exist for 
each log level (INFO,WARNING,ERROR).'''

import re
from collections import Counter
logs = '''2024-01-01 10:00:01 INFO Server started
2024-01-01 10:05:10 ERROR DB timeout 
2024-01-01 10:06:00 WARNING Slow query
2024-01-01 10:07:30 ERROR Disk full'''
levels = re.findall(r"\d{2}:\d{2}:\d{2} (\w+)",logs)
print (Counter(levels))


