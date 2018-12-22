from urllib import request

if __name__ == '__main__':
    url = 'http://www.renren.com/'

    headers = {
        'Cookie': 'anonymid=jpyxxtpg-xc3mq7; depovince=GW; _r01_=1; JSESSIONID=abcC34hG9JECc4X0UfuFw; ick_login=bf02c7fb-3898-4698-ab92-d03daa39e70e; first_login_flag=1; ln_uact=13119144223; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; ch_id=10016; jebe_key=31ce5943-724a-4f4c-ad62-1d1e59c3b01f%7C7629e5c8e0f7f334244eb5436ef05a2c%7C1545452082030%7C1%7C1545452082017; wp_fold=0; jebecookies=2a6f27d6-3584-4d77-a649-35b2ef9124e6|||||; _de=420A8DC764CD1624FC7C8526DA9A3A25; p=0ef13bb3e4c83f5f69a11b398ee647ca7; t=d7968229333933f5892744639138a3237; societyguester=d7968229333933f5892744639138a3237; id=965187997; xnsid=2bde0602'
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)