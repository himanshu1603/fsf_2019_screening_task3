import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton)
from PyQt5.QtCore import *


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

        review = QLabel('Review')


        # titleEdit = QLineEdit()
        # titleEdit1 = QLineEdit()
        # authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

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

        viewall_button = QPushButton('View All', self)
        add_button = QPushButton('Add', self)
        update_button = QPushButton('Update', self)
        close_button = QPushButton('Close', self)

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
        grid.addWidget(reviewEdit, 6, 0, 8, 5)

        grid.addWidget(viewall_button, 7, 6)
        grid.addWidget(add_button, 7, 7)
        grid.addWidget(update_button, 8, 6)
        grid.addWidget(close_button, 8, 7)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 650, 600)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())