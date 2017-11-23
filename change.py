# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:54:42 2017

@author: 吴聪
"""

import os 
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

'''#xml--->csv'''
def xml_csv(path,save_path):
    os.chdir(save_path)
    #open and read file.xml
    soup=BeautifulSoup(open(path,'r',encoding='utf-8'),'xml')
    #get attribution and text
    ref_table=[]
    for item in soup.find_all('string'):
        ref_table.append([item.get('name'),item.get_text()])
    #exchange into dataframe     
    ref_table=pd.DataFrame(ref_table,columns=['code_str','name_str'])
    #output to csv
    ref_table.to_excel(str(path)+'ref_table.xlsx',index=False)
    notification()

'''#csv--->xml'''
def excel2xml(path,ref_path,save_path):
    os.chdir(save_path)
    soup=BeautifulSoup(open(path,'r',encoding='utf-8'),'xml')
    if(ref_path.split('.')[-1])=='xlsx':
        ref_table=pd.read_excel(ref_path)
    elif(ref_path.split('.')[-1])=='csv':
        ref_table=pd.read_csv(ref_path,encoding='gbk')
    tg_str=ref_table.columns[2]
    n =ref_table.shape[0]
    for i in range(n):
        target_str=ref_table['code_str'][i]
        for item in soup.find_all('string',attrs={'name':target_str}):
            item.string=str(ref_table[tg_str][i])
    print(soup)
    with open(path,'w',encoding='utf-8') as f:
        #f.write(soup.prettify())     
        f.write(str(soup))
    notification()
    
#辅助函数
def notification():
    messagebox.showinfo(title='nofification',message='completed')
def choose1():
    excel_path=filedialog.askopenfilename()
    v1.set(excel_path)
    
def choose2():
    xml_path=filedialog.askopenfilename()
    v2.set(xml_path)
    
def choose3():
    save_path=filedialog.askdirectory()
    v3.set(save_path)

if __name__=="__main__":
    root =Tk()
    root.title('excel_xml exchange')
    Label(root,text='excel_name').grid(row=0,column=0)
    Label(root,text='xml_name').grid(row=1,column=0)
    Label(root,text='save_path').grid(row=2,column=0)
    
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    
    excel_path=Entry(root,textvariable=v1)
    xml_path=Entry(root,textvariable=v2)
    save_path=Entry(root,textvariable=v3)
    excel_path.grid(row=0,column=1,padx=15,pady=5)
    xml_path.grid(row=1,column=1,padx=15,pady=5)
    save_path.grid(row=2,column=1,padx=15,pady=5)

    Button(root,text='choose',width=10,command=choose1).grid(row=0,column=2)
    Button(root,text='choose',width=10,command=choose2).grid(row=1,column=2)
    Button(root,text='choose',width=10,command=choose3).grid(row=2,column=2)
    Button(root,text='xml->excel',width=10,command=lambda : xml_csv(xml_path.get(),save_path.get())).grid(row=3,column=0,pady=5)
    Button(root,text='excel->xml',width=10,command=lambda :excel2xml(xml_path.get(),excel_path.get(),save_path.get())).grid(row=3,column=1,sticky=W,pady=5)
    Button(root,text='exit',command=root.quit).grid(row=3,column=2,sticky=E,padx=10,pady=5)
    
    mainloop()
    root.destroy()
    