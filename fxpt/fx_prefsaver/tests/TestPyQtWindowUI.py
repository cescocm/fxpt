# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestQtWindowUI.ui'
#
# Created: Wed Oct 29 22:05:12 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(771, 584)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiLED_test1 = QtGui.QLineEdit(self.centralwidget)
        self.uiLED_test1.setObjectName(_fromUtf8("uiLED_test1"))
        self.verticalLayout.addWidget(self.uiLED_test1)
        self.uiCHK_test1 = QtGui.QCheckBox(self.centralwidget)
        self.uiCHK_test1.setObjectName(_fromUtf8("uiCHK_test1"))
        self.verticalLayout.addWidget(self.uiCHK_test1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiRAD_test1 = QtGui.QRadioButton(self.groupBox)
        self.uiRAD_test1.setObjectName(_fromUtf8("uiRAD_test1"))
        self.horizontalLayout.addWidget(self.uiRAD_test1)
        self.uiRAD_test2 = QtGui.QRadioButton(self.groupBox)
        self.uiRAD_test2.setObjectName(_fromUtf8("uiRAD_test2"))
        self.horizontalLayout.addWidget(self.uiRAD_test2)
        self.verticalLayout.addWidget(self.groupBox)
        self.uiBTN_test1 = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_test1.setCheckable(True)
        self.uiBTN_test1.setObjectName(_fromUtf8("uiBTN_test1"))
        self.verticalLayout.addWidget(self.uiBTN_test1)
        self.uiCBX_test1 = QtGui.QComboBox(self.centralwidget)
        self.uiCBX_test1.setObjectName(_fromUtf8("uiCBX_test1"))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.uiCBX_test1.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.uiCBX_test1)
        self.uiCBX_test2 = QtGui.QComboBox(self.centralwidget)
        self.uiCBX_test2.setEditable(True)
        self.uiCBX_test2.setObjectName(_fromUtf8("uiCBX_test2"))
        self.verticalLayout.addWidget(self.uiCBX_test2)
        self.uiBTN_showDialog = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_showDialog.setObjectName(_fromUtf8("uiBTN_showDialog"))
        self.verticalLayout.addWidget(self.uiBTN_showDialog)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.uiTAB_test1 = QtGui.QTabWidget(self.centralwidget)
        self.uiTAB_test1.setObjectName(_fromUtf8("uiTAB_test1"))
        self.uiTABPG_listWidget = QtGui.QWidget()
        self.uiTABPG_listWidget.setObjectName(_fromUtf8("uiTABPG_listWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.uiTABPG_listWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uiLSTWID_test1 = QtGui.QListWidget(self.uiTABPG_listWidget)
        self.uiLSTWID_test1.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.uiLSTWID_test1.setObjectName(_fromUtf8("uiLSTWID_test1"))
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.uiLSTWID_test1.addItem(item)
        self.horizontalLayout_2.addWidget(self.uiLSTWID_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_listWidget, _fromUtf8(""))
        self.uiTABPG_treeWidget = QtGui.QWidget()
        self.uiTABPG_treeWidget.setObjectName(_fromUtf8("uiTABPG_treeWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.uiTABPG_treeWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uiTREW_test1 = QtGui.QTreeWidget(self.uiTABPG_treeWidget)
        self.uiTREW_test1.setAlternatingRowColors(True)
        self.uiTREW_test1.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.uiTREW_test1.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.uiTREW_test1.setObjectName(_fromUtf8("uiTREW_test1"))
        item_0 = QtGui.QTreeWidgetItem(self.uiTREW_test1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.uiTREW_test1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.uiTREW_test1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.uiTREW_test1)
        item_0 = QtGui.QTreeWidgetItem(self.uiTREW_test1)
        item_0 = QtGui.QTreeWidgetItem(self.uiTREW_test1)
        self.uiTREW_test1.header().setDefaultSectionSize(200)
        self.uiTREW_test1.header().setMinimumSectionSize(200)
        self.horizontalLayout_3.addWidget(self.uiTREW_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_treeWidget, _fromUtf8(""))
        self.uiTABPG_tableWidget = QtGui.QWidget()
        self.uiTABPG_tableWidget.setObjectName(_fromUtf8("uiTABPG_tableWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.uiTABPG_tableWidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiTBLWID_test1 = QtGui.QTableWidget(self.uiTABPG_tableWidget)
        self.uiTBLWID_test1.setObjectName(_fromUtf8("uiTBLWID_test1"))
        self.uiTBLWID_test1.setColumnCount(2)
        self.uiTBLWID_test1.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(6, 1, item)
        self.horizontalLayout_4.addWidget(self.uiTBLWID_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_tableWidget, _fromUtf8(""))
        self.uiTABPG_listView = QtGui.QWidget()
        self.uiTABPG_listView.setObjectName(_fromUtf8("uiTABPG_listView"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.uiTABPG_listView)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.uiLSTV_test1 = QtGui.QListView(self.uiTABPG_listView)
        self.uiLSTV_test1.setObjectName(_fromUtf8("uiLSTV_test1"))
        self.horizontalLayout_7.addWidget(self.uiLSTV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_listView, _fromUtf8(""))
        self.uiTABPG_treeView = QtGui.QWidget()
        self.uiTABPG_treeView.setObjectName(_fromUtf8("uiTABPG_treeView"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.uiTABPG_treeView)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.uiTREV_test1 = QtGui.QTreeView(self.uiTABPG_treeView)
        self.uiTREV_test1.setAlternatingRowColors(True)
        self.uiTREV_test1.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.uiTREV_test1.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.uiTREV_test1.setObjectName(_fromUtf8("uiTREV_test1"))
        self.uiTREV_test1.header().setDefaultSectionSize(200)
        self.uiTREV_test1.header().setMinimumSectionSize(200)
        self.horizontalLayout_8.addWidget(self.uiTREV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_treeView, _fromUtf8(""))
        self.uiTABPG_tableView = QtGui.QWidget()
        self.uiTABPG_tableView.setObjectName(_fromUtf8("uiTABPG_tableView"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.uiTABPG_tableView)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.uiTBLV_test1 = QtGui.QTableView(self.uiTABPG_tableView)
        self.uiTBLV_test1.setObjectName(_fromUtf8("uiTBLV_test1"))
        self.horizontalLayout_10.addWidget(self.uiTBLV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_tableView, _fromUtf8(""))
        self.uiTABPG_columnView = QtGui.QWidget()
        self.uiTABPG_columnView.setObjectName(_fromUtf8("uiTABPG_columnView"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.uiTABPG_columnView)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.uiCOLV_test1 = QtGui.QColumnView(self.uiTABPG_columnView)
        self.uiCOLV_test1.setObjectName(_fromUtf8("uiCOLV_test1"))
        self.horizontalLayout_9.addWidget(self.uiCOLV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_columnView, _fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.uiTAB_test1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.uiBTN_savePrefs = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_savePrefs.setObjectName(_fromUtf8("uiBTN_savePrefs"))
        self.horizontalLayout_5.addWidget(self.uiBTN_savePrefs)
        self.uiBTN_loadPrefs = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_loadPrefs.setObjectName(_fromUtf8("uiBTN_loadPrefs"))
        self.horizontalLayout_5.addWidget(self.uiBTN_loadPrefs)
        self.uiBTN_resetPrefs = QtGui.QPushButton(self.centralwidget)
        self.uiBTN_resetPrefs.setObjectName(_fromUtf8("uiBTN_resetPrefs"))
        self.horizontalLayout_5.addWidget(self.uiBTN_resetPrefs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.uiTAB_test1.setCurrentIndex(5)
        QtCore.QObject.connect(self.uiBTN_savePrefs, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.onSavePrefsClicked)
        QtCore.QObject.connect(self.uiBTN_loadPrefs, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.onLoadPrefsClicked)
        QtCore.QObject.connect(self.uiBTN_resetPrefs, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.onResetPrefsClicked)
        QtCore.QObject.connect(self.uiBTN_showDialog, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.onShowDialogClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCHK_test1.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.uiRAD_test1.setText(QtGui.QApplication.translate("MainWindow", "RadioButton1", None, QtGui.QApplication.UnicodeUTF8))
        self.uiRAD_test2.setText(QtGui.QApplication.translate("MainWindow", "RadioButton2", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_test1.setText(QtGui.QApplication.translate("MainWindow", "Check Button", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(0, QtGui.QApplication.translate("MainWindow", "Item1", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(1, QtGui.QApplication.translate("MainWindow", "Item2", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(2, QtGui.QApplication.translate("MainWindow", "Item3", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(3, QtGui.QApplication.translate("MainWindow", "Item4", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(4, QtGui.QApplication.translate("MainWindow", "Item5", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(5, QtGui.QApplication.translate("MainWindow", "Item6", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCBX_test1.setItemText(6, QtGui.QApplication.translate("MainWindow", "Item7", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_showDialog.setText(QtGui.QApplication.translate("MainWindow", "Show Dialog", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.uiLSTWID_test1.isSortingEnabled()
        self.uiLSTWID_test1.setSortingEnabled(False)
        item = self.uiLSTWID_test1.item(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiLSTWID_test1.item(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item2", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiLSTWID_test1.item(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item3", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiLSTWID_test1.item(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item4", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiLSTWID_test1.item(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item5", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiLSTWID_test1.item(5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item6", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiLSTWID_test1.item(6)
        item.setText(QtGui.QApplication.translate("MainWindow", "Item7", None, QtGui.QApplication.UnicodeUTF8))
        self.uiLSTWID_test1.setSortingEnabled(__sortingEnabled)
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_listWidget), QtGui.QApplication.translate("MainWindow", "List Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "column1", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "column2", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.uiTREW_test1.isSortingEnabled()
        self.uiTREW_test1.setSortingEnabled(False)
        self.uiTREW_test1.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "folder1", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).setText(1, QtGui.QApplication.translate("MainWindow", "value1", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "folder11", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "value2", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "item111", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "value3", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "item112", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "value4", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "item113", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(0).child(0).child(2).setText(1, QtGui.QApplication.translate("MainWindow", "value5", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "folder2", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).setText(1, QtGui.QApplication.translate("MainWindow", "value6", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "folder21", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "value7", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "item211", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).child(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "value8", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "item212", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(1).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "item213", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "folder3", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "folder31", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(2).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "item311", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(2).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "item312", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(2).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "item313", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "rootItem1", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(4).setText(0, QtGui.QApplication.translate("MainWindow", "rootItem2", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.topLevelItem(5).setText(0, QtGui.QApplication.translate("MainWindow", "rootItem3", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTREW_test1.setSortingEnabled(__sortingEnabled)
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_treeWidget), QtGui.QApplication.translate("MainWindow", "Tree Widget", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row2", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row3", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row4", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row5", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row6", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.verticalHeaderItem(6)
        item.setText(QtGui.QApplication.translate("MainWindow", "Row7", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Column1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Column2", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.uiTBLWID_test1.isSortingEnabled()
        self.uiTBLWID_test1.setSortingEnabled(False)
        item = self.uiTBLWID_test1.item(0, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value11", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(0, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value12", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(1, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value21", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(1, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value22", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(2, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value31", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(2, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value32", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(3, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value41", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(3, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value42", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(4, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value51", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(4, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value52", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(5, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value61", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(5, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value62", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(6, 0)
        item.setText(QtGui.QApplication.translate("MainWindow", "value71", None, QtGui.QApplication.UnicodeUTF8))
        item = self.uiTBLWID_test1.item(6, 1)
        item.setText(QtGui.QApplication.translate("MainWindow", "value72", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTBLWID_test1.setSortingEnabled(__sortingEnabled)
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_tableWidget), QtGui.QApplication.translate("MainWindow", "Table Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_listView), QtGui.QApplication.translate("MainWindow", "List View", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_treeView), QtGui.QApplication.translate("MainWindow", "Tree View", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_tableView), QtGui.QApplication.translate("MainWindow", "Table View", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_columnView), QtGui.QApplication.translate("MainWindow", "Column View", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_savePrefs.setText(QtGui.QApplication.translate("MainWindow", "Save Prefs", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_loadPrefs.setText(QtGui.QApplication.translate("MainWindow", "Load Prefs", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_resetPrefs.setText(QtGui.QApplication.translate("MainWindow", "Reset Prefs", None, QtGui.QApplication.UnicodeUTF8))

