import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton, QListWidget)
from PyQt5.QtCore import *

import backend


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        

        designation = QLabel('Designation')
        designation.setAlignment(Qt.AlignRight)

        mass = QLabel('Mass')
        mass.setAlignment(Qt.AlignRight)

        area = QLabel('Area')
        area.setAlignment(Qt.AlignRight)

        d = QLabel('D')
        d.setAlignment(Qt.AlignRight)

        b = QLabel('B')
        b.setAlignment(Qt.AlignRight)

        tw = QLabel('tw')
        tw.setAlignment(Qt.AlignRight)

        t = QLabel('T')
        t.setAlignment(Qt.AlignRight)

        flangeslope = QLabel('FlangeSlope')
        flangeslope.setAlignment(Qt.AlignRight)

        r1 = QLabel('R1')
        r1.setAlignment(Qt.AlignRight)

        r2 = QLabel('R2')
        r2.setAlignment(Qt.AlignRight)

        lz = QLabel('lz')
        lz.setAlignment(Qt.AlignRight)

        ly = QLabel('ly')
        ly.setAlignment(Qt.AlignRight)

        rz = QLabel('rz')
        rz.setAlignment(Qt.AlignRight)

        ry = QLabel('ry')
        ry.setAlignment(Qt.AlignRight)

        zz = QLabel('Zz')
        zz.setAlignment(Qt.AlignRight)

        zy = QLabel('Zy')
        zy.setAlignment(Qt.AlignRight)

        zpz = QLabel('Zpz')
        zpz.setAlignment(Qt.AlignRight)

        zpy = QLabel('Zpy')
        zpy.setAlignment(Qt.AlignRight)

        source = QLabel('Source')
        source.setAlignment(Qt.AlignRight)

        view = QLabel('View')


        # titleEdit = QLineEdit()
        # titleEdit1 = QLineEdit()
        # authorEdit = QLineEdit()
        listing = QListWidget(self)

        designationEdit = QLineEdit()
        massEdit = QLineEdit()
        areaEdit = QLineEdit()
        dEdit = QLineEdit()
        bEdit = QLineEdit()
        twEdit = QLineEdit()
        tEdit = QLineEdit()
        flangeslopeEdit = QLineEdit()
        r1Edit = QLineEdit()
        r2Edit = QLineEdit()
        lzEdit = QLineEdit()
        lyEdit = QLineEdit()
        rzEdit = QLineEdit()
        ryEdit = QLineEdit()
        zzEdit = QLineEdit()
        zyEdit = QLineEdit()
        zpzEdit = QLineEdit()
        zpyEdit = QLineEdit()
        sourceEdit = QLineEdit()

        clearAll_button = QPushButton('Clear Fields', self)
        add_button = QPushButton('Add', self)
        update_button = QPushButton('Update', self)
        close_button = QPushButton('Exit', self)

        def addClicked(self):
            data = [designationEdit.text(), massEdit.text(), areaEdit.text(), dEdit.text(),
            bEdit.text(), twEdit.text(), tEdit.text(), flangeslopeEdit.text(), r1Edit.text(),
            r2Edit.text(), lzEdit.text(), lyEdit.text(), rzEdit.text(), ryEdit.text(), zzEdit.text(),
            zyEdit.text(), zpzEdit.text(), zpyEdit.text() , sourceEdit.text()]
            # print(data)
            # temp = designationEdit.text()
            backend.setDataToDB(data)
            listing.clear()
            showData()
            # print("Add button clicked:", temp)

        def clearAllClicked(self):
            designationEdit.setText(""), massEdit.setText(""), areaEdit.setText(""), dEdit.setText(""),
            bEdit.setText(""), twEdit.setText(""), tEdit.setText(""), flangeslopeEdit.setText(""), r1Edit.setText("")
            r2Edit.setText(""), lzEdit.setText(""), lyEdit.setText(""), rzEdit.setText(""), ryEdit.setText(""), zzEdit.setText(""),
            zyEdit.setText(""), zpzEdit.setText(""), zpyEdit.setText(""), sourceEdit.setText("")


        # def clearList():
        #     listing.clear()

        add_button.clicked.connect(addClicked)
        clearAll_button.clicked.connect(clearAllClicked)


        


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(designation, 1, 0)
        grid.addWidget(designationEdit, 1, 1)
        grid.addWidget(mass, 1, 2)
        grid.addWidget(massEdit, 1, 3)

        grid.addWidget(area, 1, 4)
        grid.addWidget(areaEdit, 1, 5)
        grid.addWidget(d, 1, 6)
        grid.addWidget(dEdit, 1, 7)

        grid.addWidget(b, 2, 0)
        grid.addWidget(bEdit, 2, 1)
        grid.addWidget(tw, 2, 2)
        grid.addWidget(twEdit, 2, 3)

        grid.addWidget(t, 2, 4)
        grid.addWidget(tEdit, 2, 5)
        grid.addWidget(flangeslope, 2, 6)
        grid.addWidget(flangeslopeEdit, 2, 7)

        grid.addWidget(r1, 3, 0)
        grid.addWidget(r1Edit, 3, 1)
        grid.addWidget(r2, 3, 2)
        grid.addWidget(r2Edit, 3, 3)

        grid.addWidget(lz, 3, 4)
        grid.addWidget(lzEdit, 3, 5)
        grid.addWidget(ly, 3, 6)
        grid.addWidget(lyEdit, 3, 7)

        grid.addWidget(rz, 4, 0)
        grid.addWidget(rzEdit, 4, 1)
        grid.addWidget(ry, 4, 2)
        grid.addWidget(ryEdit, 4, 3)

        grid.addWidget(zz, 4, 4)
        grid.addWidget(zzEdit, 4, 5)
        grid.addWidget(zy, 4, 6)
        grid.addWidget(zyEdit, 4, 7)

        grid.addWidget(zpz, 5, 0)
        grid.addWidget(zpzEdit, 5, 1)
        grid.addWidget(zpy, 5, 2)
        grid.addWidget(zpyEdit, 5, 3)

        grid.addWidget(source, 5, 4)
        grid.addWidget(sourceEdit, 5, 5)
        # grid.addWidget(d, 5, 6)
        # grid.addWidget(dEdit, 5, 7)



        # grid.addWidget(review, 6, 0)
        grid.addWidget(listing, 6, 0, 8, 5)

        grid.addWidget(clearAll_button, 7, 6)
        grid.addWidget(add_button, 7, 7)
        grid.addWidget(update_button, 8, 6)
        grid.addWidget(close_button, 8, 7)

