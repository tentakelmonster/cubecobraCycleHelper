import wx

class CycleHelperGui(wx.Frame):
    
    def __init__(self, parent, title, cycleData):
        wx.Frame.__init__(self, parent, title=title, size=(1300,700))
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.cycleData = cycleData

        # set up checkboxes
        self.CheckBoxSizer = wx.BoxSizer(wx.VERTICAL)

        self.cyclesCheckBoxes = wx.CheckListBox(self, choices=list(self.cycleData.keys()), name="Lands")
        self.CheckBoxSizer.Add(self.cyclesCheckBoxes, 1, wx.EXPAND)

        # set up buttons
        self.ButtonSizer = wx.BoxSizer(wx.VERTICAL)

        self.ClearButton = wx.Button(self, -1, "Clear")
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.ClearButton)
        self.ButtonSizer.Add(self.ClearButton, 1, wx.SHAPED)

        self.GenerateButton = wx.Button(self, -1, "Generate")
        self.Bind(wx.EVT_BUTTON, self.OnGenerate, self.GenerateButton)
        self.ButtonSizer.Add(self.GenerateButton, 1, wx.SHAPED)

        self.ExitButton = wx.Button(self, -1, "Exit")
        self.Bind(wx.EVT_BUTTON, self.OnExit, self.ExitButton)
        self.ButtonSizer.Add(self.ExitButton, 1, wx.SHAPED)

        # Arrange Sizers
        self.mainSizer.Add(self.CheckBoxSizer, 1, wx.SHAPED)
        self.mainSizer.Add(self.ButtonSizer, 1, wx.SHAPED)

        self.SetSizer(self.mainSizer)
        self.SetAutoLayout(1)
        #self.mainSizer.Fit(self)
        self.Show()

    def OnClear(self, event):
        for i in range(len(self.cycleData.keys())):
            self.cyclesCheckBoxes.Check(i, False)

    def OnGenerate(self, event):
        checkedCycles = self.cyclesCheckBoxes.GetCheckedStrings()
        with open("export.txt", "w") as file:
            for cycleName in checkedCycles:
                for cardName in self.cycleData[cycleName]:
                    file.write(cardName + "\n")

    def OnExit(self, event):
        self.Close(True)