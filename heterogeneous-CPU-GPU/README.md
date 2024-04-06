# Heterogeneous CPU-GPU

## Docker command
```shell
# Docker container image
$ sudo docker images

# Run container
$ sudo docker run --name gem5-gpu -it $IMAGE_ID

# Install something in docker
$ apt-get update

# Exit docker
$ exit

# If container running in background, use the following command
$ sudo docker attach gem5-gpu
```


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

## Result
```shell
root@09486f5328c1:/# gem5/build/GCN3_X86/gem5.opt gem5/configs/example/apu_se.py -n 3 -c gem5-resources/src/gpu/square/bin/square
gem5 Simulator System.  https://www.gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 version 23.0.0.1
gem5 compiled Apr  6 2024 04:50:59
gem5 started Apr  6 2024 04:57:46
gem5 executing on 09486f5328c1, pid 19879
command line: gem5/build/GCN3_X86/gem5.opt gem5/configs/example/apu_se.py -n 3 -c gem5-resources/src/gpu/square/bin/square

Num SQC =  1 Num scalar caches =  1 Num CU =  4
warn: The `get_runtime_isa` function is deprecated. Please migrate away from using this function.
warn: The `get_runtime_isa` function is deprecated. Please migrate away from using this function.
warn: The `get_runtime_isa` function is deprecated. Please migrate away from using this function.
warn: The `get_runtime_isa` function is deprecated. Please migrate away from using this function.
warn: The `get_runtime_isa` function is deprecated. Please migrate away from using this function.
Global frequency set at 1000000000000 ticks per second
warn: system.ruby.network adopting orphan SimObject param 'ext_links'
warn: system.ruby.network adopting orphan SimObject param 'int_links'
src/mem/dram_interface.cc:690: warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
src/base/statistics.hh:279: warn: One of the stats is a legacy stat. Legacy stat is a stat that does not belong to any statistics::Group. Legacy stat is deprecated.
src/base/stats/storage.hh:278: warn: Bucket size (5) does not divide range [1:75] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:10] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:64] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (5) does not divide range [1:75] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:10] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:64] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (5) does not divide range [1:75] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:10] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:64] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (5) does not divide range [1:75] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:10] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (2) does not divide range [1:64] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/statistics.hh:279: warn: One of the stats is a legacy stat. Legacy stat is a stat that does not belong to any statistics::Group. Legacy stat is deprecated.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
src/base/stats/storage.hh:278: warn: Bucket size (10000) does not divide range [1:1.6e+06] into equal-sized buckets. Rounding up.
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
src/base/statistics.hh:279: warn: One of the stats is a legacy stat. Legacy stat is a stat that does not belong to any statistics::Group. Legacy stat is deprecated.
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
Forcing maxCoalescedReqs to 32 (TLB assoc.) 
system.remote_gdb: Listening for connections on port 7000
src/sim/simulate.cc:194: info: Entering event queue @ 0.  Starting simulation...
src/mem/ruby/system/Sequencer.cc:606: warn: Replacement policy updates recently became the responsibility of SLICC state machines. Make sure to setMRU() near callbacks in .sm files!
src/sim/mem_state.cc:443: info: Increasing stack size by one page.
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall set_robust_list(...)
src/sim/syscall_emul.cc:85: warn: ignoring syscall rt_sigaction(...)
      (further warnings will be suppressed)
src/sim/syscall_emul.cc:85: warn: ignoring syscall rt_sigprocmask(...)
      (further warnings will be suppressed)
src/sim/syscall_emul.cc:74: warn: ignoring syscall get_mempolicy(...)
src/arch/generic/debugfaults.hh:145: warn: MOVNTDQ: Ignoring non-temporal hint, modeling as cacheable!

build/GCN3_X86/arch/x86/generated/exec-ns.cc.inc:27: warn: instruction 'frndint' unimplemented
src/sim/mem_state.cc:443: info: Increasing stack size by one page.
src/gpu-compute/gpu_compute_driver.cc:710: warn: unimplemented ioctl: AMDKFD_IOC_ACQUIRE_VM
src/sim/syscall_emul.hh:1890: warn: mmap: writing to shared mmap region is currently unsupported. The write succeeds on the target, but it will not be propagated to the host or shared mappings
src/sim/mem_state.cc:443: info: Increasing stack size by one page.
src/gpu-compute/gpu_compute_driver.cc:460: warn: Signal events are only supported currently
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/power_state.cc:105: warn: PowerState: Already in the requested power state, request ignored
src/sim/syscall_emul.cc:74: warn: ignoring syscall set_robust_list(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/gpu-compute/gpu_compute_driver.cc:604: warn: unimplemented ioctl: AMDKFD_IOC_SET_SCRATCH_BACKING_VA
src/gpu-compute/gpu_compute_driver.cc:614: warn: unimplemented ioctl: AMDKFD_IOC_SET_TRAP_HANDLER
info: running on device 
info: architecture on AMD GPU device is: 801
info: allocate host and device mem (  7.63 MB)
info: launch 'vector_square' kernel
src/sim/syscall_emul.cc:85: warn: ignoring syscall sched_yield(...)
      (further warnings will be suppressed)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall set_robust_list(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall madvise(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall sched_setaffinity(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall set_robust_list(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
src/sim/syscall_emul.cc:74: warn: ignoring syscall mprotect(...)
info: check result

PASSED!
Ticks: 139381328500
Exiting because  exiting with last active thread context

```


