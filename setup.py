#!/usr/bin/env python3

import setuptools

setuptools.setup(
        name = 'mpms',
        version = '0.0.2',
        packages = ['mpms'],
        entry_points = {
            'console_scripts':[
                'mpms = mpms.__main__:plot',
                'mpmsraw = mpms.__main__:raw_refitter',
                'mpmsgui = mpms.gui:main',
                ],
            },
        install_requires = [
            "importlib-metadata;python_version<'3.8'",
            "jedi==0.17.2;python_version<'3.7'",
            'pyside2',
            'numpy',
            'matplotlib',
            'scipy',
            'ipython',
            'lmfit',
            ],
        )
