import time
import sys
#  PROGRAMING TOOLS
#  ---


def recordtime(decorated):
    """Decorator to record time

    Arguments:
        decorated {function} -- Funcition to be timed
    """
    def wraper(*args, **kwargs):

        start_timer = time.perf_counter()
        result = decorated(*args, **kwargs)
        elapsed = time.perf_counter() - start_timer

        function_name = decorated.__name__
        clock = formattime(elapsed)
        print(f"{function_name} finished in {clock}")

        return result
    return wraper


def formattime(elapsed):
    s, m, h = (0, 0, 0)
    msg = None
    try:
        if not isinstance(elapsed, (float, int)):
            raise TypeError(f"{type(elapsed)} was passed!")
        if elapsed >= 60:
            h = int(elapsed//3600)
            m = elapsed % 3600
            if m > 60:
                s = m % 60
                s = int(s//1)
                m = int(m//60)
            msg = f"{h:02d}:{m:02d}:{s:02d}"
        else:
            if elapsed < 1.0e-2:
                elapsed *= 1.0e3
                msg = f"{elapsed:.2f} milisecond(ms)"
            else:
                msg = f"{elapsed:.2f} second(s)"
    except TypeError as err:
        print("Warning: Expected int of float: ", err)
    finally:
        return msg


def get_atrs(received):
    """Pass dict data to string

    Arguments:
        received {dict} -- a dictionary {k:v,}

    Returns:
        str -- string formated as '| key = value |'
    """
    return ''.join(f'| {k} = {v} | '
                   for k, v in received.items())


def progress(indeX, nstep, perc=10, **kwargs):
    """Track progress of 'for' loops

    Arguments:
        indeX {int} -- counter of the loop. must be > 1
        nstep {int} -- Total number of steps

    Keyword Arguments:
        perc {int} -- potion of iterations to print progress (default: {10})
    """
    if (indeX % int(nstep/perc) == 0):
        atrs = get_atrs(kwargs)
        message = f'Current progress: '\
                  f'{(indeX/(nstep - 1))*100:.2f}%'\
                  f' | step = {indeX} '\
                  f' {atrs}'
        print(message)


class ColorText:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def __init__(self, defaultcolor=OKGREEN):
        self.defaultcolor = defaultcolor
    
    def colorstring(self, string='', color=None, bold=False, endcolor=True):
        end = self.ENDC
        if color is None:
            color = self.defaultcolor
        if bold:
            color += self.BOLD
        if not endcolor:
            end = ''
        return f'{color}{string}{end}'
    
    def cprint(self, *objects, color=None, bold=False, endcolor=True, **kwargs):
        end = self.ENDC
        if color is None:
            color = self.defaultcolor
        if bold:
            color += self.BOLD
        if not endcolor:
            end = ''
        print(color, *objects, end, **kwargs)
        return self
