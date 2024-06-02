# FS with kernel I build

To learn more about the relationship with kernel and computer architecture,
I try to build my linux-5.10 to mount on ARM_gem5.

## Flow 
* Setting M5_PATH
* Use gem5_defconfig to make config kernel
* Build kernel
```shell
$ make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- gem5_defconfig
$ make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j `nproc`
```
* Run simulator
```shell
$ ./build/ARM/gem5.opt configs/example/arm/fs_power.py --kernel ./vmlinux --disk ./kernel.img --bootloader ./system/arm/bootloader/arm64/boot.arm64 --cache
```
* Using `m5term` to monitor kernel console
```shell
$ ./m5term 3456
```
