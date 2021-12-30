
import requests
import time

if __name__ == '__main__':
    url = 'http://api.stackexchange.com/2.3/questions'
    todate = int(time.time())
    fromdate = todate - (60 * 60 * 48)
    page = 1
    pagesize = 100
    params = {'page': page, 'pagesize': pagesize, 'fromdate': fromdate, 'todate': todate, 'order': 'desc',
              'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow'}
    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            for num, item in enumerate(response.json()['items']):
                print(f"{params['page']}-{num} ", end='')
                print(item['title'])
                print(item['link'])
            if response.json()['has_more'] == False:
                print('Success!')
                print(f'Quota max: {response.json()["quota_max"]}')
                print(f'Quota_remaining: {response.json()["quota_remaining"]}')
                break
            params['page'] += 1
            # time.sleep(5)
        else:
            print(response.json())
            break