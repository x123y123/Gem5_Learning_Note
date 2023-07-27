# Gem5 Learning Note

## How to run it on MacOS M1 by using UTM (Ubuntu 22.04)

### Prerequisite
```shell
$ sudo apt install build-essential git m4 scons zlib1g zlib1g-dev \
    libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev \
    python3-dev python libboost-all-dev pkg-config \
    libpng-dev libhdf5-serial-dev
$ git clone https://gem5.googlesource.com/public/gem5
$ util/pre-commit-install.sh
$ python3 \`which scons\` build/ARM/gem5.opt -j1
# https://github.com/mlpack/mlpack/issues/2775
```
  
## How to run it on Ubuntu 18.04
```shell
$ sudo apt install build-essential git m4 scons zlib1g zlib1g-dev \
    libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev \
    python3-dev python libboost-all-dev pkg-config

$ git clone https://github.com/gem5/gem5
$ scons build/{ISA}/gem5.{variant} -j {cpus}
$ ./build/{ISA}/gem5.{variant} [gem5 options] {simulation script} [script options]
# https://www.gem5.org/documentation/general_docs/building
```

### Test                                                              
```shell
$ build/ARM/gem5.opt --debug-flags=Exec,-ExecSymbol configs/example/se.py --cmd=tests/test-progs/hello/bin/arm/linux/hello
```
## lmbench
- lmbench: https://github.com/intel/lmbench


