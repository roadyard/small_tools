#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import datetime
import keyboard
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()                       
k = PyKeyboard()

# 当前位置
#print(m.position())    
				    
# 鼠标点击(500, 300), 第三个参数代表键位，1是左键，2是右键，3是中键
#y = k.press_key('1')
#print(y)   
#m.click(225, 255, 1)

#同花顺最大化后几个周期的鼠标点击位置





#使用说明
#这个版本需要正常使用需要从   1分钟周期    开始，不然会引入奇怪的菜单   。。。 20220815
#但是不能在 1分钟周期前引入 秒级别周期 不然又无法兼顾120的一些周期











#1mi -> (556, 42) 0
#5m  -> (596, 42) 1
#15m -> (640, 42) 2
#30m -> (686, 42) 3
#1h  -> (730, 42) 4
#2h  -> (778, 42) 5
#1d  -> (340, 42) 6
#1w  -> (384, 42) 7
#1mo -> (428, 42) 8 
#1q  -> (474, 42) 9for 
#1y  -> (516, 42) 10
#切换基准点 (160, 125)
#点位间隔： 57
#列表生成公式：
#for i in range(125,1000, 57):
#   print(i)


#'''


period_init_click =  6#默认用点击日线，这里还有非常严重的逻辑缺陷我看看怎么处理...
select_init_click = -1
y_position_values =  125



def m_right_click_sf():
    
    global period_init_click
    global select_init_click

    select_init_click = 1
    period_init_click += 1

    #print(period_init_click)

    if period_init_click == 12:
        period_init_click = 1
    elif period_init_click == 11:
        period_init_click = 0
    else:
        pass

    if period_init_click == 0:
        m.click(556, 42, 1)#1mi  0
    elif period_init_click == 1:
        m.click(596, 42, 1)#5mi  1
    elif period_init_click == 2:
        m.click(640, 42, 1)#15mi 2
    elif period_init_click == 3:
        m.click(686, 42, 1)#30mi 3
    elif period_init_click == 4:
        m.click(730, 42, 1)#1h   4
    elif period_init_click == 5:
        m.click(778, 42, 1)#2h   5
    elif period_init_click == 6:
        m.click(340, 42, 1)#1d   6
    elif period_init_click == 7:
        m.click(384, 42, 1)#1w   7
    elif period_init_click == 8:
        m.click(428, 42, 1)#1mo  8
    elif period_init_click == 9:
        m.click(474, 42, 1)#1q   9
    elif period_init_click == 10:
        m.click(516, 42, 1)#1y   10
    else:
        pass 

    if period_init_click >= 10:
        period_init_click = -1
    else:
        pass

    print('周期切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def m_left_click_sf():
    
    global period_init_click
    global select_init_click

    select_init_click = 1
    period_init_click -= 1

    #print(period_init_click)

    if period_init_click == -2:
        period_init_click = 9
    elif period_init_click == -1:
        period_init_click = 10
    else:
        pass

    if period_init_click == 0:
        m.click(556, 42, 1)#1mi  0
    elif period_init_click == 1:
        m.click(596, 42, 1)#5mi  1
    elif period_init_click == 2:
        m.click(640, 42, 1)#15mi 2
    elif period_init_click == 3:
        m.click(686, 42, 1)#30mi 3
    elif period_init_click == 4:
        m.click(730, 42, 1)#1h   4
    elif period_init_click == 5:
        m.click(778, 42, 1)#2h   5
    elif period_init_click == 6:
        m.click(340, 42, 1)#1d   6
    elif period_init_click == 7:
        m.click(384, 42, 1)#1w   7
    elif period_init_click == 8:
        m.click(428, 42, 1)#1mo  8
    elif period_init_click == 9:
        m.click(474, 42, 1)#1q   9
    elif period_init_click == 10:
        m.click(516, 42, 1)#1y   10
    else:
        pass 

    if period_init_click <= 0:
        period_init_click = 11
    else:
        pass

    print('周期切换, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))



def m_up_click_sf():

    global select_init_click
    global y_position_values

    if y_position_values > 125:
        y_position_values -= 57
    else:
        pass

    if select_init_click == -1:
        m.click(160, 125, 1)
        select_init_click = 0
    if select_init_click == 1:
        m.click(160, y_position_values, 1)
        select_init_click = 0
    else:
        pass

    print('品种选择, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def m_down_click_sf():

    global select_init_click
    global y_position_values

    if y_position_values < 980:
        y_position_values += 57
    else:
        pass

    if select_init_click == -1:
        m.click(160, 125, 1)
        select_init_click = 0
    if select_init_click == 1:
        m.click(160, y_position_values, 1)
        select_init_click = 0
    else:
        pass

    print('品种选择, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def m_tab_click_bitcoin():  
    
    #原来的位置
    m.click(677, 255, 1)
    #现在的新位置，为了避开所谓的热门推荐的位置
    #m.click(677, 662, 1)

    #前置空格有问题
    #m.click(1580, 188, 1)#aicoin pc软件的点击位置
    #m.click(677, 255, 1)#aicoin web的点击位置
    print('我刚刚去复盘了, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def time_print():
    #m.click(1468, 684, 1)
    print('我离开电脑或者回来电脑面前了, 现在时间是 : {} ...'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
 


if __name__ == '__main__':

    print('A股和商品期货程序开始执行 ...')
    keyboard.add_hotkey('space', time_print)
    keyboard.add_hotkey('tab', m_tab_click_bitcoin)             
    keyboard.add_hotkey('right', m_right_click_sf)
    keyboard.add_hotkey('left', m_left_click_sf)
    keyboard.add_hotkey('up', m_up_click_sf)
    keyboard.add_hotkey('down', m_down_click_sf)
    #keyboard.wait()#如果用这调函数程序会一直监控下去
    keyboard.wait('esc')
    #wait里也可以设置按键，说明当按到该键时结束


	#'''
    

'''
def test_a():   
    print('aaa')

def test(x):
    print(x)

if __name__ == '__main__':
    keyboard.add_hotkey('f1', test_a)
    #按f1输出aaa
    keyboard.add_hotkey('ctrl+alt', test, args=('b',))
    #按ctrl+alt输出b
    keyboard.wait()
    #wait里也可以设置按键，说明当按到该键时结束
    '''