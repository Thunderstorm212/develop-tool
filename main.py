#!/usr/bin/python
from rich.table import Table
from rich.console import Console
from rich.style import Style

tabl = Table(
    title="DevTools",
    caption="tools by thunderstorm",
    caption_justify="right",
    safe_box=True,
)

column_style = Style(color="#ffffff")

tabl.add_column('Number', justify='center', style='#a2d2ff',)
tabl.add_column('Title', justify='center', style='#a3b18a')
tabl.add_column('File', justify='center', style="#ec6b5d")
tabl.add_column('Command', justify='left', style="italic #6a994e")


tabl.add_row('1', 'Get IP address', '', '-g ip')
tabl.add_row('2', 'Send mail', '--getIP', '- ')
tabl.add_row('3', 'Get IP address', '--getIP', '-g ip')

console = Console()
print("\n")
console.print(tabl)
