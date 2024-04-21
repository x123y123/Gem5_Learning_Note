# Different system config with coremark profiling

## Result in coremark
|simple|two_level_cache|
|------|---------------|
|gem5 Simulator System.  https://www.gem5.org \gem5 is copyrighted software; use the --copyright option for details. \gem5 version 22.1.0.0 \gem5 compiled Apr 21 2024 17:50:34 \gem5 started Apr 21 2024 19:31:20 \gem5 executing on tony-ThinkPad-X13-Gen-3, pid 271918
\ command line: build/X86/gem5.opt --outdir=simple configs/learning_gem5/part1/simple.py

Global frequency set at 1000000000000 ticks per second
build/X86/mem/dram_interface.cc:690: warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
Beginning simulation!
build/X86/sim/simulate.cc:192: info: Entering event queue @ 0.  Starting simulation...
build/X86/sim/mem_state.cc:443: info: Increasing stack size by one page.
build/X86/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
build/X86/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
build/X86/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
2K performance run parameters for coremark.
CoreMark Size    : 666
Total ticks      : 15418
Total time (secs): 15.418000
Iterations/Sec   : 38.915553
Iterations       : 600
Compiler version : GCC9.4.0
Compiler flags   : -O2 -DPERFORMANCE_RUN=1  -lrt
Memory location  : Please put data memory location here
			(e.g. code in flash, data on heap etc)
seedcrc          : 0xe9f5
[0]crclist       : 0xe714
[0]crcmatrix     : 0x1fd7
[0]crcstate      : 0x8e3a
[0]crcfinal      : 0xbd59
Correct operation validated. See README.md for run and reporting rules.
CoreMark 1.0 : 38.915553 / GCC9.4.0 -O2 -DPERFORMANCE_RUN=1  -lrt / Heap
Exiting @ tick 18261215302000 because exiting with last active thread context|gem5 Simulator System.  https://www.gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 version 22.1.0.0
gem5 compiled Apr 21 2024 17:50:34
gem5 started Apr 21 2024 18:41:08
gem5 executing on tony-ThinkPad-X13-Gen-3, pid 270958
command line: build/X86/gem5.opt configs/learning_gem5/part1/two_level.py

Global frequency set at 1000000000000 ticks per second
build/X86/mem/dram_interface.cc:690: warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
Beginning simulation!
build/X86/sim/simulate.cc:192: info: Entering event queue @ 0.  Starting simulation...
build/X86/sim/mem_state.cc:443: info: Increasing stack size by one page.
build/X86/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
build/X86/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
build/X86/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)



2K performance run parameters for coremark.
CoreMark Size    : 666
Total ticks      : 11272
Total time (secs): 11.272000
Iterations/Sec   : 975.869411
Iterations       : 11000
Compiler version : GCC9.4.0
Compiler flags   : -O2 -DPERFORMANCE_RUN=1  -lrt
Memory location  : Please put data memory location here
			(e.g. code in flash, data on heap etc)
seedcrc          : 0xe9f5
[0]crclist       : 0xe714
[0]crcmatrix     : 0x1fd7
[0]crcstate      : 0x8e3a
[0]crcfinal      : 0x33ff
Correct operation validated. See README.md for run and reporting rules.
CoreMark 1.0 : 975.869411 / GCC9.4.0 -O2 -DPERFORMANCE_RUN=1  -lrt / Heap
Exiting @ tick 12411303763000 because exiting with last active thread context
|