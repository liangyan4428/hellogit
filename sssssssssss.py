#! -*-coding:utf-8 -*-
import xlrd,unittest
import requests
import time
import json
#
class MYtest(unittest.TestCase):
    # def __init__(self):
    #     self.path = xlrd.open_workbook("D:/啊啊啊啊啊啊.xlsx")

    @classmethod
    def setUpClass(cls):
         print("test start")

    @classmethod
    def tearDownClass(cls):
        print("test stop")

    def lll(self,jihang,count):
        data = xlrd.open_workbook("D:/啊啊啊啊啊啊.xlsx")
        st = data.sheet_by_index(1)
        # 读取一整列的数据
        lie = [str(st.cell_value(i, 0)) for i in range(0, st.nrows)]
        # 读取一整行的数据
        hang = [str(st.cell_value(jihang, i)) for i in range(0, st.ncols)]
        return eval(hang[count])

    def hhhh(self,jilie,count):
        data = xlrd.open_workbook("D:/啊啊啊啊啊啊.xlsx")
        st = data.sheet_by_index(1)
        # 读取一整列的数据
        lie = [str(st.cell_value(i,jilie)) for i in range(0, st.nrows)]
        # 读取一整行的数据
        hang = [str(st.cell_value(1, i)) for i in range(0, st.ncols)]
        return lie[count]

    # def test_add(self):
    #     self.assertEqual(self.lll(1,0),self.lll(1,1))

    def sdf(self):
        url = self.hhhh(1,4)
        header = self.lll(6,0)
        data = self.lll(5,0)

        response = requests.post(url, data=data, headers=header)
        res = json.loads(response.text)
        return res

    def test_responce(self):
        self.assertEqual(self.sdf(),self.lll(7,0))

if __name__ == '__main__':
    unittest.main()
    #MYtest().sdf()






