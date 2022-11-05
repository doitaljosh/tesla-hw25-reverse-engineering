import argparse
import lzf
import os
import struct

# Copyright (c) 2016 dpanda (https://github.com/dpanda)
# Copyright (c) 2022 Joshua Currier (doitaljosh@gmail.com)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

