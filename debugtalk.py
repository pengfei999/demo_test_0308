import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


'''
{"title":"正常登录","username":"keyou1","password":"123456",
 "status_code":200,"body_msg":"token"},
{"title": "密码错误", "username": "keyou1", "password": "1234567",
 "status_code": 400, "body_msg": "no_field_errors"},
{"title": "用户名错误", "username": "keyou1222", "password": "123456",
 "status_code": 400, "body_msg": "no_field_errors"},
{"title": "用户名为空", "username": "", "password": "123456",
 "status_code": 400, "body_msg": "username"},
{"title": "密码为空", "username": "keyou1", "password": "",
 "status_code": 400, "body_msg": "password"}
 '''

def sleep(n_secs):
    time.sleep(n_secs)
def get_accounts():
    accounts=[
        {"title": "正常登录", "username": "keyou1", "password": "123456",
         "status_code": 200, "body_msg": "token"},
        {"title": "密码错误", "username": "keyou1", "password": "123456",
         "status_code": 200, "body_msg": "token"},
        {"title": "用户名错误", "username": "keyou1", "password": "123456",
         "status_code": 200, "body_msg": "token"},
        {"title": "用户名为空", "username": "keyou1", "password": "123456",
         "status_code": 200, "body_msg": "token"},
        {"title": "密码为空", "username": "keyou1", "password": "123456",
         "status_code": 200, "body_msg": "token"}

     ]

    return accounts
if __name__=="__main__":
    print(get_accounts())