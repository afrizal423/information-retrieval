import re
import os
import collections
import time

# This is the map where dictionary terms will be stored as keys and value will be posting list with position in the file
dictionary = {}
matrix = {}
# This is the map of docId to input file name
docIdMap = {}

class index:
    def __init__(self, path):
        self.path = path
        pass

    def proses_pertama(self):       
        docId = 1
        """
            Membuat pengulangan sesuai jumlah data txt pada suatu folder
        """
        fileList = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        """
            membuat 2 file txt
            frekuensi.txt untuk menampilkan frekuensi kemunculan suatu kata
            matrix.txt untuk menampilkan kata tersebut masuk kedalam file txt mana
        """
        fileobj = open('frekuensi.txt', 'w')
        fileobj1 = open('matrix.txt', 'w')
        for eachFile in fileList:
            position = 1
            count = 0
            # docName = "Doc_Id_" + str(docId)
            # docName =  str(docId)
            """
            Di variable bawah ini nanti akan dimasukkan id File dan nama File txtnya
            """
            docIdMap[docId] = eachFile
            """
            DI variable bawah ini kita akan mendapatkan kalimat dari tiap barisnya
            """
            lines = [line.rstrip('\n') for line in open(self.path + "/" + eachFile)]
            # print(lines) #pembuktian
            for eachLine in lines:
                """
                Di variable bawah ini kita akan memisahkan tiap kata-kata dalam 1 baris kalimat tersebut
                """
                wordList = re.split('\W+', eachLine)
                # print(wordList) #pembuktian
                while '' in wordList:
                    wordList.remove('')
                    # print("kita hapus spasi/tanda lain ", wordList) #pembuktian
                
                for word in wordList:
                    """
                    Jika kata ada di 'dictionary', cari ID dokumen.
                    Jika document id sama dengan doc id saat ini, tambahkan posisi kata ke daftar posting yang lain, buat map baru dengan docId sebagai key dan posisi sebagai value.
                    Jika kata tidak ada dalam dictionary, buat entri baru di map dengan kata sebagai key, docId dan posisinya sebagai value
                    """
                    if (word.lower() in dictionary):
                        postingList = dictionary[word.lower()]
                        if (docId in postingList):
                            postingList[docId].append(position)
                            position = position + 1
                        else:
                            postingList[docId] = [position]
                            position = position + 1
                    else:
                        dictionary[word.lower()] = {docId: [position]}
                        position = position + 1
            docId = docId + 1
        length_dict = {key: len(value) for key, value in dictionary.items()}
        """
        Membuat file frekuensi.txt
        """
        for w in length_dict:
            # ini nanti dibuat menangkap jumlah kata di suatu file txt
            # if str(w) == 'red':
            #     fileobj.write(w +"   |   "+str(length_dict[w]))
            #     fileobj.write("\n")
            fileobj.write(w +"   |   "+str(length_dict[w]))
            fileobj.write("\n")
        fileobj.close()
    

def main():
    AlamatDir = input("Masukkan nama direktori text / datasetnya  : ")
    # queryFile = input("Masukkan nama file untuk querynya : ")
    indexObj = index(AlamatDir)
    indexObj.proses_pertama()

    # print("")
    # # print("Inverted Index :")
    # indexObj.print_dict()

    # print("")
    # print("List Dokumen :")
    # indexObj.print_doc_list()
    # print("")

    # QueryLines = [line.rstrip('\n') for line in open(queryFile)]
    # for eachLine in QueryLines:
    #     wordList = re.split('\W+', eachLine)

    #     while '' in wordList:
    #         wordList.remove('')

    #     wordsInLowerCase = []
    #     for word in wordList:
    #         wordsInLowerCase.append(word.lower())
    #     indexObj.and_query(wordsInLowerCase)

if __name__ == '__main__':
    main()