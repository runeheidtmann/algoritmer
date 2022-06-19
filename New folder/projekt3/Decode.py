import sys
import os
from Huffman import Huffman
from bitIO import BitReader
from HuffmanWriters import HuffmanDecompressionWriter


def decode_file(nameOfCompressedFile,nameOfDecodedFile):
    #Read the compressed file
    reader = read_compressed_file(nameOfCompressedFile)    
    
    #Make freq_table from the first 256 x 32 bits in the file
    freq_table = get_frequency_table_from_file(reader)
    
    huff_tree = Huffman(freq_table)
    
    #When Huffman tree is made, we can read bit by bit and decompress the compressed file
    decompression_writer = HuffmanDecompressionWriter()
    decompression_writer.decompress(reader,huff_tree.root,nameOfDecodedFile)
    
    reader.close()

def read_compressed_file(nameOfCompressedFile):
    inputFile = open(nameOfCompressedFile, "rb")
    return BitReader(inputFile)

def get_frequency_table_from_file(reader):
    frequencyTable = []
    for i in range(256):
        frequencyTable.append(reader.readint32bits())

    return frequencyTable
   

#Take inputs from
nameOfCompressedFile = sys.argv[1]
nameOfDecodedFile = sys.argv[2]
decode_file(nameOfCompressedFile,nameOfDecodedFile)