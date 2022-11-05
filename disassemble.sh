#!/bin/bash

FLASH_SIZE=67108864
BCH_SIZE="0x200"
OUT_DIR="${PWD}/${1}_extracted"
DTS_DIR="${OUT_DIR}/dts"

dd_func() {
	INFILE=$1
	OUTFILE=$2
	OFFSET=$3
	LENGTH=$4
	BS=1024

	if (( $(($OFFSET)) % $BS == 0 )); then
		SKIP=$((${OFFSET}/${BS}))
	else
		SKIP=0
	fi

	echo "Skipping to $((${OFFSET}))"

	dd if=$INFILE of=$OUTFILE bs=$BS skip=$SKIP count=$(($LENGTH/$BS))
}

extract_section() {
	dd_func $1 $1_extracted/$2 $3 $4
}

# Extract all binaries from the given SPI ROM dump
extract_all() {
	extract_section $1 bct.bin 0x0 0x80000
	extract_section $1 mb1.bin 0x80000 0x40000
	extract_section $1 mb1-bct.bin 0x100000 0x40000
	extract_section $1 fuse-bypass.bin 0x180000 0x40000
	extract_section $1 mb2.bin 0x1c0000 0x40000
	extract_section $1 mts-preboot.bin 0x240000 0x40000
	extract_section $1 mts-bootpack.bin 0x2c0000 0x280000
	extract_section $1 pt.bin 0x7c0000 0x80000
	extract_section $1 bpmp-fw.bin 0x840000 0xc0000
	extract_section $1 bpmp-fw-dtb.bin 0x9c0000 0x40000
	extract_section $1 sce-fw.bin 0xa40000 0x40000
	extract_section $1 adsp-fw.bin 0xac0000 0x200000
	extract_section $1 cpu-bootloader.bin 0xec0000 0x40000
	extract_section $1 secure-os.bin 0xf40000 0x200000
	extract_section $1 eks.bin 0x1340000 0x40000
	extract_section $1 ENV.bin 0x13c0000 0x80000
	extract_section $1 recovery-linux-dtb.bin 0x1440000 0x40000
	extract_section $1 kernel-a-dtb.bin 0x1480000 0x40000
	extract_section $1 kernel-b-dtb.bin 0x14c0000 0x40000
	extract_section $1 recovery-linux.img 0x1500000 0xb00000
	extract_section $1 kernel-a.img 0x2000000 0xc00000
	extract_section $1 kernel-a-initramfs.img 0x2c00000 0x300000
	extract_section $1 kernel-b.img 0x2f00000 0xc00000
	extract_section $1 kernel-b-initramfs.img 0x3b00000 0x300000
}

remove_ext() {
	cut -f 1 -d '.' $1
}

dtb_bin_to_dts() {
	DTB=$(echo $1 | remove_ext).dtb
	DTS=$(echo $1 | remove_ext).dts
	echo "Decompiling to ${DTS}"
	dd if=$OUT_DIR/$1 of=$DTS_DIR/$DTB bs=32 skip=$(($BCH_SIZE/32))
	dtc -I dtb -O dts -o $DTS_DIR/$DTS $DTS_DIR/$DTB
}

if [ ! -d $OUT_DIR ]; then
        mkdir $OUT_DIR
fi

if [ ! -d $DTS_DIR ]; then
        mkdir $DTS_DIR
fi

echo "extracting images from ${1}..."

if [[ $# -ne 0 ]]; then
	if [[ $(wc -c $1 | awk '{print $1}') == $FLASH_SIZE ]]; then
		extract_all $1

		echo "decompiling device trees..."

		dtb_bin_to_dts bpmp-fw-dtb.bin
		dtb_bin_to_dts recovery-linux-dtb.bin
		dtb_bin_to_dts kernel-a-dtb.bin
		dtb_bin_to_dts kernel-b-dtb.bin
	else
		echo "error: file size of dump must be ${FLASH_SIZE}"
	fi

	echo "done"
else
	echo "usage: ${0} [ROM dump file]"
fi
