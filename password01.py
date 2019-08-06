# 生成随机密码， eg: 8位

import random
import string

count = 8
password = string.ascii_letters + string.digits
print("".join(random.choice(password) for i in range (count)))


#函数版

def pwd(count):
    pswd = string.digits +string.ascii_letters
    return "".join(random.choice(pswd) for i in range(count))

print(pwd(8))




