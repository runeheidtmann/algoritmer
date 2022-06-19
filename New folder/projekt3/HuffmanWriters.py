from bitIO import BitWriter
from Element import Element

class HuffmanCompressionWriter:
    
    def compress(self,huffman_tree, nameOfOriginalFile, nameOfCompressedFile):
        self.write_compressed_file(huffman_tree, nameOfOriginalFile, nameOfCompressedFile)

    def write_compressed_file(self,huffman_tree,nameOfOriginalFile,nameOfCompressedFile):    
        
        #make new compressed file
        out = open(nameOfCompressedFile, "wb")

        #write to file with BitWriter object.
        bitio = BitWriter(out)
        self.write_freq_table_to_outputfile(bitio, huffman_tree.frequencyTable)
        
        f = open(nameOfOriginalFile, "rb")
        self.writeHuffmanCode2File(f,bitio,huffman_tree)

        bitio.close()
    
    def write_freq_table_to_outputfile(self,bitio,frequencyTable):
        for freq in frequencyTable:
            bitio.writeint32bits(freq)
        
    def writeHuffmanCode2File(self,f,bitio,huff_tree):
        
        code_table = huff_tree.get_huffman_code_table()

        while b := f.read(1):
            codestring = code_table[b[0]]
            for oneBit in codestring:
                bitio.writebit(int(oneBit))

class HuffmanDecompressionWriter:
    def decompress(self,reader,root,nameOfDecodedFile):
        self.writeDecodedFile(reader,root,nameOfDecodedFile)
    
    def writeDecodedFile(self,reader,root,nameOfDecodedFile):
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
