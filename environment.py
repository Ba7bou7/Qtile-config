class Screen_Design:

    def __init__(self,screen):
        pass

    def Show(self):
        from libqtile.config import Screen
        env = [
            Screen(
                bottom = self.Bar(),
                wallpaper = '',
                wallpaper_mode = 'fill',
            )
        ]

    def Bar(self):
        from libqtile import bar
        init = bar.Bar(
            self.widgets(),
            30, # Thickness of the bar
            background = '#101010',
            border_color = ['#e93434']*4,
            border_width = [3]*4,
            margin = [1]*4,
            opacity = 4,
        )

        return init

    def Widgets(self):
        from libqtile import widget
        content = [
            widget.Clock(format='%I:%M %p'),
            widget.Sep(),
            widget.AGroupBox(),
            widget.CurrentLayout(),
            widget.Systray(),
            widget.Sep(),
            widget.Prompt(),
            widget.Spacer(),
            widget.Notify(),
            widget.Sep(),
            widget.Net(format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}'),
            widget.Memory(format='
                Mem: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}\n
                Swap: {SwapUsed: .0f}{ms}/{SwapTotal: .0f}{ms}
            '),
            widget.CPU(),
            widget.PulseVolume(),
            widget.Sep(),
            widget.Clock(format='  %A  \n%d/%m/%y'),
            widget.QuickExit(),
            # ...
        ]

        return content
