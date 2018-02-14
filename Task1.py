import requests
from bs4 import BeautifulSoup
import os
import re
from string import maketrans

S_PATH = 'D:\\IR-6200\\hw3\\task1hw3' #mention source path which contains uncleaned corpus of '.html' format
D_PATH = 'D:\\IR-6200\\hw3\\parsetextfiles'  #mention destination path here to get all the cleaned corpus
CASE_FOLD = True #give false here if case folding is not required
PUNCTUATION_HANDLER = True  #give false here to retain all the punctuations

def getCleanCorpus(dirName,caseFold,phandler):
    files = os.listdir(dirName)
    for eachFile in files:
        print eachFile
        fileName = open(dirName + '\\' + eachFile, 'r+')
        data = fileName.read()

        soup = BeautifulSoup(data,'html.parser')

        # to remove formualae present in each document
        for formulae in soup('semantics'):
            formulae.decompose()
        text_data = ""

        #consider texts between only p,h1,h2,h3,h4 tags
        for data in soup.find_all(['p','h1','h2','h3','h4']):
            text_data = text_data + data.text + " "

        #to remove utf-8 data
        text_data= str(text_data.encode('ascii','ignore').decode('ascii'))
        text_data = text_data.split()
        formatted_data = " ".join(text_data)

        # regex to remove citations present in the document
        formatted_data = re.sub('\\[[0-9,.]*\\]','',formatted_data)

        # regex to remove , . and ' everywhere except in between the numbers
        formatted_data = re.sub('(?<=[^0-9])[.,\']|[.,\'](?=[^0-9])', '', formatted_data)

        # punctuation handler to remove puntuations if user needs to
        # punctuation that come under string.punctuation are considered
        if(phandler):
            intab =  "\"#!$%&()*+/:;<=>?@[\]_`{|}^~?"
            outtab = "                             "
            trantab = maketrans(intab, outtab)
            formatted_data = formatted_data.translate(trantab)

        # regex to remove extra spaces between the words
        formatted_data = re.sub('\s\s+', ' ', formatted_data)

        #to convert to lower case if user needs
        if(caseFold):
            formatted_data = formatted_data.lower()

        newFileName = eachFile.split(".html")
        f = open(D_PATH + '\\' + newFileName[0] + '.txt', 'w+')
        f.write(formatted_data)
        f.close()

#call to generate clean corpus
getCleanCorpus(S_PATH,CASE_FOLD,PUNCTUATION_HANDLER)





























