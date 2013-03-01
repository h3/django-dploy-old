def color(string=None, c=None):
    """
    Returns a string wrapped in a shell color.
    If no color is given, the string is returned prefixed 
    with the color reset code. if no arguments are provided at all,
    the color reset code is returned.
    """
    if c is None:
        if string is None:
            return "\x1b[0m"
        else:
            return "\x1b[0m%s" % string
    else:
        _c = {
            'black':'0;30',  'bold_black':'1;30',  'under_black':'4;30',
            'red':'0;31',    'bold_red':'1;31',    'under_red':'4;31',
            'green':'0;32',  'bold_green':'1;32',  'under_green':'4;32',
            'yellow':'0;33', 'bold_yellow':'1;33', 'under_yellow':'4;33',
            'blue':'0;34',   'bold_blue':'1;34',   'under_blue':'4;34',
            'purple':'0;35', 'bold_purple':'1;35', 'under_purple':'4;35',
            'cyan':'0;36',   'bold_cyan':'1;36',   'under_cyan':'4;36',
            'white':'0;37',  'bold_white':'1;37',  'under_white':'4;37',
        }
        return "\x1b[%sm%s\x1b[0m" % (_c[c.lower()], string)
