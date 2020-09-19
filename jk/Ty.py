from utils.Lei import DBUtils

qiao = DBUtils.get_qiao()   #调用类方法里的get_qiao 方法
lv = DBUtils.get_lu(qiao)   #调用类方法里的get_lu 方法
# try:     #事务的操作
#     spl1 = "select * from t_area"
#     spl2 = "select area_name from t_area"
#     lv.execute(spl1)
#     lv.execute(spl2)
#     qiao.commit()
# except Exception as e:
#     print("异常信息是：",e)
#     qiao.rollback()
# finally:
spl = "select * from t_area"
ck = lv.execute(spl)

rows =lv.fetchall()  #用容器装数据库全部数据

for c in rows:   #遍历
    print("数据是",c)

DBUtils.clos_res(lv,qiao)    #调用类方法里的clos_res 方法