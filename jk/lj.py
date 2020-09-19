# import pymysql    #导入pymysql包
#
# qiao=pymysql.Connect(host="127.0.0.1",port=3306,database="test",
#                      user="root",password="123456",charset="utf8")   #建立连接数据库并输入URL、端口
#端口、数据库、用户名、密码、编码格式。
# print(qiao)

# lu=qiao.cursor()  #利用连接建立传输游标
# print(lu)
# show table status where NAME ='t_area'   #查看当前默认引擎   t_area是表名
# alter table t_area engine=innodb;    #修改指定表引擎        t_area是表名

# spl2="insert into t_area(area_name, priority, create_time, update_time)values(123,123,123,123)"    #增
# lu.execute(spl2)
# qiao.commit()     #连接提交实现数据写入数据
#
# spl3="update t_area set priority = 333 where area_id = 10"    #改
# lu.execute(spl3)
# qiao.commit()


# try:
#     spl1 = "select area_name from t_area"  # 增
#     spl2 = "select * from t_area"
#
#     lu.execute(spl1)
#     lu.execute(spl2)
#
#     qiao.commit()
# except Exception as e:
#     print("异常信息是", e)
#     qiao.rollback()
# finally:
#     spl3="select * from t_area"
#     lu.execute(spl3)
#     lu.close()
#     qiao.close()


# spl4="delete from t_area where area_id = 13"    #删
# lu.execute(spl4)
# qiao.commit()     #修改数据库需要添加qiao.commit()
#
# spl="select * from t_area"    #利用容器装要执行的spl语句
# q=lu.execute(spl)       #利用游标执行spl语句
#
# # print("受影响的数据有", q)
#
# # print("受影响行数有{}行".format(lu.rowcount) )
# #
# row=lu.fetchall()
# for ro in row:
#     print("受影响的数据是", ro)
    # print(ro[0])
#     # print(row[0][0])
#
#
# lu.close()    #断开游标
#
# qiao.close()   #断开连接
