#!/usr/bin/env python
# coding: utf-8

# In[1]:


# transform file encoding from big5 to utf8
def big5ToUtf8(pathFile, newPathFile):
    # 開啟 Big5 輸入檔案
    inFile = open(pathFile, "r", encoding = "Big5")

    # 開啟 UTF-8 輸出檔案
    outFile = open(newPathFile, "w", encoding = "UTF-8")

    # 以 Big5 編碼讀取檔案
    content = inFile.read()

    # 以 UTF-8 編碼寫入檔案
    outFile.write(content)

    # 關閉檔案
    inFile.close()
    outFile.close()
    
# transform file encoding from big5 to utf8
def Utf8ToBig5(pathFile, newPathFile):
    # 開啟 Big5 輸入檔案
    inFile = open(pathFile, "r", encoding = "UTF-8")

    # 開啟 UTF-8 輸出檔案
    outFile = open(newPathFile, "w", encoding = "Big5")

    # 以 Big5 編碼讀取檔案
    content = inFile.read()

    # 以 UTF-8 編碼寫入檔案
    outFile.write(content)

    # 關閉檔案
    inFile.close()
    outFile.close()


# In[ ]:




