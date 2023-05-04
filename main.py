# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:33:54 2022

@author: DELL
"""
#%% 分三段
import pandas as pd
import xarray as xr
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

for i in range(6):
    
    
    w = pd.read_excel(r"C:\Users\DELL\Desktop\耕地GPPNEE.xlsx",sheet_name=i)
        
    x = w.iloc[:,1]
    
    IAV = w.iloc[:,3]
    
    
    #### slope computing ####
    turn_point11 = 8
    turn_point22 = 19
    turn_point33 = 32
    
    x1 = x[:turn_point11]
    x2 = x[turn_point11:turn_point22]
    x3 = x[turn_point22:turn_point33]
    
    turn_point1 = np.argmax(x1)
    turn_point2 = np.argmax(x2)+turn_point11
    turn_point3 = np.argmax(x3)+turn_point22
    
    
    
    xx1 = x[:turn_point11]
    y_ndvi = IAV[:turn_point11]
    
    DATA = pd.concat([xx1,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA.columns = ['x1','y_ndvi']
    x1 = DATA.x1
    y_ndvi = DATA.y_ndvi
    
    slope1, c1, r_value, p1_value, std_err = stats.linregress(x1, y_ndvi)
    # print(p1_value)
    # print(slope1)
    
    xx2 = x[turn_point11:turn_point22]
    y_ndvi = IAV[turn_point11:turn_point22]
    
    DATA = pd.concat([xx2,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA.columns = ['x2','y_ndvi']
    x2 = DATA.x2
    y_ndvi = DATA.y_ndvi
    
    slope2, c2, r_value, p2_value, std_err = stats.linregress(x2, y_ndvi)
    # print(p2_value)
    # print(slope2)
    
    xx3 = x[turn_point22:turn_point33]
    y_ndvi = IAV[turn_point22:turn_point33]
    
    DATA = pd.concat([xx3,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA.columns = ['x3','y_ndvi']
    x3 = DATA.x3
    y_ndvi = DATA.y_ndvi
    
    
    slope3, c3, r_value, p3_value, std_err = stats.linregress(x3, y_ndvi)
    # print(p3_value)
    # print(slope3)
    
    
    #### graph
    from matplotlib import rcParams
    
    config = {
            "font.family": 'Times new roman',
            "font.size"  : 18,
            "font.serif" : ['SimSun'],
            "mathtext.fontset" : 'stix',
            "axes.unicode_minus": False
                
                }
    
    rcParams.update(config)
    
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    
    # x = np.arange(1982,2014,1)
    
    y = IAV
    
    fig = plt.figure(figsize=(20,10), dpi=200)
    
    ax = fig.add_subplot(111)
    
    # ax.plot(x, y, marker='o', alpha = 0.7, markersize=20, markerfacecolor= 'g', linewidth=3, color='g', linestyle='-', label='$\mathrm{Interannual}$ $\mathrm{variation}$ $\mathrm{of}$ $\mathrm{NEE}$')
    ax.scatter(w.iloc[:turn_point11,1], w.iloc[:turn_point11,2], marker='o', alpha = 0.7,s=500)
    ax.scatter(w.iloc[turn_point11:turn_point22,1], w.iloc[turn_point11:turn_point22,2], marker='v', alpha = 0.7,s=500)
    ax.scatter(w.iloc[turn_point22:turn_point33,1], w.iloc[turn_point22:turn_point33,2], marker='d', alpha = 0.7,s=500)

    
    ax.plot(x1, slope1 * x1 + c1, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    ax.plot(x2, slope2 * x2 + c2, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    ax.plot(x3, slope3 * x3 + c3, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    
    # ax.scatter(x, y, s=area, alpha=0.5)  # 绘制散点图，面积随机
    
    # plt.grid(alpha=0.6)
    
    # plt.xticks(range(1982,2014,5),fontsize = 24)
    plt.yticks(fontsize = 24)
    
    
    plt.xlabel('$\mathrm{rate}$',fontsize = 32, labelpad=15)
    
    # plt.ylabel('$\mathrm{NEE(gC/m^2/year)}$',fontsize = 32, labelpad=15)
    plt.ylabel('$\mathrm{GPP(gC/m^2/year)}$',fontsize = 32, labelpad=15)
    
    plt.legend(fontsize=24, loc=4, bbox_to_anchor=(0.95,0.09),ncol=1,fancybox=True,shadow=False,frameon=False)
    
    # plt.axvline(1989,c='k',ls='-.',lw=3)
    
    # plt.axvline(2002,c='k',ls='-.',lw=3)
    
    # plt.fill_between(np.arange(1980,1990), 73,83,facecolor='lightyellow', alpha=0.4)
    # plt.fill_between(np.arange(1989,2003), 73,83,facecolor='lightgray', alpha=0.4)
    # plt.fill_between(np.arange(2002,2021), 73,83,facecolor='wheat', alpha=0.4)
    
    
    # plt.xlim(5,30)
    # plt.ylim(73,83)
#%% 分两段 y1 y2 反推
import pandas as pd
import xarray as xr
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


for i in range(6):
    
    
    # w = pd.read_excel(r"C:\Users\DELL\Desktop\耕地GPPNEE.xlsx",sheet_name=i)
    w = pd.read_excel(r"C:\Users\DELL\Desktop\7.9  耕地GPPNEE.xlsx",sheet_name=i)

    
    
    
    x = w.iloc[:,1]
    
    IAV = w.iloc[:,3]
    
    
    #### slope computing ####
    turn_point11 = 18
    # turn_point22 = 19
    turn_point33 = 31
    
    x1 = x[:turn_point11]
    # x2 = x[turn_point11:turn_point22]
    x3 = x[turn_point11:turn_point33]
    
    turn_point1 = np.argmax(x1)
    # turn_point2 = np.argmax(x2)+turn_point11
    turn_point3 = np.argmax(x3)+turn_point11
    
    
    
    xx1 = x[:turn_point11]
    y_ndvi = IAV[:turn_point11]
    
    DATA = pd.concat([xx1,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA.columns = ['x1','y_ndvi']
    x1 = DATA.x1
    y_ndvi = DATA.y_ndvi
    
    slope1, c1, r_value, p1_value, std_err = stats.linregress(x1, y_ndvi)
    # print(p1_value)
    # print(slope1)
    
    # xx2 = x[turn_point11:turn_point2]
    # y_ndvi = IAV[turn_point11:turn_point2]
    
    # DATA = pd.concat([xx2,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    # DATA.columns = ['x2','y_ndvi']
    # x2 = DATA.x2
    # y_ndvi = DATA.y_ndvi
    
    # slope2, c2, r_value, p2_value, std_err = stats.linregress(x2, y_ndvi)
    # # print(p2_value)
    # # print(slope2)
    
    xx3 = x[turn_point11:turn_point33]
    y_ndvi = IAV[turn_point11:turn_point33]
    
    DATA = pd.concat([xx3,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA.columns = ['x3','y_ndvi']
    x3 = DATA.x3
    y_ndvi = DATA.y_ndvi
    
    
    slope3, c3, r_value, p3_value, std_err = stats.linregress(x3, y_ndvi)
    # print(p3_value)
    # print(slope3)
    
    
    #### graph
    from matplotlib import rcParams
    
    config = {
            "font.family": 'Times new roman',
            "font.size"  : 18,
            "font.serif" : ['SimSun'],
            "mathtext.fontset" : 'stix',
            "axes.unicode_minus": False
                
                }
    
    rcParams.update(config)
    
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    
    # x = np.arange(1982,2014,1)
    
    y = IAV
    
    fig = plt.figure(figsize=(20,10), dpi=200)
    
    ax = fig.add_subplot(111)
    
    # ax.plot(x, y, marker='o', alpha = 0.7, markersize=20, markerfacecolor= 'g', linewidth=3, color='g', linestyle='-', label='$\mathrm{Interannual}$ $\mathrm{variation}$ $\mathrm{of}$ $\mathrm{NEE}$')
    ax.scatter(w.iloc[:turn_point11,1], w.iloc[:turn_point11,2], marker='o', alpha = 0.7,s=500)
    # ax.scatter(w.iloc[turn_point11:turn_point22,1], w.iloc[turn_point11:turn_point22,2], marker='v', alpha = 0.7,s=500)
    ax.scatter(w.iloc[turn_point11:turn_point33,1], w.iloc[turn_point11:turn_point33,2], marker='d', alpha = 0.7,s=500)

    
    ax.plot(x1, slope1 * x1 + c1, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    # ax.plot(x2, slope2 * x2 + c2, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    ax.plot(x3, slope3 * x3 + c3, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    
    # ax.scatter(x, y, s=area, alpha=0.5)  # 绘制散点图，面积随机
    
    # plt.grid(alpha=0.6)
    
    # plt.xticks(range(1982,2014,5),fontsize = 24)
    plt.yticks(fontsize = 24)
    
    
    plt.xlabel('$\mathrm{rate}$',fontsize = 32, labelpad=15)
    
    # plt.ylabel('$\mathrm{NEE(gC/m^2/year)}$',fontsize = 32, labelpad=15)
    plt.ylabel('$\mathrm{GPP(gC/m^2/year)}$',fontsize = 32, labelpad=15)
    
    plt.legend(fontsize=24, loc=4, bbox_to_anchor=(0.95,0.09),ncol=1,fancybox=True,shadow=False,frameon=False)
    
    # plt.axvline(1989,c='k',ls='-.',lw=3)
    
    # plt.axvline(2002,c='k',ls='-.',lw=3)
    
    # plt.fill_between(np.arange(1980,1990), 73,83,facecolor='lightyellow', alpha=0.4)
    # plt.fill_between(np.arange(1989,2003), 73,83,facecolor='lightgray', alpha=0.4)
    # plt.fill_between(np.arange(2002,2021), 73,83,facecolor='wheat', alpha=0.4)
    
    
    # plt.xlim(5,30)
    # plt.ylim(73,83)


#%%分两段 趋势 ***这个部分***

import pandas as pd
import xarray as xr
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


for i in range(3):
    
    string = ['$\mathrm{GPP-ANN(gC/m^2/year)}$','$\mathrm{GPP-MARS(gC/m^2/year)}$','$\mathrm{GPP-RF(gC/m^2/year)}$']
    
    y_lim=([6,17],[8,19],[11,25])
        
    
    # w = pd.read_excel(r"C:\Users\DELL\Desktop\耕地GPPNEE.xlsx",sheet_name=i)
    
    w = pd.read_excel(r"C:\Users\DELL\Desktop\7.9  耕地GPPNEE.xlsx",sheet_name=i)
    
    
    
    x = w.iloc[:,1]
    
    IAV = w.iloc[:,2]
    
    
    #### slope computing ####
    turn_point11 = 18
    # turn_point22 = 19
    turn_point33 = 31
    
    # x1 = x[:turn_point11]
    # # x2 = x[turn_point11:turn_point22]
    # x3 = x[turn_point11:turn_point33]
    
    # turn_point1 = np.argmax(x1)
    # # turn_point2 = np.argmax(x2)+turn_point11
    # turn_point3 = np.argmax(x3)+turn_point11
    
    
    
    xx1 = x[:turn_point11]
    y_ndvi = IAV[:turn_point11]
    
    DATA1 = pd.concat([xx1,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA1.columns = ['x1','y_ndvi']
    x1 = DATA1.x1
    y_ndvi = DATA1.y_ndvi
    
    slope1, c1, r_value, p1_value, std_err = stats.linregress(x1, y_ndvi)
    print(p1_value)
    # print(slope1)
    
    # xx2 = x[turn_point11:turn_point2]
    # y_ndvi = IAV[turn_point11:turn_point2]
    
    # DATA = pd.concat([xx2,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    # DATA.columns = ['x2','y_ndvi']
    # x2 = DATA.x2
    # y_ndvi = DATA.y_ndvi
    
    # slope2, c2, r_value, p2_value, std_err = stats.linregress(x2, y_ndvi)
    # # print(p2_value)
    # # print(slope2)
    
    xx3 = x[turn_point11:turn_point33]
    y_ndvi = IAV[turn_point11:turn_point33]
    
    DATA3 = pd.concat([xx3,y_ndvi],axis=1,ignore_index=True).sort_values(by=0,axis=0,ascending=True)
    DATA3.columns = ['x3','y_ndvi']
    x3 = DATA3.x3
    y_ndvi = DATA3.y_ndvi
    
    
    slope3, c3, r_value, p3_value, std_err = stats.linregress(x3, y_ndvi)
    print(p3_value)
    # print(slope3)
    
    
    #### graph
    from matplotlib import rcParams
    
    config = {
            "font.family": 'Times new roman',
            "font.size"  : 18,
            "font.serif" : ['SimSun'],
            "mathtext.fontset" : 'stix',
            "axes.unicode_minus": False
                
                }
    
    rcParams.update(config)
    
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    
    # x = np.arange(1982,2014,1)
    
    y = IAV
    
    fig = plt.figure(figsize=(20,10), dpi=200)
    
    ax = fig.add_subplot(111)
    
    # ax.plot(x, y, marker='o', alpha = 0.7, markersize=20, markerfacecolor= 'g', linewidth=3, color='g', linestyle='-', label='$\mathrm{Interannual}$ $\mathrm{variation}$ $\mathrm{of}$ $\mathrm{NEE}$')
    ax.scatter(w.iloc[:turn_point11,1], w.iloc[:turn_point11,2], marker='o', alpha = 0.7,s=500)
    # ax.scatter(w.iloc[turn_point11:turn_point22,1], w.iloc[turn_point11:turn_point22,2], marker='v', alpha = 0.7,s=500)
    ax.scatter(w.iloc[turn_point11:turn_point33,1], w.iloc[turn_point11:turn_point33,2], marker='d', alpha = 0.7,s=500)

    
    ax.plot(x1, slope1 * x1 + c1, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    # ax.plot(x2, slope2 * x2 + c2, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    ax.plot(x3, slope3 * x3 + c3, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
    
    # ax.scatter(x, y, s=area, alpha=0.5)  # 绘制散点图，面积随机
    sns.regplot(x='x1', y='y_ndvi',  ci=95, data=DATA1, ax=ax, line_kws={'color':'b','alpha':0}, scatter_kws={'s':500,'alpha':0.6,'color':'g'})
    sns.regplot(x='x3', y='y_ndvi',  ci=95, data=DATA3, ax=ax, line_kws={'alpha':0},marker='d',scatter=False,scatter_kws={'s':500,'alpha':0.6})

    # plt.grid(alpha=0.6)
    
    # plt.xticks(range(1982,2014,5),fontsize = 24)
    plt.yticks(fontsize = 24)
    plt.xticks(fontsize = 24)

    
    plt.xlabel('Percentage of cultivated land/%',fontsize = 32, labelpad=15)
    
    # plt.ylabel('$\mathrm{NEE(gC/m^2/year)}$',fontsize = 32, labelpad=15)
    plt.ylabel(string[i],fontsize = 32, labelpad=15)
    
    plt.legend(fontsize=24, loc=4, bbox_to_anchor=(0.95,0.09),ncol=1,fancybox=True,shadow=False,frameon=False)
    
    plt.axvline(xx1[np.argmax(xx1)],c='k',ls='-.',lw=2)
    upper = xx1[np.argmax(xx1)]
    plt.axvline(xx3.iloc[np.argmin(xx3)],c='k',ls='-.',lw=2)
    below = xx3.iloc[np.argmin(xx3)]
    plt.fill_between([0,upper],y_lim[i][0],y_lim[i][1],facecolor='lightyellow', alpha=0.4)
    plt.fill_between([below,20], y_lim[i][0],y_lim[i][1],facecolor='lightgray', alpha=0.4)
    
    
    plt.xlim(8.4,18.2)
    plt.ylim(y_lim[i])

    # plt.text(.04,.26,'$\it{p}=$'+str(round(p1_value,4)), fontsize=30, transform=ax.transAxes)
    # plt.text(.7,.56,'$\it{p}=$'+str(round(p3_value,4)), fontsize=30, transform=ax.transAxes)
