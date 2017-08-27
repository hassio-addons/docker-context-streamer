# Docker Context Streamer

![Project Stage][project-stage-shield]
![Maintenance][maintenance-shield]
![Awesome][awesome-shield]
[![License][license-shield]](LICENSE.md)

This little tool allows you to add file context to Dockerfiles fed to
Docker using STDIN by creating a tar file stream.

## What is does

If you, for whatever reason, are streaming your Dockerfile into the Docker
build command, your file context will be ignored by Docker. e.g., Stuff like
ADD and COPY won't work. This tool work around this problem by using Dockers
ability to accept a tar stream containing the full context. 

Pipe your in memory Dockerfile into the Docker Context Streamer,
specify the directory on disk you'd like to use as the file context, and next
stream the output of this tool into Docker build.

## Example

```bash
$ export DOCKERFILE="FROM alpine"
# Do some stuff with your Docker file here, like sed replacing or adding things
$ echo $DOCKERFILE | docker-context-streamer ./context/dir | docker build -
```

## Notice

Using this tool is a general warning sign that you are doing it wrong.
This tool is created for a very special case, where there was no other way.

## Installation

Using pip, the Python package manager:

```bash
sudo pip install docker-context-streamer
```

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our [contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Authors & contributors

The original setup of this repository is by [Franck Nijhof][frenck].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

MIT License

Copyright (c) 2017 Franck Nijhof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[awesome-shield]: https://img.shields.io/badge/awesome%3F-yes-brightgreen.svg
[license-shield]: https://img.shields.io/github/license/hassio-addons/docker-context-streamer.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2017.svg
[project-stage-shield]: https://img.shields.io/badge/Project%20Stage-Experimental-yellow.svg
