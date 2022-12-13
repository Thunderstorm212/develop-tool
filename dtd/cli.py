# dtd/cli.py
import typer
import socket

from typing import Optional
from rich.table import Table
from rich.console import Console
from rich.style import Style
from dtd import __app_name__, __version__
from dtd import network_scanner_ip

app = typer.Typer()

console = Console()

text_style = Style(color="#588157", bold=True)
value_stile = Style(color="#00b4d8")


class callbacks:

    def _help_callback(self, value: bool) -> None:

        tabl_options = Table(
            title="Options",
            title_justify="left",
            caption_justify="right",
            safe_box=True,
            box=None,
            padding=(0, 0, 0, 8)
        )

        tabl_options.add_column(style=value_stile)
        tabl_options.add_column(style=text_style)

        tabl_options.add_row("-h, --help", "application help")
        tabl_options.add_row("-v, --version", "view app version")
        tabl_options.add_row("-t, --tools", "view all tolls in dtd")

        tabl_command = Table(
            title="Commands",
            title_justify="left",
            caption_justify="right",
            safe_box=True,
            box=None,
            padding=(0, 0, 0, 8)
        )

        tabl_command.add_column(style=value_stile)
        tabl_command.add_column(style=text_style)

        tabl_command.add_row("get -ip", "Get my Ip address")
        tabl_command.add_row("get -Nip", "Get network users Ip address")

        if value:
            console.print("\n",
                          tabl_options, "\n",
                          tabl_command,
                          "\n"
                          )
            raise typer.Exit()

    def _version_callback(self, value: bool) -> None:
        if value:
            console.print(f"{__app_name__} [b #00b4d8]v{__version__}[b /#00b4d8]")
            raise typer.Exit()


class commands:

    @staticmethod
    def _getMyIP_callback(self, value: bool) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            my_IP = s.getsockname()[0]
        except Exception:
            my_IP = '127.0.0.1'
        finally:
            s.close()
        if value:
            console.print(f"""
            My IP address : {my_IP}
            """)
            typer.Exit()

    @staticmethod
    def _getNetworkIp_callback(self, value: bool) -> None:
        if value:
            print("scan")
            typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(None, "--version", "-v", callback=callbacks._version_callback, is_eager=True),
        help: Optional[bool] = typer.Option(None, "--help", "-h", callback=callbacks._help_callback),

 ) -> None: return


@app.command()
def get(
        network_ip: Optional[bool] = typer.Option(None, "--net-ip", "-Nip", prompt="", help="get [ARGS]", ),
) -> None: return


