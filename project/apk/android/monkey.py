#https://www.cnblogs.com/test_home_c/p/10087781.html
#encoding=gbk
import os,time
from common.getpackacti import GetPackActi
class Monkey:
    def __init__(self,apkname):
        dict = GetPackActi(apkname).get_packacti()
        self.package = dict['package']

    def monkey_app(self):
        os.system('adb shell monkey -p %s -v -v  --throttle 1000 200'%self.package)

if __name__ == '__main__':
    a=Monkey('marimo_v2.03_release_190819.apk')
    a.monkey_app()