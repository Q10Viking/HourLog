from datetime import datetime,timezone,timedelta
import os
import logging


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

def store_date(content):
    utc_dt = datetime.utcnow()
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

    bj_date = bj_dt.strftime("%Y-%m-%d")
    bj_time = bj_dt.strftime("%H:%M:%S")

    file_end = "-log.csv"
    # 以月份来存储数据
    fname_csv = bj_date[:-3]+file_end
    folder = bj_date[:4]
    if not os.path.isfile(fname_csv):
        logging.info("文件不存在")
        create_file_csv(fname_csv)

    # 写入数据
    row = "{},{},{}\n".format(bj_date,bj_time,content)
    with open(fname_csv,"a+") as f:
        f.write(row)
    logging.info("存储成功")


def create_file_csv(filename):
    
    title = "date,time,record\n"
    with open(filename,'w+') as f:
        f.write(title)
    logging.info(filename+"创建成功")
    

if __name__ == "__main__":
    store_date("test")