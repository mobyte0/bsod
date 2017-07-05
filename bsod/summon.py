"""makes fake error messages, inspired by the classic windows error screen"""
#!/usr/bin/python
import platform
import random
import urwid

PALETTE = [
    ('title', '', '', '', '#00a', '#aaa'),
    ('text', '', '', '', '#fff', '#00a'),
    ('bg', '', '', '', '#00a', '#00a'),
    ]

def exitscreen(*_):
    """quits the program with a keypress"""
    raise urwid.ExitMainLoop()

def summon():
    """summons the classic bsod"""
    sys_info = " {} {} ".format(platform.system(), platform.release())
    error2 = "{:02x}".format(random.randint(0, 17)).upper()
    error4 = "{:04x}".format(random.randint(0, 4095)).upper()
    error8 = "{:08x}".format(random.randint(0, 68719476736)).upper()
    message = """
An error has occurred. To continue:

Press Enter to return to {}, or

Press CTRL+ALT+DEL to restart your computer. If you do this,
you will lose any unsaved information in all open applications.

Error: {} : {} : {}
    """.format(platform.system(), error2, error4, error8)
    end = "Press any key to continue "

    bg_map = urwid.AttrMap(urwid.SolidFill(' '), 'bg')
    body = urwid.Filler(
        urwid.AttrMap(
            urwid.Text(message, align='left'),
            'text'))
    body_text = urwid.Overlay(
        body, bg_map,
        'center', 63,
        'middle', 10,
        63, 10)
    continue_ln = urwid.AttrMap(
        urwid.Edit(end, align='center'),
        'text')
    title_txt = urwid.AttrMap(
        urwid.Text(sys_info, align='center'),
        'title')
    fill_scrn = urwid.Overlay(
        urwid.Filler(title_txt), bg_map,
        'center', len(sys_info),
        'middle', 1,
        len(sys_info), 1)
    text_stack = urwid.Filler(urwid.Pile([(1, fill_scrn),
                                    (10, body_text),
                                    ('pack', continue_ln)]))
    bg_fill = urwid.AttrMap(text_stack, 'bg')

    loop = urwid.MainLoop(bg_fill, PALETTE, input_filter=exitscreen)
    loop.screen.set_terminal_properties(colors=256)
    loop.run()

if __name__ == '__main__':
    summon()
