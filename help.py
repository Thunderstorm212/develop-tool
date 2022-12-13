from rich.console import Console
from rich.table import Table
from rich.style import Style

text_style = Style(color="#588157", bold=True)
value_stile = Style(color="#00b4d8")

tabl_options = Table(
    title="Options",
    title_justify="left",
    caption_justify="right",
    safe_box=True,
    box=None,
    padding=(0, 0, 0, 4)
)

console = Console()


def _help_callback():
    tabl_options.add_column(style=text_style)
    tabl_options.add_column(style=value_stile)
    tabl_options.add_row("Version",     "-v, --version", "view app version")
    tabl_options.add_row("Show",        "-s, --show")
    tabl_options.add_row("Config",      "-c, --config")

    console.print("\n", tabl_options, "\n")


_help_callback()
