#!/usr/bin/env python
from setuptools import setup, Extension, find_packages
from distutils import sysconfig
import subprocess
import glob
import sys

srcs = [x for x in 
    glob.glob("lib2bit/*.c")]
srcs.append("py2bit.c")

#libs=[]
#if sysconfig.get_config_vars('BLDLIBRARY') is not None:
#    #Note the "-l" prefix!
#    for e in sysconfig.get_config_vars('BLDLIBRARY')[0].split():
#        if e[0:2] == "-l":
#            libs.append(e[2:])
#elif(sys.version_info[0] >= 3 and sys.version_info[1] >= 3) :
#    libs.append("python%i.%im" % (sys.version_info[0], sys.version_info[1]))
#else :
#    libs.append("python%i.%i" % (sys.version_info[0], sys.version_info[1]))

additional_libs = [sysconfig.get_config_var("LIBDIR"), sysconfig.get_config_var("LIBPL")]

module1 = Extension('py2bit',
                    sources = srcs,
                    # libraries = libs,
                    library_dirs = additional_libs, 
                    include_dirs = ['lib2bit', sysconfig.get_config_var("INCLUDEPY")])

setup(name = 'py2bit',
       version = '0.1.0',
       description = 'A package for accessing 2bit files using lib2bit',
       author = "Devon P. Ryan",
       author_email = "ryan@ie-freiburg.mpg.de",
       url = "https://github.com/dpryan79/pyBigWig",
       download_url = "https://github.com/dpryan79/py2bit/tarball/0.1.0",
       keywords = ["bioinformatics", "2bit"],
       classifier = ["Development Status :: 5 - Production/Stable",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved",
                     "Programming Language :: C",
                     "Programming Language :: Python",
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 2.7",
                     "Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.3",
                     "Programming Language :: Python :: 3.4",
                     "Programming Language :: Python :: 3.5",
                     "Programming Language :: Python :: Implementation :: CPython",
                     "Operating System :: POSIX",
                     "Operating System :: Unix",
                     "Operating System :: MacOS"],
       packages = find_packages(),
       include_package_data=True,
       ext_modules = [module1])