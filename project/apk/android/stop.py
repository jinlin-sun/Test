import os,time
from common.getpackacti import GetPackActi

class Stop:
    def __init__(self,apkname):
        # 调用公共方法获取包名和类名
        dict = GetPackActi(apkname).get_packacti()
        self.package = dict['package']

    def stop_app(self):
        #ADB命令强制关闭APP
        os.system('adb shell am force-stop %s' % self.package)
        time.sleep(5)
        # 通过ps命令查看进程
        process = os.popen('adb shell ps | findstr "%s"' % self.package).read()
        time.sleep(2)
        # print(process)
        # print(len(process))
        #杀死APP断言
        if len(process) == 0:
            result='杀死APP成功'
        else:
            result = '杀死APP失败'
        return result

if __name__ == '__main__':
    result=Stop('marimo_v2.03_debug_190816_1.apk').stop_app()
    print(result)