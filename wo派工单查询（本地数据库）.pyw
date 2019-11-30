# -*- coding: utf-8 -*-
"""
开发者：周梦雄
最后更新日期：2019/11/5
"""
import pymysql
from PyQt5.QtCore import QDate
from Ui_wo_query import *
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QDateEdit, QMainWindow, QTableWidget, QMessageBox, QTableWidgetItem, \
    QAbstractItemView


class MyMainWindow(QMainWindow, Ui_wo_query):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget_result.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.tableWidget_result.setColumnCount(10)
        self.tableWidget_result.setRowCount(1000)
        self.tableWidget_result.resizeColumnsToContents()
        self.tableWidget_result.resizeRowsToContents()
        self.start_date.setDate(QDate.currentDate())
        self.end_date.setDate(QDate.currentDate())
        self.start_date_str = self.start_date.date().toString("yyyy-MM-dd")
        self.end_date_str = self.end_date.date().toString("yyyy-MM-dd")
        self.db = pymysql.connect("localhost", "root",
                                  "Dream123$", "raw_data", charset='utf8', autocommit=True)
        # 获取游标、数据
        self.cur = self.db.cursor()
        self.sqlstring = r"select * from wos where "
        self.sqlstring1 = r"select count(DISTINCT `派工单号`) from wos where "
        self.sqlstring2 = r"select sum(`入库数量`) from wos where "
        self.exit.clicked.connect(self.buttonExit)
        self.query.clicked.connect(self.click_query)
        self.start_date.dateChanged.connect(self.on_date_changed)
        self.end_date.dateChanged.connect(self.on_date_changed)
        self.btn_prod_qty.clicked.connect(self.click_prod_qty)
        self.btn_wo_qty.clicked.connect(self.click_wo_qty)
        # self.export_records.clicked.connect(self.export_id_to_excel)

        self.show()

    def buttonExit(self):
        self.db.commit()
        self.close()

    def click_prod_qty(self):
        try:
            temp_sqlstring = self.sqlstring2
            is_first = True
            if self.cb_start_date.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`入库日期` >= '" + self.start_date_str + "'"
                else:
                    temp_sqlstring += " and `入库日期` >= '" + self.start_date_str + "'"

            if self.cb_end_date.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`入库日期` <= '" + self.end_date_str + "'"
                else:
                    temp_sqlstring += " and `入库日期` <= '" + self.end_date_str + "'"

            if self.cb_wo.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`派工单号` = '" + self.le_wo.text().upper() + "'"
                else:
                    temp_sqlstring += " and `派工单号` = '" + self.le_wo.text().upper() + "'"

            if self.cb_approval.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`审批编号` = '" + self.le_approval.text() + "'"
                else:
                    temp_sqlstring += " and `审批编号` = '" + self.le_approval.text() + "'"

            # 执行查询（传递开始测试日期时间参数）
            self.cur.execute(temp_sqlstring)
            self.tb_query.setText("")
            self.tb_query.append("完成设备数量：%s" %
                                 (str(self.cur.fetchall()[0][0])))
        except Exception:
            QMessageBox.warning(
                self, "啧啧 >_<", "你好像忘了设置查询条件哦！", QMessageBox.Ok
            )

    def click_wo_qty(self):
        try:
            temp_sqlstring = self.sqlstring1
            is_first = True
            if self.cb_start_date.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`入库日期` >= '" + self.start_date_str + "'"
                else:
                    temp_sqlstring += " and `入库日期` >= '" + self.start_date_str + "'"

            if self.cb_end_date.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`入库日期` <= '" + self.end_date_str + "'"
                else:
                    temp_sqlstring += " and `入库日期` <= '" + self.end_date_str + "'"

            if self.cb_wo.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`派工单号` = '" + self.le_wo.text().upper() + "'"
                else:
                    temp_sqlstring += " and `派工单号` = '" + self.le_wo.text().upper() + "'"

            if self.cb_approval.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`审批编号` = '" + self.le_approval.text() + "'"
                else:
                    temp_sqlstring += " and `审批编号` = '" + self.le_approval.text() + "'"

            # 执行查询（传递开始测试日期时间参数）
            self.cur.execute(temp_sqlstring)
            self.tb_query.setText("")
            self.tb_query.append("完成工单数量：%s" %
                                 (str(self.cur.fetchall()[0][0])))
        except Exception:
            QMessageBox.warning(
                self, "啧啧 >_<", "你好像忘了设置查询条件哦！", QMessageBox.Ok
            )

    def on_date_changed(self):
        self.start_date_str = self.start_date.date().toString("yyyy-MM-dd")
        self.end_date_str = self.end_date.date().toString("yyyy-MM-dd")

    def click_query(self):
        try:
            temp_sqlstring = self.sqlstring
            is_first = True
            if self.cb_start_date.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`入库日期` >= '" + self.start_date_str + "'"
                else:
                    temp_sqlstring += " and `入库日期` >= '" + self.start_date_str + "'"

            if self.cb_end_date.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`入库日期` <= '" + self.end_date_str + "'"
                else:
                    temp_sqlstring += " and `入库日期` <= '" + self.end_date_str + "'"

            if self.cb_wo.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`派工单号` = '" + self.le_wo.text().upper() + "'"
                else:
                    temp_sqlstring += " and `派工单号` = '" + self.le_wo.text().upper() + "'"

            if self.cb_approval.isChecked():
                if is_first:
                    is_first = False
                    temp_sqlstring += "`审批编号` = '" + self.le_approval.text() + "'"
                else:
                    temp_sqlstring += " and `审批编号` = '" + self.le_approval.text() + "'"

            self.tableWidget_result.clearContents()  # 每一次查询时清除表格中信息
            # 执行查询（传递开始测试日期时间参数）
            self.cur.execute(temp_sqlstring)
            for k, i in enumerate(self.cur):
                print("----------", i)
                for w, j in enumerate(i):
                    if type(j) != str:
                        newItem = QTableWidgetItem(str(j))
                    else:
                        newItem = QTableWidgetItem(j)
                    # 根据循环标签一次对table中的格子进行设置
                    self.tableWidget_result.setItem(k, w, newItem)
            self.tableWidget_result.resizeColumnsToContents()
            self.tableWidget_result.resizeRowsToContents()
            self.tb_query.setText("")
            self.tb_query.append(temp_sqlstring)
            print("query button pressed")
        except Exception:
            QMessageBox.warning(
                self, "啧啧 >_<", "你好像忘了设置查询条件哦！", QMessageBox.Ok
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
