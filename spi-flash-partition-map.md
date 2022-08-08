## Flash map:

| ID | Name | Offset | Length | Description |
| -- | ---- | ------ | ------ | ----------- |
| 0 | bct-normal | 0x0 | 0x20000 | Normal boot configuration table |
| 1 | bct-normal-bak | 0x20000 | 0x20000 | Normal BCT backup |
| 2 | bct-safe | 0x40000 | 0x20000 | Safe boot configuration table |
| 3 | bct-safe-bak | 0x60000 | 0x20000 | Safe BCT backup |
| 4 | mb1 | 0x80000 | 0x40000 | Microboot 1st stage bootloader |
| 5 | mb1-b | 0xc0000 | 0x40000 | MB1 backup |
| 6 | mb1-bct | 0x100000 | 0x40000 | MB1 boot configuration table |
| 7 | mb1-bct-b | 0x140000 | 0x40000 | MB1 BCT backup |
| 8 | mb2 | 0x1c0000 | 0x40000 | Microboot 2nd stage bootloader |
| 9 | mb2-b | 0x200000 | 0x40000 | MB2 backup |
| 10 | mts-preboot | 0x240000 | 0x40000 | Preboot microcode |
| 11 | mts-preboot-b | 0x280000 | 0x40000 | Preboot microcode backup |
| 12 | mts-proper | 0x2c0000 | 0x280000 | Proper microcode |
| 13 | mts-proper-b | 0x540000 | 0x280000 | Proper microcode backup |
| 14 | bpmp-fw | 0x840000 | 0xc0000 | Boot/power management processor firmware |
| 15 | bpmp-fw-b | 0x900000 | 0xc0000 | BPMP FW backup |
| 16 | bpmp-fw-dtb | 0x9c0000 | 0x40000 | BPMP FW device tree blob |
| 17 | bpmp-fw-dtb-b | 0xa00000 | 0x40000 | BPMP FW DTB backup |
| 18 | sce-fw | 0xa40000 | 0x40000 | SCE block firmware |
| 19 | sce-fw-b | 0xa80000 | 0x40000 | SCE FW backup |
| 20 | adsp-fw | 0xac0000 | 0x200000 | Audio DSP firmware |
| 21 | adsp-fw-b | 0xcc0000 | 0x200000 | ADSP FW backup |
| 22 | cpu-bootloader | 0xec0000 | 0x280000 | Quickboot loader |
| 23 | cpu-bootloader-dtb | 0xf00000 | 0x40000 | QB device tree blob |
| 24 | secure-os | 0xf40000 | 0x200000 | Trusted OS image |
| 25 | secure-os-b | 0x1140000 | 0x200000 | TOS backup |
| 26 | eks | 0x1340000 | 0x40000 | Encrypted keys |
| 27 | eks-b | 0x1380000 | 0x40000 | Encrypted keys backup |
| 28 | env | 0x13c0000 | 0x80000 | Persistent environment variables |
| 29 | recovery-linux-dtb | 0x1440000 | 0x40000 | Recovery kernel device tree blob |
| 30 | kernel-a-dtb | 0x1480000 | 0x40000 | Main kernel device tree blob |
| 31 | kernel-b-dtb | 0x14c0000 | 0x40000 | Backup kernel device tree blob |
| 32 | recovery-linux | 0x1500000 | 0xb00000 | Recovery Linux kernel |
| 33 | kernel-a | 0x2000000 | 0xc00000 | Main Linux kernel |
| 34 | kernel-a-initramfs | 0x2c00000 | 0x300000 | Main ramdisk |
| 35 | kernel-b | 0x2f00000 | 0xc00000 | Backup Linux kernel |
| 36 | kernel-b-initramfs | 0x3b00000 | 0x500000 | Backup ramdisk |
