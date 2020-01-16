import pandas as pd
from datetime import date
import cpca as cp


class Data(object):
    name = str(date.today())+'订单' + '.xls'

    def __init__(self, choose_excel_path, download_path_path):
        self.choose_excel_path = choose_excel_path
        self.download_path_path = download_path_path

    def storage(self, df):
        df.to_excel(self.download_path_path + '/' + self.name,index=None)

    def processing(self, df):
        self.storage(df)

    def main(self):
        df = pd.read_excel(self.choose_excel_path)
        self.processing(df)




location_str = ["浙江省杭州市下城区青云街40号3楼"]
a = cp.transform(location_str, cut=False, pos_sensitive=True)
print(a)
