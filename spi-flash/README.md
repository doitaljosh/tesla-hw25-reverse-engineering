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

## Example
[Google Drive](https://drive.google.com/file/d/19GVI92Pjh3grQjPpLlgB7n6iioEYzzW4/view?usp=share_link)
1. Download the file from Google Drive.
2. Copy the downloaded file to this directory.
3. Run the decryption script on the file to decrypt/extract it: ```./decrypt file_downloaded_from_drive.enc```
4. Run ```./decompile decrypted_file.bin```
NOTE: password is ```$p4C3b@11$```
