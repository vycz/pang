import http.client
import re

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

def print_price(codes):
    generated_url_ext = ','.join(codes)
    httpClient = generate_client(generated_url_ext)
    res = httpClient.getresponse()
    data = res.read()
    split_data = data.decode("GBK").split(';')
    for signal_data in split_data:
        matchObj = re.match( 'var hq_str_(\\w+?)=\"(.*?)\"', signal_data, re.M|re.I)
        if matchObj:
            code = matchObj.group(1)
            vars = matchObj.group(2).split(',')
            name = vars[0]
            now = vars[3]
            yesterday = vars[2]
            diff = round(float(now) - float(yesterday),2)
            diff_percent = round(float(diff) / float(yesterday),2)
            print('64 bytes from 220.181.38.148: icmp_seq=%s ttl=%s time=%s ms' % (str(diff_percent*100),str(diff),str(now)))

if __name__ == '__main__':
    httpClient = generate_client('sh600150')
    res = httpClient.getresponse()
    data = res.read()
    print(data.decode("GBK"))