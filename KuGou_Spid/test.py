from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree
import time
import csv
import random

def csv_process(filepath):
    with open(filepath,mode='r',encoding='utf-8',newline='') as f:
        datas = f.readlines()
    ran_num = random.choice(datas)
    ip = ran_num.strip().split('/r')
    proxies = {'http://'+ ip[0]}
    return proxies

def main():
    filepath = 'IP/validate.csv'
    ff=csv_process(filepath)
    print(ff)

if __name__ == '__main__':
    main()


#return IP_LEBEL[random.randint(1,i)]
#参数encoding = 'utf-8'防止出现乱码
'''
csv_file_read = open('IP/validate.csv', 'r')
i=len(csv_file_read.readlines())
#print(i)
a = random.randint(1,i)
lines = csv.reader(csv_file_read)

for line in lines:
    print(line)
    csv_file_read.close()
'''
