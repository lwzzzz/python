# 利用urllib模块模拟浏览器提交数据，并得到服务
# 器的response，进一步的处理
# url为百度翻译 =http://fanyi.baidu.com/sug
# 这里可能还有别的baseurl这里只列举一个
from urllib import request, parse
import tkinter
import threading
import json

urlbase = "http://fanyi.baidu.com/sug"
global data
data = {'kw': 'happy'}
headers = {
    'Content-Length': len(data)
}


def chazhao():
    ci = yuanwen.get()
    data['kw'] = ci
    data1 = parse.urlencode(data).encode('utf-8')
    # req = request.Request(url=urlbase,data=data,headers=headers)
    rsq = request.urlopen(url=urlbase, data=data1, )
    json_data = rsq.read().decode('utf-8')
    json_data = json.loads(json_data)
    s = ""
    for item in json_data['data']:
        s = s + item['k'] + "     " + item['v'] + "\n"
    text.set(s)
    tk.update()
    print(s)


tk = tkinter.Tk()
yuanwen = tkinter.Entry(tk)
yuanwen.pack()
fanyi = tkinter.Button(tk, text='翻译', command=chazhao)
fanyi.pack()
text = tkinter.StringVar()
text.set("")
jieguo = tkinter.Label(tk, textvariable=text)
jieguo.pack()
tk.mainloop()
