import pymysql.cursors

# 连接数据库
# noinspection SpellCheckingInspection
connect = pymysql.Connect(
    host='rm-bp1i4822kfj045mayso.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='Lanxi101!',
    db='lanxi_dev_001',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()
code1 = 0

# 查询数据
sql = "SELECT vertify_code FROM `lx_vertify_code` WHERE `phone` LIKE '%18626879419%' ORDER BY `create_time` DESC limit 3 "
# data = ('9010',)
cursor.execute(sql)
# code=cursor.fetchall()
# fetchone 返回单个元组，也就是一条记录的值:eg:3433，无数据时返回空()（可对比fetchall()的用法）
for code1 in cursor.fetchone():
    # print(code1)
    a = str(code1)
    first = a.split('\'')[0]
    print(first)

# fetchall()的用法  可以多个元组，也就是多条记录(eg:3433 3466 6433)
# for code1 in cursor.fetchall():
#     # print(code1)
#     a = str(code1)
#     first1 = a.split('\'')[1]
#     print(first1)

# 关闭连接
cursor.close()
connect.close()