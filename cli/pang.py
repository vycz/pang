import http.client
import re
import time
import pickle
import os
import click

@click.group(invoke_without_command=True)
@click.argument('name')
def pang(name):
    mydb  = open('dbase', 'rb')
    table = pickle.load(mydb)
    code = table[name]
    while True:
        print_price(code)
        time.sleep(3)

@pang.command()
def list():
    mydb  = open('dbase', 'rb')
    if not mydb:
        return
    table = pickle.load(mydb)
    for key,value in table.items():
        print(key+'|'+value)

def generate_client(code):
    conn = http.client.HTTPSConnection("hq.sinajs.cn")
    payload = ''
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'Access-Control-Allow-Credentials': 'true',
    'Referer': 'https://finance.sina.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
    }
    conn.request("GET", "/list="+code, payload, headers)
    return conn

def print_price(code):
    httpClient = generate_client(code)
    res = httpClient.getresponse()
    data = res.read()
    #print(data.decode("GBK"))
    matchObj = re.match( 'var hq_str_(\\w+?)=\"(.*?)\";', data.decode("GBK"), re.M|re.I)
    if matchObj:
        code = matchObj.group(1)
        #print('code:'+code)
        vars = matchObj.group(2).split(',')
        name = vars[0]
        now = vars[3]
        yesterday = vars[2]
        diff = round(float(now) - float(yesterday),2)
        diff_percent = round(float(diff) / float(yesterday),2)
        print('64 bytes from 220.181.38.148: icmp_seq=%s ttl=%s time=%s ms' % (str(diff_percent*100),str(diff),str(now)))

@pang.command()
@click.option('-name',help='简写')
@click.option('-code',help='代码')
def add(name,code):
    print('1')
    if not os.path.exists('dbase'):
        table = {}
        print('2')
        mydb  = open('dbase', 'wb')  
        print('3')
        pickle.dump(table, mydb)
    print('4')
    mydb  = open('dbase', 'rb')
    print('5')
    table = pickle.load(mydb)
    table[name]=code
    print('6')
    mydb  = open('dbase', 'wb') 
    print('7') 
    pickle.dump(table, mydb)

if __name__ == '__main__':
    pang()



