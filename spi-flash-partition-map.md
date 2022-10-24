## Flash map:

| ID | Name | Offset | Length | Description |
| -- | ---- | ------ | ------ | ----------- |
| 0 | bct | 0x0 | 0x80000 | Boot configuration table |
| 1 | mb1-bootloader | 0x80000 | 0x40000 | Microboot 1st stage bootloader |
| 2 | mb1-bootloader-r | 0xc0000 | 0x40000 | MB1 backup |
| 3 | mb1-bct | 0x100000 | 0x40000 | MB1 boot configuration table |
| 4 | mb1-bct-r | 0x140000 | 0x40000 | MB1 BCT backup |
| 5 | fuse-bypass | 0x180000 | 0x40000 | Fuse bypass area |
| 6 | mb2-bootloader | 0x1c0000 | 0x40000 | Microboot 2nd stage bootloader |
| 7 | mb2-bootloader-r | 0x200000 | 0x40000 | MB2 backup |
| 8 | mts-preboot | 0x240000 | 0x40000 | Preboot microcode |
| 9 | mts-preboot-r | 0x280000 | 0x40000 | Preboot microcode backup |
| 10 | mts-bootpack | 0x2c0000 | 0x280000 | Bootpack microcode |
| 11 | mts-bootpack-r | 0x540000 | 0x280000 | Bootpack microcode backup |
| 12 | pt | 0x7c0000 | 0x80000 | Partition table |
| 13 | bpmp-fw | 0x840000 | 0xc0000 | Boot/power management processor firmware |
| 14 | bpmp-fw-r | 0x900000 | 0xc0000 | BPMP FW backup |
| 15 | bpmp-fw-dtb | 0x9c0000 | 0x40000 | BPMP FW device tree blob |
| 16 | bpmp-fw-dtb-r | 0xa00000 | 0x40000 | BPMP FW DTB backup |
| 17 | sce-fw | 0xa40000 | 0x40000 | SCE block firmware |
| 18 | sce-fw-r | 0xa80000 | 0x40000 | SCE FW backup |
| 19 | adsp-fw | 0xac0000 | 0x200000 | Audio DSP firmware |
| 20 | adsp-fw-r | 0xcc0000 | 0x200000 | ADSP FW backup |
| 21 | cpu-bootloader | 0xec0000 | 0x40000 | CPU bootloader |
| 22 | cpu-bootloader-r | 0xf00000 | 0x40000 | CPU bootloader backup |
| 23 | secure-os | 0xf40000 | 0x200000 | Trusted OS image |
| 24 | secure-os-r | 0x1140000 | 0x200000 | TOS backup |
| 25 | eks | 0x1340000 | 0x40000 | Encrypted keys |
| 26 | eks-r | 0x1380000 | 0x40000 | Encrypted keys backup |
| 27 | ENV | 0x13c0000 | 0x80000 | Persistent environment variables |
| 28 | recovery-linux-dtb | 0x1440000 | 0x40000 | Recovery kernel device tree blob |
| 29 | kernel-a-dtb | 0x1480000 | 0x40000 | Main kernel device tree blob |
| 30 | kernel-b-dtb | 0x14c0000 | 0x40000 | Backup kernel device tree blob |
| 31 | recovery-linux | 0x1500000 | 0xb00000 | Recovery Linux kernel |
| 32 | kernel-a | 0x2000000 | 0xc00000 | Main Linux kernel |
| 33 | kernel-a-initramfs | 0x2c00000 | 0x300000 | Main ramdisk |
| 34 | kernel-b | 0x2f00000 | 0xc00000 | Backup Linux kernel |
| 35 | kernel-b-initramfs | 0x3b00000 | 0x300000 | Backup ramdisk |
| 36 | mtdoops | 0x3e00000 | 0x200000 | Bad blocks reserved area |
