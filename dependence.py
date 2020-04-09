# encoding: utf-8
from os import system,_exit,chdir
from time import sleep
import re,ctypes
from subprocess import getoutput
id = str()#设备标识
ip = str()#设备ip
_getid = str()
run = True#控制是否退出
con_ctrl = True#用于控制选择连接方式的循环
METHOD = """
请选择连接方式（输入数字）：
    1、通过USB连接
    2、通过局域网连接（还没写完）
    3、退出
"""
mETHOD = ("Con_By_USB()","Con_By_LAN()","_exit(0)")


MENU = """
请选择您要进行的操作：
    1、调整分辨率
    2、自定义动画缩放速度（Bluestacks模拟器没有这个设置，会直接返回菜单）
    3、激活冰箱Ice Box（两种模式）
    4、激活小黑屋Stopapp（两种模式）
    5、激活黑阈
    6、退出
"""
mENU=("Size()","Velocity()","Active_Icebox()","Active_Stopapp()","Brevent()","run=False")



FOREGROUND_BLUE = 0x01
FOREGROUND_GREEN= 0x02
FOREGROUND_RED = 0x04
FOREGROUND_INTENSITY = 0x08 #前景高亮
def cprint(text,color, handle=ctypes.windll.kernel32.GetStdHandle(-11)):#输出彩色字体
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    print(text)
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def Con_By_USB():#USB连接
    system("cls")
    global id,_getid,con_ctrl
    input("\n\n确保已用数据线连接到电脑，打开USB调试并安装好驱动后按下回车")
    getoutput("taskkill /im adb.exe /f")
    print("正在启动adb，请稍候...")
    _getid = getoutput("adb devices")
    _getid = re.findall("(?<=\n).*(?=\tdevice)",_getid)#尝试匹配设备标识
    if not len(_getid):#无设备
        print("没有可用的设备，即将自动返回连接方式选择界面",end="",flush=True)
        for i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
        con_ctrl = True
        system("cls")
        return
    elif 1==len(_getid):#仅一个设备
        id = _getid[0]
        system("cls")
        print("已连接到",id,'自动进入菜单')
    else:#多个设备
        print("当前可用的设备如下：")
        i = 1
        while i:
            try:print(str(i)+'、'+_getid[i-1])
            except:i = 0
            else:i += 1
        id = input("请选择要连接的编号：")
        while 1:
            try:id = _getid[int(id)-1]
            except:id = input("请输入正确的编号：")
            else:break
        system("cls")
        print("已连接到",id,"自动进入菜单")
def Con_By_LAN():
    """
    global id,ip,con_ctrl
    input("确保已打开USB调试并已打开网络adb服务后按下回车")
    getoutput("taskkill /im adb.exe /f")
    print("请输入ip(若不输入端口则为默认5555)：",end="",flush=True)
    ip = input()
    try:re.search("already",getoutput("adb connect "+ip)).group()
    except:
        print("连接失败，请检查ip是否正确以及是否已开启网络adb\n即将自动返回连接方式选择界面",end='')
        for _i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
        con_ctrl = True
        system("cls")
        return
    else:
        system("cls")
        id = ip
        print("已连接到",ip,"自动进入菜单")
    """
    global con_ctrl
    system("cls")
    print("\n都说了没写完了(╬￣皿￣)=○")
    print("没有可用的设备，即将自动返回连接方式选择界面",end="",flush=True)
    for _i in range(1,4):
        print(".",end='',flush=True)
        sleep(1)
    con_ctrl = True
    system("cls")
    return


def Size():#修改分辨率
    system("cls")
    now = re.findall("[0-9]+",getoutput("adb -s "+id+" shell wm size"))
    print("默认宽度为："+now[0]," 默认长度为："+now[1])
    print("当前宽度为："+(now[0] if len(now)-4 else now[2])," 当前长度为："+(now[1] if len(now)-4 else now[3]))
    if "yes"!=input("键入yes继续更改，键入其余任意内容返回菜单："):
        system("cls")
        return
    width = input("请输入新的宽度（像素数）：")
    while not width.isdigit():width = input("请输正确的宽度（正整数）：")
    length = input("请输入新的长度（像素数）：")
    while not length.isdigit():width = input("请输正确的长度（正整数）：")
    getoutput("adb -s "+id+" shell wm size "+width+'x'+length)
    print("修改成功，即将返回菜单",end='')
    for _i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
    system("cls")
