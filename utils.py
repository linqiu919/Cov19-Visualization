import time
import pymysql

def get_time(): # 获取前端时间
    time_str = time.strftime("%Y{}%m{}%d{} %X") #格式化
    return time_str.format("年","月","日") # 填充



def get_conn(): # 建立连接
    # 建立连接
    conn = pymysql.connect(host="localhost", user="root", password="123456", db="cov19", charset="utf8")
    # 创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor): # 关闭数据库 释放资源
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args): # 查询sql语句 *args是多个参数
    """

    :param sql:
    :param args:
    :return:
    """
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res

def test(): # 查看所有细节
    sql = "select * from details"
    res = query(sql)
    return res[0]

def get_c1_data():
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal),sum(dead) from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) "
    res = query(sql)
    return res[0] #返回第一条数据

def get_c1_time(): # 获取前端时间
    sql = "select max(update_time) from details"
    res = query(sql)
    update_time = res[0][0].strftime("%Y-%m-%d %H:%M:%S")
    return update_time # 返回最晚更新时间

def get_c2_data(): #获取最新的数据
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res

def get_l1_data():
    """
    :return:  返回全国累计趋势数据
    """
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res

def get_l2_data():
    """
    :return:  返回全国新增趋势数据
    """
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_r1_data():
    """
    :return:  返回城市确诊人数前5名
    """
    sql = 'SELECT province,confirm_add FROM ' \
          '(select province,sum(confirm_add) as confirm_add from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'group by province) as a ' \
          'ORDER BY confirm_add DESC LIMIT 5'
    res = query(sql)
    return res

def get_r2_data():
    '''
    获取国内新增病例城市的疫情数据
    :return:
    '''
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select province,confirm_add from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) and confirm_add > 0 " \
          "group by province,confirm_add"
    res = query(sql)
    return res

def get_recent():
    sql = "select title,href from recent_news limit 10"
    res = query(sql)
    return res

def get_fakes():
    sql = "select title,href from fakes limit 10"
    res = query(sql)
    return res

def get_oversea():
    sql = "select title,href from oversea limit 10"
    res = query(sql)
    return res



if __name__ == "__main__":


    print(get_c1_time())
    print(type(get_c1_time()[0]))