#!/usr/bin/env python
import logging
import os
import re
import sys

import docopt

__doc__: str = """
Usage:
    script.py [--debug | --verbose]

Options:
    --debug           Enable debug logging.
    --verbose         Enable verbose logging.
"""

def setup_logging(debug: bool, verbose: bool) -> None:
    """
    Sets up logging based on the debug and verbose flags.

    Args:
        debug (bool): Enable debug logging if True.
        verbose (bool): Enable verbose logging if True.
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)


def main(args) -> int:
    """
    Main function

    Args:
    """
    debug: bool = bool(args["--debug"])
    verbose: bool = bool(args["--verbose"])

    setup_logging(debug, verbose)
    return 0

if __name__ == "__main__":
    cli_arguments: Dict = docopt.docopt(__doc__, options_first=True, version="0.0.1")
    sys.exit(main(cli_arguments))
