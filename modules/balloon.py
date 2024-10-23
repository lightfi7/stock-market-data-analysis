import time

from win32api import *
from win32gui import *
import win32con
import os
import sys


class SystemNotification:
    def __init__(self, title, message):
        message_map = {win32con.WM_DESTROY: self.on_destroy}

        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "SystemNotificationClass"
        wc.lpfnWndProc = message_map
        class_atom = RegisterClass(wc)

        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(class_atom, "System Notification", style,
                                 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hinst, None)
        UpdateWindow(self.hwnd)

        icon_path = os.path.abspath(os.path.join(sys.path[0], "icon_notification.ico"))
        icon_flags = LR_LOADFROMFILE | LR_DEFAULTSIZE

        try:
            hicon = LoadImage(hinst, icon_path, IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_WARNING)

        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "System Notification")
        Shell_NotifyIcon(NIM_ADD, nid)

        Shell_NotifyIcon(NIM_MODIFY, (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, hicon,
                                      "System Notification", message, 200, title))
        time.sleep(10)
        DestroyWindow(self.hwnd)
        UnregisterClass(class_atom, hinst)

    def on_destroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)


def show_notification(title, message):
    SystemNotification(title, message)


