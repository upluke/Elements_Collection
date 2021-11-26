# 16.4 Compute the binomial coefficients
# The number of subproblems is O(nk) and once(n-1 -- k) and (n-1 -- k-1) are known, (n -- k) can be computed in O(1) time, yielding an O(nk) time complexity. The space complexity is also O(nk); it can easily be reuced to O(k)
# https://www.youtube.com/watch?v=Eo21CfNJfCs&t=4s
# https://www.youtube.com/watch?v=s19dWIHficY
def compute_binomial_coefficient(n, k):

    if k in (0, n):
        return 1

    without_k = compute_binomial_coefficient(n - 1, k)
    with_k = compute_binomial_coefficient(n - 1, k - 1)
    return without_k + with_k


print(compute_binomial_coefficient(12, 4))  # 495
