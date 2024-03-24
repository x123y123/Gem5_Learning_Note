# Two-level cache
## System arch
<img align="center" src="https://github.com/x123y123/Gem5_Learning_Note/blob/main/two_level_cache/image/system_arch.jpg" width="500" height="700">

## Method
* Cache Simobjection we can find in `src/mem/cache/Cache.py`
* Using `BaseCache` to build our L1Icache, L1Dcache and L2cache.
* Then link them in `arm-two_level.py`

## Command 
```shell
cd gem5/configs && git clone git@github.com:x123y123/Gem5_Learning_Note.git
$ build/ARM/gem5.opt configs/two_level_cache/simple-arm.py 

gem5 Simulator System.  https://www.gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 version 22.1.0.0
gem5 compiled Nov  9 2023 14:41:49
gem5 started Mar 24 2024 05:14:05
gem5 executing on ubuntutony, pid 87925
command line: build/ARM/gem5.opt configs/learning_gem5/part1/arm-two_level.py

L1I
L1D
warn: l2bus.slave is deprecated. `slave` is now called `cpu_side_ports`
warn: l2bus.slave is deprecated. `slave` is now called `cpu_side_ports`
warn: l2bus.master is deprecated. `master` is now called `mem_side_ports`
warn: membus.slave is deprecated. `slave` is now called `cpu_side_ports`
Global frequency set at 1000000000000 ticks per second
warn: No dot file generated. Please install pydot to generate the dot file and pdf.
build/ARM/mem/dram_interface.cc:690: warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
Beginning simulation!
build/ARM/sim/simulate.cc:192: info: Entering event queue @ 0.  Starting simulation...
Hello world!
Exiting @ tick 51339000 because exiting with last active thread context
```