def Velocity():#自定义动画速度
    system("cls")
    print("当前窗口动画缩放："+re.search(r"[0-9]+(\.[0-9]+)*",getoutput("adb -s "+id+" shell settings get global window_animation_scale")).group())
    print("当前过度动画缩放："+re.search(r"[0-9]+(\.[0-9]+)*",getoutput("adb -s "+id+" shell settings get global transition_animation_scale")).group())
    print("当前动画程序时长缩放："+re.search(r"[0-9]+(\.[0-9]+)*",getoutput("adb -s "+id+" shell settings get global animator_duration_scale")).group())
    if "yes"!=input("键入yes继续更改，键入其余任意内容返回菜单："):
        system("cls")
        return
    a = input("请输入新的窗口动画缩放：")
    while True:
        try:
            if float(a)<0 or float(a)>10:raise Exception
        except:a = input("请输入正确的窗口动画缩放（范围[0-10]）：")
        else:break
    b = input("请输入新的过度动画缩放：")
    while True:
        try:
            if float(b)<0 or float(b)>10:raise Exception
        except:b = input("请输入正确的过度动画缩放（范围[0-10]）：")
        else:break
    c = input("请输入新的动画程序时长缩放：")
    while True:
        try:
            if float(c)<0 or float(c)>10:raise Exception
        except:c = input("请输入正确的动画程序时长缩放（范围[0-10]）：")
        else:break
    getoutput("adb -s "+id+" shell settings put global window_animation_scale "+a)
    getoutput("adb -s "+id+" shell settings put global transition_animation_scale "+b)
    getoutput("adb -s "+id+" shell settings put global animator_duration_scale "+c)
    print("修改成功，即将返回菜单",end='')
    for _i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
    system("cls")
def Active_Icebox():
    ICEBOX_MODE="""
请选择模式：
    1、普通adb模式（使用此模式激活后请勿关闭USB调试，否则即失效）
    2、设备管理员模式
"""
    iCEBOX_MODE = ("adb -s "+id+" shell sh /sdcard/Android/data/com.catchingnow.icebox/files/start.sh","adb -s "+id+" shell dpm set-device-owner com.catchingnow.icebox/.receiver.DPMReceiver")
    con = True
    back = str()
    system("cls")
    cprint("P.S.请确保已完整阅读过官方文档\n若由于使用本工具而未仔细阅读官方文档相关内容造成不良后果作者将不承担任何责任",FOREGROUND_RED|FOREGROUND_INTENSITY)
    if "yes"!=input("确保已了解相关事项输入yes确认继续，确认即视为同意P.S.中内容，输入其余任意内容返回菜单"):
        system("cls")
        return
    while con:
        mode = input(ICEBOX_MODE)
        try:
            con = False
            if int(mode)<1:raise Exception
            back=getoutput(iCEBOX_MODE[int(mode)-1])
        except:
            con = True
            print("\n请输入正确的数字：")
    try:re.search(r"success",back,re.IGNORECASE).group()
    except AttributeError:
        try:re.search(r"already set",back).group()
        except AttributeError:
            try:
                if len(re.findall("--user",back)):raise Exception
                re.search(r"account|user",back,re.IGNORECASE).group()
            except:
                print("我怀疑你还没安装冰箱")
                print("即将返回菜单",end='')
                for _i in range(1,4):
                    print(".",end='',flush=True)
                    sleep(1)
                system("cls")
                return
            else:
                print("仍存在用户或账号，请手动删除所有账号（包括Google账号、华为账号、小米账号等），删除或关闭所有多用户/访客模式/应用双开\n若仍无法激活，请尝试打开飞行模式卸载支付宝（激活完成后可重新安装），即将返回菜单",end='')
                for _i in range(1,4):
                    print(".",end='',flush=True)
                    sleep(1)
                system("cls")
                return
        else:
            print("已存在设备管理员，激活失败，即将返回菜单",end='')
            for _i in range(1,4):
                print(".",end='',flush=True)
                sleep(1)
            system("cls")
            return
    else:
        print("激活成功，即将返回菜单",end='')
        for _i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
        system("cls")
        return
