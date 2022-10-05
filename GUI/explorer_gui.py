#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Oct 04, 2022 04:08:50 PM PDT  platform: Windows NT

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
    _style_code_ran = 1

class MainWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1020x681+165+157")
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

        _style_code()
        self.TabGroup = ttk.Notebook(self.top)
        self.TabGroup.place(relx=0.0, rely=0.0, relheight=0.999, relwidth=1.001)
        self.TabGroup.configure(takefocus="")
        self.PairPlotTab = tk.Frame(self.TabGroup)
        self.TabGroup.add(self.PairPlotTab, padding=3)
        self.TabGroup.tab(0, text='''PairPlot''', compound="left"
                ,underline='''-1''', )
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

        self.PairPlotButton = tk.Button(self.PairPlotTab)
        self.PairPlotButton.place(relx=0.098, rely=0.942, height=24, width=67)
        self.PairPlotButton.configure(activebackground="beige")
        self.PairPlotButton.configure(activeforeground="black")
        self.PairPlotButton.configure(background="#d9d9d9")
        self.PairPlotButton.configure(command=explorer_gui_support.create_pairplot)
        self.PairPlotButton.configure(compound='left')
        self.PairPlotButton.configure(disabledforeground="#a3a3a3")
        self.PairPlotButton.configure(foreground="#000000")
        self.PairPlotButton.configure(highlightbackground="#d9d9d9")
        self.PairPlotButton.configure(highlightcolor="black")
        self.PairPlotButton.configure(pady="0")
        self.PairPlotButton.configure(text='''PairPlot''')

        self.LeftPaneGroup = ttk.Panedwindow(self.PairPlotTab, orient="vertical")

        self.LeftPaneGroup.place(relx=0.029, rely=0.043, relheight=0.878
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

        top.geometry("533x193+410+226")
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

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.056, rely=0.052, height=24, width=58)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Input File:''')
        self.TLabel1.configure(compound='left')

        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(relx=0.056, rely=0.363, height=24, width=84)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Import kwargs:''')
        self.TLabel2.configure(compound='left')

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
        self.CancelButton.configure(cursor="fleur")

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




