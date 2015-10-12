

from mameebox.printer.driver.proto import ThermalPrinter


class Printer:

    def __init__(self, *args, **kwargs):
        self.driver = ThermalPrinter(*args, **kwargs)

    def print_text(self, msg, *args, **kwargs):
        msg = msg.encode('utf8')
        return self.driver.print_text(msg, *args, **kwargs)

