import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import font
from tkinter import colorchooser
import tkinter.scrolledtext as tkst
from tkinter import *
import fileinput
import docx
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx import *
import threading
import time
import os
import random
t1 = []
root = None



path = ""
document = Document()


def thread_it(func, *args):
  t = threading.Thread(target=func, args=args)
  t.setDaemon(True)
  t.start()
  
def about():
  messagebox.showinfo(title = "版本",message = "** 版本:0.0.3 Release **")
  messagebox.showinfo(title = "作者",message = "** 作者:Tony **")
  messagebox.showinfo(title = "版权",message = "** 版权所有:Stack_Overflow **")

def caution(): 
  messagebox.showinfo(title = "注意事项",message = "** 本软件中的字体与颜色无法保存 **")
  messagebox.showinfo(title = "注意事项",message = "** 建议使用软件自带的退出功能，或使用Esc键退出 **")

class editor():
  def __init__(self,rt):
    if rt == None:
      self.tk = tk.Tk()
    else:
      self.tk = tk.Toplevel(rt)
    self.tk.title("文本编辑器")


 

    self.bar = tk.Menu(rt)
    self.filemenu = tk.Menu(self.bar)
    self.filemenu.add_command(label = "新建",command = lambda:thread_it(self.new),accelerator = "     Ctrl + N")
    self.filemenu.bind_all("<Control-n>",self.new)
    self.filemenu.add_command(label = "打开",command = lambda:thread_it(self.openfile1),accelerator = "     Ctrl + O")
    self.filemenu.bind_all("<Control-o>",self.openfile1)
    self.filemenu.add_command(label = "保存",command = lambda:thread_it(self.savefile1),accelerator = "     Ctrl + S ")
    self.filemenu.bind_all("<Control-s>",self.savefile1)
    self.filemenu.add_command(label = "另存为",command = lambda:thread_it(self.saveasfile1),accelerator = "     Ctrl + Shift + S ")
    self.filemenu.bind_all("<Control-Shift-s>",self.saveasfile1)

    self.filemenu.add_command(label = "关闭",command = self.close,accelerator = "     ESC")
    self.filemenu.bind_all("<Escape>",self.close)
    
    self.editmenu = tk.Menu(self.bar)
    self.editmenu.add_command(label = "复制    Ctrl + C",command = self.copy)
    self.editmenu.bind_all(self.copy)
    self.editmenu.add_command(label = "粘贴    Ctrl + V",command = self.paste)
    self.editmenu.bind_all(self.paste)
    self.editmenu.add_command(label = "剪切    Ctrl + X",command = self.cut)
    self.editmenu.bind_all(self.cut)
    self.editmenu.add_command(label = "删除    Del",command = self.delete_text,)
    self.editmenu.bind_all(self.delete_text)
    self.editmenu.add_command(label = "全选    Ctrl + A",command = self.select_all_chars)
    self.editmenu.bind_all("<Control-a>",self.select_all_chars)

    self.formatmenu = tk.Menu(self.bar)
    self.formatmenu.add_command(label = "字体颜色",command = self.change_color,accelerator = "Alt + C")
    self.formatmenu.bind_all("<Alt-c>",self.change_color)
    self.formatmenu.add_command(label = "字体格式",command = self.change_font,accelerator = "Alt + F")
    self.formatmenu.bind_all("<Alt-f>",self.change_font)

    self.helpmenu = tk.Menu(self.bar)
    self.helpmenu.add_command(label = "关于",command = about)
    self.helpmenu.add_command(label = "注意事项",command = caution)

    self.bar.add_cascade(label = "文件",menu = self.filemenu)
    self.bar.add_cascade(label = "编辑",menu = self.editmenu)
    self.bar.add_cascade(label = "格式",menu = self.formatmenu)
    self.bar.add_cascade(label = "帮助",menu = self.helpmenu)
    
    self.tk.config(menu = self.bar)

    self.st = tkst.ScrolledText(self.tk)
    self.st.pack(expand=1,fill=tk.BOTH)



  def close(self,event = None):
    """
    try:
      with open(path,"r") as content:
        if (path!="") and (self.st.get(1.0,tk.END)==content.read()):
          ask_save = tk.messagebox.askokcancel("保存?","是否保存文件?")
          if ask_save==True:
            exitsavefile1_ = open(path,"w")
            exitsavefile1_.write(self.st.get(1.0,tk.END))
            exitsavefile1_.flush()
            exitsavefile1_.close()
          else:
            pass
        else:
          pass
    except FileNotFoundError:
      pass
    """
    self.tk.destroy()
    
  def openfile1(self,event = None):
    global path
    path = filedialog.askopenfilename(filetypes = [("打开文件","*.txt")])
    if path:
      for line in fileinput.input(path):
        self.st.delete(1.0,tk.END)
        self.st.insert("1.0",line)
      self.tk.title(path)
      

  def savefile1(self,event = None):
    if os.path.isfile(self.tk.title()):
      savefile1_ = open(self.tk.title(),"w")
      savefile1_.write(self.st.get(1.0,tk.END))
      savefile1_.flush()
      savefile1_.close()
    else:
      path = filedialog.asksaveasfilename(title = "另存为...",filetypes = [("保存文件","*.txt")],defaultextension = ".txt")
      if path:
        savefile1_ = open(savename,"w")
        savefile1_.write(self.st.get(1.0,tk.END))
        savefile1_.flush()
        savefile1_.close()
        self.tk.title(path)
      
  def saveasfile1(self,event = None):
    global path
    path = filedialog.asksaveasfilename(title = "另存为...",filetypes = [("保存文件","*.txt")],defaultextension = ".txt")
    if path:
     saveasfile1_ = open(saveasname,"w")
     saveasfile1_.write(self.st.get(1.0,tk.END))
     saveasfile1_.flush()
     saveasfile1_.close()
     self.tk.title(path)
    
  def new(self,event = None):
    global root
    t1.append(editor(root))


  def copy(self,event = None):
    text = self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
    self.st.clipboard_append(text)

  def paste(self,event = None):
    try:
      text = self.st.selection_get(selection = "CLIPBOARD")
      self.st.insert(tk.INSERT,text)
    except tk.TclError:
      pass
    
  def cut(self,event = None):
    text = self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
    self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
    self.st.clipboard_append(text)
    
  def delete_text(self):
    self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
                
  def select_all_chars(self,event = None):
    self.st.tag_add(tk.SEL,1.0,tk.END)
    self.st.see(tk.INSERT)
    self.st.focus()
    
  def change_color(self,event = None):
    color = colorchooser.askcolor()
    self.st["foreground"] = color[1]
    
  def change_font(self,event = None):
    self.tk_font = tk.Toplevel()
    self.tk_font.title("字体选择面板")
    self.label_size = Label(self.tk_font,text = "字体大小")
    self.label_shape = Label(self.tk_font,text = "字体形状")
    self.label_font = Label(self.tk_font,text = "字体类型")
    self.label_weight = Label(self.tk_font,text = "字体粗细")
    self.label_size.grid(row=0 ,column=0,padx=30)
    self.label_shape.grid(row=0,column=4,padx=30)
    self.label_font.grid(row=0,column=2,padx=30)
    self.label_weight.grid(row=0,column=6,padx=30)
    
    self.scroll_size = Scrollbar(self.tk_font)
    self.scroll_size.grid(row=1,column=1,stick=NS)
    self.scroll_shape = Scrollbar(self.tk_font)
    self.scroll_shape.grid(row=1,column=3,stick=NS)
    self.scroll_font = Scrollbar(self.tk_font)
    self.scroll_font.grid(row=1,column=5,stick=NS)
    self.scroll_weight = Scrollbar(self.tk_font)
    self.scroll_weight.grid(row=1,column=7,stick=NS)

    list_var_font = StringVar()
    list_var_size = StringVar()
    list_var_shape = StringVar()
    list_var_weight = StringVar()
    
    self.list_font = Listbox(self.tk_font,selectmode = BROWSE,listvariable = list_var_font,exportselection = 0)
    self.list_font.grid(row=1,column=2,padx=4)
    list_font_item = ["\"Arial\"","\"Arial Baltic\"","\"Arial Black\"","\"Arial CE\"","\"Arial CYR\"","\"Arial Greek\"","\"Arial Narrow\"",
             "\"Arial TUR\"","\"Baiduan Number\"","\"Batang,BatangChe\""]
    for item in list_font_item:
      self.list_font.insert(0,item)
    self.list_font.bind("<ButtonRelease-1>",self.change_font_)

    self.list_shape = Listbox(self.tk_font,selectmode = BROWSE,listvariable =list_var_shape,exportselection = 0 )
    self.list_shape.grid(row=1,column=4,padx=4)
    list_shape_item = ["italic","roman"]
    for item in list_shape_item:
      self.list_shape.insert(0,item)
    self.list_shape.bind("<ButtonRelease-1>",self.change_shape)

    self.list_size = Listbox(self.tk_font,selectmode = BROWSE,listvariable = list_var_size,exportselection = 0)
    self.list_size.grid(row=1,column=0,padx=4)
    list_size_item = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    for item in list_size_item :
      self.list_size.insert(0,item)
    self.list_size.bind("<ButtonRelease-1>",self.change_size)
    
    self.list_weight = Listbox(self.tk_font,selectmode = BROWSE,listvariable = list_var_weight,exportselection = 0)
    self.list_weight.grid(row=1,column=6,padx=4)
    list_weight_item = ["bold","normal"]
    for item in list_weight_item:
      self.list_weight.insert(0,item)
    self.list_weight.bind("<ButtonRelease-1>",self.change_weight)
    
    self.labFra_display = LabelFrame(self.tk_font,text = "字体样式演示区域")
    self.labFra_display.grid(row=2,column=0,pady=4)
    self.lab_display = Label(self.labFra_display,text = "文本编辑器")
    self.lab_display.pack()

    self.btn_ok = Button(self.tk_font,text = "确定",width=10,height=2,command=self.change)
    self.btn_ok.grid(row=2,column=2,pady=4)
    self.btn_cancel = Button(self.tk_font,width=10,height=2,text = "取消",command=self.exit_fontwindow)
    self.btn_cancel.grid(row=2,column=4,pady=4)
    
  def change_size(self,event):
    tk.customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline = 0)
    size = tk.customFont["size"]
    tk.customFont.configure(size =self.list_size.get(self.list_size.curselection()))
    self.st.config(font = tk.customFont)
    self.size_count=1
    pass
      
  def change_font_(self,event = None):
    tk.customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline = 0)
    family = tk.customFont["family"]
    tk.customFont.configure(family =self.list_font.get(self.list_font.curselection()))
    self.st.config(font = tk.customFont)
    self.font_count=1
    pass

  def change_shape(self,event):
    tk.customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline =0)
    slant = tk.customFont["slant"]
    tk.customFont.configure(slant =self.list_shape.get(self.list_shape.curselection()))
    self.st.config(font = tk.customFont)
    self.shape_count=1
    pass
  
  def change_weight(self,event):
    tk.customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline =0)
    weight = tk.customFont["weight"]
    tk.customFont.configure(weight =self.list_weight.get(self.list_weight.curselection()))
    self.st.config(font = tk.customFont)
    self.shape_count=1
    
  def change(self):
    pass
  
  def exit_fontwindow(self,event = None):
    self.tk_font.destroy()


    
    
if __name__ == "__main__":
  root = None
  t1.append(editor(root))
  root = t1[0].tk
  root.mainloop()
