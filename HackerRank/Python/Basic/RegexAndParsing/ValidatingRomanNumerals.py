regex_pattern = r"^M{0,3}(?:CM|DC{0,3}|CD|C{0,3})(?:XC|LX{0,3}|XL|X{0,3})(?:IX|VI{0,3}|IV|I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
