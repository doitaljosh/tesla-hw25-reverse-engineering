## Normal boot flow:

1. Boot ROM initializes flash/DRAM, checks fuses, loads BCT, then verifies and loads MB1
2. MB1 unhalts CCPLEX then verifies and loads MB2
3. MB2 verifies and loads BPMP/SCE/ADSP/TOS firmwares, then verifies and loads Quickboot
4. Quickboot unhalts BPMP then verifies and loads kernel/dtb/initramfs
5. Kernel loads/mounts initramfs then loads init scripts
6. Verify/mount eMMC rootfs then pivot_root and execute systemd
7. Systemd starts autopilot services and daemons
