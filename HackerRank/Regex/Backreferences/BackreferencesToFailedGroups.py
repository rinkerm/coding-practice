Regex_Pattern = r"^\d{2}([-]{0,1})\d{2}\1\d{2}\1\d{2}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
