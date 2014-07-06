#counter function implementation…

from collections import Counter

import string
data=raw_data('data:')
print data
bag_collections=data.split()
print bag_collections
finalise_bag=Counter(bag_collections)
print finalise_bag
