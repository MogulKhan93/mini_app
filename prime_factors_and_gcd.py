#  Determine the prime factors of the following two numbers and
#  use those prime factorisations to determine gcd(a, b)

def factors_for(n):  # Determination of prime factors of a number
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def prime_factor_gcd(a, b):  # Finding the greatest common divisor of two numbers
    gcd_list = []
    num1_list = factors_for(a)
    num2_list = factors_for(b)

    for j in num1_list:
        for k in num2_list:
            if j == k:
                num2_list.remove(k)
                gcd_list.append(j)
                break
            else:
                continue
    gcd = 1
    for i in gcd_list:
        gcd *= i
    return gcd


print(f'gcd = {prime_factor_gcd(5940, 5808)}')
