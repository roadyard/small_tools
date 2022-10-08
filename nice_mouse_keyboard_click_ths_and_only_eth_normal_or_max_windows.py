#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import datetime
import win32gui
import keyboard
from pymouse    import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()#这个好像用不上，但是先留着吧。 2022年10月7日

'''
#程序描述：
#目前的点击对象为：aicoin，同花顺，其他的待补充
#目前需要改变和定义根据不同软件点击的不同位置的几个按键有 ： tab,up,down,right,left



#特别说明：现在这个版本是针对数字货币中单个eth的，其他的点击版本暂时还没有做，主要是因为周期切换一个在上一个在下，下次开始的时候就做一个全部的，而且要改也是什么难事 2022年10月7日



'''


#global_para
aicoin_period_init_click =  4     #aicoin默认点击15分钟
ths_period_init_click    =  6     #同花顺默认点击日线， 2022年10月7日
ths_select_init_click    = -1
ths_y_position_values    =  125
f11_init_values          =  0 #这个其实逻辑上有点感觉，如果0是在最大化的时候，就会影响点击程序的切换，不过先不管了，留个注意事项。 2022年10月9日



def f11_function_define():
    #print('f11')

    global f11_init_values

    if f11_init_values == 0:
        f11_init_values = 1
    elif f11_init_values == 1:
        f11_init_values = 0
    else:
        f11_init_values = 0#修正预防
        print('f11 出现其他值，理论上是不可能的，请检查...')

    #print(f11_init_values)


