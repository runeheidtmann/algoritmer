############################################################
#
#    Authors
#    -------
#    Rune Heidtmann, ruhei08@student.sdu.dk
#    Lauge Løvig Thomassen, lthom19@student.sdu.dk
#
###########################################################

from bitIO import BitWriter
from AlteredElement import Element

class HuffmanCompressionWriter:
    """
    A class used to write huffman code onto new file.

    Methods
    -------
    compress()
        Initiates compression of file.
    
    writeCompressedFile():
        Writes new codes onto new file.
    
    """
    def compress(self,huffman_tree, nameOfOriginalFile, nameOfCompressedFile):
        self.writeCompressedFile(huffman_tree, nameOfOriginalFile, nameOfCompressedFile)

    def writeCompressedFile(self,huffman_tree,nameOfOriginalFile,nameOfCompressedFile):    

        #make new file
        out = open(nameOfCompressedFile, "wb")

        #write to file with BitWriter object.
        bitio = BitWriter(out)
         
        #Every Encoded file must start with the frequency tabel used to make huffman codes.
        #This is the key to decode the rest of the file.

        self.writeFrequencyTableToOutputfile(bitio, huffman_tree.frequencyTable)
        
        #Read original file once more and translate the bytes to huffman codes.
        f = open(nameOfOriginalFile, "rb")
        self.writeHuffmanCode2File(f,bitio,huffman_tree)
        f.close()

        bitio.close()
    
    def writeFrequencyTableToOutputfile(self,bitio,frequencyTable):
        for freq in frequencyTable:
            bitio.writeint32bits(freq)
        
    def writeHuffmanCode2File(self,f,bitio,huffmanTree):
        
        #Get a table with huffmancodes by traversing the huffman tree
        codeTable = huffmanTree.getHuffmanCodeTable()

        #Read every byte in file. Look up new code for the byte in the codeTable and write it onto new file.
        while b := f.read(1):
            codestring = codeTable[b[0]]
            for bit in codestring:
                bitio.writebit(int(bit))

class HuffmanDecompressionWriter:
    """
    A class used to decompress huffman-encoded files onto new file.

    Methods
    -------
    decompress(reader,root,nameOfDecodedFile)
        Initiates compression of file.
    
    writeDecodedFile(reader,root,nameOfDecodedFile):
        Writes new codes onto new file.
    
    """
    
    def decompress(self,reader,root,nameOfDecodedFile):
        self.writeDecodedFile(reader,root,nameOfDecodedFile)
    
    def writeDecodedFile(self,reader,root,nameOfDecodedFile):
        """
        Reads encoded file bit by bit. To find the right path down a huffman tree.
        If the bit is 0 it moves left down the tree. If it is 1 it moves right.
        When it finds a leaf, it writes the byte stored in the leaf.

        Parameters
        ----------
        reader : Bitreader, required
            Bitreader object helps reading bits.
            
        root : Element, required
            The root element of a huffman tree
        
        nameOfDecodedFile : string, required
            The name of the decoded output file.
        """
        out = open(nameOfDecodedFile, "wb")
    
        #Read bit by bit until end of file
        maxBytes = root.key
        bytesWritten = 0
        
        while reader.readsucces() and bytesWritten < maxBytes: 
            
            #Start search for byte at root
            x = root 
            
            #The leaf is found in the end of a sequence of bits:
            while isinstance(x.left,Element) or isinstance(x.right,Element):
                b = reader.readbit()
                if b == 0:
                    x = x.left
                if b == 1:
                    x = x.right

            #When x is a leaf-element it must hold data, which is the ordinal number of a char.
            if reader.readsucces():
                b = x.data
                out.write(bytes([b]))
                bytesWritten += 1
        
        out.close()   
