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
#### Patch a given SPI flash image with new kernels/dtbs/initrds.
```./patch-image image kernel-a-dtb kernel-a kernel-a-initramfs kernel-b-dtb kernel-b kernel-b-initramfs```

### Raspberry Pi spi-nor DTBO with partitions
#### Read and write all partitions using a RPi connected to the flash chip.
1. Copy `spiflash-tesla-ap2x.dtbo` to `/boot/overlays`.
2. Add `dtoverlay=spiflash-tesla-ap2x,flash-spi0-0` to `/boot/config.txt`

### Example
[Google Drive](https://drive.google.com/file/d/19GVI92Pjh3grQjPpLlgB7n6iioEYzzW4/view?usp=share_link)
1. Download the file from Google Drive.
2. Copy the extracted file to this directory.
3. Run the decryption script on the file to decrypt/extract it: ```./decrypt file_downloaded_from_drive.enc```
4. Run ```./decompile decrypted_file.bin```
NOTE: password is ```$p4C3b@11$```
