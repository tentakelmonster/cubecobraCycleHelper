"""
Collect each card from the chosen cycles and print them into a copy-able file.


Author: Max
Date: 21.11.2025
Version: yes
"""
import wx
from bin import gui, cycle_helper

cycles = cycle_helper.CycleData()

app = wx.App(False)
mainframe = gui.CycleHelperGui(None, "Cycle Import Helper", cycles.getCycleData())
app.MainLoop()
