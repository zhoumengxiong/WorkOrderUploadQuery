# -*- coding: utf-8 -*-
"""
开发者：周梦雄
最后更新日期：2019/9/12
"""
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QDateEdit, QMainWindow, QMessageBox
from Ui_wo_upload import *
from PyQt5.QtCore import QDate
import pymysql


class MyMainWindow(QMainWindow, Ui_wo_upload):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dateEdit_date_toWH.setDate(QDate.currentDate())
        # 连接数据库
        self.db = pymysql.connect("localhost", "root",
                                  "Dream123$", "raw_data", charset='utf8', autocommit=True)
        # 获取游标、数据
        self.cur = self.db.cursor()
        self.bt_upload.clicked.connect(self.add_to_db)
        self.bt_update.clicked.connect(self.update_db)
        self.comboBox_2.setCurrentIndex(7)
        self.show()
        # QMessageBox.warning(
        #    self, "千万小心！", "更新数据库时，一定要核对派工单号、产品形态、芯片方案是否填写正确，否则会造成严重后果！", QMessageBox.Ok)

    def add_to_db(self):
        try:
            value_lst = [self.le_wo.text().upper(), self.le_approval_no.text(), self.comboBox.currentText(), self.le_prod_qty.text(), self.dateEdit_date_toWH.date().toString("yyyy-MM-dd"), self.le_guy_send.text(),
                         self.le_guy_receive.text(), self.comboBox_2.currentText(), self.comboBox_chip.currentText(), self.le_remarks.text()]
            self.cur.execute("select * from wos_flask WHERE `WoNumber` = %s and `ProductClass`=%s and `ChipSolution`=%s",
                             [self.le_wo.text().upper(), self.comboBox.currentText(), self.comboBox_chip.currentText()])
            if self.cur.fetchall():
                QMessageBox.warning(
                    self, "兄嘚!", "你已经上传过哦！", QMessageBox.Ok)
            else:
                self.cur.execute(
                    "INSERT INTO wos_flask(WoNumber,ApprovalNumber,ProductClass,InQuantity,InDate,InOperator,ReceiveOperator,CurrentNode,ChipSolution,Supplement) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", value_lst)
                self.db.commit()
                self.statusbar.setStyleSheet(
                    "* { color: #00CD00;font-size:30px;font-weight:bold;}")
                self.statusbar.showMessage("上传数据库成功！", 3000)

        except Exception:
            QMessageBox.warning(
                self, "真糟糕，上传数据库失败！", "除补充说明外其它都是必填项！入库数量和审批编号是否填写纯数字？", QMessageBox.Ok
            )

    def update_db(self):
        if self.le_wo.text().upper() == '':
            QMessageBox.warning(
                self, "警告！", "你没有填写派工单号，无法更新！", QMessageBox.Ok
            )
        else:
            value_lst1 = [self.comboBox_2.currentText(), self.dateEdit_date_toWH.date().toString(
                "yyyy-MM-dd"), self.le_remarks.text(), self.le_wo.text().upper(), self.comboBox.currentText(), self.comboBox_chip.currentText()]
            self.cur.execute(
                r"update wos_flask set CurrentNode=%s,InDate=%s,Supplement=%s where WoNumber=%s and ProductClass=%s and ChipSolution=%s", value_lst1)
            self.db.commit()
            self.statusbar.setStyleSheet(
                "* { color: #00CD00;font-size:30px;font-weight:bold;}"
            )
            self.statusbar.showMessage("数据库更新成功！", 3000)

    def closeEvent(self, event):
        self.db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
