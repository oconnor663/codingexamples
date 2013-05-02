from PyQt4 import QtCore, QtGui, QtWebKit

app = QtGui.QApplication([])

browser = QtWebKit.QWebView()
browser.setUrl(QtCore.QUrl("http://www.google.com"))

browser.show()

app.exec_()
