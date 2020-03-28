import requests



login_url = 'http://182.92.81.159/api/sys/login'

class LoginApi:
    def login(self,mobile,password):
        jsonData = {"mobile":mobile, "password":password}
        response = requests.post(url=login_url,json=jsonData)
        return response



if __name__ == '__main__':
    l = LoginApi()
    result = l.login('13800000002','123456')
    print(result.json())



