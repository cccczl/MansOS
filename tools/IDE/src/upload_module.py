# -*- coding: utf-8 -*-
#
# Copyright (c) 2008-2012 the MansOS team. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#  * Redistributions of source code must retain the above copyright notice,
#    this list of  conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import wx

from newMote import NewMote
from motelist import Motelist
from Translater import localize

class UploadModule(wx.Panel):
    def __init__(self, parent, API):
        super(UploadModule, self).__init__(parent = parent)

        self.API = API
        self.editorManager = self.API.tabManager.GetCurrentPage()
        self.filename = self.editorManager.fileName
        Motelist.addUpdateCallback(self.updateMotelist)

        self.tmpDir = self.API.path + '/temp/'
        self.haveMote = False
        self.platform = "telosb"
        self.moteOrder = list()
        # this is path from /mansos/tools/IDE
        self.pathToMansos = self.API.path + "/../.."
        self.motes = []

        self.main = wx.BoxSizer(wx.VERTICAL)
        self.controls = wx.GridBagSizer(10, 10)

        #self.source = wx.ComboBox(self, choices = ["USB", "Shell"])
        #self.source.SetValue("USB")
        self.upload = wx.Button(self, label = localize("Upload"))
        self.platforms = wx.ComboBox(self, choices = self.API.getPlatforms())
        self.refresh = wx.Button(self, label = localize("Refresh"))
        self.compile = wx.Button(self, label = localize("Compile"))
        self.newMote = wx.Button(self, label = localize("Add mote"))
        self.platforms.SetValue(self.API.getActivePlatform())
        if self.API.platformOnly != None:
            self.platforms.Enable(False)

        self.controls.Add(self.compile, (0, 0), flag = wx.EXPAND | wx.ALL)
        self.controls.Add(self.platforms, (0, 1), flag = wx.EXPAND | wx.ALL)
        self.controls.Add(self.upload, (0, 2), span = (2, 2),
                          flag = wx.EXPAND | wx.ALL)

        #self.controls.Add(self.source, (1, 1), flag = wx.EXPAND | wx.ALL)
        self.controls.Add(self.newMote, (1, 1), flag = wx.EXPAND | wx.ALL)
        self.controls.Add(self.refresh, (1, 0), flag = wx.EXPAND | wx.ALL)

        self.list = wx.CheckListBox(self, wx.ID_ANY, style = wx.MULTIPLE)

        self.main.Add(self.controls, 0, wx.EXPAND | wx.ALL, 3);
        self.main.Add(self.list, 0, wx.EXPAND | wx.ALL, 3);

        self.Bind(wx.EVT_BUTTON, self.API.doCompile, self.compile)
        self.Bind(wx.EVT_BUTTON, self.API.doUpload, self.upload)
        self.Bind(wx.EVT_BUTTON, self.updateMotelist, self.refresh)
        #self.Bind(wx.EVT_COMBOBOX, self.populateMotelist, self.source)
        self.Bind(wx.EVT_BUTTON, self.openNewMoteDialog, self.newMote)
        self.Bind(wx.EVT_COMBOBOX, self.API.changePlatform, self.platforms)
        self.Bind(wx.EVT_CHECKLISTBOX, self.modifyTargets, self.list)

        self.SetSizerAndFit(self.main)
        self.SetAutoLayout(1)
        self.Show()

        self.updateMotelist()

    def __del__(self):
        Motelist.removeUpdateCallback(self.updateMotelist)

    def updateMotelist(self, event = None):
        old = self.list.GetCheckedStrings()
        pos = 0

        self.list.Clear()

        for mote in Motelist.getMotelist(False):
            self.list.Enable(True)
            self.list.Insert(mote.getNiceName(), pos)

            if mote.getNiceName() in old:
                self.list.Check(pos)

            pos += 1

        if self.list.GetCount() == 0:
            self.list.Enable(False)
            self.list.Insert(localize("No devices found!"), 0)

    def modifyTargets(self, event):
        temp = list()

        for target in self.list.GetCheckedStrings():
            if target.count("(") != 0:
                temp.append(target.split("(")[1].split(")")[0])

        self.API.targets = temp

    def openNewMoteDialog(self, event):
        dialog = NewMote(self, self.API)
        dialog.ShowModal()
        dialog.Destroy()
        self.updateMotelist()


