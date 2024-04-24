# Extending custom RISC-V instruction

## Setup RISC-V toolchain
```shell
$ git clone https://github.com/riscv/riscv-gnu-toolchain && cd riscv-gnu-toolchain
$ ./configure --prefix=/opt/riscv32_custom --with-arch=rv32gc --with-abi=ilp32d
$ make
```

