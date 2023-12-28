
##-*$*-## created by Ba7bou7 at --2023 ##-*$*-##

################################################################
#                                ###############################
#   HDDDDDDD      GGGGGGGGGGGG   ###########         ###########
#   H       O               G    #########  #########  #########
#   H        O             G     #######  #############  #######
#   H       O             G      #######  #############  #######
#   HEEEEEEDD            G       #######  #############  #######
#   H        O          G        #######  #######  ####  #######
#   H         O        G         #######  #########  ##  #######
#   H         O       G          #########  #########  #########
#   H        O       G           ###########        ###  #######
#   HDDDDDDDD       G            ########################  #####
#                                ###############################
################################################################

###<<<=@=VARIABLE=@=>>>#########################################
                                                               #
screens = [] # 1                                               #
layouts = [] # 2                                               #
groups = []  # 3                                               #
keys = []    # 4                                               #
mouse = []   # 5                                               #
                                                               #
################################################################
                                                               #
#auto_minimize = True                                          #
#auto_fullscreen = True                                        #
                                                               #
################################################################
                                                               #
#wmname = "Qtile"                                              #
#wl_input_rules = None                                         #
#reconfigure_screens = True                                    #
#focus_on_window_activation = "smart"                          #
                                                               #
################################################################
                                                               #
#dgroups_key_binder = None                                     #
#dgroups_app_rules = []  # type: list                          #
#floating_layout = None                                        #
                                                               #
################################################################
                                                               #
#widget_defaults = {}                                          #
#extension_defaults = {}                                       #
                                                               #
################################################################
                                                               #
#follow_mouse_focus = True                                     #
#bring_front_click = False                                     #
#cursor_warp = False                                           #
                                                               #
################################################################

###<<<=@=IMPORTING=@=>>>########################################
                                                               #
from environment import Screen_Design                          #
#from objects.keyboard import keybinders                       #
#from workspaces import Code, Net                              #
                                                               #
################################################################

#######<<<===SCREEN===>>>#######################################
                                                               #
Screen_Design(screens)                                         #
                                                               #
################################################################

####<<<=@=WORKSPACE=@=>>>#######################################
                                                               #
#Home(groups)                                                  #
#Net(groups)                                                   #
#Code(groups,layouts)                                          #
#Board(groups)                                                 #
#Studio(groups)                                                #
#Temp(groups)                                                  #
                                                               #
################################################################

###<<<=@=KEYBINDERS=@=>>>#######################################
                                                               #
#keybinders.GenKey(keys)                                       #
#keybinders.WsKey(keys)                                        #
#keybinders.LayKey(keys)                                       #
#keybinders.WinKey(keys)                                       #
#keybinders.AppKey(keys)                                       #
                                                               #
################################################################

