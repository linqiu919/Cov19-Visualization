from flask import Flask as _Flask,jsonify
from flask import request
from flask import render_template
from flask.json import JSONEncoder as _JSONEncoder
from jieba.analyse import extract_tags
import decimal
import utils
import string

class JSONEncoder(_JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                return float(o)
            super(_JSONEncoder, self).default(o)

class Flask(_Flask):
    json_encoder = JSONEncoder


app = Flask(__name__)


@app.route('/')
def hello_word3():
    return render_template("main.html") #返回初始页面


# 前端 请求时间
@app.route('/time')
def get_time():
    return utils.get_time()

# 中间的第一部分，综合信息显示
@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    # 把字典转换为json
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})
# 中间的第二部分，疫情地图
@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # 拼装成字典然后追加到列表中去
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

# 左边第一部分，全国累计趋势
@app.route('/l1')
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]: # 从1.20号开始
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

# 左边第二部分，全国新增趋势
@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    day,confirm_add,suspect_add = [],[],[]
    for a,b,c in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day":day,"confirm_add":confirm_add,"suspect_add":suspect_add})

# 右边第一部分，全国新增确诊病例前五城市
@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    # 获取城市列表
    city = []
    # 获取确诊列表
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city,"confirm": confirm})

# 右边第二部分，全国新增确诊病例城市汇总
@app.route('/r2')
def get_r2_data():
    res = []
    for tup in utils.get_r2_data():
        # print(tup)
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

# 国内疫情资讯
@app.route('/recent')#
def get_recent_news():
    data = utils.get_recent()
    # 获取标题列表
    title = []
    # 获取链接列表
    href = []
    for key, value in data:
        if len(key) > 22:
            key = key[0:20] + ".."
        title.append(key)
        href.append(value)

    return jsonify({"title":title, "href":href})

# 国外疫情资讯
@app.route('/oversea')#
def get_oversea_news():
    data = utils.get_oversea()
    # 获取标题列表
    title = []
    # 获取链接列表
    href = []
    for key, value in data:
        if len(key) > 22:
            key = key[0:20] + ".."
        title.append(key)
        href.append(value)

    return jsonify({"title": title, "href": href})

# 疫情辟谣信息
@app.route('/fakes')#
def get_fakes():
    data = utils.get_fakes()
    # 获取标题列表
    title = []
    # 获取链接列表
    href = []
    for key, value in data:
        if len(key) > 22:
            key = key[0:20] + ".."
        title.append(key)
        href.append(value)

    return jsonify({"title": title, "href": href})

# 获取更新时间
@app.route('/update_time')
def get_update():
    data = utils.get_c1_time()
    return jsonify({"update_time":data})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
