def tinh_tong_chu_so(n):
    tong = n
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

n = 2023
print(tinh_tong_chu_so(n))