#################################################################################################################

        def Clicked(item):
            row1 = backend.show_details(item.text())
            # print(row1)
            designationEdit.setText(str(row1[0][1])), massEdit.setText(str(row1[0][2])), areaEdit.setText(str(row1[0][3]))
            dEdit.setText(str(row1[0][4])), bEdit.setText(str(row1[0][5])), twEdit.setText(str(row1[0][6])), tEdit.setText(str(row1[0][7])),
            flangeslopeEdit.setText(str(row1[0][8])), r1Edit.setText(str(row1[0][9])), r2Edit.setText(str(row1[0][10])), 
            lzEdit.setText(str(row1[0][11])), lyEdit.setText(str(row1[0][12])), rzEdit.setText(str(row1[0][13])), ryEdit.setText(str(row1[0][14])),
            zzEdit.setText(str(row1[0][15])), zyEdit.setText(str(row1[0][16])), zpzEdit.setText(str(row1[0][17])), zpyEdit.setText(str(row1[0][18])),
            sourceEdit.setText(str(row1[0][19]))

        listing.itemClicked.connect(Clicked)

            # print(item.text())
      #QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())

        def showData():

            for row in backend.show_beams():
                print(row)
                listing.addItem(row[1])
            # self.myTableWidget.setItem(row, col, QtGui.QTableWidgetItem(sqlRow[col]))

            # Following line to be added for printing list with item number and designation
            # listing.addItem('{}  {}'.format(row[0],row[1]))

            # listing.addItem(row[1])
        showData()


            # print (listing.currentRow())



#####################################################################################################################



        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 650, 600)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())