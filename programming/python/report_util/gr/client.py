import sys
import datetime
from PySide2 import QtWidgets
from functions import complex_settings, fiscal_and_reg, request_for_work
from interFace import Ui_MainWindow

date = datetime.datetime.now().strftime('%d-%m-%Y')


class ReportGroupApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.constant_data = dict()
        self.list_type = dict()

        self.comboBox.setItemData(0, 'fiscal')
        self.comboBox.setItemData(1, 'complex')
        self.comboBox.setItemData(2, 'market')
        self.comboBox.setItemData(3, 'reg-off-fn')
        self.comboBox.setItemData(4, 'envd')
        self.comboBox.setItemData(5, 'reg-with-fn')
        self.comboBox.setItemData(6, 'unstay')
        self.comboBox.setItemData(7, 'ingenico')
        self.comboBox.setItemData(8, 'update')

        self.printReestr.clicked.connect(self.make_registry_report)
        self.printRequest.clicked.connect(self.make_request_report)

    def make_registry_report(self):
        d_name_company = self.name_company.text()
        d_address_work = self.address_work.text()
        d_inn_company = self.inn_company.text()
        d_kpp_company = self.kpp_company.text()
        d_number_bill = self.number_bill.text()
        d_model_kkt = self.model_kkt.text()
        d_serial_kkt = self.serial_kkt.text()
        d_serial_fn = self.serial_fn.text()
        spec_name = self.spec_name.text()

        combobox_item = self.comboBox.currentData()

        registry_data = {
            'C1': date,
            'C2': d_name_company,
            'C3': d_address_work,
            'C5': d_inn_company,
            'C6': d_kpp_company,
            'C7': d_number_bill,
            'H2': d_model_kkt,
            'H3': d_serial_kkt,
            'H5': d_serial_fn,
        }

        data_type = {
            'complex': ['complex', 'H29'],
            'market': ['market', 'H26'],
            'reg-off-fn': ['reg-off-fn', 'H23'],
            'envd': ['envd', 'H23'],
            'reg-with-fn': ['reg-with-fn', 'H23'],
            'unstay': ['unstay', 'H21'],
            'ingenico': ['ingenico', 'H24'],
            'update': ['update', 'H24'],
        }

        if combobox_item == 'fiscal':
            fiscal_and_reg(spec_name, **registry_data)
        else:
            complex_settings(spec_name, *data_type[combobox_item], **registry_data)

    def make_request_report(self):
        d_name_company = self.name_company.text()
        d_inn_company = self.inn_company.text()
        d_kpp_company = self.kpp_company.text()
        d_number_bill = self.number_bill.text()
        d_model_kkt = self.model_kkt.text()
        d_serial_kkt = self.serial_kkt.text()
        d_serial_fn = self.serial_fn.text()

        request_data = {
            'B1': date,
            'E1': f'{d_inn_company}-{d_kpp_company}',
            'E2': d_name_company,
            'E4': d_number_bill,
            'E13': d_model_kkt,
            'E14': d_serial_kkt,
            'E15': d_serial_fn,
        }

        request_for_work(**request_data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mrg = ReportGroupApp()
    mrg.show()
    sys.exit(app.exec_())