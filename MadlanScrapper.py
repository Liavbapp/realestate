import time

import pandas as pd
from bs4 import BeautifulSoup
import codecs
import requests
import ast
from urllib.request import Request, urlopen
# from fake_useragent import UserAgent
import random
from bs4 import BeautifulSoup
from IPython.core.display import clear_output
from Utils.CommonStr import MadlanAssetInfo


class MadlanScrapper:

    def __init__(self, headers, proxy):
        self.headers = headers
        self.proxy = proxy
        # self.headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        #     'referer': 'https://www.madlan.co.il/'}

    def scrap_info(self, url):
        soup_html = self.prepare_soup_html(url)
        scripts_lst = soup_html.find_all('script')
        raw_data = self.extract_raw_data(scripts_lst)
        if raw_data is None:
            print(f'data not avilable link {url}')

        else:
            data = self.manipulate_raw_data(raw_data)
            data_dict = ast.literal_eval(data)
            data_dict.update({'link': url})
            self.save_data_to_csv(data_dict)

    def prepare_soup_html(self, url):
        proxy = {
            # "https": 'https://157.230.103.189:46237',
            "http": 'https://51.159.24.172:3154'
        }
        session = requests.Session()
        html = session.get(url, headers=self.headers, timeout=80, proxies=self.proxy).content.decode('utf-8')
        soup_html = BeautifulSoup(html, 'html.parser')
        return soup_html

    def extract_raw_data(self, scripts_lst):
        data = None
        for script in scripts_lst:
            script_str = str(script)
            if 'window.__SSR_HYDRATED_CONTEXT__' in script_str:
                data = script_str
                break
        return data

    def manipulate_raw_data(self, raw_data):
        # raw_data = \
        # raw_data[len('window.__SSR_HYDRATED_CONTEXT__='):].split(',"eventsHistory"')[0].split('"addressDetails":{')[
        #     1].replace('{', '').replace('}', '')
        # raw_data = '{' + raw_data + '}'
        # raw_data = raw_data.replace('null', '""')
        data_lst = raw_data[len('window.__SSR_HYDRATED_CONTEXT__='):].split('"addressDetails":')[1:]
        man_data = data_lst[-1].split(',"structuredAddress"')[0].replace('"Address"}', '"Address"') + '}'
        man_data = man_data.replace('null', '""')
        return man_data

    def save_data_to_csv(self, data_dict):
        cols = MadlanAssetInfo.cols
        df = pd.DataFrame(columns=cols, data=data_dict, index=[0])
        try:
            df_old = pd.read_csv(f'C:\\Users\\LiavB\\OneDrive\\Desktop\\projects\\real_estate\\assets.csv')
        except Exception as ex:
            df_old = pd.DataFrame(columns=cols)

        df_combined = pd.concat([df_old, df])
        df_combined.to_csv(f'C:\\Users\\LiavB\\OneDrive\\Desktop\\projects\\real_estate\\assets.csv', index=False,
                           encoding='utf-8-sig')

#
# if __name__ == '__main__':
#
#     scrapper = MadlanScrapper()
#     links = [
#         "https://www.madlan.co.il/listings/bA5UV37Hf5p?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/fDo1yX65SqH?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/kv7e7CToot8?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/jdBJyx8uITq?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/h1SO0xejaX8?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/eybPduCVoWn?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/bCXVsUn28dU?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/gJOKpF60EOV?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/e4WGExhFenU?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/hzRgPyP21VE?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/kKcvzbsjVwN?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/dcSE48nkBGO?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/bdseMwT0OoU?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/fV2v7I4oNxX?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/ptjBhOCLUV?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/bnlZFPPfKU4?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/c3vT9hy0T6U?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/cLWk4ADJFQQ?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/cH65fahqmLK?tracking_event_source=favorites",
#         "https://www.madlan.co.il/listings/h5skLr46yqO?tracking_event_source=favorites"]
#     i = 0
#     len_links = len(links)
#     for link in links:
#         i += 1
#         print(f'{i} out of {len_links}')
#         scrapper.scrap_info(link)


if __name__ == '__main__':
    links = [
        "https://www.madlan.co.il/listings/bA5UV37Hf5p?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/fDo1yX65SqH?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/kv7e7CToot8?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/jdBJyx8uITq?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/h1SO0xejaX8?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/eybPduCVoWn?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/bCXVsUn28dU?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/gJOKpF60EOV?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/e4WGExhFenU?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/hzRgPyP21VE?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/dcSE48nkBGO?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/bdseMwT0OoU?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/fV2v7I4oNxX?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/ptjBhOCLUV?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/bnlZFPPfKU4?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/c3vT9hy0T6U?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/cLWk4ADJFQQ?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/cH65fahqmLK?tracking_event_source=favorites",
        "https://www.madlan.co.il/listings/h5skLr46yqO?tracking_event_source=favorites"]

    # Retrieve latest proxies
    user_agent_list = (
        # Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        # Firefox
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    )
    proxies = []
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', random.choice(user_agent_list))
    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
            'ip': row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })


    a = 1
    for i in range(0, len(links)):
        print(f'{i} out of {len(links)}')
        proxy = random.choice(proxies)
        headers = {'User-Agent': random.choice(user_agent_list), 'referer': 'https://www.madlan.co.il/'}
        scrapper = MadlanScrapper(headers, proxy)
        scrapper.scrap_info(links[i])
        time.sleep(5)
