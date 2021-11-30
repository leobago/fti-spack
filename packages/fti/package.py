# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install fti
#
# You can edit this file again by typing:
#
#     spack edit fti
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Fti(CMakePackage):
    """FTI - Fault Tolerance Interface - multi-level checkpointing for HPC"""

    homepage = "https://fault-tolerance-interface.readthedocs.io/en/latest/"
    url      = "https://github.com/leobago/fti/archive/v1.6.tar.gz"
    git      = "https://github.com/leobago/fti/fti.git"

    maintainers = ['leobago', 'kellekai']

    version('develop', branch='develop')
    version('master',  branch='master')
    version('1.6',   sha256='fbeb4f873b1ca03b23d9054f882009f138a836e4da9ab04de5e9d43e4eadb65f', preferred=True)
    version('1.5',   sha256='c839d796adb462dd68c19d1cab005d52b4151933e471253530e52e5ec5272abb')
    version('1.4',   sha256='fb0c16c87e1249bcd5340884b61cf5ec1a88a43dbbaf8743ece04ce3c8987d2c')
    version('1.3',   sha256='dded205de589d886a52c3859d433ba8dee3c620cb007fe30cd9aaf00cd0365eb')
    version('1.2',   sha256='795ab4c85958d0fe390dca2d1d3b086c511fb74ea1392436246c53ee17b2b923')
    version('1.1',   sha256='c990f694f0a6306fb653c9c95dea15054c2226783cf880ff8b8b37c76248fd6a')
    version('1.0',   sha256='12e92f8b89ccc905dd1cefba510f79e200c026583fc19dee85fa0ce9e4e6e656')
    version('0.9.8', sha256='354b62443594eb0931e2eb21c737fd92786b6cb6ec961530b9fc58c28505912e')
    version('0.9.7', sha256='77ff9c0fe35f400fb52916f1ce15b14bbb1ad9fda16b4231d44dff0d44e3cfd0')
    version('0.9.6', sha256='f13886ab140549da483d94d3a35afa242af95041b833a7f17deabc2db55a9f76')

    variant('fortran',       default=True, description = 'Enables the generation of the Fortran wrapper for FTI')
    variant('examples',      default=False, when='@1.6:', description = 'Enables the generation of examples')
    variant('sion',          default=False, when='@0.9.8:', description = 'Enables the parallel I/O SIONlib for FTI')
    variant('hdf5',          default=True, when='@1.1:', description = 'Enables the HDF5 checkpoints for FTI')
    variant('fiio',          default=False, when='@1.3:', description = 'Enables the I/O failure injection mechanism')
    variant('lustre',        default=False, when='@1.0:', description = 'Enables Lustre Support')
    variant('doc',           default=False, when='@1.6:', description = 'Enables the generation of a Doxygen documentation')
    variant('tutorial',      default=False, when='@1.6:', description = 'Enables the generation of tutorial files')

    depends_on('zlib',                          type=('build', 'link', 'run'))
    depends_on('mpi',                           type=('build', 'link', 'run'))
    depends_on('cmake@3.4:',                    type='build')
    depends_on('hdf5+mpi+shared+hl',            type=('build', 'link', 'run'), when='+hdf5')
    depends_on('hdf5+mpi+shared+hl+fortran',    type=('build', 'link', 'run'), when='+hdf5+fortran')
    depends_on('sionlib@1.7.6',                 type=('build', 'link', 'run'), when='+sion')
    depends_on('doxygen',                       type='build', when='+doc')

    def cmake_args(self):
        if '+fortran' in self.spec and (self.compiler.f90 is None) or (self.compiler.fc is None):
            raise InstallError('+fortran was selected, however, no Fortran compiler is available!')
        args = [
            self.define_from_variant('ENABLE_FORTRAN', 'fortran'),
            self.define_from_variant('ENABLE_EXAMPLES', 'examples'),
            self.define_from_variant('ENABLE_SIONLIB', 'sion'),
            self.define_from_variant('ENABLE_HDF5', 'hdf5'),
            self.define_from_variant('ENABLE_FI_IO', 'fiio'),
            self.define_from_variant('ENABLE_LUSTRE', 'lustre'),
            self.define_from_variant('ENABLE_DOCU', 'doc'),
            self.define_from_variant('ENABLE_TUTORIAL', 'tutorial'),
        ]
        if self.spec.satisfies('@1.4:'):
            args = args + [
                self.define('ENABLE_IME_NATIVE', False),
            ]
        if self.spec.satisfies('@0.9.8:'):
            args = args + [
                self.define('ENABLE_TESTS', False),
            ]
        return args

