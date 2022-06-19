import sys
import os
from Huffman import Huffman
from HuffmanWriters import HuffmanCompressionWriter

def compressFile(nameOfOriginalFile,nameOfCompressedFile):
    
    freq_table = get_frequency_table(nameOfOriginalFile)
    huff_tree = generateHuffmanTree(freq_table)
    
    compression_writer = HuffmanCompressionWriter()
    compression_writer.compress(huff_tree,nameOfOriginalFile,nameOfCompressedFile)

def get_frequency_table(nameOfOriginalFile):
    
    frequencyTable = [0 for x in range(256)]
    
    f = open(nameOfOriginalFile, "rb")
    while b := f.read(1):
        frequencyTable[b[0]] += 1
    f.close()
    
    return frequencyTable

def generateHuffmanTree(freq_table):
    return Huffman(freq_table)


# Execution of file starts here by reading input arguments from terminal.
nameOfOriginalFile = sys.argv[1]
nameOfCompressedFile = sys.argv[2]
compressFile(nameOfOriginalFile,nameOfCompressedFile)

