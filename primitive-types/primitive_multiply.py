# 4.5 Compute product without arithmetical operators
# The time complexity of additon is O(n), where n is the number of bits needed to represent the operands. Since we do n addtions to perform a single multiplication, the total time complexity is O(n^2)


def multiply(x, y):
    def add(a, b):
        if b == 0:
            return a
        else:
            return add(a ^ b, (a & b) << 1)

    running_sum = 0
    while x:  # examines each bit of x
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1

    return running_sum

# x             y
# 3: 0011       5:0101

# x&1
# 0011 & 0001 : 1

# running_sum = add(0, 5)
# a             b          a^b        a&b     (a&b)<<1
# 0:0000      5:0101      5:0101       0         0

# >>> add(a^b, (a&b)<<1)
# a:0           b:5
# a^b:5  (a&b)<<1: 0
# a:5           b:0
# >>> if b==0:
# return a:5

# running_num= 5

# x: 3>>1: 1
# y: 5<<1: 10

# x              y
# x:1: 0001      y:10: 1010

# x&1
# x: 0001 & 1:0001 = 1

# running_sum = add(5, 10)

# a             b          a^b        a&b     (a&b)<<1
# 5:0101      10:1010    15:1111       0         0

# >>> add(a^b, (a&b)<<1)
# a^b: 15:1111    (a&b)<<1: (a:0101 & b:1010)<<1 : (0)<<1:0
# >>> if b==0:
# return a:15

# running_num= 15

# x               y
# x:0: 0000       y:20: 10100
# >>> while(x)
# return running_num:15


print(multiply(3, 5))
