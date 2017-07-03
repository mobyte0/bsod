from urwid import ExitMainLoop, AttrMap, SolidFill, Text, Filler, Overlay, Edit,\
    Pile, MainLoop
from platform import system, release
from random import randint

PALETTE = [
    ('title', '', '', '', '#00a', '#aaa'),
    ('text', '', '', '', '#fff', '#00a'),
    ('bg', '', '', '', '#00a', '#00a'),
    ]

def exitscreen(*_):
    raise ExitMainLoop()

def main():
    sysinfo = " {} {} ".format(system(), release())
    error2 = "{:02x}".format(randint(0, 17)).upper()
    error4 = "{:04x}".format(randint(0, 4095)).upper()
    error8 = "{:08x}".format(randint(0, 68719476736)).upper()
    message = """
An error has occurred. To continue:

Press Enter to return to {}, or

Press CTRL+ALT+DEL to restart your computer. If you do this,
you will lose any unsaved information in all open applications.

Error: {} : {} : {}
    """.format(system(), error2, error4, error8)
    end = "Press any key to continue "

    attr2 = AttrMap(SolidFill(' '), 'bg')
    body = AttrMap(Text(message, align='left'), 'text')
    body = Filler(body)
    body2 = Overlay(
        body, attr2,
        'center', 63,
        'middle', 10,
        63, 10)
    presskey = Edit(end, align='center')
    cont = AttrMap(presskey, 'text')
    txt = Text(sysinfo, align='center')
    attr1 = AttrMap(txt, 'title')
    txt = Filler(attr1)
    fill = Overlay(
        txt, attr2,
        'center', len(sysinfo),
        'middle', 1,
        len(sysinfo), 1)
    pile = Filler(Pile([(1, fill), (10, body2), ('pack', cont)]))
    attr3 = AttrMap(pile, 'bg')

    loop = MainLoop(attr3, PALETTE, input_filter=exitscreen)
    loop.screen.set_terminal_properties(colors=256)
    loop.run()

if __name__ == '__main__':
    main()
