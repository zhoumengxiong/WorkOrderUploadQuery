import configparser
# 初始化
conf = configparser.ConfigParser()
# 配置文件的绝对路径
conf_path=r"C:\Users\zhoum\Desktop\TestParam.ini"
# 读取配置文件
conf.read(conf_path)
# 返回section中option的值
value_sub_conf = conf.get("STADeliveryTestItem", "Value41")
print("此单修改参数信息如下：\n%s" %value_sub_conf)