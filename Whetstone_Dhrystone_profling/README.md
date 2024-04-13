# Whetstone/Dhrystone with gem5

## Running Whetstone
Found the `Whetstone` from (Netlib)[https://www.netlib.org/benchmark/whetstone.c].
And placed it into `tests/test-progs/whetstone/src/whetstone.c`.
### Compiling Whetstone
```shell
$ g++ -static -o whetstone whetstone.c
```

### Run with gem5
Replaced the benchmark path into simple.py
```python
binary = 'tests/test-progs/whetstone/src/whetstone'
# for gem5 V21 and beyond
system.workload = SEWorkload.init_compatible(binary)
process = Process()
process.cmd = [binary, '-c', 3000]
```
And Run
```shell
$ build/X86/gem5.opt configs/learning_gem5/part1/simple.py
```
You will get the result
```shell
gem5 Simulator System.  https://www.gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 version 23.0.0.1
gem5 compiled Apr 13 2024 06:03:58
gem5 started Apr 13 2024 06:21:40
gem5 executing on 09486f5328c1, pid 18167
command line: build/X86/gem5.opt configs/learning_gem5/part1/simple.py

Global frequency set at 1000000000000 ticks per second
src/mem/dram_interface.cc:690: warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
src/base/statistics.hh:279: warn: One of the stats is a legacy stat. Legacy stat is a stat that does not belong to any statistics::Group. Legacy stat is deprecated.
system.remote_gdb: Listening for connections on port 7000
Beginning simulation!
src/sim/simulate.cc:194: info: Entering event queue @ 0.  Starting simulation...
src/sim/mem_state.cc:443: info: Increasing stack size by one page.
src/sim/syscall_emul.hh:1014: warn: readlink() called on '/proc/self/exe' may yield unexpected results in various settings.
      Returning '/gem5/tests/test-progs/benchmark/whetstone/src/whetstone'
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)

Loops: 3000, Iterations: 1, Duration: 39 sec.
C Converted Double Precision Whetstones: 7.7 MIPS
```


