import os,time,re
from common.getpackacti import GetPackActi

class Run:
    def __init__(self,apkname):
        # 调用公共方法获取包名和类名
        dict = GetPackActi(apkname).get_packacti()
        self.package = dict['package']
        self.activity=dict['activity']

    def run_app(self):
        #ADB命令启动APP
        output = os.popen('adb shell am start -W -n %s/%s' % (self.package,self.activity)).read()
        # print(output)
        time.sleep(3)
        # 通过ps命令查看进程
        process = os.popen('adb shell ps | findstr "%s"' % self.package).read()
        # print(process)
        time.sleep(3)
        if 'Status: ok' in output and len(process) != 0:
            starttime=re.findall("TotalTime: \\d*",output)
            result='启动APP成功，时间%s'%starttime[0]+'毫秒'
        else:
            result= "启动APP失败"
        return result


if __name__ == '__main__':
    result=Run('android.apk').run_app()
    print(result)