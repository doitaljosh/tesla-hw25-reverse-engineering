# SPI flash

## Test point and ball mapping
![Pinout](https://github.com/doitaljosh/tesla-hw25-reverse-engineering/blob/main/spi-flash/hw25-qspi-test-points.jpg)

## Scripts:

### decompile
```./decompile [dump_file.bin]```
#### Output directory structure:
1. `./dump_file.bin_extracted` - raw partition files
2. `./dump_file.bin_extracted/dts` - dtb and dts files
3. `./dump_file.bin_extracted/kernel` - compressed and uncompressed kernel images

### patch-image
#### patch a given SPI flash image with new kernels/dtbs/initrds
```./patch-image image kernel-a-dtb kernel-a kernel-a-initramfs kernel-b-dtb kernel-b kernel-b-initramfs```
