# string_in = "abcdef" # 0
# string_in = "bababc" # 1, 1
# string_in = "abbcde" # 1, 0
# string_in = "abcccd" # 0, 1
# string_in = "aabcdd" # 2, 0
# string_in = "abcdee" # 1, 0
# string_in = "ababab" # 0, 2
# input = """abcdef
# bababc
# abbcde
# abcccd
# aabcdd
# abcdee
# ababab"""


count_string_with_2 = 0
count_string_with_3 = 0

ids = input.split()
for string_in in ids:
    count_each_letter = {}

    for char in string_in:
        if char in count_each_letter:
            count_each_letter[char] = count_each_letter[char] + 1
        else:
            count_each_letter[char] = 1

    if 2 in list(count_each_letter.values()):
        count_string_with_2 = count_string_with_2 + 1
    if 3 in list(count_each_letter.values()):
        count_string_with_3 = count_string_with_3 + 1

print("Chars occurring twice: ", count_string_with_2)
print("Chars occurring thrice: ", count_string_with_3)
print("Count 2 * Count 3: ", count_string_with_2 * count_string_with_3)
