


################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
                                                               #
class Net:                                                     #
    def __init__(self,group):                                  #
        self.Space(group)                                      #
                                                               #
    def Space(self,group):                                     # 
        from libqtile.config import Group, Match               #
        name = 'Net'                                           #
        space = Group(                                         #
            name,                                              #
            position = 2,                                      #
            spawn = 'firefox-bin',                             #
            layout = 'max',                                    #
            matches = [ Match(wm_class=["Firefox"]) ],         #
            exclusive = True,                                  #
        )                                                      #
        group.append(space)                                    #
                                                               #
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
                                                               #
                                                               #
class Code:                                                    #
                                                               #
    def __init__(self,group,layout):                           #
        self.Space(group)                                      #
        self.Layer(layout)                                     #
                                                               #
    def Space(self,group):                                     #
        from libqtile.config import Group                      #
        name = 'Code'                                          #
        space = Group(                                         #
            name,                                              #
            persist = False,                                   #
            init = True,                                       #
            position = 1,                                      #
            layout = 'monadthreecol',                          #
            spawn = ['alacritty','alacritty -e ranger'],       #
        )                                                      #
        group.append(space)                                    #
                                                               #
    def Layer(self,layout): # <<-------------------------------# The primary layout for code workspace
        from libqtile import layout as Layout                  #
        Layouts = [                                            #
            # The Main Layout                                  #
            Layout.MonadThreeCol(                              #
                # Layout Settings                              #
            ),                                                 #
            # The Full-screen Focus Layout                     #
            Layout.Max(),                                      #
        ]                                                      #
                                                               #
        layout.extend(Layouts)                                 #
                                                               #
################################################################