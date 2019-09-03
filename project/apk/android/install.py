import os,time
from common.getpackacti import GetPackActi

class Install:
    def __init__(self, apkname):
        #调用，获取apk路径
        self.folder=GetPackActi(apkname).get_fold()
        # print(self.folder)

    def install_app(self):
        output=os.popen('adb install -r %s' % self.folder).read()
        print(output)
        time.sleep(3)
        #安装断言，返回断言结果
        if 'Success' or ''  in output:
            result='安装APP成功'
        else:
            result = '安装APP失败'
        return result

if __name__ == '__main__':
    result=Install('marimo_v2.03_release_190819.apk').install_app()
    print(result)

    # 'performance_v2.03_release_190822.apk''production_v2.03_release_190819.apk''marimo_v2.03_release_190819.apk'