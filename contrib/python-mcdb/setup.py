#! /usr/bin/env python

from distutils.core import setup, Extension

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    ('License :: OSI Approved :: GNU Library or Lesser General Public '
     'License (LGPL)'),
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules']

setup (
        name = "python-mcdb",
        version = "0.01",
        description = "Interface to mcdb constant database files",
        url = "https://github.com/gstrauss/mcdb/",
        author = "gstrauss",
        author_email = "code()gluelogic.com",
        license = "LGPL",
        classifiers = classifiers,
        long_description = \
'''Python interface to create and read mcdb constant databases.

The python-mcdb extension module wraps interfaces in libmcdb.so
See https://github.com/gstrauss/mcdb/ for latest info on mcdb.
mcdb is based on D. J. Bernstein's constant database package
(see http://cr.yp.to/cdb.html).''',
        platforms = 'POSIX, Unix',
        ext_modules = [ Extension( "mcdb",
                                   ["src/mcdbpy.c"],
                                   # compile,link with local, static libmcdb.a
                                   include_dirs=["../../.."],
                                   extra_link_args=["../../libmcdb.a",
                                     "-Wl,--version-script,src/pythonext.map"],
                                   # compile,link with system libmcdb.so
                                   #libraries=['mcdb']
                                 )
                      ],
      )
