import os,time
from common.getpackacti import GetPackActi

class Uninstall:
    def __init__(self,apkname):
        #调用公共方法获取PACKAGE
        dict=GetPackActi(apkname).get_packacti()
        self.package=dict['package']
        # self.activity=dict['activity']
        # print(self.package)
        # print(self.activity)

    def uninstall_app(self):
        output=os.popen("adb uninstall %s"%self.package).read()
        # print(output)
        time.sleep(2)
        if 'Success' in output:
            result='卸载APP成功'
        else:
            result='卸载APP失败'
        return result

if __name__ == '__main__':
    result=Uninstall('android.apk').uninstall_app()
    print(result)