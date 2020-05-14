import os
import time
import xlrd
from xlutils.copy import copy

BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = os.path.join(BATH_PATH, 'config', 'casedata.xls')
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
        self.cols = self.table.ncols  # 列数

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(self.get_lines()):
                result.append(self.table.row_values(i))  # 将每行的内容添加到列表中。
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows  # 行数
        if rows is not None:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)
        time.sleep(1)


if __name__ == '__main__':
    eu = ExcelUtil()
    eu.write_value(10, 8)
