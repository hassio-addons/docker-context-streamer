# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from dcs import (
    __author__, __email__, __license__, __url__, __download__,
    APP_NAME, APP_VERSION, APP_DESCRIPTION
)

setup(
    name=APP_NAME,
    version=APP_VERSION,
    author=__author__,
    author_email=__email__,
    description=APP_DESCRIPTION.split('\n')[0],
    long_description=APP_DESCRIPTION,
    license=__license__,
    url=__url__,
    download_url=__download__,
    keywords=['docker', 'dockerfile', 'stream'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    requires=["six"],
    install_requires=["six >=1.10"],
    tests_require=['tox'],
    entry_points={'console_scripts': [
        'docker-context-streamer=dcs.cli:run',
        'dcs=dcs.cli:run'
    ]}
)