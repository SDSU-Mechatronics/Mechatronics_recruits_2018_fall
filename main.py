from PyQt4 import QtCore, QtGui, uic
import sys


class OurWidget(QtGui.QWidget):
	
	def __init__(self):
		super(OurWidget, self).__init__()
		self.ui = uic.loadUi("Mission Commander.ui")
		self.ui.show()
		self.debug = False
		
		self.ui.debugCheck.stateChanged.connect(self.changeText)
		self.missionWidget()
		
		'''self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.changeText)
		self.timer.start(5000)'''
		
	def connectSignals():
		pass
		
	def changeText(self):
		if self.debug == False:
			self.ui.startButton.setText("Start Debug")
                	self.ui.stopButton.setText("Stop Debug")
		else:
			self.ui.startButton.setText("Start")
			self.ui.stopButton.setText("Stop")
		self.debug = not self.debug
		

	def missionWidget(self):
		'''self.ui.abstractWidget = QtGui.QAbstractItemView(parent=self.ui.listWidget)'''
		self.ui.listWidget.setAlternatingRowColors(False)
		self.ui.listWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
		
		
app = QtGui.QApplication(sys.argv)
myWidget = OurWidget()
sys.exit(app.exec_())
