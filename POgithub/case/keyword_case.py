import os
from keywordselenium.actionMethod import ActionMethod
from utils.excel_util import ExcelUtil
BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BATH_PATH, 'config', 'keyword.xls')


class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil(file_path)
        case_lines = handle_excel.get_lines()         # 获取excel行数
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                # print(is_run)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)
                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)
                    self.run_method(method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print("没有else")
                    else:
                        print('预期结果为空')

    # 获取预期结果值
    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result


if __name__ == '__main__':
    kw = KeywordCase()
    kw.run_main()










