# FTI-Spack
Spack repository for FTI (https://github.com/leobago/fti.git).
# Add Package to Spack
1) clone fti spack-repo into the repos directory of the spack installation  
`git clone https://github.com/leobago/fti-spack <spack_path>/var/spack/repos/`  
2) Add the Repo  
`spack repo add spack/var/spack/repos/fti`  
# Versions  
to list the available versions and variants, issue:   
`spack info fti`  
# Install FTI  
for a basic installation do:    
`spack install fti`  
To install a variant (e.g. HDF5, SIONlib, etc.) add +variant. For instance:    
`spack install fti+hdf5`  
to install FTI with HDF5 support.  
  
For more information about spack, visit https://spack-tutorial.readthedocs.io/en/latest/index.html
# Dependencies
To install FTI with SIONlib support, please install the sionlib spack-package from  
-> https://gitlab.version.fz-juelich.de/cstao-public/SIONlib/spack-repository  
