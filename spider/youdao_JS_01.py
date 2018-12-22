from urllib import request, parse

'''
var r = function(e) {
        var t = n.md5(navigator.appVersion),
        r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
        }
    };
'''
#def getMD5(v):
#    import hashlib
#    md5 = hashlib.md5()
#    md5.update(v.encode('utf-8'))
#    sign = md5.hexdigest()
#    return sign
def get_js():
    f = open('./youdao_md5.js', 'r', encoding='utf-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def getMD5(v):
    import execjs
    js_str = get_js()
    c_js = execjs.compile(js_str)
    return c_js.call('md5', v)

def getSalt(key):
    import time, random
    t = getMD5(r'5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    r = str(int(time.time()*1000))
    i = r + random.randint(0, 10)
    return {
        'ts': r,
        'bv': t,
        'salt': i,
        'sign': getMD5('fanyideskweb' + key + i + 'p09@Bn{h02_BIEe]$P^nG"')
    }
def youdao_tranlate(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    verify_info = getSalt(key=key)
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': verify_info['salt'],
        'sign': verify_info['sign'] ,
        'ts': verify_info['ts'],
        'bv': verify_info['bv'],
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'False',
    }
    data = parse.urlencode(data).encode()

    headers = {
        'Accept': 'application/json, text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '261',
        'Content-Type': 'application/x-www-form-urlencoded;charset = UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-974412601@10.169.0.83; JSESSIONID=aaaBwT8mhOA0d_UfaCvFw; OUTFOX_SEARCH_USER_ID_NCOO=1683899592.8576999; ___rl__test__cookies=1545485977398',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com /',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested - With': 'XMLHttpRequest',
    }
    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao_tranlate('girl')


'''

    t.generateSaltSign = r
    t.asyRequest = function(e) {
        var t = e.i,
        o = r.generateSaltSign(t);
        i && i.abort(),
        i = n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/bbk/translate_m.do",
            data: {
                i: e.i,
                client: e.client,
                salt: o.salt,
                sign: o.sign,
                ts: o.ts,
                bv: o.bv,
                tgt: e.tgt,
                from: e.from,
                to: e.to,
                doctype: "json",
                version: "3.0",
                cache: !0
            },
            dataType: "json",
            success: function(t) {
                t && 0 == t.errorCode ? e.success && e.success(t) : e.error && e.error(t)
            },
            error: function(e) {}
        })
    }
'''