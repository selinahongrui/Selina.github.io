#按规则生成密码
import string 
import random 
import base64
import pyperclip


def login():
    count = input('选择生成密码的位数（正整数呦）：')
    pwd = input('请输入你的提示密码：')
    salt = input ('输入你想加入的盐：')
    position = input('选择从第几位开始取值(1~5):')
    try:
        count = int(count) 
        position = int(position)
        if count == int(count) and position == int(position):
            saltpwd = pwd + salt
            secretpwd = base64.b64encode(saltpwd.encode('utf-8'))
            length = count + position
            if len(secretpwd) < length :
                secretpwd = str(secretpwd)
                secretpwd = secretpwd.ljust(length,'%')
                secretpwd = base64.b64encode(secretpwd.encode('utf-8'))
                finalpwd = secretpwd.decode('utf-8')
                pyperclip.copy(finalpwd[position - 1 : count + position - 1])
                return 'OK啦！让我们去粘贴密码吧~！'
            else:
                finalpwd = secretpwd.decode('utf-8')
                pyperclip.copy(finalpwd[position - 1 : count + position - 1])
                return 'OK啦！让我们去粘贴密码吧~！'
        else: 
            return 'error'
    except Exception as e:
        print(e)

print(login())
    