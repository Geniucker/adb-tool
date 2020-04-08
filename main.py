# encoding: utf-8
import dependence as d

d.chdir("adb")
d.system("cls")
print("版本：v0.0.1")
d.cprint("连接操作会停止其他adb的进程，若正在进行其他adb操作请完成后再使用本工具",d.FOREGROUND_RED|d.FOREGROUND_INTENSITY)
while d.con_ctrl:
    _method = input(d.METHOD)
    try:
        d.con_ctrl = False
        if int(_method)<1:raise Exception
        exec("d."+d.mETHOD[int(_method)-1])
    except:
        d.con_ctrl = True
        d.system("cls")
        d.cprint("请输入正确的数字",d.FOREGROUND_GREEN|d.FOREGROUND_INTENSITY)

while d.run:
    _method = input(d.MENU)
    try:
        if int(_method)<1:raise Exception
        exec("d."+d.mENU[int(_method)-1])
    except:
        d.system("cls")
        d.cprint("请输入正确的数字",d.FOREGROUND_GREEN|d.FOREGROUND_INTENSITY)
d.getoutput("taskkill /im adb.exe /f")
