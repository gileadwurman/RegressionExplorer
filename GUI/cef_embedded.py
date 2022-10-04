# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:44:59 2022

@author: gwurm
"""
import tkinter as tk
from cefpython3 import cefpython as cef
import platform
import ctypes
import logging as _logging

logger = _logging.getLogger("tkinter_.py")

logger.setLevel(_logging.DEBUG)
stream_handler = _logging.StreamHandler()
formatter = _logging.Formatter("[%(filename)s] %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.info("CEF Python {ver}".format(ver=cef.__version__))
logger.info("Python {ver} {arch}".format(
        ver=platform.python_version(), arch=platform.architecture()[0]))
logger.info("Tk {ver}".format(ver=tk.Tcl().eval('info patchlevel')))

# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")

# MAC IMPLEMENTATION OMITTED

class MainFrame(tk.Frame):

    def __init__(self, rootframe):
        self.browser_frame = None
        # self.navigation_bar = None

        # Root
        # root.geometry("900x640")
        tk.Grid.rowconfigure(rootframe, 0, weight=1)
        tk.Grid.columnconfigure(rootframe, 0, weight=1)

        # MainFrame
        tk.Frame.__init__(self, rootframe)
        # self.master.title("Tkinter example")
        self.master.bind("<Destroy>", self.on_close)
        self.master.bind("<Configure>", self.on_root_configure)
        # self.setup_icon()
        self.bind("<Configure>", self.on_configure)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        # NavigationBar
        # self.navigation_bar = NavigationBar(self)
        # self.navigation_bar.grid(row=0, column=0,
        #                          sticky=(tk.N + tk.S + tk.E + tk.W))
        # tk.Grid.rowconfigure(self, 0, weight=0)
        # tk.Grid.columnconfigure(self, 0, weight=0)

        # BrowserFrame
        self.browser_frame = BrowserFrame(self)
        self.browser_frame.grid(row=1, column=0,
                                sticky=(tk.N + tk.S + tk.E + tk.W))
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        # Pack MainFrame
        self.pack(fill=tk.BOTH, expand=tk.YES)
    
    def on_root_configure(self, _):
        logger.debug("MainFrame.on_root_configure")
        if self.browser_frame:
            self.browser_frame.on_root_configure()

    def on_configure(self, event):
        logger.debug("MainFrame.on_configure")
        if self.browser_frame:
            width = event.width
            height = event.height
            # if self.navigation_bar:
            #     height = height - self.navigation_bar.winfo_height()
            self.browser_frame.on_mainframe_configure(width, height)

    def on_focus_in(self, _):
        logger.debug("MainFrame.on_focus_in")
        pass

    def on_focus_out(self, _):
        logger.debug("MainFrame.on_focus_out")
        pass

    def on_close(self, _):
        logger.debug("MainFrame.on_close")
        if self.browser_frame:
            self.browser_frame.on_root_close()
        self.master.destroy()

    def get_browser(self):
        logger.debug("MainFrame.get_browser")
        if self.browser_frame:
            return self.browser_frame.browser
        return None

class BrowserFrame(tk.Frame):

    def __init__(self, mframe):
        self.closing = False
        self.browser = None
        tk.Frame.__init__(self, mframe)
        self.mframe = mframe
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Configure>", self.on_configure)
        # """For focus problems see Issue #255 and Issue #535. """
        self.focus_set()

    def embed_browser(self):
        logger.debug("BrowserFrame.embed_browser")
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info, url="")
        assert self.browser
        #self.browser.SetClientHandler(LifespanHandler(self))
        #self.browser.SetClientHandler(LoadHandler(self))
        #self.browser.SetClientHandler(FocusHandler(self))
        self.message_loop_work()

    def get_window_handle(self):
        # MAC IMPLEMENTATION OMITTED
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception("Couldn't obtain window handle")

    def message_loop_work(self, delay=10):
        cef.MessageLoopWork()
        self.after(delay, self.message_loop_work)

    def on_configure(self, _):
        logger.debug("BrowserFrame.on_configure")
        if not self.browser:
            self.embed_browser()

    def on_root_configure(self):
        logger.debug("BrowserFrame.on_root_configure")
        # Root <Configure> event will be called when top window is moved
        if self.browser:
            self.browser.NotifyMoveOrResizeStarted()

    def on_mainframe_configure(self, width, height):
        logger.debug("BrowserFrame.on_mainframe_configure")
        if self.browser:
            if WINDOWS:
                ctypes.windll.user32.SetWindowPos(
                    self.browser.GetWindowHandle(), 0,
                    0, 0, width, height, 0x0002)
            self.browser.NotifyMoveOrResizeStarted()

    def on_focus_in(self, _):
        logger.debug("BrowserFrame.on_focus_in")
        if self.browser:
            self.browser.SetFocus(True)

    def on_focus_out(self, _):
        logger.debug("BrowserFrame.on_focus_out")
        """For focus problems see Issue #255 and Issue #535. """
        pass

    def on_root_close(self):
        logger.info("BrowserFrame.on_root_close")
        if self.browser:
            logger.debug("CloseBrowser")
            self.browser.CloseBrowser(True)
            self.clear_browser_references()
        else:
            logger.debug("tk.Frame.destroy")
            self.destroy()
    
    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None