

from mameebox.printer.driver.proto import ThermalPrinter


class Printer:

    def __init__(self, *args, **kwargs):
        self.driver = ThermalPrinter(*args, **kwargs)

    def print_text(self, *args, **kwargs):
        return self.driver.print_text(*args, **kwargs)



