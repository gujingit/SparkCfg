# coding=utf-8
from bs4 import BeautifulSoup as bs
import re


def extractExecutionTime():
    htmlFileName = "resultHtml/History Server.html"
    confFileName = "JavaOutput/WordCount/jobConfFile.txt"
    outputFileName = "result/wordcount.csv"

    htmlFile = open(htmlFileName, "r")
    confFile = open(confFileName, "r")
    outputFile = open(outputFileName, "w+")

    p = bs(htmlFile.read())
    durationClass = p.findAll("span", {"class": "durationClass"})
    length = durationClass.__len__()
    durationTime = [0.0] * length

    index = 0
    for item in durationClass:
        job = str(item).split(">")[1].split("<")[0].split(" ")
        if job[1] == "min":
            job[0] = float(job[0]) * 60
        durationTime[index] = job[0]
        index += 1

    confLines = confFile.readlines()
    confLen = confLines.__len__()
    if confLen != length:
        print "The length of cfgFile %d doesn't equal the length of JobHtml %d!\n" % (confLen,length)
        return 0
    i = 0
    for line in confLines:
        line = line.strip()+","+str(durationTime[i])+"\n"
        i += 1
        outputFile.writelines(line)
    #outputFile.writelines(confLines)

    htmlFile.close()
    confFile.close()
    outputFile.close()


if __name__ == "__main__":
    extractExecutionTime()





