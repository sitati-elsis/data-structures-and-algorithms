def isPalindrome(string):
    # Write your code here.
    if len(string) == 1:
        return True
    i = 0 
    j = len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i+=1
        j-=1
    return True
