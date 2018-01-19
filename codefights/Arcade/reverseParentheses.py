def reverseParentheses(s):
    "return reversed strings contained in each pair of matching parentheses"
    pairs = []
    left_brackets = []
    
    #determine the bracket pairs first
    for i in range(len(s)):
        if s[i] == '(':
            left_brackets.append(i)
        elif s[i] == ')':
            left_bracket = left_brackets[-1]
            del left_brackets[-1]
            pairs.append((left_bracket, i))
            
    for pair in pairs:
        left, right = pair
        #reverse strings in parentheses
        strings = s[left:right][::-1]
        s = s[:left] + strings + s[right:]
    
    s = s.replace('(', '').replace(')', '')
    return s
