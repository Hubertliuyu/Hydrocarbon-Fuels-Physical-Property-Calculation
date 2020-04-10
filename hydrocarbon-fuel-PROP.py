
from tkinter import *
from tkinter.scrolledtext import ScrolledText

from math import sqrt,log
import CoolProp.CoolProp as CP
fluid = 'n-Decane'

root = Tk()

root.minsize(500,400)
root.title("碳氢燃料物理性质计算")




def cal_den():

    global denH
    global denPR
    denH = CP.PropsSI('D','T', Temp,'P', pres, fluid)
    denPR= CP.PropsSI('D','T', Temp,'P', pres, 'PR::n-Decane')

    if Temp<=675:
        contents.insert(INSERT, '碳氢燃料密度为')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, denH)
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, 'Kg/m3')
    if Temp>675 and Temp<710:
        contents.insert(INSERT, '碳氢燃料密度为')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, denPR)
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, 'Kg/m3')
    if Temp>710:
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '超过热裂解温度，燃料开始发生裂解')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '碳氢燃料密度为')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, denPR)
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, 'Kg/m3')

    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')

def cal_cp():

    global cpH
    global cpPR
    cpH = CP.PropsSI('CPMASS','T', Temp,'P', pres, fluid)
    cpPR= CP.PropsSI('CPMASS','T', Temp,'P', pres, 'PR::n-Decane')

    if Temp<=675:
        contents.insert(INSERT, '碳氢燃料定压比热容为')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, cpH)
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, 'J/Kg/K')
    if Temp > 675 and Temp < 710:
        contents.insert(INSERT, '碳氢燃料定压比热容为')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, cpPR)
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, 'J/Kg/K')
    if Temp>710:
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '超过热裂解温度，燃料开始发生裂解')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '碳氢燃料定压比热容为')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, cpPR)
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, '\n')
        contents.insert(INSERT, 'Kg/m3')

    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')





def cal_vis():

    Tc = 617.7
    pc = 2.103e6
    w = 0.4884
    R = 8.314
    M = 0.1423
    na = 6.022e23
    kb = 1.3806505e-23
    ek = 270.1
    sigma = 6.42e-10
    pie = 3.1415926
    Tstar = Temp / ek
    lnTstar = log(Tstar)
    omega22 = 0.298 * lnTstar * lnTstar - 0.8059 * lnTstar + 1.593
    vis0 = (5 / 16 / (sigma * sigma)) * (sqrt((M / na) * kb * Temp / pie)) / omega22
    Tr = Temp / Tc
    kappa = 0.37464 + 1.54226 * w - 0.26992 * w * w
    alpha = (1 + kappa * (1 - sqrt(Tr))) * (1 + kappa * (1 - sqrt(Tr)))
    aTc = 0.45724 * R * R * Tc * Tc / pc
    a = alpha * aTc
    b = 0.0778 * R * Tc / pc
    u = -kappa * a / sqrt(Temp * Tc * alpha)
    volHm = M/denH
    bpg = (volHm / R) * (R / (volHm - b) - u / (volHm * (volHm + b) + b * (volHm - b))) - 1
    bp = (1 / volHm) * (b - u / R)
    Avis = -0.0003 * bpg * bpg - 0.656 * bpg + 2.8741
    vis = bp * vis0 * ((1 / bpg) + Avis + 0.7614 * bpg)

    contents.insert(INSERT, '碳氢燃料粘度为')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, vis)
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, 'Pa*s')

    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')



def cal_thermcond():

    Tc = 617.7
    pc = 2.103e6
    w = 0.4884
    R = 8.314
    M = 0.1423
    na = 6.022e23
    kb = 1.3806505e-23
    ek = 270.1
    sigma = 6.42e-10
    pie = 3.1415926
    Tstar = Temp / ek
    lnTstar = log(Tstar)
    omega22 = 0.298 * lnTstar * lnTstar - 0.8059 * lnTstar + 1.593
    vis0 = (5 / 16 / (sigma * sigma)) * (sqrt((M / na) * kb * Temp / pie)) / omega22
    thermcond0 = 2.5 * vis0 * 1.5 * R / M
    Tr = Temp / Tc
    kappa = 0.37464 + 1.54226 * w - 0.26992 * w * w
    alpha = (1 + kappa * (1 - sqrt(Tr))) * (1 + kappa * (1 - sqrt(Tr)))
    aTc = 0.45724 * R * R * Tc * Tc / pc
    a = alpha * aTc
    b = 0.0778 * R * Tc / pc
    u = -kappa * a / sqrt(Temp * Tc * alpha)
    volHm = M/denH
    bpg = (volHm / R) * (R / (volHm - b) - u / (volHm * (volHm + b) + b * (volHm - b))) - 1
    bp = (1 / volHm) * (b - u / R)
    Athermcond = -0.7325 * bpg + 4.6443
    thermcond = bp * thermcond0 * ((1 / bpg) + Athermcond + 0.755 * bpg)


    contents.insert(INSERT, '碳氢燃料导热系数为')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, thermcond)
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, 'W/m/K')

    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')


def enter_click01(event):
    global Temp
    p=float(x_entry01.get())
    Temp=p
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '温度值   ')
    contents.insert(INSERT, Temp)
    contents.insert(INSERT, ' K  加载成功')
    contents.insert(INSERT, '\n')

def enter_click02(event):
    global pres
    q=float(x_entry02.get())
    pres=q*1e6
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '压力值   ')
    contents.insert(INSERT, q)
    contents.insert(INSERT, ' MPa  加载成功')
    contents.insert(INSERT, '\n')
    contents.insert(INSERT, '----------------------------')
    contents.insert(INSERT, '\n')


def quit():
    sys.exit()



label01 = Label(root,text="K").place(x = '120',y='60',width = '80',height='30')

Button(text='密度计算',bg='DarkGray',command=cal_den).place(x = '40',y='110',width = '90',height='30')
Button(text='比热容计算',bg='DarkGray',command=cal_cp).place(x = '150',y='110',width = '90',height='30')
Button(text='粘度计算',bg='DarkGray',command=cal_vis).place(x = '250',y='110',width = '90',height='30')
Button(text='热导率计算',bg='DarkGray',command=cal_thermcond).place(x = '350',y='110',width = '90',height='30')
label02 = Label(root,text="MPa").place(x = '420',y='60',width = '80',height='30')



x_entry01= Entry(root)
x_entry01.place(x = '40',y='60',width = '100',height='30')
enter_button01 = Button(root,bg='DarkGray', text="加载温度值")
enter_button01.place(x = '40',y='30',width = '100',height='30')
enter_button01.bind("<Button-1>", enter_click01)
enter_button01.bind("<Return>", enter_click01)


x_entry02= Entry(root)
x_entry02.place(x = '340',y='60',width = '100',height='30')
enter_button02 = Button(root,bg='DarkGray', text="加载压力值")
enter_button02.place(x = '340',y='30',width = '100',height='30')
enter_button02.bind("<Button-1>", enter_click02)
enter_button02.bind("<Return>", enter_click02)



contents = ScrolledText()
contents.place(x = '5',y='150',width = '480',height='200')


Button(text='退出系统',bg='DarkGray', command=quit).place(x = '200',y='360',width = '80',height='30')


mainloop()