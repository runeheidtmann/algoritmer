############################################################
#
#    Authors
#    -------
#    Rune Heidtmann, ruhei08@student.sdu.dk
#    Lauge Løvig Thomassen, lthom19@student.sdu.dk
#
###########################################################

import sys
from Huffman import Huffman
from bitIO import BitReader
from HuffmanWriters import HuffmanDecompressionWriter


def decode_file(nameOfCompressedFile,nameOfDecodedFile):
    """
    Initiating decompression of file by calling relevant objects and methods in the right order.

    Parameters
    ----------
    nameOfCompressedFile: string, required

    nameOfDecompressedFile : string, required
    """
    
    #Read the compressed file
    reader = readCompressedFile(nameOfCompressedFile)    
    
    #Make freqTable from the first 256 x 32 bits in the file
    freqTable = getFrequencyTableFromFile(reader)
    
    #Make Huffman tree
    huffmanTree = Huffman(freqTable)
    
    #When Huffman tree is made, we can read bit by bit (starting from where the frequencytable ended) and decompress the compressed file
    decompressionWriter = HuffmanDecompressionWriter()
    decompressionWriter.decompress(reader,huffmanTree.root,nameOfDecodedFile)
    
    reader.close()

def readCompressedFile(nameOfCompressedFile):
    inputFile = open(nameOfCompressedFile, "rb")
    return BitReader(inputFile)

def getFrequencyTableFromFile(reader):
    frequencyTable = []
    for i in range(256):
        frequencyTable.append(reader.readint32bits())

    return frequencyTable
   

#Take inputs from
nameOfCompressedFile = sys.argv[1]
nameOfDecodedFile = sys.argv[2]
decode_file(nameOfCompressedFile,nameOfDecodedFile)