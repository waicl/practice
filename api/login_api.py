# api是封装被测系统的接口
# 导包
import requests
class LoginApi:
    def login(self,mobile,password):
        jsonData = {"mobile":mobile,"password":password}
        response = requests.post(url='http://182.92.81.159/api/sys/login',
                                 json=jsonData)
        return response

# json格式下的数据都是固定写死的，不管是谁调用，都是会返回用户13800000002的结果

if __name__ == '__main__':
    login_api = LoginApi()
    login_api.login(3,4)












