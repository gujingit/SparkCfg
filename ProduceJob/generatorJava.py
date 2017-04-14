#coding=utf-8
confFileName = "OutputJavaOfJobs/WordCount/jobConfFile.txt"
javaFileName="RawJavaOfJobs/WordCount.java"
outputFileName="OutputJavaOfJobs/WordCount/"
confFile = open(confFileName,"r")
confLines = confFile.readlines()
javaFile = open(javaFileName,'r')
javaLines = javaFile.readlines()

num = 0
index = 24 #WordCount 24
for line in confLines:
    num += 1
    attr = line.strip().split(",")
    javaLines[index] = "\tString fileName = \"/home/configTuning/input/data"+attr[15]+"\";\n"
    javaLines[index+1] = "\tString[] confVar = {"\
                       +"\""+attr[0]+"\"" + ",\""+attr[1]+"m\"" + ",\"" + attr[2] + "g\"" \
                       + ",\"" + attr[3] + "g\""+ ",\"" + attr[4] + "m\"" + ",\"" + attr[5] + "m\"" \
                       + ",\"" + attr[6] + "\"" + ",\"" + attr[7] + "\"" + ",\"" + attr[8] + "\"" \
                       + ",\"" + attr[9] + "s\"" + ",\"" + attr[10] + "\"" + ",\"" + attr[11] + "\"" \
                       + ",\"" + attr[12] + "\"" + ",\"" + attr[13] + "\""+",\"" + attr[14] + "\"" \
                       + ",\"0\"" \
                       + ",\"RunTime\"" \
                       +"};\n"

    output = open(outputFileName + str(num) + ".java", "w+")
    output.writelines(javaLines)
    output.close()

javaFile.close()
confFile.close()

