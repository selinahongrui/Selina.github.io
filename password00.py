# 校验用户名密码

user_pwd = {'user':'Selina', 'pwd':'qwe@123'}

username = input('请输入用户名：')
password = input('请输入密码：')

if username == user_pwd['user'] and password == user_pwd['pwd']:
    print ('Success!')
else:
    print ('Permission denied!')


# 函数版

# 也需要这句 user_pwd = {'user':'Selina', 'pwd':'qwe@123'}
# 只不过在前面写过了已经


def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == user_pwd['user'] and password == user_pwd['pwd']:
        return 'Success!'
    else:
        return 'Permission denied!'

print(login())
