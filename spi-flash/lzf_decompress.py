import argparse
import lzf
import os
import struct

def decompress(lzf_file, out_file):

    chunk_number=1

    while True:
        prefix = lzf_file.read(2)

        if len(prefix) == 0: 
            # end of file
            print('end of file')
            break

        elif prefix!=b'ZV':
            # not a valid lzf chunk
            print("Chunk #{} is invalid, does not begin with 'ZV' ('{}' found instead)".format(chunk_number, prefix.decode('utf8')))
            break

        # it's a lzf file
        typ  = lzf_file.read(1)
        chunk_len = struct.unpack('>H', lzf_file.read(2))[0]

        if typ == b'\x00':
            print('Chunk #{} is uncompressed, {} bytes'.format(chunk_number, chunk_len))
            chunk = lzf_file.read(chunk_len)

        elif typ == b'\x01':
            uncompressed_len = struct.unpack(">H", lzf_file.read(2))[0]
            print('Chunk #{} is compressed,  {} bytes (original size: {} bytes)'.format(chunk_number, chunk_len, uncompressed_len))
            compressed_data = lzf_file.read(chunk_len)
            chunk = lzf.decompress(compressed_data, uncompressed_len)

        else:
            print('3rd bytes of chunk #{} has an invalid value: "{}". Exiting'.format(chunk_number, typ))
            return

        out_file.write(chunk)
        chunk_number += 1


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Decompress an LZF file')
    parser.add_argument('inputfile', metavar='input_file', type=str, help='the LZF file to decompress')
    parser.add_argument('outputfile', metavar='output_file', type=str, help='location to store decompressed file')
    args = parser.parse_args()

    path = args.inputfile
    path_out = args.outputfile

    with open(path,'rb') as in_file, open(path_out, 'wb') as out_file:
        decompress(in_file, out_file)

