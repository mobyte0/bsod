import urwid
import platform
import random

def exitscreen(*_):
    raise urwid.ExitMainLoop()
    
sysinfo = " {} {} ".format(platform.system(), platform.release())
errornum1 = "{:02x}".format(random.randint(0, 17))
errornum2 = "{:04x}".format(random.randint(0, 4095))
errornum3 = "{:08x}".format(random.randint(0, 68719476736))
message = """
An error has occurred. To continue:

Press Enter to return to {}, or

Press CTRL+ALT+DEL to restart your computer. If you do this, 
you will lose any unsaved information in all open applications.

Error: {} : {} : {}
""".format(platform.system(), errornum1, errornum2, errornum3)
end = "Press any key to continue "
    
palette = [
    ('title', '', '', '', '#00a', '#aaa'),
    ('text', '', '', '', '#fff', '#00a'),
    ('bg', '', '', '', '#00a', '#00a'),
    ]

attr2 = urwid.AttrMap(urwid.SolidFill(' '), 'bg')
body = urwid.AttrMap(urwid.Text(message, align='left'), 'text')
body = urwid.Filler(body)
body2 = urwid.Overlay(
    body, attr2,
    'center', 63,
    'middle', 10,
    63, 10)
presskey = urwid.Edit(end, align='center')
cont = urwid.AttrMap(presskey, 'text')
txt = urwid.Text(sysinfo, align='center')
attr1 = urwid.AttrMap(txt, 'title')
txt = urwid.Filler(attr1)
fill = urwid.Overlay(
    txt, attr2,
    'center', len(sysinfo),
    'middle', 1,
    len(sysinfo), 1)
pile = urwid.Filler(urwid.Pile([(1, fill), (10, body2), ('pack', cont)]))
attr3 = urwid.AttrMap(pile, 'bg')

loop = urwid.MainLoop(attr3, palette, input_filter=exitscreen)
loop.screen.set_terminal_properties(colors=256)
loop.run()
