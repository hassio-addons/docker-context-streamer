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

"""
Docker Context Streamer.

This little tool allows you to add file context to Dockerfiles fed to
Docker using STDIN by creating a tar file stream.
"""


APP_NAME = 'docker-context-streamer'
APP_VERSION = '0.0.3'
APP_DESCRIPTION = __doc__

__author__ = 'Franck Nijhof'
__email__ = 'frenck@geekchimp.com'
__copyright__ = 'Copyright 2017, Franck Nijhof'
__license__ = 'GPLv3'
__url__ = 'https://github.com/hassio-addons/docker-context-streamer'
__download__ = 'https://github.com/hassio-addons/docker-context-streamer/archive/0.0.3.tar.gz'
__version__ = APP_VERSION
