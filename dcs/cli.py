
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2017 Franck Nijhof
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""CLI Handler for the Docker Context Streamer.

This file handles the parsing of the CLI input
"""

import argparse
import os.path
import sys

from dcs import APP_DESCRIPTION, APP_NAME, APP_VERSION
from dcs.streamer import Streamer


def run(argv=None):
    """Run the Docker Context Streamer."""
    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description=APP_DESCRIPTION,
        epilog=("Example: cat ~/Dockerfile | "
                "docker-context-streamer . | docker build -")
    )
    parser.add_argument(
        'context',
        type=str,
        default='.',
        help='Path to directory to use as context'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%s %s' % (APP_NAME, APP_VERSION)
    )

    parsed = parser.parse_args()

    if sys.stdin.isatty():
        parser.error("Missing Dockerfile on STDIN")

    dockerfile = sys.stdin.read()
    dockerignore = ""
    dockerignorefile = os.path.relpath(
        os.path.join(
            parsed.context,
            '.dockerignore'
        )
    )
    if os.path.isfile(dockerignorefile):
        with open(dockerignorefile, 'r') as f:
            dockerignore = (f.read()).split('\n')

    streamer = Streamer(
        dockerfile, os.path.relpath(parsed.context), dockerignore
    )
    streamer.stream_context()