def Active_Stopapp():
    STOPAPP_MODE="""
请选择模式：
    1、麦克斯韦妖模式（使用此模式激活后请勿关闭USB调试，否则即失效）
    2、设备管理员模式
"""
    sTOPAPP_MODE = ("adb -s "+id+" shell sh /sdcard/Android/data/web1n.stopapp/files/demon.sh","adb -s "+id+" shell dpm set-device-owner web1n.stopapp/.receiver.AdminReceiver")
    con = True
    back = str()
    system("cls")
    cprint("P.S.请确保已完整阅读过官方文档\n若由于使用本工具而未仔细阅读官方文档相关内容造成不良后果作者将不承担任何责任",FOREGROUND_RED|FOREGROUND_INTENSITY)
    if "yes"!=input("确保已了解相关事项输入yes确认继续，确认即视为同意P.S.中内容，输入其余任意内容返回菜单"):
        system("cls")
        return
    while con:
        mode = input(STOPAPP_MODE)
        try:
            con = False
            if int(mode)<1:raise Exception
            back=getoutput(sTOPAPP_MODE[int(mode)-1])
        except:
            con = True
            print("\n请输入正确的数字：")
    try:re.search(r"success|(daemon process started)",back,re.IGNORECASE).group()
    except AttributeError:
        try:re.search(r"already set",back).group()
        except AttributeError:
            try:
                if len(re.findall("--user",back)):raise Exception
                re.search(r"account|user",back,re.IGNORECASE).group()
            except AttributeError:
                print("我怀疑你还没安装小黑屋")
                print("即将返回菜单",end='')
                for _i in range(1,4):
                    print(".",end='',flush=True)
                    sleep(1)
                system("cls")
                return
            else:
                print("仍存在用户或账号，请手动删除所有账号（包括Google账号、华为账号、小米账号等），删除或关闭所有多用户/访客模式/应用双开\n若仍无法激活，请尝试打开飞行模式卸载支付宝（激活完成后可重新安装），即将返回菜单",end='')
                for _i in range(1,4):
                    print(".",end='',flush=True)
                    sleep(1)
                system("cls")
                return
        else:
            print("已存在设备管理员，激活失败，即将返回菜单",end='')
            for _i in range(1,4):
                print(".",end='',flush=True)
                sleep(1)
            system("cls")
            return
    else:
        print("激活成功，即将返回菜单",end='')
        for _i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
        system("cls")
        return
def Brevent():
    system("cls")
    cprint("P.S.请确保已完整阅读过官方文档\n若由于使用本工具而未仔细阅读官方文档相关内容造成不良后果作者将不承担任何责任",FOREGROUND_RED|FOREGROUND_INTENSITY)
    if "yes"!=input("确保已了解相关事项输入yes确认继续，确认即视为同意P.S.中内容，输入其余任意内容返回菜单"):
        system("cls")
        return
    back = getoutput("adb -s "+id+" shell sh /data/data/me.piebridge.brevent/brevent.sh")
    try:re.search("success",back,re.IGNORECASE).group()
    except AttributeError:
        try:re.search("root",back,re.IGNORECASE).group()
        except:
            print("我怀疑你还没安装黑阈")
            print("即将返回菜单",end='')
            for _i in range(1,4):
                print(".",end='',flush=True)
                sleep(1)
            system("cls")
            return
        else:
            print("已经以root模式激活")
            print("即将返回菜单",end='')
            for _i in range(1,4):
                print(".",end='',flush=True)
                sleep(1)
            system("cls")
            return
    else:
        print("激活成功，即将返回菜单",end='')
        for _i in range(1,4):
            print(".",end='',flush=True)
            sleep(1)
        system("cls")
        return