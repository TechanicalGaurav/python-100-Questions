#find the top 3 most frequent words in a paragraph, ignoring case,punctuations, and stop words

import re
from collections import Counter
text = "The cat and the dog. The dog barked;, the cat ran away!"
stop = {"the","and","a","an"}
words = [w for w in re.findall(r"[a-z]+",text.lower()) if w not in stop]
print (Counter(words).most_common(3))