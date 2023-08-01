# GDUFE_Login

闲的无聊随便写的...<br>
基于python,使用 dddocr进行验证码识别,request模拟登录
实现:
- [√] 登录教务系统
- [√] 获取课表,bs4整理后,以html保存到本地
- [√] 获取成绩,bs4整理后,以html保存到本地
- [√] 生成偷跑链接,在第二轮选课未开始时可以先获取课表


偷跑链接: 
```
http://jwxt.gdufe.edu.cn/jsxsd/xskb/xskb_print.do?xnxq01id={???}&zc=
```
将上面链接的{???}替换为具体学期时间,例如我要获取2023-2024-1的课表,则改为
```
http://jwxt.gdufe.edu.cn/jsxsd/xskb/xskb_print.do?xnxq01id=2023-2024-1&zc=
```
在浏览器登录教务系统的前提下，复制该链接到地址栏进行下载
