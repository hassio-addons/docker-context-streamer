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

"""Docker Context Streamer.

This provides the actual Docker Context Streamer.
It will in take the given Dockerfile (via STDIN) and a path, and will
output a tar stream containing both.
"""

from fnmatch import fnmatchcase
from six import StringIO
from tarfile import TarFile, TarInfo
import sys


class Streamer(object):
    """Docker Context Streamer.

    This provides the actual Docker Context Streamer.
    It will in take the given Dockerfile (via STDIN) and a path, and will
    output a tar stream containing both.
    """

    def __init__(self, dockerfile, context, dockerignore):
        """Class init."""
        self.dockerfile = dockerfile
        self.context = context
        self.dockerignore = dockerignore

    def exclude(self, filename):
        """Exclude files from the stream."""
        if filename.startswith(self.context):
            filename = filename[len(self.context)+1:]

        if filename == 'Dockerfile' or filename == '.dockerignore':
            return True
        elif any(
            fnmatchcase(filename, pattern) for pattern in self.dockerignore
        ):
            return True
        else:
            print filename
            return False

    def stream_context(self):
        """Start streaming the tar context for Docker."""
        with TarFile.open(mode='w|', fileobj=sys.stdout) as tarfile:

            tarfile.add(
                self.context,
                arcname='.',
                exclude=self.exclude
            )

            tarinfo = TarInfo('./Dockerfile')
            tarinfo.size = len(self.dockerfile)
            tarfile.addfile(tarinfo, StringIO(self.dockerfile))
