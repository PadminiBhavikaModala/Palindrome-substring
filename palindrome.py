def longestPalindrome(s):

    if s == "" or s == len(s) * s[0]:
        return s

    p = ""
    l = 1

    for i in range(len(s)):
          for j in range(len(s), 0, -1):
               w = s[i:j]

               
               if w == w[::-1] and len(w) > l:
                    p = w
                    l = len(w)
    return p
string = input()
print(longestPalindrome(string))
