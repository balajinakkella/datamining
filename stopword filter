#removing unwanted words from the data input…

from collections import Counter

import string
common_words = frozenset(("if", "but", "and", "the", "when", "use", "to", "for"))
title = "When to use Python for web applications"
title_words = set(title.lower().split())
keywords = title_words.difference(common_words)
print(keywords)
