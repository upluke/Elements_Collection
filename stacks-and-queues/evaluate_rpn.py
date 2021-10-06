
# 8.2
# RPN
# since we perform O(1) computation per character of the string,the time complexity is O(n)

def evaluate(str):
    intermediate_results = []
    delimiter = ','
    operators = {
        '+': lambda y, x: x+y,
        '-': lambda y, x: x-y,
        '*': lambda y, x: x*y,
        '/': lambda y, x: x//y
    }

    for token in str.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
    return intermediate_results[-1]


print(evaluate("2,1,+,3,*"))

# Evaluate Reverse Polish Notation

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# lc:
def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t not in "+-*/":
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == "+":
                stack.append(l+r)
            elif t == "-":
                stack.append(l-r)
            elif t == "*":
                stack.append(l*r)
            else:
                stack.append(int(float(l)/r))
    return stack.pop()


print(evalRPN(["2", "1", "+", "3", "*"]))


# # init:
# def evalRPN(tokens):
#   nums=[]
#   res=0
#   for t in tokens:
#     if  t[t[0] in '-+':].isalnum():
#       nums.append(t)
#     else:
#       pair= nums[-2:]
#       nums=nums[:-2]
#       newNum=helper(pair, t)
#       nums.append(newNum)
#   print(nums.pop())

# def helper(pair, operator):
#   num1, num2=int(pair[0]), int(pair[1])
#   if operator=='+':
#     return num1+num2
#   elif operator=='-':
#     return num1-num2
#   elif operator=='*':
#     return num1*num2
#   else:
#     return int(float(num1)/num2) # abs(int(num1/num2)) doesn't work!!!


# evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
