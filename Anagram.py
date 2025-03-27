# An anagram is when two words have the same letters but in a different order.

# 🔹 Example:

# "listen" and "silent" → ✅ Anagram (same letters, different order)

# "hello" and "world" → ❌ Not an Anagram (different letters)


def is_anagram(str1,str2):
    return sorted(str1) == sorted(str2)

wrd1 = "listen"
wrd2 = "silent"
print(is_anagram(wrd1, wrd2))


