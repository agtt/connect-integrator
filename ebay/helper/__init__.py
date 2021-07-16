import requests
from config import *
from ebaysdk.trading import Connection

headers = {
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB',
    'Authorization': 'Bearer ' + ACCESS_TOKEN,
    'Content-Type': 'application/json'
}


def callApi(method='POST', url='', payload=''):
    r = requests.request(method, url, headers=headers, data=payload)
    try:
        return r.json()
    except Exception as e:
        print('Call API Error : ' + str(e))
        return {
            'errors': 'API Connect hatasi',
            'error': 'API Connect hatasi',
        }

    # api = Connection(siteid=3,appid="AgitISIK-IOVATest-PRD-869ec6b8e-1bb52401", devid="84df14f5-a489-4df1-9a87-54f70828cc7d",
    #                  certid="PRD-69ec6b8e6d46-e982-499e-826e-d6e4",
    #                  token="AgAAAA**AQAAAA**aAAAAA**FVfvYA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6MHkYemDpeGpwudj6x9nY+seQ**fDoGAA**AAMAAA**6lgeEeUulx37Bv5ZRQkw+9RY2JWA63Eb2o8FYpwynM6zuQBzxMhsVt6H5DAMqeO5iigPYEox82hFi8UJNmQp52+Ebi5wYNUzGktlnzFbfRwANtEKQJ3w9CJu6C11FWA9nuF9vwiVcIfy9B7+itMAnXOPYwlVazudZdEMeyg6RwDw8hbEPkksOAAgnvzd5y9p67PTJErZvIIpiv29qOre+5POnbs4eQFkiBxEtBVnPhx+oOJda41wX+5JGK86ojH6kpsSf8au7yBgzQqswluYYiZVu+YSJ3Lk2cpB/GrS2s5NPazkHjSizN+bmUBaxE+Yc6F8HSYG25RuT7Hq7QV4obqJKQ/wFiNeS8HIvYEni1NEV91/XNh/EoLO78fmRvhaxOmGwU1jmjEF6Jh3diF5VX3bDr+i7OMYYQ1A6b9rXrtXyyKMnnd6UwNSMzMbc0g+gpjMLo2Sxm32uOXtjUzbbjV2H82arSosfGEP+27Lp6djqx0oojEwk8Ms//4ng/t0OJOJVQxIniTW/oEtUGl0wgadL9jQiyiD64pAUy+lzAPsBqREfRd+ksajc4ePj3Xe/ZDhlG7WFpKW7HjlzypXjyjIpNQSU05MUxnAGXsJuUZ4VXG4SC5OBkaQCSEZASCrNSIO1xTqKJ2YuXawwm1LhzZKaJLtVcEkxhEhxi4W7KyRwSfDKIFcw1shH77aJDohnbCVSObhq8PHtq1HW/k8P5dajPxF5rhq278f8g/dxCXKTkQvYJbz8eCRRA11584i",
    #                  domain="api.ebay.com", debug=False, config_file=None)


def api():
    try:
        connect = Connection(appid=APPID, devid=DEVID, certid=CERTID,
                             token=TOKEN,
                             domain="api.sandbox.ebay.com",
                             debug=False, config_file=None)
        print('CONNECTION SUCCESSFUL')
        return connect
    except Exception as e:
        print(str(e))
        print('CONNECTION ERROR')
