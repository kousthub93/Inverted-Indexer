^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

STEPS TO RUN TASK 1:

1. Provide the source directory ('S_PATH' - gloabl variable in the code) which includes uncleaned raw corpus present in    '.html' format (raw_html data) .
2. Provide the destination directory ('D_PATH' - global variable in the code) where cleaned corpus will be generated for    use in task2
3. To avoid default case folding, change the value of the gloabl variable 'CASE_FOLD' to False.
4. To avoid default punctuation handling, change the value of the global variable 'PUNCTUATION_HANDLER' to False.
5. Import the following:

   import requests
   from bs4 import BeautifulSoup
   import os
   import re
   from string import maketrans

6. Navigate to the directory in which the file Task1.py is present and run the following command
   python Task1.py.
   
Notes:
- The list of puntuations removed are taken from 'string.puntuation' function which provides a list of punctuations usually considered in python
- hyphens are not removed.
- ,.' are not removed if these are present between the numbers. 

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

STEPS TO RUN TASK 2:
1. Provide source directory in 'S_PATH'- global variable which includes cleaned coprus in '.txt' format(processed data).
2. Import the following:
   
   import requests
   from bs4 import BeautifulSoup
   import os
   import re
   from string import maketrans
   import operator
  	
3. Navigate to the directory in which the file Task2.py is present and run the following command
   python Task2.py.
4. Toatl 12 files will be generated as part of the assignment which are listed below.
5. Dictionary data structure is considered mainly to implement inverted index where,
   key is the term and value is again a dictionary having filname as key and frequency of word in that file as value

Note: It approximately takes 3 min 30 sec to generate all 12 files as part of the assignment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FILES PRESENT IN HERE:

1. Task1.py               - Code to get cleaned corpus 
2. Task2.py               - Code to generate files as part of task2 and task 3
2. inverted_index_unigram - inverted index for unigrams-task2
3. inverted_index_bigram  - inverted index for bigrams-task2
4. inverted_index_trigram - inverted index for trigrams-task2
6. Unigram_Tf             - term frequency table for unigram-task3.1
7. Bigram_Tf              - term frequency table for bigram-task3.1
8. Trigram_Tf             - term frequency table for triigram-task3.1
9. Unigram_Df             - document frequeny table for unigrams-task3.2
10.Bigram_Df              - document frequeny table for bigrams-task3.2
11.Trigram_Df             - document frequeny table for trigrams-task3.2
12.unigram_tokens         - table comprising filenames and number of tokens in that for unigram - task2
13.bigram_tokens          - table comprising filenames and number of tokens in that for bigrams - task2
14.trigram_tokens         - table comprising filenames and number of tokens in that for trigrams - task2
15.StopList.text          - Generation of stop lists and explaination for cut off frequency- task3.3
16.README.txt             - Readme file providing various information on how to run the programs

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^