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
from HuffmanWriters import HuffmanCompressionWriter

def compressFile(nameOfOriginalFile,nameOfCompressedFile):
    """
    Initiating compression of file by calling relevant objects and methods in the right order.

    Parameters
    ----------
    nameOfOriginalFile : string, required
   
    nameOfCompressedFile: string, required
    """
    
    #Make Huffman tree from file.
    frequencyTable = getFrequencyTable(nameOfOriginalFile)
    huffmanTree = Huffman(frequencyTable)
    
    #Write Huffmancoded version of file to new file.
    compressionWriter = HuffmanCompressionWriter()
    compressionWriter.compress(huffmanTree,nameOfOriginalFile,nameOfCompressedFile)

def getFrequencyTable(nameOfOriginalFile):
    """
    Reading a file byte by byte.
    Returning a frequency table with frequencies of each individual byte.

    Parameters
    ----------
    nameOfOriginalFile : string, required
    """
    
    frequencyTable = [0 for x in range(256)]
    f = open(nameOfOriginalFile, "rb")
    while b := f.read(1):
        frequencyTable[b[0]] += 1
    f.close()
    
    return frequencyTable
    

# Execution of file starts here by reading input arguments from terminal.
nameOfOriginalFile = sys.argv[1]
nameOfCompressedFile = sys.argv[2]
compressFile(nameOfOriginalFile,nameOfCompressedFile)

