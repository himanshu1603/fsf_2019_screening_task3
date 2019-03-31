import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton, QListWidget,QComboBox,QMessageBox,QErrorMessage)
from PyQt5.QtCore import *

import backend
import dictnry

with open("log.txt", "w") as f:  
    f.write("1")


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

        iz = QLabel('Iz')
        iz.setAlignment(Qt.AlignRight)

        iy = QLabel('Iy')
        iy.setAlignment(Qt.AlignRight)

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

        type1 = QLabel('Type')
        type1.setAlignment(Qt.AlignRight)

        select = QLabel('Select Type:')
        select.setAlignment(Qt.AlignRight)

        cy = QLabel('Cy')
        cy.setAlignment(Qt.AlignRight)

        cz = QLabel('Cz')
        cz.setAlignment(Qt.AlignRight)

        iuMax = QLabel('Iu(max)')
        iuMax.setAlignment(Qt.AlignRight)

        ivMin = QLabel('Iv(min)')
        ivMin.setAlignment(Qt.AlignRight)

        ruMax = QLabel('ru(max)')
        ruMax.setAlignment(Qt.AlignRight)

        rvMin = QLabel('rv(min)')
        rvMin.setAlignment(Qt.AlignRight)

        axb = QLabel('AXB')
        axb.setAlignment(Qt.AlignRight)

        tan = QLabel('Tan?')
        tan.setAlignment(Qt.AlignRight)


        

        view = QLabel('View')


        selectBox = QComboBox(self)
        # selectBox.addItem("Select Any")
        selectBox.addItem("Angles")
        selectBox.addItem("Beams")
        selectBox.addItem("Channels")



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
        izEdit = QLineEdit()
        iyEdit = QLineEdit()
        rzEdit = QLineEdit()
        ryEdit = QLineEdit()
        zzEdit = QLineEdit()
        zyEdit = QLineEdit()
        zpzEdit = QLineEdit()
        zpyEdit = QLineEdit()
        sourceEdit = QLineEdit()
        type1Edit = QLineEdit()
        cyEdit = QLineEdit()
        iuMaxEdit = QLineEdit()
        ivMinEdit = QLineEdit()
        ruMaxEdit = QLineEdit()
        rvMinEdit = QLineEdit()
        axbEdit = QLineEdit()
        tanEdit = QLineEdit()
        czEdit = QLineEdit()


        clearAll_button = QPushButton('Clear Fields', self)
        add_button = QPushButton('Add', self)
        update_button = QPushButton('Update', self)
        close_button = QPushButton('Exit', self)

        def addClicked(self):

            table = type1Edit.text()

            data = []

            if table == "Angles":
                wle = [designationEdit,massEdit,areaEdit,axbEdit,tEdit,r1Edit,r2Edit,czEdit ,cyEdit,tanEdit,izEdit,iyEdit,iuMaxEdit,ivMinEdit,rzEdit,ryEdit,ruMaxEdit,rvMinEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in wle:
                    data.append(i.text())
                backend.setDataToDB(data, table)

            elif table == "Beams":
                wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in wle:
                    data.append(i.text())
                backend.setDataToDB(data, table)

            elif table == "Channels":
                wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,cyEdit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in wle:
                    data.append(i.text())
                backend.setDataToDB(data, table)
            else:
                showDialog()
                listing.clear()

            

        def clearAllClicked(self):
            if dictnry.Type[designationEdit.text()] == "Angles":
                wle = [designationEdit,massEdit,areaEdit,axbEdit,tEdit,r1Edit,r2Edit,czEdit ,cyEdit,tanEdit,izEdit,iyEdit,iuMaxEdit,ivMinEdit,rzEdit,ryEdit,ruMaxEdit,rvMinEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in range(24):
                    wle[i].setText("")

            elif dictnry.Type[designationEdit.text()] == "Beams":
                wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in range(20):
                    wle[i].setText("")

            elif dictnry.Type[designationEdit.text()] == "Channels":
                wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,cyEdit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in range(21):
                    wle[i].setText("")


        add_button.clicked.connect(addClicked)
        clearAll_button.clicked.connect(clearAllClicked)

        close_button.clicked.connect(self.close)

        def showDialog():
            error_dialog = QErrorMessage()
            error_dialog.showMessage("Error!! <br>You have entered wrong value for type field. <br>Allowed values are 'Angles', 'Beams' and 'Channels'")
            grid.addWidget(error_dialog,10,3,11,5)

            # grid.removeWidget(error_dialog)

        grid = QGridLayout()
        grid.setSpacing(10)

        ############  ANGLES######

        def A():
            wl = [designation,mass,area,axb,t,r1,r2,cz,cy,tan,iz,iy,iuMax,ivMin,rz,ry,ruMax,rvMin,zz,zy,zpz,zpy,source,type1]
            wle = [designationEdit,massEdit,areaEdit,axbEdit,tEdit,r1Edit,r2Edit,czEdit ,cyEdit,tanEdit,izEdit,iyEdit,iuMaxEdit,ivMinEdit,rzEdit,ryEdit,ruMaxEdit,rvMinEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
            for i in range(24):
                grid.addWidget(wl[i],(i//4)+1, (2*i)%8)
            for i in range(24):
                grid.addWidget(wle[i],((i)//4)+1,(2*i+1)%8)

           

            grid.addWidget(select, 7, 0)
            grid.addWidget(selectBox, 7, 1)

                
            grid.addWidget(listing, 8, 0, 10, 4)

            grid.addWidget(clearAll_button, 9, 6)
            grid.addWidget(add_button, 9, 7)
            grid.addWidget(update_button, 10, 6)
            grid.addWidget(close_button, 10, 7)  


        def destroyA():
            wl = [designation,mass,area,axb,t,r1,r2,cz,cy,tan,iz,iy,iuMax,ivMin,rz,ry,ruMax,rvMin,zz,zy,zpz,zpy,source,type1]
            wle = [designationEdit,massEdit,areaEdit,axbEdit,tEdit,r1Edit,r2Edit,czEdit ,cyEdit,tanEdit,izEdit,iyEdit,iuMaxEdit,ivMinEdit,rzEdit,ryEdit,ruMaxEdit,rvMinEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
            for i in range(24):
                grid.removeWidget(wl[i])
            for i in range(24):
                grid.removeWidget(wle[i])

            others = [select, selectBox, listing, clearAll_button, add_button, update_button,close_button]

            for i in others:
                grid.removeWidget(i)



        ######   BEAMS####

        def B():

            wl = [designation,mass,area,d,b,tw,t,flangeslope,r1,r2,iz,iy,rz,ry,zz,zy,zpz,zpy,source,type1]
            wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]

            for i in range(20):
                grid.addWidget(wl[i],(i//4)+1, (2*i)%8)
            for i in range(20):
                grid.addWidget(wle[i],((i)//4)+1,(2*i+1)%8)

            

            grid.addWidget(select, 6, 0)
            grid.addWidget(selectBox, 6, 1)

                
            grid.addWidget(listing, 7, 0, 9, 4)

            grid.addWidget(clearAll_button, 8, 6)
            grid.addWidget(add_button, 8, 7)
            grid.addWidget(update_button, 9, 6)
            grid.addWidget(close_button, 9, 7) 


        def destroyB():
            wl = [designation,mass,area,d,b,tw,t,flangeslope,r1,r2,iz,iy,rz,ry,zz,zy,zpz,zpy,source,type1]
            wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]

            for i in range(20):
                grid.removeWidget(wl[i])
            for i in range(20):
                grid.removeWidget(wle[i])

            others = [select, selectBox, listing, clearAll_button, add_button, update_button,close_button]

            for i in others:
                grid.removeWidget(i)

   
        ############################### CHANNELS################
        def C():
            wl = [designation,mass,area,d,b,tw,t,flangeslope,r1,r2,cy,iz,iy,rz,ry,zz,zy,zpz,zpy,source,type1]
            wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,cyEdit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]

            for i in range(21):
                grid.addWidget(wl[i],(i//4)+1, (2*i)%8)
            for i in range(21):
                grid.addWidget(wle[i],((i)//4)+1,(2*i+1)%8)

            grid.addWidget(select, 7, 0)
            grid.addWidget(selectBox, 7, 1)

                
            grid.addWidget(listing, 8, 0, 10, 4)

            grid.addWidget(clearAll_button, 9, 6)
            grid.addWidget(add_button, 9, 7)
            grid.addWidget(update_button, 10, 6)
            grid.addWidget(close_button, 10, 7)

        def destroyC():
            wl = [designation,mass,area,d,b,tw,t,flangeslope,r1,r2,cy,iz,iy,rz,ry,zz,zy,zpz,zpy,source,type1]
            wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,cyEdit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]

            for i in range(21):
                grid.removeWidget(wl[i])
            for i in range(21):
                grid.removeWidget(wle[i])

            others = [select, selectBox, listing, clearAll_button, add_button, update_button,close_button]

            for i in others:
                grid.removeWidget(i)


        A()

        def destroy():

            wlA = [designation,mass,area,axb,t,r1,r2,cz,cy,tan,iz,iy,iuMax,ivMin,rz,ry,ruMax,rvMin,zz,zy,zpz,zpy,source,type1]
            wleA = [designationEdit,massEdit,areaEdit,axbEdit,tEdit,r1Edit,r2Edit,czEdit ,cyEdit,tanEdit,izEdit,iyEdit,iuMaxEdit,ivMinEdit,rzEdit,ryEdit,ruMaxEdit,rvMinEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
            wlC = [designation,mass,area,d,b,tw,t,flangeslope,r1,r2,cy,iz,iy,rz,ry,zz,zy,zpz,zpy,source,type1]
            wleC = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,cyEdit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
            others = [select, selectBox, listing, clearAll_button, add_button, update_button,close_button]


            allWidgets = wlA + wleA + wlC + wleC + others 

            set1 = set(allWidgets)

            allWidgets = list(set1)

            for i in allWidgets:
                grid.removeWidget(i)


 
            




        def style_choice(text):
            
            
            listing.clear()  
    
            destroy()

            
            
            if text == "Angles":
                A()
            
            elif text == "Beams":
                B()
                
            elif text == "Channels":
                C()
                
            showData(text)
            
         

        selectBox.activated[str].connect(style_choice)
        



        def Clicked(item):
            row1 = backend.show_details(item.text())
            # print(row1)



            if dictnry.Type[item.text()] == "Angles":

                wle = [designationEdit,massEdit,areaEdit,axbEdit,tEdit,r1Edit,r2Edit,czEdit ,cyEdit,tanEdit,izEdit,iyEdit,iuMaxEdit,ivMinEdit,rzEdit,ryEdit,ruMaxEdit,rvMinEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in range(23):
                    wle[i].setText(str(row1[0][i+1]))

                type1Edit.setText(dictnry.Type[str(row1[0][1])])

            if dictnry.Type[item.text()] == "Beams":
                wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in range(19):
                    wle[i].setText(str(row1[0][i+1]))
                    type1Edit.setText(dictnry.Type[str(row1[0][1])])

            if dictnry.Type[item.text()] == "Channels":
                wle = [designationEdit,massEdit,areaEdit,dEdit,bEdit,twEdit,tEdit,flangeslopeEdit ,r1Edit,r2Edit,cyEdit,izEdit,iyEdit,rzEdit,ryEdit,zzEdit,zyEdit,zpzEdit,zpyEdit,sourceEdit,type1Edit]
                for i in range(20):
                    wle[i].setText(str(row1[0][i+1]))
                    type1Edit.setText(dictnry.Type[str(row1[0][1])])



           

        listing.itemClicked.connect(Clicked)

        def showData(table):

            for row in backend.show_designations(table):
                listing.addItem(row[1])

        self.setLayout(grid)

        self.setGeometry(300, 300, 650, 600)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())