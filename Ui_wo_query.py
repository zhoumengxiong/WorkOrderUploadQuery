# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python_project\PyQt5\wo_query.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wo_query(object):
    def setupUi(self, wo_query):
        wo_query.setObjectName("wo_query")
        wo_query.resize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        wo_query.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/resources/Mac_Finder_256px_1180091_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wo_query.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(wo_query)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_end_date = QtWidgets.QCheckBox(self.groupBox)
        self.cb_end_date.setObjectName("cb_end_date")
        self.horizontalLayout_2.addWidget(self.cb_end_date)
        self.end_date = QtWidgets.QDateEdit(self.groupBox)
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_2.addWidget(self.end_date)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_start_date = QtWidgets.QCheckBox(self.groupBox)
        self.cb_start_date.setObjectName("cb_start_date")
        self.horizontalLayout.addWidget(self.cb_start_date)
        self.start_date = QtWidgets.QDateEdit(self.groupBox)
        self.start_date.setObjectName("start_date")
        self.horizontalLayout.addWidget(self.start_date)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cb_approval = QtWidgets.QCheckBox(self.groupBox_2)
        self.cb_approval.setObjectName("cb_approval")
        self.horizontalLayout_6.addWidget(self.cb_approval)
        self.le_approval = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_approval.setObjectName("le_approval")
        self.horizontalLayout_6.addWidget(self.le_approval)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cb_wo = QtWidgets.QCheckBox(self.groupBox_2)
        self.cb_wo.setObjectName("cb_wo")
        self.horizontalLayout_5.addWidget(self.cb_wo)
        self.le_wo = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_wo.setObjectName("le_wo")
        self.horizontalLayout_5.addWidget(self.le_wo)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(130, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tb_query = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_query.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tb_query.sizePolicy().hasHeightForWidth())
        self.tb_query.setSizePolicy(sizePolicy)
        self.tb_query.setObjectName("tb_query")
        self.verticalLayout.addWidget(self.tb_query)
        self.tableWidget_result = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.tableWidget_result.sizePolicy().hasHeightForWidth())
        self.tableWidget_result.setSizePolicy(sizePolicy)
        self.tableWidget_result.setObjectName("tableWidget_result")
        self.tableWidget_result.setColumnCount(10)
        self.tableWidget_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(9, item)
        self.verticalLayout.addWidget(self.tableWidget_result)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_prod_qty = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prod_qty.setObjectName("btn_prod_qty")
        self.horizontalLayout_3.addWidget(self.btn_prod_qty)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn_wo_qty = QtWidgets.QPushButton(self.centralwidget)
        self.btn_wo_qty.setObjectName("btn_wo_qty")
        self.horizontalLayout_3.addWidget(self.btn_wo_qty)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.query = QtWidgets.QPushButton(self.centralwidget)
        self.query.setObjectName("query")
        self.horizontalLayout_3.addWidget(self.query)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setObjectName("exit")
        self.horizontalLayout_3.addWidget(self.exit)
        self.horizontalLayout_3.setStretch(0, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        wo_query.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wo_query)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 18))
        self.menubar.setObjectName("menubar")
        wo_query.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wo_query)
        self.statusbar.setObjectName("statusbar")
        wo_query.setStatusBar(self.statusbar)

        self.retranslateUi(wo_query)
        self.exit.clicked.connect(wo_query.close)
        QtCore.QMetaObject.connectSlotsByName(wo_query)

    def retranslateUi(self, wo_query):
        _translate = QtCore.QCoreApplication.translate
        wo_query.setWindowTitle(_translate("wo_query", "派工单查询"))
        self.groupBox.setTitle(_translate("wo_query", "批量查询："))
        self.cb_end_date.setText(_translate("wo_query", "结束日期："))
        self.cb_start_date.setText(_translate("wo_query", "开始日期："))
        self.groupBox_2.setTitle(_translate("wo_query", "单一查询："))
        self.cb_approval.setText(_translate("wo_query", "审批单号："))
        self.le_approval.setPlaceholderText(_translate("wo_query", "填写审批编号后6位"))
        self.cb_wo.setText(_translate("wo_query", "派工单号："))
        self.le_wo.setText(_translate("wo_query", "X201911"))
        item = self.tableWidget_result.horizontalHeaderItem(0)
        item.setText(_translate("wo_query", "派工单号"))
        item = self.tableWidget_result.horizontalHeaderItem(1)
        item.setText(_translate("wo_query", "审批编号"))
        item = self.tableWidget_result.horizontalHeaderItem(2)
        item.setText(_translate("wo_query", "产品形态"))
        item = self.tableWidget_result.horizontalHeaderItem(3)
        item.setText(_translate("wo_query", "入库数量"))
        item = self.tableWidget_result.horizontalHeaderItem(4)
        item.setText(_translate("wo_query", "入库日期"))
        item = self.tableWidget_result.horizontalHeaderItem(5)
        item.setText(_translate("wo_query", "入库人员"))
        item = self.tableWidget_result.horizontalHeaderItem(6)
        item.setText(_translate("wo_query", "接收人员"))
        item = self.tableWidget_result.horizontalHeaderItem(7)
        item.setText(_translate("wo_query", "当前节点"))
        item = self.tableWidget_result.horizontalHeaderItem(8)
        item.setText(_translate("wo_query", "芯片方案"))
        item = self.tableWidget_result.horizontalHeaderItem(9)
        item.setText(_translate("wo_query", "补充说明"))
        self.btn_prod_qty.setText(_translate("wo_query", "完成设备数"))
        self.btn_wo_qty.setText(_translate("wo_query", "完成工单数"))
        self.query.setText(_translate("wo_query", "工单明细查询"))
        self.exit.setText(_translate("wo_query", "退出"))
import apprcc_rc
