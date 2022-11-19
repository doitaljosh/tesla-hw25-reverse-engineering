## SPI Flash map:
# Chip size = 67108864
| ID | Name | Offset | Length | Description | MTD partition ID |
| -- | ---- | ------ | ------ | ----------- | ---------------- |
| 1 | bct | 0x0 | 0x80000 | Boot configuration table | /dev/mtd35 |
| 2 | mb1-bootloader | 0x80000 | 0x40000 | Microboot 1st stage bootloader | /dev/mtd34 |
| 3 | mb1-bootloader-r | 0xc0000 | 0x40000 | MB1 backup | /dev/mtd33 |
| 4 | mb1-bct | 0x100000 | 0x40000 | MB1 boot configuration table | /dev/mtd32 |
| 5 | mb1-bct-r | 0x140000 | 0x40000 | MB1 BCT backup | /dev/mtd31 |
| 6 | fuse-bypass | 0x180000 | 0x40000 | Fuse bypass area | /dev/mtd30 |
| 7 | mb2-bootloader | 0x1c0000 | 0x40000 | Microboot 2nd stage bootloader | /dev/mtd29 |
| 8 | mb2-bootloader-r | 0x200000 | 0x40000 | MB2 backup | /dev/mtd28 |
| 9 | mts-preboot | 0x240000 | 0x40000 | Preboot microcode | /dev/mtd27 |
| 10 | mts-preboot-r | 0x280000 | 0x40000 | Preboot microcode backup | /dev/mtd26 |
| 11 | mts-bootpack | 0x2c0000 | 0x280000 | Bootpack microcode | /dev/mtd25 |
| 12 | mts-bootpack-r | 0x540000 | 0x280000 | Bootpack microcode backup | /dev/mtd24 |
| 13 | pt | 0x7c0000 | 0x80000 | Partition table | /dev/mtd23 |
| 14 | bpmp-fw | 0x840000 | 0xc0000 | Boot/power management processor firmware | /dev/mtd22 |
| 15 | bpmp-fw-r | 0x900000 | 0xc0000 | BPMP FW backup | /dev/mtd21 |
| 16 | bpmp-fw-dtb | 0x9c0000 | 0x40000 | BPMP FW device tree blob | /dev/mtd20 |
| 17 | bpmp-fw-dtb-r | 0xa00000 | 0x40000 | BPMP FW DTB backup | /dev/mtd19 |
| 18 | sce-fw | 0xa40000 | 0x40000 | SCE block firmware | /dev/mtd18 |
| 19 | sce-fw-r | 0xa80000 | 0x40000 | SCE FW backup | /dev/mtd17 |
| 20 | adsp-fw | 0xac0000 | 0x200000 | Audio DSP firmware | /dev/mtd16 |
| 21 | adsp-fw-r | 0xcc0000 | 0x200000 | ADSP FW backup | /dev/mtd15 |
| 22 | cpu-bootloader | 0xec0000 | 0x40000 | CPU bootloader | /dev/mtd14 |
| 23 | cpu-bootloader-r | 0xf00000 | 0x40000 | CPU bootloader backup | /dev/mtd13 |
| 24 | secure-os | 0xf40000 | 0x200000 | Trusted OS image | /dev/mtd12 |
| 25 | secure-os-r | 0x1140000 | 0x200000 | TOS backup | /dev/mtd11 |
| 26 | eks | 0x1340000 | 0x40000 | Encrypted keys | /dev/mtd10 |
| 27 | eks-r | 0x1380000 | 0x40000 | Encrypted keys backup | /dev/mtd9 |
| 28 | ENV | 0x13c0000 | 0x80000 | Persistent environment variables | /dev/mtd8 |
| 29 | recovery-linux-dtb | 0x1440000 | 0x40000 | Recovery kernel device tree blob | /dev/mtd7 |
| 30 | kernel-a-dtb | 0x1480000 | 0x40000 | Main kernel device tree blob | /dev/mtd6 |
| 31 | kernel-b-dtb | 0x14c0000 | 0x40000 | Backup kernel device tree blob | /dev/mtd5 |
| 32 | recovery-linux | 0x1500000 | 0xb00000 | Recovery Linux kernel | /dev/mtd4 |
| 33 | kernel-a | 0x2000000 | 0xc00000 | Main Linux kernel | /dev/mtd3 |
| 34 | kernel-a-initramfs | 0x2c00000 | 0x300000 | Main ramdisk | /dev/mtd2 |
| 35 | kernel-b | 0x2f00000 | 0xc00000 | Backup Linux kernel | /dev/mtd1 |
| 36 | kernel-b-initramfs | 0x3b00000 | 0x300000 | Backup ramdisk | /dev/mtd0 |
| 37 | mtdoops | 0x3e00000 | 0x200000 | Bad blocks reserved area |

## eMMC Flash map:
# Chip size = 31268519424
| ID | Name | Offset | Length | Description |
| -- | ---- | ------ | ------ | ----------- |
| 38 | fs-gp1 | 0x0 | 0x40000 | ??? |
| 39 | rootfs-a | 0x40000 | 0x40000000 | Primary root filesystem |
| 40 | rootfs-b | 0x40040000 | 0x40000000 | Secondary root filesystem |
| 41 | var | 0x8004000 | 0x40000000 | /var |
| 42 | home | 0xc0040000 | 0x680000000 | /home |
| 43 | fs-gpt | 0x747bfbe00 | 0x4200 | GPT |
