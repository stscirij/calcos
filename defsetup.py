from __future__ import division, print_function # confidence high
import distutils
import distutils.core
import distutils.sysconfig

try:
    import numpy
except ImportError:
    print("NUMPY was not found. It may not be installed or it may not be on your PYTHONPATH")

pkg = "calcos"

setupargs = {
    'version' :			"3.1.7",
    'description' :		"C extension module for calcos",
    'author' :			"Phil Hodge",
    'author_email' :	"help@stsci.edu",
    'platforms' :		["Linux", "Solaris", "Mac OS X", "Windows"],
    'scripts' :			['lib/calcos/calcos'],
    'package_dir' :     { 'calcos' : 'lib/calcos', },

    'ext_modules' :		[
                            distutils.core.Extension ("calcos.ccos", ["src/ccos.c"],
                               define_macros = [('NUMPY', '1')],
                               include_dirs = [ distutils.sysconfig.get_python_inc(),
                                                numpy.get_include()
                                              ]
                            )
                        ],
}

