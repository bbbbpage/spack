##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://scalability-llnl.github.io/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class Callpath(Package):
    """Library for representing callpaths consistently in
       distributed-memory performance tools."""

    homepage = "https://github.com/scalability-llnl/callpath"
    url      = "https://github.com/scalability-llnl/callpath/archive/v1.0.1.tar.gz"

    version('1.0.2', 'b1994d5ee7c7db9d27586fc2dcf8f373')
    version('1.0.1', '0047983d2a52c5c335f8ba7f5bab2325')

    depends_on("dyninst")
    depends_on("adept-utils")
    depends_on("mpi")

    def install(self, spec, prefix):
        # TODO: offer options for the walker used.
        cmake('.', "-DCALLPATH_WALKER=dyninst", *std_cmake_args)
        make()
        make("install")
