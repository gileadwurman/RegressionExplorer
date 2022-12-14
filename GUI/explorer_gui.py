#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Nov 07, 2022 07:31:11 PM PST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import explorer_gui_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _ana2color)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.map('TRadiobutton',background =
           [('selected', _bgcolor), ('active', _ana2color)], indicatorcolor =
           [('selected', _fgcolor), ('!active', _bgcolor)])
    _style_code_ran = 1

class MainWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1020x691+363+124")
        top.minsize(120, 1)
        top.maxsize(1924, 1041)
        top.resizable(1,  1)
        top.title("Regression Explorer")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.header_list = tk.StringVar()

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(command=explorer_gui_support.import_window
                ,label='Import...')
        self.sub_menu = tk.Menu(top, activebackground='beige', activeborderwidth=1
                ,activeforeground='black', background='#d9d9d9', borderwidth=1
                ,disabledforeground='#a3a3a3', foreground='#000000', tearoff=0)
        self.menubar.add_cascade(label='DataFrame',menu=self.sub_menu,)
        self.sub_menu.add_command(command=explorer_gui_support.menu_df_info
                ,label='Info')
        self.sub_menu.add_command(command=explorer_gui_support.menu_df_describe
                ,label='Describe')
        self.sub_menu.add_command(command=explorer_gui_support.menu_df_dropna
                ,label='Drop NA')

        _style_code()
        self.TabGroup = ttk.Notebook(self.top)
        self.TabGroup.place(relx=0.0, rely=0.0, relheight=0.999, relwidth=1.001)
        self.TabGroup.configure(takefocus="")
        self.PairPlotTab = tk.Frame(self.TabGroup)
        self.TabGroup.add(self.PairPlotTab, padding=3)
        self.TabGroup.tab(0, text='''EDA''', compound="left", underline='''-1'''
                ,)
        self.PairPlotTab.configure(background="#d9d9d9")
        self.PairPlotTab.configure(highlightbackground="#d9d9d9")
        self.PairPlotTab.configure(highlightcolor="black")
        self.RegressionTab = tk.Frame(self.TabGroup)
        self.TabGroup.add(self.RegressionTab, padding=3)
        self.TabGroup.tab(1, text='''Regression''', compound="left"
                ,underline='''-1''', )
        self.RegressionTab.configure(background="#d9d9d9")
        self.RegressionTab.configure(highlightbackground="#d9d9d9")
        self.RegressionTab.configure(highlightcolor="black")

        self.PairPlotFrame = tk.Frame(self.PairPlotTab)
        self.PairPlotFrame.place(relx=0.285, rely=0.0, relheight=1.003
                , relwidth=0.717)
        self.PairPlotFrame.configure(relief='groove')
        self.PairPlotFrame.configure(borderwidth="2")
        self.PairPlotFrame.configure(relief="groove")
        self.PairPlotFrame.configure(background="#d9d9d9")
        self.PairPlotFrame.configure(highlightbackground="#d9d9d9")
        self.PairPlotFrame.configure(highlightcolor="black")

        self.LeftPaneGroup = ttk.Panedwindow(self.PairPlotTab, orient="vertical")

        self.LeftPaneGroup.place(relx=0.029, rely=0.044, relheight=0.877
                , relwidth=0.226)
        self.PlotOptionsPane = ttk.Labelframe(self.LeftPaneGroup, height=45
                , text='PairPlot Option')
        self.LeftPaneGroup.add(self.PlotOptionsPane, weight=0)
        self.PlotOptionsPane.configure(text='''PairPlot Option''')
        self.HeaderPane = ttk.Labelframe(self.LeftPaneGroup, text='')
        self.LeftPaneGroup.add(self.HeaderPane, weight=0)
        self.__funcid0 = self.LeftPaneGroup.bind('<Map>', self.__adjust_sash0)

        self.PlotOptionMenu = ttk.Combobox(self.PlotOptionsPane)
        self.PlotOptionMenu.place(relx=0.0, rely=0.444, relheight=0.467
                , relwidth=1.0, bordermode='ignore')
        self.value_list = ['linear','log base 10','natural log','square root','categorical','exclude','index',]
        self.PlotOptionMenu.configure(values=self.value_list)
        self.PlotOptionMenu.configure(textvariable=self.combobox)
        self.PlotOptionMenu.configure(takefocus="")
        self.PlotOptionMenu.bind('<<ComboboxSelected>>',explorer_gui_support.plot_option_changed)

        self.HeaderList = ScrolledListBox(self.HeaderPane)
        self.HeaderList.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0
                , bordermode='ignore')
        self.HeaderList.configure(background="white")
        self.HeaderList.configure(cursor="xterm")
        self.HeaderList.configure(disabledforeground="#a3a3a3")
        self.HeaderList.configure(font="TkFixedFont")
        self.HeaderList.configure(foreground="black")
        self.HeaderList.configure(highlightbackground="#d9d9d9")
        self.HeaderList.configure(highlightcolor="#d9d9d9")
        self.HeaderList.configure(selectbackground="#c4c4c4")
        self.HeaderList.configure(selectforeground="black")
        self.HeaderList.configure(listvariable=self.header_list)
        self.HeaderList.bind('<<ListboxSelect>>',explorer_gui_support.header_select)

        self.PairPlotButton = ttk.Button(self.PairPlotTab)
        self.PairPlotButton.place(relx=0.049, rely=0.934, height=25, width=76)
        self.PairPlotButton.configure(command=explorer_gui_support.create_pairplot)
        self.PairPlotButton.configure(takefocus="")
        self.PairPlotButton.configure(text='''PairPlot''')
        self.PairPlotButton.configure(compound='left')

        self.ClusterMapButton = ttk.Button(self.PairPlotTab)
        self.ClusterMapButton.place(relx=0.138, rely=0.934, height=25, width=76)
        self.ClusterMapButton.configure(command=explorer_gui_support.create_clustermap)
        self.ClusterMapButton.configure(takefocus="")
        self.ClusterMapButton.configure(text='''ClusterMap''')
        self.ClusterMapButton.configure(compound='left')

    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [45, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0

class ImportWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("533x193+716+235")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Import File")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.input_file_str = tk.StringVar()
        self.import_kwargs_str = tk.StringVar()

        _style_code()
        self.InputFileField = ttk.Entry(self.top)
        self.InputFileField.place(relx=0.056, rely=0.207, relheight=0.109
                , relwidth=0.705)
        self.InputFileField.configure(textvariable=self.input_file_str)
        self.InputFileField.configure(validate="focusout")
        validate_input_file = self.InputFileField.register(explorer_gui_support.validate_input_file)
        self.InputFileField.configure(validatecommand=(validate_input_file, '%P'))
        self.InputFileField.configure(takefocus="")
        self.InputFileField.configure(cursor="ibeam")

        self.SelectFileButton = ttk.Button(self.top)
        self.SelectFileButton.place(relx=0.788, rely=0.207, height=25, width=76)
        self.SelectFileButton.configure(command=explorer_gui_support.open_file_chooser)
        self.SelectFileButton.configure(takefocus="")
        self.SelectFileButton.configure(text='''Select''')
        self.SelectFileButton.configure(compound='left')

        self.ImportKwargsField = ttk.Entry(self.top)
        self.ImportKwargsField.place(relx=0.056, rely=0.518, relheight=0.109
                , relwidth=0.874)
        self.ImportKwargsField.configure(textvariable=self.import_kwargs_str)
        self.ImportKwargsField.configure(validate="focusout")
        validate_import_kwargs = self.ImportKwargsField.register(explorer_gui_support.validate_import_kwargs)
        self.ImportKwargsField.configure(validatecommand=(validate_import_kwargs, '%P'))
        self.ImportKwargsField.configure(takefocus="")
        self.ImportKwargsField.configure(cursor="ibeam")

        self.ImportFileLabel = ttk.Label(self.top)
        self.ImportFileLabel.place(relx=0.056, rely=0.052, height=24, width=58)
        self.ImportFileLabel.configure(background="#d9d9d9")
        self.ImportFileLabel.configure(foreground="#000000")
        self.ImportFileLabel.configure(font="TkDefaultFont")
        self.ImportFileLabel.configure(relief="flat")
        self.ImportFileLabel.configure(anchor='w')
        self.ImportFileLabel.configure(justify='left')
        self.ImportFileLabel.configure(text='''Input File:''')
        self.ImportFileLabel.configure(compound='left')

        self.ImportKwargsLabel = ttk.Label(self.top)
        self.ImportKwargsLabel.place(relx=0.056, rely=0.363, height=24, width=84)

        self.ImportKwargsLabel.configure(background="#d9d9d9")
        self.ImportKwargsLabel.configure(foreground="#000000")
        self.ImportKwargsLabel.configure(font="TkDefaultFont")
        self.ImportKwargsLabel.configure(relief="flat")
        self.ImportKwargsLabel.configure(anchor='w')
        self.ImportKwargsLabel.configure(justify='left')
        self.ImportKwargsLabel.configure(text='''Import kwargs:''')
        self.ImportKwargsLabel.configure(compound='left')

        self.ImportButton = ttk.Button(self.top)
        self.ImportButton.place(relx=0.356, rely=0.725, height=25, width=76)
        self.ImportButton.configure(command=explorer_gui_support.import_file)
        self.ImportButton.configure(takefocus="")
        self.ImportButton.configure(text='''Import''')
        self.ImportButton.configure(compound='left')
        self.ImportButton.configure(state='disabled')

        self.CancelButton = ttk.Button(self.top)
        self.CancelButton.place(relx=0.507, rely=0.725, height=25, width=76)
        self.CancelButton.configure(command=explorer_gui_support.import_cancel)
        self.CancelButton.configure(takefocus="")
        self.CancelButton.configure(text='''Cancel''')
        self.CancelButton.configure(compound='left')

class DescDialog:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x233+655+310")
        top.minsize(120, 1)
        top.maxsize(4484, 2326)
        top.resizable(1,  1)
        top.title("DataFrame Descrption")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        _style_code()
        self.DescCloseButton = ttk.Button(self.top)
        self.DescCloseButton.place(relx=0.433, rely=0.871, height=25, width=76)
        self.DescCloseButton.configure(command=explorer_gui_support.close_desc)
        self.DescCloseButton.configure(takefocus="")
        self.DescCloseButton.configure(text='''Close''')
        self.DescCloseButton.configure(compound='left')

        self.DescTextBox = ScrolledText(self.top)
        self.DescTextBox.place(relx=0.0, rely=0.0, relheight=0.85, relwidth=1.0)
        self.DescTextBox.configure(background="#ffffff")
        self.DescTextBox.configure(font="-family {Courier New} -size 11")
        self.DescTextBox.configure(foreground="black")
        self.DescTextBox.configure(highlightbackground="#d9d9d9")
        self.DescTextBox.configure(highlightcolor="black")
        self.DescTextBox.configure(insertbackground="black")
        self.DescTextBox.configure(insertborderwidth="3")
        self.DescTextBox.configure(relief="flat")
        self.DescTextBox.configure(selectbackground="#c4c4c4")
        self.DescTextBox.configure(selectforeground="black")
        self.DescTextBox.configure(state='disabled')
        self.DescTextBox.configure(wrap="none")

class InfoDialog:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("404x450+593+474")
        top.minsize(120, 1)
        top.maxsize(4484, 2326)
        top.resizable(1,  1)
        top.title("DataFrame Info")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        _style_code()
        self.InfoCloseButton = ttk.Button(self.top)
        self.InfoCloseButton.place(relx=0.433, rely=0.92, height=25, width=76)
        self.InfoCloseButton.configure(command=explorer_gui_support.close_info)
        self.InfoCloseButton.configure(takefocus="")
        self.InfoCloseButton.configure(text='''Close''')
        self.InfoCloseButton.configure(compound='left')

        self.InfoTextBox = ScrolledText(self.top)
        self.InfoTextBox.place(relx=0.0, rely=0.0, relheight=0.9, relwidth=1.0)
        self.InfoTextBox.configure(background="#ffffff")
        self.InfoTextBox.configure(font="-family {Courier New} -size 11")
        self.InfoTextBox.configure(foreground="black")
        self.InfoTextBox.configure(highlightbackground="#d9d9d9")
        self.InfoTextBox.configure(highlightcolor="black")
        self.InfoTextBox.configure(insertbackground="black")
        self.InfoTextBox.configure(insertborderwidth="3")
        self.InfoTextBox.configure(relief="flat")
        self.InfoTextBox.configure(selectbackground="#c4c4c4")
        self.InfoTextBox.configure(selectforeground="black")
        self.InfoTextBox.configure(state='disabled')
        self.InfoTextBox.configure(wrap="none")

class DnaDialog:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("822x607+531+125")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Drop NA Values")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.dropna_axis = tk.IntVar()
        self.dropna_how = tk.IntVar()

        _style_code()
        self.DnaAxisFrame = ttk.Frame(self.top)
        self.DnaAxisFrame.place(relx=0.012, rely=0.016, relheight=0.186
                , relwidth=0.208)
        self.DnaAxisFrame.configure(relief='groove')
        self.DnaAxisFrame.configure(borderwidth="2")
        self.DnaAxisFrame.configure(relief="groove")

        self.DnaAxisRadio2 = ttk.Radiobutton(self.DnaAxisFrame)
        self.DnaAxisRadio2.place(relx=0.082, rely=0.531, relwidth=0.83
                , relheight=0.0, height=21)
        self.DnaAxisRadio2.configure(variable=self.dropna_axis)
        self.DnaAxisRadio2.configure(text='''Columns*''')
        self.DnaAxisRadio2.configure(compound='left')

        self.DnaAxisRadio1 = ttk.Radiobutton(self.DnaAxisFrame)
        self.DnaAxisRadio1.place(relx=0.082, rely=0.336, relwidth=0.842
                , relheight=0.0, height=21)
        self.DnaAxisRadio1.configure(variable=self.dropna_axis)
        self.DnaAxisRadio1.configure(value='0')
        self.DnaAxisRadio1.configure(text='''Rows''')
        self.DnaAxisRadio1.configure(compound='left')

        self.DnaAxisLabel = ttk.Label(self.DnaAxisFrame)
        self.DnaAxisLabel.place(relx=0.082, rely=0.08, height=27, width=143)
        self.DnaAxisLabel.configure(background="#d9d9d9")
        self.DnaAxisLabel.configure(foreground="#000000")
        self.DnaAxisLabel.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.DnaAxisLabel.configure(relief="flat")
        self.DnaAxisLabel.configure(anchor='w')
        self.DnaAxisLabel.configure(justify='left')
        self.DnaAxisLabel.configure(text='''Axis to remove:''')
        self.DnaAxisLabel.configure(compound='left')

        self.DnaHowFrame = ttk.Frame(self.top)
        self.DnaHowFrame.place(relx=0.231, rely=0.016, relheight=0.186
                , relwidth=0.242)
        self.DnaHowFrame.configure(relief='groove')
        self.DnaHowFrame.configure(borderwidth="2")
        self.DnaHowFrame.configure(relief="groove")

        self.DnaHowRadio1 = ttk.Radiobutton(self.DnaHowFrame)
        self.DnaHowRadio1.place(relx=0.07, rely=0.354, relwidth=0.834
                , relheight=0.0, height=21)
        self.DnaHowRadio1.configure(variable=self.dropna_how)
        self.DnaHowRadio1.configure(text='''Any''')
        self.DnaHowRadio1.configure(compound='left')

        self.DnaHowRadio2 = ttk.Radiobutton(self.DnaHowFrame)
        self.DnaHowRadio2.place(relx=0.07, rely=0.54, relwidth=0.834
                , relheight=0.0, height=21)
        self.DnaHowRadio2.configure(variable=self.dropna_how)
        self.DnaHowRadio2.configure(value='2')
        self.DnaHowRadio2.configure(text='''All''')
        self.DnaHowRadio2.configure(compound='left')

        self.DnaHowRadio3 = ttk.Radiobutton(self.DnaHowFrame)
        self.DnaHowRadio3.place(relx=0.07, rely=0.726, relwidth=0.834
                , relheight=0.0, height=21)
        self.DnaHowRadio3.configure(variable=self.dropna_how)
        self.DnaHowRadio3.configure(value='3')
        self.DnaHowRadio3.configure(text='''At least''')
        self.DnaHowRadio3.configure(compound='left')

        self.DnaHowLabel = ttk.Label(self.DnaHowFrame)
        self.DnaHowLabel.place(relx=0.07, rely=0.088, height=27, width=171)
        self.DnaHowLabel.configure(background="#d9d9d9")
        self.DnaHowLabel.configure(foreground="#000000")
        self.DnaHowLabel.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.DnaHowLabel.configure(relief="flat")
        self.DnaHowLabel.configure(anchor='w')
        self.DnaHowLabel.configure(justify='left')
        self.DnaHowLabel.configure(text='''NaNs required:''')
        self.DnaHowLabel.configure(compound='left')

        self.DnaMinNA = tk.Spinbox(self.DnaHowFrame, from_=2.0, to=100.0)
        self.DnaMinNA.place(relx=0.553, rely=0.726, relheight=0.168
                , relwidth=0.372)
        self.DnaMinNA.configure(activebackground="#f9f9f9")
        self.DnaMinNA.configure(background="white")
        self.DnaMinNA.configure(buttonbackground="#d9d9d9")
        self.DnaMinNA.configure(disabledforeground="#a3a3a3")
        self.DnaMinNA.configure(font="TkDefaultFont")
        self.DnaMinNA.configure(foreground="black")
        self.DnaMinNA.configure(highlightbackground="black")
        self.DnaMinNA.configure(highlightcolor="black")
        self.DnaMinNA.configure(insertbackground="black")
        self.DnaMinNA.configure(selectbackground="#c4c4c4")
        self.DnaMinNA.configure(selectforeground="black")

        self.DnaCurrentTextBox = ScrolledText(self.top)
        self.DnaCurrentTextBox.place(relx=0.0, rely=0.297, relheight=0.705
                , relwidth=0.501)
        self.DnaCurrentTextBox.configure(background="white")
        self.DnaCurrentTextBox.configure(font="-family {Courier New} -size 11")
        self.DnaCurrentTextBox.configure(foreground="black")
        self.DnaCurrentTextBox.configure(highlightbackground="#d9d9d9")
        self.DnaCurrentTextBox.configure(highlightcolor="black")
        self.DnaCurrentTextBox.configure(insertbackground="black")
        self.DnaCurrentTextBox.configure(insertborderwidth="3")
        self.DnaCurrentTextBox.configure(selectbackground="#c4c4c4")
        self.DnaCurrentTextBox.configure(selectforeground="black")
        self.DnaCurrentTextBox.configure(wrap="none")

        self.DnaAfterTextBox = ScrolledText(self.top)
        self.DnaAfterTextBox.place(relx=0.499, rely=0.297, relheight=0.705
                , relwidth=0.5)
        self.DnaAfterTextBox.configure(background="white")
        self.DnaAfterTextBox.configure(font="-family {Courier New} -size 11")
        self.DnaAfterTextBox.configure(foreground="black")
        self.DnaAfterTextBox.configure(highlightbackground="#d9d9d9")
        self.DnaAfterTextBox.configure(highlightcolor="black")
        self.DnaAfterTextBox.configure(insertbackground="black")
        self.DnaAfterTextBox.configure(insertborderwidth="3")
        self.DnaAfterTextBox.configure(selectbackground="#c4c4c4")
        self.DnaAfterTextBox.configure(selectforeground="black")
        self.DnaAfterTextBox.configure(wrap="none")

        self.DnaButtonFrame = ttk.Frame(self.top)
        self.DnaButtonFrame.place(relx=0.487, rely=0.016, relheight=0.186
                , relwidth=0.135)
        self.DnaButtonFrame.configure(relief='groove')
        self.DnaButtonFrame.configure(borderwidth="2")
        self.DnaButtonFrame.configure(relief="groove")

        self.DnaApplyButton = ttk.Button(self.DnaButtonFrame)
        self.DnaApplyButton.place(relx=0.18, rely=0.115, height=25, width=76)
        self.DnaApplyButton.configure(command=lambda :explorer_gui_support.dna_dropna('apply'))
        self.DnaApplyButton.configure(takefocus="")
        self.DnaApplyButton.configure(text='''Apply''')
        self.DnaApplyButton.configure(compound='left')

        self.DnaCommitButton = ttk.Button(self.DnaButtonFrame)
        self.DnaCommitButton.place(relx=0.18, rely=0.398, height=25, width=76)
        self.DnaCommitButton.configure(command=lambda :explorer_gui_support.dna_dropna('commit'))
        self.DnaCommitButton.configure(takefocus="")
        self.DnaCommitButton.configure(text='''Commit''')
        self.DnaCommitButton.configure(compound='left')

        self.DnaCloseButton = ttk.Button(self.DnaButtonFrame)
        self.DnaCloseButton.place(relx=0.18, rely=0.681, height=25, width=76)
        self.DnaCloseButton.configure(command=explorer_gui_support.close_dropna)
        self.DnaCloseButton.configure(takefocus="")
        self.DnaCloseButton.configure(text='''Close''')
        self.DnaCloseButton.configure(compound='left')

        self.DnaCurrentLabel = ttk.Label(self.top)
        self.DnaCurrentLabel.place(relx=0.0, rely=0.247, height=29, width=404)
        self.DnaCurrentLabel.configure(background="#d9d9d9")
        self.DnaCurrentLabel.configure(foreground="#000000")
        self.DnaCurrentLabel.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.DnaCurrentLabel.configure(relief="flat")
        self.DnaCurrentLabel.configure(anchor='w')
        self.DnaCurrentLabel.configure(justify='left')
        self.DnaCurrentLabel.configure(text='''Current''')
        self.DnaCurrentLabel.configure(compound='left')

        self.DnaAfterLabel = ttk.Label(self.top)
        self.DnaAfterLabel.place(relx=0.499, rely=0.247, height=29, width=405)
        self.DnaAfterLabel.configure(background="#d9d9d9")
        self.DnaAfterLabel.configure(foreground="#000000")
        self.DnaAfterLabel.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.DnaAfterLabel.configure(relief="flat")
        self.DnaAfterLabel.configure(anchor='w')
        self.DnaAfterLabel.configure(justify='left')
        self.DnaAfterLabel.configure(text='''After Drop NA''')
        self.DnaAfterLabel.configure(compound='left')

        self.DnaColumnsNote = ttk.Label(self.top)
        self.DnaColumnsNote.place(relx=0.012, rely=0.214, height=19, width=405)
        self.DnaColumnsNote.configure(background="#d9d9d9")
        self.DnaColumnsNote.configure(foreground="#000000")
        self.DnaColumnsNote.configure(font="TkDefaultFont")
        self.DnaColumnsNote.configure(relief="flat")
        self.DnaColumnsNote.configure(anchor='w')
        self.DnaColumnsNote.configure(justify='left')
        self.DnaColumnsNote.configure(text='''*Removing columns will reset EDA plot settings''')
        self.DnaColumnsNote.configure(compound='left')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    explorer_gui_support.main()

if __name__ == '__main__':
    explorer_gui_support.main()




