import logging
from rich.logging import RichHandler
from rich.console import Console

# Open the log file once to avoid repeated file handle leaks
_logfile = open("report.log", 'wt')

logging.basicConfig(
	level="NOTSET",
	format="%(message)s",
	datefmt="[%X]",
	handlers=[
		RichHandler(
			rich_tracebacks=True,
			console=Console(
				file=_logfile
			)
		)
	]
)
log = logging.getLogger("rich")
