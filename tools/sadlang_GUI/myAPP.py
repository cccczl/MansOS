import wx
from src import tabManager
from src import uploadModule
from src import listenModule
from src import APIcore 

class Example(wx.Frame):
    
    def __init__(self,  *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
        
    def addAPI(self, API):
        self.API = API
        self.InitUI()
        
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        save = fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl+S', 'Save generated code')
        upload = fileMenu.Append(wx.ID_ANY, '&Upload\tCtrl+U', 'Upload generated code')
        output = fileMenu.Append(wx.ID_ANY, '&Output\tCtrl+O', 'Listen to mote\'s output')
        close = fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+Q', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.toolbar = self.CreateToolBar()
        extTool = self.toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('src/exit.jpeg'))
        uplTool = self.toolbar.AddLabelTool(wx.ID_ANY, 'Upload', wx.Bitmap('src/upload.gif'))
        outputTool = self.toolbar.AddLabelTool(wx.ID_ANY, 'Output', wx.Bitmap('src/output.gif'))
        self.toolbar.Realize()
        
        self.Bind(wx.EVT_MENU, self.OnQuit, close)
        self.Bind(wx.EVT_TOOL, self.OnQuit, extTool)
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        self.Bind(wx.EVT_MENU, self.OnUpload, upload)
        self.Bind(wx.EVT_TOOL, self.OnUpload, uplTool)
        self.Bind(wx.EVT_MENU, self.OnOutput, output)
        self.Bind(wx.EVT_TOOL, self.OnOutput, outputTool)
        
    def OnQuit(self, e):
        self.Close()
        
    def OnSave(self, e):
        print "Save not suported :("
        
    def OnUpload(self, e):
        dialog = uploadModule.UploadModule(None, 'Upload and compile', self.API)
        dialog.ShowModal()
        dialog.Destroy()

    def OnOutput(self, e):
        dialog = listenModule.ListenModule(None, 'Listen to output', self.API)
        dialog.ShowModal()
        dialog.Destroy()

def main():
    API = APIcore.ApiCore()
    ex = wx.App()
    frame = Example(None, title="My app", size = (800,500), pos=(100,100))
    frame.addAPI(API)
    tabManager.tabManager(frame, API)
    frame.Show()
    ex.MainLoop()

if __name__ == '__main__':
    main()
