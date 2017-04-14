#coding=utf-8
import random
confFileName = "OutputJavaOfJobs/WordCount/jobConfFile.txt"
jobConfFile = open(confFileName,'w+')
#资源分配: worker上的资源分配给driver (系统资源) executor 为应用申请资源
#当前的worker内存和cpu均大于当前driver请求的mem和cpu，则启动driver
driverCores = 1 # 1-8
driverMaxResult = 512
driverMemory = 1 #1-8g
executorCores = 2 #2,4,8 #相当于App申请所需的核数 不能大于8
executorMemory= 1 #1-4g #小于4g # App所需内存大小 不能大于系统内存数量
reduceMaxSizeInFlight = 1 # (1-8m)*12
blockSize = 2 #2-8m
parallelism = 4 # cores * 1-3
shuffleIOMaxRetries = 0 #1-5
shuffleIORetryWait = 5 #1-20s 5s
cacheEntries = 1024 #512 1024 1536 2048
#workInstances = 1 #增加该值,系统中的work会增加; 一个app在一个worker上仅有一个executor;
shuffleCompress = True
spillCompress= True
broadcastCompress= True
speculation = False
inputData = 1


for i in range(1, 2001):
    driverCores = random.randint(1,8) #randint(a,b) range is [a,b]
    driverMemory = random.randint(1,8) #[1-4g]
    driverMaxResultSize = 512 * random.randint(1,4)
    executorCores = 2 * random.randint(1,4)
    executorMemory = min(8 / executorCores,random.randint(1,8))
    reduceMaxSizeInFlight = 12 * random.randint(1, 8)
    blockSize = random.randint(2,8)
    parallelism = executorCores * random.randint(1,3)
    shuffleIOMaxRetries = random.randint(0,5)
    shuffleIORetryWait = random.randint(1,20)
    cacheEntries = 512*random.randint(1,4)
    inputData = random.randint(1,100)
    #workInstances = random.randint(1,5)
    if i % 2 == 0:
        shuffleCompress = "TRUE"
    else:
        shuffleCompress = "FALSE"
    if i % 3 == 0:
        spillCompress = "TRUE"
    else:
        spillCompress = "FALSE"
    if i % 5 == 0:
        broadcastCompress = "TRUE"
    else:
        broadcastCompress = "FALSE"
    if i % 7 == 0:
        speculation = "TRUE"
    else:
        speculation = "FALSE"

    jobConfFile.write(str(driverCores) + "," +
                      str(driverMaxResultSize) + "," +
                      str(driverMemory) + "," +
                      str(executorMemory)+","+
                      str(reduceMaxSizeInFlight)+","+
                      str(blockSize)+","+
                      str(executorCores)+","+
                      str(parallelism)+","+
                      str(shuffleIOMaxRetries)+","+
                      str(shuffleIORetryWait)+","+
                      str(cacheEntries)+","+
                      shuffleCompress + "," +
                      spillCompress + "," +
                      broadcastCompress + "," +
                      speculation +","+
                      str(inputData)+"\n")

jobConfFile.close()





