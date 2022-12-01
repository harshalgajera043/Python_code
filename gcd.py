def cal_gcd(a,b):
    if (a==0):
        return b
    return cal_gcd(b%a,a)
print(cal_gcd(52,4))