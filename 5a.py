import re

input = """dabAcCaCBAcCcaDA"""

exp = re.compile(r'aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|Rr|rR|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz')
while exp.search(input) is not None:
    input = re.sub(exp, '', input)

print(input)
print(len(input))