def space_click():
    #print('tab')

    #点击对象：任意
    #作用：获取鼠标位置
    mouse_position = m.position()
    print('啊，刚才敲键盘了，当前鼠标位置是：{}， 现在时间是 : {} ...'.format(mouse_position, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def tab_click():
    #print('tab')

    #点击对象：aicoin
    current_windowns_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #print(current_windowns_title)
    split_temp = re.split(r'[\s|]+', current_windowns_title)
    #print(split_temp)

    if (('AICoin-为价值，更高效' in split_temp)&('Chrome' in split_temp)):
        #print('aicoin_click')
        print('数字货币复盘了 - 品种切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        m.click(677, 222, 1)
    else:
        pass


def right_click():
    #print('right')
    
    #点击对象：aicoin，同花顺，其他晚点再补充
    current_windowns_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #print(current_windowns_title)
    split_temp = re.split(r'[\s|]+', current_windowns_title)
    #print(split_temp)

    if (('AICoin-为价值，更高效' in split_temp)&('Chrome' in split_temp)):
        #print('aicoin_click')
        print('数字货币复盘了 - 周期切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        global aicoin_period_init_click

        aicoin_period_init_click += 1
        #print(aicoin_period_init_click)

        #窗口最大最小化点击控制
        if f11_init_values == 0:#最小化
            moust_y_position_values = 90
        elif f11_init_values == 1:#最大化
            moust_y_position_values = 20
        else:
            moust_y_position_values = 90#修正防止

        if aicoin_period_init_click == 20:
            aicoin_period_init_click = 1
        elif aicoin_period_init_click == 19:
            aicoin_period_init_click = 0
        else:
            pass

        if aicoin_period_init_click == 0:
            m.click(884, moust_y_position_values, 1)#1mi 0
        elif aicoin_period_init_click == 1:
            m.click(916, moust_y_position_values, 1)#3mi 1
        elif aicoin_period_init_click == 2:
            m.click(950, moust_y_position_values, 1)#5mi 2
        elif aicoin_period_init_click == 3:
            m.click(990, moust_y_position_values, 1)#10mi 3
        elif aicoin_period_init_click == 4:
            m.click(1030, moust_y_position_values, 1)#15mi 4
        elif aicoin_period_init_click == 5:
            m.click(1072, moust_y_position_values, 1)#30mi 5
        elif aicoin_period_init_click == 6:
            m.click(1110, moust_y_position_values, 1)#1h   6
        elif aicoin_period_init_click == 7:
            m.click(1148, moust_y_position_values, 1)#2h   7
        elif aicoin_period_init_click == 8:
            m.click(1180, moust_y_position_values, 1)#3h   8
        elif aicoin_period_init_click == 9:
            m.click(1212, moust_y_position_values, 1)#4h   9
        elif aicoin_period_init_click == 10:
            m.click(1248, moust_y_position_values, 1)#6h   10
        elif aicoin_period_init_click == 11:
            m.click(1288, moust_y_position_values, 1)#12h  11
        elif aicoin_period_init_click == 12:
            m.click(1328, moust_y_position_values, 1)#1d   12
        elif aicoin_period_init_click == 13:
            m.click(1360, moust_y_position_values, 1)#2d   13
        elif aicoin_period_init_click == 14:
            m.click(1392, moust_y_position_values, 1)#3d   14
        elif aicoin_period_init_click == 15:
            m.click(1428, moust_y_position_values, 1)#5d   15
        elif aicoin_period_init_click == 16:
            m.click(1464, moust_y_position_values, 1)#1w   16
        elif aicoin_period_init_click == 17:
            m.click(1500, moust_y_position_values, 1)#1mo  17
        elif aicoin_period_init_click == 18:
            m.click(1530, moust_y_position_values, 1)#1q   18
        else:
            pass

        if aicoin_period_init_click >= 18:
            aicoin_period_init_click = -1
        else:
            pass

    elif ('同花顺远航版' in split_temp):
        #print('同花顺远航版 click')
        print('期货股票复盘了 - 周期切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        global ths_period_init_click
        global ths_select_init_click

        ths_select_init_click = 1
        ths_period_init_click += 1
        #print(ths_period_init_click)

        if ths_period_init_click == 12:
            ths_period_init_click = 1
        elif ths_period_init_click == 11:
            ths_period_init_click = 0
        else:
            pass

        if ths_period_init_click == 0:
            m.click(556, 42, 1)#1mi  0
        elif ths_period_init_click == 1:
            m.click(596, 42, 1)#5mi  1
        elif ths_period_init_click == 2:
            m.click(640, 42, 1)#15mi 2
        elif ths_period_init_click == 3:
            m.click(686, 42, 1)#30mi 3
        elif ths_period_init_click == 4:
            m.click(730, 42, 1)#1h   4
        elif ths_period_init_click == 5:
            m.click(778, 42, 1)#2h   5
        elif ths_period_init_click == 6:
            m.click(340, 42, 1)#1d   6
        elif ths_period_init_click == 7:
            m.click(384, 42, 1)#1w   7
        elif ths_period_init_click == 8:
            m.click(428, 42, 1)#1mo  8
        elif ths_period_init_click == 9:
            m.click(474, 42, 1)#1q   9
        elif ths_period_init_click == 10:
            m.click(516, 42, 1)#1y   10
        else:
            pass

        if ths_period_init_click >= 10:
            ths_period_init_click = -1
        else:
            pass

    else:
        pass


def left_click():
    #print('left')

    #点击对象：aicoin，同花顺，其他晚点再补充
    current_windowns_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #print(current_windowns_title)
    split_temp = re.split(r'[\s|]+', current_windowns_title)
    #print(split_temp)

    if (('AICoin-为价值，更高效' in split_temp)&('Chrome' in split_temp)):
        #print('aicoin_click')
        print('数字货币复盘了 - 周期切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        global aicoin_period_init_click

        aicoin_period_init_click -= 1
        #print(aicoin_period_init_click)

        #窗口最大最小化点击控制
        if f11_init_values == 0:#最小化
            moust_y_position_values = 90
        elif f11_init_values == 1:#最大化
            moust_y_position_values = 20
        else:
            moust_y_position_values = 90#修正防止

        #不知道为什么，上面部分实现了，其实下面部分可以不管的，但是我还是不舒服这边也要搞定它 20220815
        if aicoin_period_init_click == -2:
            aicoin_period_init_click = 17
        elif aicoin_period_init_click == -1:
            aicoin_period_init_click = 18
        else:
            pass

        if aicoin_period_init_click == 0:
            m.click(884, moust_y_position_values, 1)#1mi 0
        elif aicoin_period_init_click == 1:
            m.click(916, moust_y_position_values, 1)#3mi 1
        elif aicoin_period_init_click == 2:
            m.click(950, moust_y_position_values, 1)#5mi 2
        elif aicoin_period_init_click == 3:
            m.click(990, moust_y_position_values, 1)#10mi 3
        elif aicoin_period_init_click == 4:
            m.click(1030, moust_y_position_values, 1)#15mi 4
        elif aicoin_period_init_click == 5:
            m.click(1072, moust_y_position_values, 1)#30mi 5
        elif aicoin_period_init_click == 6:
            m.click(1110, moust_y_position_values, 1)#1h   6
        elif aicoin_period_init_click == 7:
            m.click(1148, moust_y_position_values, 1)#2h   7
        elif aicoin_period_init_click == 8:
            m.click(1180, moust_y_position_values, 1)#3h   8
        elif aicoin_period_init_click == 9:
            m.click(1212, moust_y_position_values, 1)#4h   9
        elif aicoin_period_init_click == 10:
            m.click(1248, moust_y_position_values, 1)#6h   10
        elif aicoin_period_init_click == 11:
            m.click(1288, moust_y_position_values, 1)#12h  11
        elif aicoin_period_init_click == 12:
            m.click(1328, moust_y_position_values, 1)#1d   12
        elif aicoin_period_init_click == 13:
            m.click(1360, moust_y_position_values, 1)#2d   13
        elif aicoin_period_init_click == 14:
            m.click(1392, moust_y_position_values, 1)#3d   14
        elif aicoin_period_init_click == 15:
            m.click(1428, moust_y_position_values, 1)#5d   15
        elif aicoin_period_init_click == 16:
            m.click(1464, moust_y_position_values, 1)#1w   16
        elif aicoin_period_init_click == 17:
            m.click(1500, moust_y_position_values, 1)#1mo  17
        elif aicoin_period_init_click == 18:
            m.click(1530, moust_y_position_values, 1)#1q   18
        else:
            pass

        if aicoin_period_init_click <= 0:
            aicoin_period_init_click = 19
        else:
            pass

    elif ('同花顺远航版' in split_temp):
        #print('同花顺远航版 click')
        print('期货股票复盘了 - 周期切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        global ths_period_init_click
        global ths_select_init_click

        ths_select_init_click = 1
        ths_period_init_click -= 1
        #print(ths_period_init_click)

        if ths_period_init_click == -2:
            ths_period_init_click = 9
        elif ths_period_init_click == -1:
            ths_period_init_click = 10
        else:
            pass

        if ths_period_init_click == 0:
            m.click(556, 42, 1)#1mi  0
        elif ths_period_init_click == 1:
            m.click(596, 42, 1)#5mi  1
        elif ths_period_init_click == 2:
            m.click(640, 42, 1)#15mi 2
        elif ths_period_init_click == 3:
            m.click(686, 42, 1)#30mi 3
        elif ths_period_init_click == 4:
            m.click(730, 42, 1)#1h   4
        elif ths_period_init_click == 5:
            m.click(778, 42, 1)#2h   5
        elif ths_period_init_click == 6:
            m.click(340, 42, 1)#1d   6
        elif ths_period_init_click == 7:
            m.click(384, 42, 1)#1w   7
        elif ths_period_init_click == 8:
            m.click(428, 42, 1)#1mo  8
        elif ths_period_init_click == 9:
            m.click(474, 42, 1)#1q   9
        elif ths_period_init_click == 10:
            m.click(516, 42, 1)#1y   10
        else:
            pass

        if ths_period_init_click <= 0:
            ths_period_init_click = 11
        else:
            pass

    else:
        pass


def up_click():
    #print('up')

    #点击对象：同花顺，其他晚点再补充
    current_windowns_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #print(current_windowns_title)
    split_temp = re.split(r'[\s|]+', current_windowns_title)
    #print(split_temp)

    if ('同花顺远航版' in split_temp):
        #print('同花顺远航版 click')
        print('期货股票复盘了 - 品种切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        global ths_select_init_click
        global ths_y_position_values

        if ths_y_position_values > 125:
            ths_y_position_values -= 57
        else:
            pass

        if ths_select_init_click == -1:
            m.click(160, 125, 1)
            ths_select_init_click = 0
        if ths_select_init_click == 1:
            m.click(160, ths_y_position_values, 1)
            ths_select_init_click = 0
        else:
            pass

    else:
        pass


def down_click():
    #print('down')

    #点击对象：同花顺，其他晚点再补充
    current_windowns_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #print(current_windowns_title)
    split_temp = re.split(r'[\s|]+', current_windowns_title)
    #print(split_temp)

    if ('同花顺远航版' in split_temp):
        #print('同花顺远航版 click')
        print('期货股票复盘了 - 品种切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        global ths_select_init_click
        global ths_y_position_values

        if ths_y_position_values < 980:
            ths_y_position_values += 57
        else:
            pass

        if ths_select_init_click == -1:
            m.click(160, 125, 1)
            ths_select_init_click = 0
        if ths_select_init_click == 1:
            m.click(160, ths_y_position_values, 1)
            ths_select_init_click = 0
        else:
            pass

    else:
        pass

def key_test():
    print('f11 test ...')


if __name__ == '__main__':

    print('按键监控程序开始运行中，可以按 esc 键退出 ...')

    keyboard.add_hotkey('space', space_click)
    keyboard.add_hotkey('f11', f11_function_define)
    keyboard.add_hotkey('tab', tab_click)
    keyboard.add_hotkey('right', right_click)
    keyboard.add_hotkey('left', left_click)
    keyboard.add_hotkey('up', up_click)
    keyboard.add_hotkey('down', down_click)

    keyboard.wait('esc')
    #wait里也可以设置按键，说明当按到该键时结束
