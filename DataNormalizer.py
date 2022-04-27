import os
import pandas as pd

inputFolder = "./data/to-convert/"
outputFolder = "./data/converted/"

nonNumberColumns = ["phrase", "label"]

def getOutputFileLocation(fileName):
    return outputFolder + fileName

def getFileAndProperties(folderPath):
    #we shall store all the file names in this list
    filelist = []
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            #append the file name to the list
            filelist.append((file, os.path.join(root,file)))
    return filelist

getFileList = getFileAndProperties("./data/to-convert/")
for file, location in getFileList:
    totalDf = pd.read_csv(location)
    df = totalDf.loc[:, list(set(totalDf.columns) - set(nonNumberColumns))]
    df=(df-df.min())/(df.max()-df.min())    # min-max normalization:
    #df=(df-df.mean())/df.std()  ## mean normalization
    df["phrase"] = totalDf["phrase"]
    df["label"] = totalDf["label"]
    df.to_csv(getOutputFileLocation(file), index=False)
print("Done")