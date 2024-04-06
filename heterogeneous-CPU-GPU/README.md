# Heterogeneous CPU-GPU

## Set the env
* x86 thinkpad notebook
```shell
$ sudo docker pull gcr.io/gem5-test/gcn-gpu:v22-0
$ sudo docker images # Get image id
$ sudo docker run --name gem5-gpu -it $IMAGE_ID

#build gem5
$ git clone https://gem5.googlesource.com/public/gem5
$ cd gem5
$ scons build/GCN3_X86/gem5.opt -j 32

# Obtaining Squaire-GPU Sample
$ cd .. # Should be one level above
$ git clone https://gem5.googlesource.com/public/gem5-resources

# Run
$ cd ../gem5-resources/src/gpu/square
$ make square # Will spit out perl warnings but will work
$ cd ~
$ gem5/build/GCN3_X86/gem5.opt gem5/configs/example/apu_se.py -n 3 -c gem5-resources/src/gpu/square/bin/square
```


