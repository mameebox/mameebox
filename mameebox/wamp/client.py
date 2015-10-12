
import sys

from path import Path

from .wamplitude import App

from mameebox.printer.adapter.proto import Printer

printer = Printer()

app = App()

@app.register('printmessage')
async def _(text):
    printer.print_text(text)
    printer.linefeed()
    printer.linefeed()
    printer.linefeed()

@app.on('joined')
async def _(session):
    print('Connecté')

