# requests登录校园网并进行操作
import requests
import ddddocr
from bs4 import BeautifulSoup


class GdufeSchoolSystem:

    ses = requests.session()

    # 获取验证码
    def get_code_img(self):
        ocr = ddddocr.DdddOcr()
        header = {
            "Content-Type": "image/jpeg;charset=UTF-8",
            "Vary": "Accept-Encoding"
        }
        code = self.ses.get("http://jwxt.gdufe.edu.cn/jsxsd/verifycode.servlet", headers=header, timeout=5)
        # 验证码图片保存到本地
        with open('code.jpg', 'wb') as file:
            file.write(code.content)
        # 识别验证码并返回验证码
        with open('code.jpg', 'rb') as f:
            img_bytes = f.read()
            res = ocr.classification(img_bytes)
            return res
    # 登录
    def login(self):
        username = input("请输入学号:")
        password = input("请输入密码:")
        PostData = {
            'USERNAME': username,
            'PASSWORD': password,
            'RANDOMCODE': self.get_code_img()
        }
        url = 'http://jwxt.gdufe.edu.cn/jsxsd/xk/LoginToXkLdap'
        try:
            self.ses.post(url, data=PostData, timeout=5)
            print("登录成功")
        except:
            print("登录失败")
    # 获取成绩
    def get_class_score(self):
        time = input("请输入学期(如:2019-2020-1):")
        PostData = {
            "kksj":time,
            "fxkc": "0",
            "xsfs": "all"
        }
        url = 'http://jwxt.gdufe.edu.cn/jsxsd/kscj/cjcx_list'
        msgtext = self.ses.post(url, data=PostData, timeout=5).text
        soup = BeautifulSoup(msgtext, 'lxml')
        target = soup.find_all('div',class_ = 'Nsb_pw')
        # 添加css
        css = """
        <style>
            th , td {
                border: 1px solid #000;
            }
        </style>
        """
        target[0].insert(0,css)
        with open("学期成绩.html" , "w" , encoding= "utf-8") as fq :
            fq.write(str(target[0]))
            print("学期成绩.html 保存成功")
    # 获取课表
    def get_class_table(self):
        time = input("请输入学期(如:2019-2020-1):")
        PostData = {
            "xnxq01id": time
        }
        url = 'http://jwxt.gdufe.edu.cn/jsxsd/xskb/xskb_list.do'
        msgtext = self.ses.post(url, data=PostData, timeout=5).text
        soup = BeautifulSoup(msgtext, 'lxml')
        target = soup.find_all('table',class_ = 'Nsb_r_list Nsb_table')
        with open('class_table.html','w',encoding='utf-8') as f:
            f.write(str(target[0]))
    # 生成课表外部下载链接
    def download_class_table(self):
        time = input("请输入学期(如:2019-2020-1):")
        url = f'http://jwxt.gdufe.edu.cn/jsxsd/xskb/xskb_print.do?xnxq01id=${0}&zc='.format(time)
        print('点击下载课表：',url)
    # 获取考试安排
    def get_exam_arrange(self):
        time = input("请输入学期(如:2019-2020-1):")
        PostData = {
            "xnxq01id": time
        }
        url = 'http://jwxt.gdufe.edu.cn/jsxsd/xsks/xsksap_list'
        msgtext = self.ses.post(url, data=PostData, timeout=5).text
        # 保存考试安排.html
        with open("考试安排.html" , "w" , encoding= "utf-8") as fq :
            fq.write(msgtext)
            print("考试安排.html 保存成功")
