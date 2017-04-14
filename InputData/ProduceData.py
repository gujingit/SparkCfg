#coding=utf-8
import random
small_data_file = open('Data/data1','r') #2kb
#middle_data_file = open('Data/data2','r') #1M #513
#middle_data_file2 = open('Data/data3','w+') #10M 4911
data = small_data_file.read()

for i in range(2,42):

    index = random.randint(513,4900)
    output_file = open('Data/data' + str(i+60), 'w+')
    for i in range(index):
        output_file.write(data+'\n')
    output_file.close()


small_data_file.close()
