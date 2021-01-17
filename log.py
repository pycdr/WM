import logging
from rich.logging import RichHandler
from rich.console import Console

logging.basicConfig(
	level="NOTSET",
	format="%(message)s",
	datefmt="[%X]",
	handlers=[
		RichHandler(
			rich_tracebacks=True,
			console = Console(
				file=open("report.log", 'wt')
			)
		)
	]
)
log = logging.getLogger("rich")
