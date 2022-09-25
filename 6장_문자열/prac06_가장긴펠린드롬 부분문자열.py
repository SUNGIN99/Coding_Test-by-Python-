

def longestPalindrome(s : str) -> str:

    def expand(left : int, right : int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        print(left, right, s[left+1 : right])
        return s[left+1 : right] #끝난거에서 한칸 다시 땡겨서 return(while문 탈출후 마지막 번복)

    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''

    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key = len)
        #print(result)

    return result

print(longestPalindrome("babad"))