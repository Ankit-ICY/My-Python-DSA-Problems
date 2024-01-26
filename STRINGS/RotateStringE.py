s = "abcde"
goal = "cdeab"
for i in range(len(s)):
    if goal == s[i:] + s[0:i]:
        print( True)
        break


