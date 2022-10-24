from PyQt6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt6.QtCore import QIODevice, QTimer
from PyQt6.QtWidgets import QFileDialog, QWidget
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
import pyqtgraph
from pyqtgraph import PlotWidget, GraphicsView
import numpy
import serial
import collections

BaudRate = 9600
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
        portList.append(port.portName())

DarkSolarized = [[0,30,38],[131,148,150],[220,50,47],[38,139,210],[133,153,0]]



class Ui_Spikeling(QWidget):
    def setupUi(self, Spikeling):
        Spikeling.setObjectName("Spikeling")
        Spikeling.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(Spikeling)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("color: rgb(131, 148, 150);\n"
"background-color: rgb(7, 54, 66);")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.TabSpikeling = QtWidgets.QWidget()
        self.TabSpikeling.setObjectName("TabSpikeling")
        self.NeuronParametersBox = QtWidgets.QGroupBox(self.TabSpikeling)
        self.NeuronParametersBox.setGeometry(QtCore.QRect(1070, 0, 200, 645))
        self.NeuronParametersBox.setStyleSheet("color: rgb(147, 161, 161);")
        self.NeuronParametersBox.setObjectName("NeuronParametersBox")
        self.Synapse1Label = QtWidgets.QLabel(self.NeuronParametersBox)
        self.Synapse1Label.setGeometry(QtCore.QRect(5, 290, 190, 31))
        self.Synapse1Label.setStyleSheet("color: rgb(147, 161, 161);")
        self.Synapse1Label.setObjectName("Synapse1Label")
        self.Synapse2Label = QtWidgets.QLabel(self.NeuronParametersBox)
        self.Synapse2Label.setGeometry(QtCore.QRect(5, 470, 190, 31))
        self.Synapse2Label.setStyleSheet("color: rgb(147, 161, 161);")
        self.Synapse2Label.setObjectName("Synapse2Label")
        self.NeuronParametersLine2 = QtWidgets.QFrame(self.NeuronParametersBox)
        self.NeuronParametersLine2.setGeometry(QtCore.QRect(1, 460, 198, 20))
        self.NeuronParametersLine2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.NeuronParametersLine2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.NeuronParametersLine2.setObjectName("NeuronParametersLine2")
        self.VoltageClampLabel = QtWidgets.QLabel(self.NeuronParametersBox)
        self.VoltageClampLabel.setGeometry(QtCore.QRect(5, 20, 190, 31))
        self.VoltageClampLabel.setStyleSheet("color: rgb(147, 161, 161);")
        self.VoltageClampLabel.setObjectName("VoltageClampLabel")
        self.NeuronParametersLine1 = QtWidgets.QFrame(self.NeuronParametersBox)
        self.NeuronParametersLine1.setGeometry(QtCore.QRect(1, 140, 198, 3))
        self.NeuronParametersLine1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.NeuronParametersLine1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.NeuronParametersLine1.setObjectName("NeuronParametersLine1")
        self.MembranePotentialValue = QtWidgets.QLineEdit(self.NeuronParametersBox)
        self.MembranePotentialValue.setEnabled(False)
        self.MembranePotentialValue.setGeometry(QtCore.QRect(60, 80, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.MembranePotentialValue.setFont(font)
        self.MembranePotentialValue.setMaxLength(100)
        self.MembranePotentialValue.setFrame(True)
        self.MembranePotentialValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MembranePotentialValue.setObjectName("MembranePotentialValue")
        self.Synapse1DecayCheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.Synapse1DecayCheckBox.setGeometry(QtCore.QRect(10, 410, 100, 20))
        self.Synapse1DecayCheckBox.setObjectName("Synapse1DecayCheckBox")
        self.Synapse1RecoveryCheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.Synapse1RecoveryCheckBox.setGeometry(QtCore.QRect(10, 440, 100, 20))
        self.Synapse1RecoveryCheckBox.setObjectName("Synapse1RecoveryCheckBox")
        self.Synapse2RecoveryCheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.Synapse2RecoveryCheckBox.setGeometry(QtCore.QRect(10, 620, 100, 20))
        self.Synapse2RecoveryCheckBox.setObjectName("Synapse2RecoveryCheckBox")
        self.Synapse2DecayCheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.Synapse2DecayCheckBox.setGeometry(QtCore.QRect(10, 590, 100, 20))
        self.Synapse2DecayCheckBox.setObjectName("Synapse2DecayCheckBox")
        self.Synapse2RecoveryValue = QtWidgets.QLineEdit(self.NeuronParametersBox)
        self.Synapse2RecoveryValue.setEnabled(False)
        self.Synapse2RecoveryValue.setGeometry(QtCore.QRect(110, 620, 75, 20))
        self.Synapse2RecoveryValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Synapse2RecoveryValue.setObjectName("Synapse2RecoveryValue")
        self.Synapse2DecayValue = QtWidgets.QLineEdit(self.NeuronParametersBox)
        self.Synapse2DecayValue.setEnabled(False)
        self.Synapse2DecayValue.setGeometry(QtCore.QRect(110, 590, 75, 20))
        self.Synapse2DecayValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Synapse2DecayValue.setObjectName("Synapse2DecayValue")
        self.SynapticGain2CheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.SynapticGain2CheckBox.setEnabled(True)
        self.SynapticGain2CheckBox.setGeometry(QtCore.QRect(5, 520, 190, 20))
        self.SynapticGain2CheckBox.setObjectName("SynapticGain2CheckBox")
        self.MembranePotentialCheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.MembranePotentialCheckBox.setGeometry(QtCore.QRect(5, 60, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MembranePotentialCheckBox.setFont(font)
        self.MembranePotentialCheckBox.setTristate(False)
        self.MembranePotentialCheckBox.setObjectName("MembranePotentialCheckBox")
        self.SynapticGain1CheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.SynapticGain1CheckBox.setGeometry(QtCore.QRect(5, 340, 190, 20))
        self.SynapticGain1CheckBox.setObjectName("SynapticGain1CheckBox")
        self.label_6 = QtWidgets.QLabel(self.NeuronParametersBox)
        self.label_6.setGeometry(QtCore.QRect(5, 150, 190, 21))
        self.label_6.setStyleSheet("color: rgb(147, 161, 161);")
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.NeuronParametersBox)
        self.line_2.setGeometry(QtCore.QRect(0, 280, 198, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.NoiseLevelCheckBox = QtWidgets.QCheckBox(self.NeuronParametersBox)
        self.NoiseLevelCheckBox.setGeometry(QtCore.QRect(5, 200, 190, 20))
        self.NoiseLevelCheckBox.setObjectName("NoiseLevelCheckBox")
        self.NoiseLevelSlider = QtWidgets.QSlider(self.NeuronParametersBox)
        self.NoiseLevelSlider.setEnabled(False)
        self.NoiseLevelSlider.setGeometry(QtCore.QRect(5, 220, 190, 27))
        self.NoiseLevelSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.NoiseLevelSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.NoiseLevelSlider.setObjectName("NoiseLevelSlider")
        self.mVLabel = QtWidgets.QLabel(self.NeuronParametersBox)
        self.mVLabel.setGeometry(QtCore.QRect(150, 87, 25, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.mVLabel.setFont(font)
        self.mVLabel.setObjectName("mVLabel")
        self.Noise0Label = QtWidgets.QLabel(self.NeuronParametersBox)
        self.Noise0Label.setGeometry(QtCore.QRect(6, 245, 10, 16))
        self.Noise0Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Noise0Label.setObjectName("Noise0Label")
        self.NoiseMaxLabel = QtWidgets.QLabel(self.NeuronParametersBox)
        self.NoiseMaxLabel.setGeometry(QtCore.QRect(170, 245, 25, 16))
        self.NoiseMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NoiseMaxLabel.setObjectName("NoiseMaxLabel")
        self.Synapse1DecayValue = QtWidgets.QLineEdit(self.NeuronParametersBox)
        self.Synapse1DecayValue.setEnabled(False)
        self.Synapse1DecayValue.setGeometry(QtCore.QRect(110, 410, 75, 20))
        self.Synapse1DecayValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Synapse1DecayValue.setObjectName("Synapse1DecayValue")
        self.Synapse1RecoveryValue = QtWidgets.QLineEdit(self.NeuronParametersBox)
        self.Synapse1RecoveryValue.setEnabled(False)
        self.Synapse1RecoveryValue.setGeometry(QtCore.QRect(110, 440, 75, 20))
        self.Synapse1RecoveryValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Synapse1RecoveryValue.setObjectName("Synapse1RecoveryValue")
        self.SynapticGain2Slider = QtWidgets.QSlider(self.NeuronParametersBox)
        self.SynapticGain2Slider.setEnabled(False)
        self.SynapticGain2Slider.setGeometry(QtCore.QRect(5, 540, 190, 27))
        self.SynapticGain2Slider.setMinimum(-50)
        self.SynapticGain2Slider.setMaximum(50)
        self.SynapticGain2Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SynapticGain2Slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.SynapticGain2Slider.setObjectName("SynapticGain2Slider")
        self.SynapticGain1Slider = QtWidgets.QSlider(self.NeuronParametersBox)
        self.SynapticGain1Slider.setEnabled(False)
        self.SynapticGain1Slider.setGeometry(QtCore.QRect(5, 360, 190, 27))
        self.SynapticGain1Slider.setMinimum(-50)
        self.SynapticGain1Slider.setMaximum(50)
        self.SynapticGain1Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SynapticGain1Slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.SynapticGain1Slider.setObjectName("SynapticGain1Slider")
        self.LicenseTab1 = QtWidgets.QLabel(self.TabSpikeling)
        self.LicenseTab1.setGeometry(QtCore.QRect(770, 670, 500, 20))
        self.LicenseTab1.setStyleSheet("color: rgb(131, 148, 150);")
        self.LicenseTab1.setObjectName("LicenseTab1")
        self.StimulationParametersBox = QtWidgets.QGroupBox(self.TabSpikeling)
        self.StimulationParametersBox.setGeometry(QtCore.QRect(860, 0, 200, 645))
        self.StimulationParametersBox.setStyleSheet("color: rgb(147, 161, 161);")
        self.StimulationParametersBox.setObjectName("StimulationParametersBox")
        self.StimulusLabel = QtWidgets.QLabel(self.StimulationParametersBox)
        self.StimulusLabel.setGeometry(QtCore.QRect(5, 20, 190, 21))
        self.StimulusLabel.setStyleSheet("color: rgb(147, 161, 161);")
        self.StimulusLabel.setObjectName("StimulusLabel")
        self.PhotoReceptorLabel = QtWidgets.QLabel(self.StimulationParametersBox)
        self.PhotoReceptorLabel.setGeometry(QtCore.QRect(5, 470, 190, 31))
        self.PhotoReceptorLabel.setStyleSheet("color: rgb(147, 161, 161);")
        self.PhotoReceptorLabel.setObjectName("PhotoReceptorLabel")
        self.StimulationParametersLine1 = QtWidgets.QFrame(self.StimulationParametersBox)
        self.StimulationParametersLine1.setGeometry(QtCore.QRect(1, 460, 198, 16))
        self.StimulationParametersLine1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.StimulationParametersLine1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.StimulationParametersLine1.setObjectName("StimulationParametersLine1")
        self.CustomStimuliDisplay = QtWidgets.QWidget(self.StimulationParametersBox)
        self.CustomStimuliDisplay.setEnabled(False)
        self.CustomStimuliDisplay.setGeometry(QtCore.QRect(5, 400, 190, 50))
        self.CustomStimuliDisplay.setStyleSheet("background-color: rgb(0, 30, 38);")
        self.CustomStimuliDisplay.setObjectName("CustomStimuliDisplay")
        self.CustomStimulusCheckBox = QtWidgets.QCheckBox(self.StimulationParametersBox)
        self.CustomStimulusCheckBox.setGeometry(QtCore.QRect(5, 350, 190, 20))
        self.CustomStimulusCheckBox.setObjectName("CustomStimulusCheckBox")
        self.StimStrCheckBox = QtWidgets.QCheckBox(self.StimulationParametersBox)
        self.StimStrCheckBox.setGeometry(QtCore.QRect(5, 200, 190, 20))
        self.StimStrCheckBox.setObjectName("StimStrCheckBox")
        self.StimFreCheckBox = QtWidgets.QCheckBox(self.StimulationParametersBox)
        self.StimFreCheckBox.setGeometry(QtCore.QRect(5, 60, 190, 20))
        self.StimFreCheckBox.setObjectName("StimFreCheckBox")
        self.PhotoGainCheckBox = QtWidgets.QCheckBox(self.StimulationParametersBox)
        self.PhotoGainCheckBox.setGeometry(QtCore.QRect(5, 520, 190, 20))
        self.PhotoGainCheckBox.setObjectName("PhotoGainCheckBox")
        self.PRRecoveryCheckBox = QtWidgets.QCheckBox(self.StimulationParametersBox)
        self.PRRecoveryCheckBox.setGeometry(QtCore.QRect(10, 620, 100, 20))
        self.PRRecoveryCheckBox.setObjectName("PRRecoveryCheckBox")
        self.PRDecayCheckBox = QtWidgets.QCheckBox(self.StimulationParametersBox)
        self.PRDecayCheckBox.setGeometry(QtCore.QRect(10, 590, 100, 20))
        self.PRDecayCheckBox.setObjectName("PRDecayCheckBox")
        self.PRRecoveryValue = QtWidgets.QLineEdit(self.StimulationParametersBox)
        self.PRRecoveryValue.setEnabled(False)
        self.PRRecoveryValue.setGeometry(QtCore.QRect(110, 620, 75, 20))
        self.PRRecoveryValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.PRRecoveryValue.setObjectName("PRRecoveryValue")
        self.PRDecayValue = QtWidgets.QLineEdit(self.StimulationParametersBox)
        self.PRDecayValue.setEnabled(False)
        self.PRDecayValue.setGeometry(QtCore.QRect(110, 590, 75, 20))
        self.PRDecayValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.PRDecayValue.setObjectName("PRDecayValue")
        self.StimStrImage = QtWidgets.QLabel(self.StimulationParametersBox)
        self.StimStrImage.setGeometry(QtCore.QRect(10, 260, 180, 50))
        self.StimStrImage.setText("")
        self.StimStrImage.setPixmap(QtGui.QPixmap("Pictures & Logos/StimStrenght.png"))
        self.StimStrImage.setScaledContents(True)
        self.StimStrImage.setObjectName("StimStrImage")
        self.StimFreImage = QtWidgets.QLabel(self.StimulationParametersBox)
        self.StimFreImage.setGeometry(QtCore.QRect(10, 130, 180, 25))
        self.StimFreImage.setText("")
        self.StimFreImage.setPixmap(QtGui.QPixmap("Pictures & Logos/StimFrequency.png"))
        self.StimFreImage.setScaledContents(True)
        self.StimFreImage.setObjectName("StimFreImage")
        self.CustomStimuluComboBox = QtWidgets.QComboBox(self.StimulationParametersBox)
        self.CustomStimuluComboBox.setEnabled(False)
        self.CustomStimuluComboBox.setGeometry(QtCore.QRect(10, 370, 180, 22))
        self.CustomStimuluComboBox.setObjectName("CustomStimuluComboBox")
        self.StimStr0Label = QtWidgets.QLabel(self.StimulationParametersBox)
        self.StimStr0Label.setGeometry(QtCore.QRect(95, 245, 10, 16))
        self.StimStr0Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.StimStr0Label.setObjectName("StimStr0Label")
        self.StimStrSlider = QtWidgets.QSlider(self.StimulationParametersBox)
        self.StimStrSlider.setEnabled(False)
        self.StimStrSlider.setGeometry(QtCore.QRect(5, 220, 190, 27))
        self.StimStrSlider.setMinimum(-50)
        self.StimStrSlider.setMaximum(50)
        self.StimStrSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.StimStrSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.StimStrSlider.setObjectName("StimStrSlider")
        self.StimFreSlider = QtWidgets.QSlider(self.StimulationParametersBox)
        self.StimFreSlider.setEnabled(False)
        self.StimFreSlider.setGeometry(QtCore.QRect(5, 80, 190, 27))
        self.StimFreSlider.setMinimum(-50)
        self.StimFreSlider.setMaximum(50)
        self.StimFreSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.StimFreSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.StimFreSlider.setObjectName("StimFreSlider")
        self.PhotoGainSlider = QtWidgets.QSlider(self.StimulationParametersBox)
        self.PhotoGainSlider.setEnabled(False)
        self.PhotoGainSlider.setGeometry(QtCore.QRect(5, 540, 190, 27))
        self.PhotoGainSlider.setMinimum(-50)
        self.PhotoGainSlider.setMaximum(50)
        self.PhotoGainSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.PhotoGainSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.PhotoGainSlider.setObjectName("PhotoGainSlider")
        self.StimulusLabel.raise_()
        self.PhotoReceptorLabel.raise_()
        self.StimulationParametersLine1.raise_()
        self.CustomStimuliDisplay.raise_()
        self.CustomStimulusCheckBox.raise_()
        self.StimStrCheckBox.raise_()
        self.StimFreCheckBox.raise_()
        self.PhotoGainCheckBox.raise_()
        self.PRRecoveryCheckBox.raise_()
        self.PRDecayCheckBox.raise_()
        self.PRRecoveryValue.raise_()
        self.PRDecayValue.raise_()
        self.StimStrImage.raise_()
        self.CustomStimuluComboBox.raise_()
        self.StimStr0Label.raise_()
        self.StimStrSlider.raise_()
        self.StimFreSlider.raise_()
        self.PhotoGainSlider.raise_()
        self.StimFreImage.raise_()
        self.Oscilloscope1 = PlotWidget(self.TabSpikeling)
        self.Oscilloscope1.setGeometry(QtCore.QRect(10, 70, 840, 480))
        self.Oscilloscope1.setAutoFillBackground(False)
        self.Oscilloscope1.setStyleSheet("\n"
"background-color: rgb(0, 30, 38);")
        self.Oscilloscope1.setObjectName("Oscilloscope1")
        self.Osc1VmCheckbox = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1VmCheckbox.setEnabled(True)
        self.Osc1VmCheckbox.setGeometry(QtCore.QRect(10, 0, 100, 20))
        self.Osc1VmCheckbox.setAutoFillBackground(False)
        self.Osc1VmCheckbox.setStyleSheet("color: rgb(220, 50, 47);")
        self.Osc1VmCheckbox.setChecked(True)
        self.Osc1VmCheckbox.setObjectName("Osc1VmCheckbox")
        self.Osc1InputCurrentCheckbox = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1InputCurrentCheckbox.setEnabled(True)
        self.Osc1InputCurrentCheckbox.setGeometry(QtCore.QRect(60, 0, 100, 20))
        self.Osc1InputCurrentCheckbox.setAutoFillBackground(False)
        self.Osc1InputCurrentCheckbox.setStyleSheet("color: rgb(133, 153, 0);")
        self.Osc1InputCurrentCheckbox.setChecked(True)
        self.Osc1InputCurrentCheckbox.setObjectName("Osc1InputCurrentCheckbox")
        self.Osc1StimulusCheckbox = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1StimulusCheckbox.setEnabled(True)
        self.Osc1StimulusCheckbox.setGeometry(QtCore.QRect(165, 0, 100, 20))
        self.Osc1StimulusCheckbox.setAutoFillBackground(False)
        self.Osc1StimulusCheckbox.setStyleSheet("color: rgb(38, 139, 210);")
        self.Osc1StimulusCheckbox.setChecked(True)
        self.Osc1StimulusCheckbox.setObjectName("Osc1StimulusCheckbox")
        self.Osc1Syn1VmCheckbox = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1Syn1VmCheckbox.setEnabled(True)
        self.Osc1Syn1VmCheckbox.setGeometry(QtCore.QRect(325, 0, 100, 20))
        self.Osc1Syn1VmCheckbox.setAutoFillBackground(False)
        self.Osc1Syn1VmCheckbox.setStyleSheet("color: rgb(203, 75, 22);")
        self.Osc1Syn1VmCheckbox.setChecked(False)
        self.Osc1Syn1VmCheckbox.setObjectName("Osc1Syn1VmCheckbox")
        self.Osc1Syn1InputCheckbox = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1Syn1InputCheckbox.setEnabled(True)
        self.Osc1Syn1InputCheckbox.setGeometry(QtCore.QRect(430, 0, 110, 20))
        self.Osc1Syn1InputCheckbox.setAutoFillBackground(False)
        self.Osc1Syn1InputCheckbox.setStyleSheet("color: rgb(42, 161, 152);")
        self.Osc1Syn1InputCheckbox.setChecked(False)
        self.Osc1Syn1InputCheckbox.setObjectName("Osc1Syn1InputCheckbox")
        self.Osc1Syn2VmCheckbox = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1Syn2VmCheckbox.setEnabled(True)
        self.Osc1Syn2VmCheckbox.setGeometry(QtCore.QRect(610, 0, 100, 20))
        self.Osc1Syn2VmCheckbox.setAutoFillBackground(False)
        self.Osc1Syn2VmCheckbox.setStyleSheet("color: rgb(181, 137, 0);")
        self.Osc1Syn2VmCheckbox.setChecked(False)
        self.Osc1Syn2VmCheckbox.setObjectName("Osc1Syn2VmCheckbox")
        self.Osc1Syn1InputCheckbox_2 = QtWidgets.QCheckBox(self.Oscilloscope1)
        self.Osc1Syn1InputCheckbox_2.setEnabled(True)
        self.Osc1Syn1InputCheckbox_2.setGeometry(QtCore.QRect(720, 0, 110, 20))
        self.Osc1Syn1InputCheckbox_2.setAutoFillBackground(False)
        self.Osc1Syn1InputCheckbox_2.setStyleSheet("color: rgb(108, 113, 196);")
        self.Osc1Syn1InputCheckbox_2.setChecked(False)
        self.Osc1Syn1InputCheckbox_2.setObjectName("Osc1Syn1InputCheckbox_2")
        self.DataRecordingBox = QtWidgets.QGroupBox(self.TabSpikeling)
        self.DataRecordingBox.setGeometry(QtCore.QRect(10, 555, 840, 90))
        self.DataRecordingBox.setStyleSheet("color: rgb(147, 161, 161);")
        self.DataRecordingBox.setObjectName("DataRecordingBox")
        self.RecordingComboBox = QtWidgets.QComboBox(self.DataRecordingBox)
        self.RecordingComboBox.setGeometry(QtCore.QRect(10, 20, 190, 22))
        self.RecordingComboBox.setObjectName("RecordingComboBox")
        self.RecordingComboBox.addItem("")
        self.RecordingComboBox.addItem("")
        self.RecordPushButton = QtWidgets.QPushButton(self.DataRecordingBox)
        self.RecordPushButton.setGeometry(QtCore.QRect(675, 50, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.RecordPushButton.setFont(font)
        self.RecordPushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
"background-color: rgb(220, 50, 47);")
        self.RecordPushButton.setObjectName("RecordPushButton")
        self.RecordFolderValue = QtWidgets.QLineEdit(self.DataRecordingBox)
        self.RecordFolderValue.setEnabled(False)
        self.RecordFolderValue.setGeometry(QtCore.QRect(540, 20, 200, 22))
        self.RecordFolderValue.setText("")
        self.RecordFolderValue.setObjectName("RecordFolderValue")
        self.RecordFolderDirPushButton = QtWidgets.QPushButton(self.DataRecordingBox)
        self.RecordFolderDirPushButton.setGeometry(QtCore.QRect(750, 20, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.RecordFolderDirPushButton.setFont(font)
        self.RecordFolderDirPushButton.setObjectName("RecordFolderDirPushButton")
        self.SelectRecordFolderLabel = QtWidgets.QLabel(self.DataRecordingBox)
        self.SelectRecordFolderLabel.setGeometry(QtCore.QRect(400, 20, 131, 20))
        self.SelectRecordFolderLabel.setObjectName("SelectRecordFolderLabel")
        self.pushButton = QtWidgets.QPushButton(self.DataRecordingBox)
        self.pushButton.setGeometry(QtCore.QRect(885, 124, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.NumberOfLoopsValue = QtWidgets.QLineEdit(self.DataRecordingBox)
        self.NumberOfLoopsValue.setGeometry(QtCore.QRect(120, 50, 75, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.NumberOfLoopsValue.setFont(font)
        self.NumberOfLoopsValue.setText("")
        self.NumberOfLoopsValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumberOfLoopsValue.setObjectName("NumberOfLoopsValue")
        self.NumberOfLoopsLabel = QtWidgets.QLabel(self.DataRecordingBox)
        self.NumberOfLoopsLabel.setGeometry(QtCore.QRect(10, 52, 101, 16))
        self.NumberOfLoopsLabel.setObjectName("NumberOfLoopsLabel")
        self.SelectedFolderLabel = QtWidgets.QLabel(self.DataRecordingBox)
        self.SelectedFolderLabel.setGeometry(QtCore.QRect(198, 50, 471, 24))
        self.SelectedFolderLabel.setText("")
        self.SelectedFolderLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.SelectedFolderLabel.setObjectName("SelectedFolderLabel")
        self.SelectPortComboBox = QtWidgets.QComboBox(self.TabSpikeling)
        self.SelectPortComboBox.setGeometry(QtCore.QRect(110, 5, 161, 22))
        self.SelectPortComboBox.setObjectName("SelectPortComboBox")
        self.SelectPortComboBox.addItem("")
        self.SelectPortLabel = QtWidgets.QLabel(self.TabSpikeling)
        self.SelectPortLabel.setGeometry(QtCore.QRect(10, 5, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SelectPortLabel.setFont(font)
        self.SelectPortLabel.setObjectName("SelectPortLabel")
        self.radioButton = QtWidgets.QRadioButton(self.TabSpikeling)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(290, 5, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.BadenLabLogoTab1 = QtWidgets.QLabel(self.TabSpikeling)
        self.BadenLabLogoTab1.setGeometry(QtCore.QRect(10, 645, 170, 45))
        self.BadenLabLogoTab1.setText("")
        self.BadenLabLogoTab1.setPixmap(QtGui.QPixmap("Pictures & Logos/Lab Logo.png"))
        self.BadenLabLogoTab1.setScaledContents(True)
        self.BadenLabLogoTab1.setObjectName("BadenLabLogoTab1")
        self.ONLogoTab1 = QtWidgets.QLabel(self.TabSpikeling)
        self.ONLogoTab1.setGeometry(QtCore.QRect(170, 655, 201, 21))
        self.ONLogoTab1.setText("")
        self.ONLogoTab1.setPixmap(QtGui.QPixmap("Pictures & Logos/ON Logo.png"))
        self.ONLogoTab1.setScaledContents(True)
        self.ONLogoTab1.setObjectName("ONLogoTab1")
        self.TrendLogoTab1 = QtWidgets.QLabel(self.TabSpikeling)
        self.TrendLogoTab1.setGeometry(QtCore.QRect(390, 648, 51, 41))
        self.TrendLogoTab1.setText("")
        self.TrendLogoTab1.setPixmap(QtGui.QPixmap("Pictures & Logos/TReND Logo 2.png"))
        self.TrendLogoTab1.setScaledContents(True)
        self.TrendLogoTab1.setObjectName("TrendLogoTab1")
        self.NeuronBrowsePushButton = QtWidgets.QPushButton(self.TabSpikeling)
        self.NeuronBrowsePushButton.setGeometry(QtCore.QRect(700, 35, 75, 30))
        self.NeuronBrowsePushButton.setObjectName("NeuronBrowsePushButton")
        self.NeuronModeLabel = QtWidgets.QLabel(self.TabSpikeling)
        self.NeuronModeLabel.setGeometry(QtCore.QRect(250, 35, 160, 26))
        self.NeuronModeLabel.setStyleSheet("color: rgb(147, 161, 161);")
        self.NeuronModeLabel.setObjectName("NeuronModeLabel")
        self.NeuronModeComboBox = QtWidgets.QComboBox(self.TabSpikeling)
        self.NeuronModeComboBox.setGeometry(QtCore.QRect(430, 35, 261, 30))
        self.NeuronModeComboBox.setStyleSheet("color: rgb(131, 148, 150);\n"
"font: 12pt \"Segoe UI\";")
        self.NeuronModeComboBox.setObjectName("NeuronModeComboBox")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeComboBox.addItem("")
        self.NeuronModeLabel.raise_()
        self.NeuronModeComboBox.raise_()
        self.TrendLogoTab1.raise_()
        self.BadenLabLogoTab1.raise_()
        self.LicenseTab1.raise_()
        self.NeuronParametersBox.raise_()
        self.Oscilloscope1.raise_()
        self.DataRecordingBox.raise_()
        self.StimulationParametersBox.raise_()
        self.SelectPortComboBox.raise_()
        self.SelectPortLabel.raise_()
        self.radioButton.raise_()
        self.ONLogoTab1.raise_()
        self.NeuronBrowsePushButton.raise_()
        self.tabWidget.addTab(self.TabSpikeling, "")
        self.TabNeuronGenerator = QtWidgets.QWidget()
        self.TabNeuronGenerator.setObjectName("TabNeuronGenerator")
        self.LicenseTab2 = QtWidgets.QLabel(self.TabNeuronGenerator)
        self.LicenseTab2.setGeometry(QtCore.QRect(889, 670, 381, 20))
        self.LicenseTab2.setObjectName("LicenseTab2")
        self.Oscilloscope2 = PlotWidget(self.TabNeuronGenerator)
        self.Oscilloscope2.setGeometry(QtCore.QRect(10, 250, 800, 335))
        self.Oscilloscope2.setStyleSheet("background-color: rgb(0, 30, 38);")
        self.Oscilloscope2.setObjectName("Oscilloscope2")
        self.Osc2StimulusCheckbox_2 = QtWidgets.QCheckBox(self.Oscilloscope2)
        self.Osc2StimulusCheckbox_2.setEnabled(False)
        self.Osc2StimulusCheckbox_2.setGeometry(QtCore.QRect(60, 0, 100, 20))
        self.Osc2StimulusCheckbox_2.setAutoFillBackground(False)
        self.Osc2StimulusCheckbox_2.setStyleSheet("color: rgb(38, 139, 210);\n"
"background-color: rgb(0, 30, 38);")
        self.Osc2StimulusCheckbox_2.setChecked(True)
        self.Osc2StimulusCheckbox_2.setObjectName("Osc2StimulusCheckbox_2")
        self.Osc2VmCheckbox = QtWidgets.QCheckBox(self.Oscilloscope2)
        self.Osc2VmCheckbox.setEnabled(False)
        self.Osc2VmCheckbox.setGeometry(QtCore.QRect(5, 0, 100, 20))
        self.Osc2VmCheckbox.setAutoFillBackground(False)
        self.Osc2VmCheckbox.setStyleSheet("color: rgb(220, 50, 47);\n"
"background-color: rgb(0, 30, 38);")
        self.Osc2VmCheckbox.setChecked(True)
        self.Osc2VmCheckbox.setObjectName("Osc2VmCheckbox")
        self.Osc2VmCheckbox.raise_()
        self.Osc2StimulusCheckbox_2.raise_()
        self.IzhikevichParameters = QtWidgets.QGroupBox(self.TabNeuronGenerator)
        self.IzhikevichParameters.setGeometry(QtCore.QRect(820, 42, 440, 605))
        self.IzhikevichParameters.setObjectName("IzhikevichParameters")
        self.aLabel = QtWidgets.QLabel(self.IzhikevichParameters)
        self.aLabel.setGeometry(QtCore.QRect(10, 55, 16, 25))
        self.aLabel.setObjectName("aLabel")
        self.a_Izhikevich = QtWidgets.QLineEdit(self.IzhikevichParameters)
        self.a_Izhikevich.setGeometry(QtCore.QRect(30, 60, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.a_Izhikevich.setFont(font)
        self.a_Izhikevich.setFrame(True)
        self.a_Izhikevich.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.a_Izhikevich.setObjectName("a_Izhikevich")
        self.b_Izhikevich = QtWidgets.QLineEdit(self.IzhikevichParameters)
        self.b_Izhikevich.setGeometry(QtCore.QRect(30, 150, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.b_Izhikevich.setFont(font)
        self.b_Izhikevich.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.b_Izhikevich.setObjectName("b_Izhikevich")
        self.c_Izhikevich = QtWidgets.QLineEdit(self.IzhikevichParameters)
        self.c_Izhikevich.setGeometry(QtCore.QRect(30, 315, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.c_Izhikevich.setFont(font)
        self.c_Izhikevich.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.c_Izhikevich.setObjectName("c_Izhikevich")
        self.d_Izhikevich = QtWidgets.QLineEdit(self.IzhikevichParameters)
        self.d_Izhikevich.setGeometry(QtCore.QRect(30, 400, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.d_Izhikevich.setFont(font)
        self.d_Izhikevich.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.d_Izhikevich.setObjectName("d_Izhikevich")
        self.DisplayNeuronPushButton = QtWidgets.QPushButton(self.IzhikevichParameters)
        self.DisplayNeuronPushButton.setEnabled(True)
        self.DisplayNeuronPushButton.setGeometry(QtCore.QRect(30, 530, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.DisplayNeuronPushButton.setFont(font)
        self.DisplayNeuronPushButton.setStyleSheet("color: rgb(147, 161, 161);")
        self.DisplayNeuronPushButton.setObjectName("DisplayNeuronPushButton")
        self.Tab2Text3 = QtWidgets.QTextBrowser(self.IzhikevichParameters)
        self.Tab2Text3.setGeometry(QtCore.QRect(165, 50, 271, 451))
        self.Tab2Text3.setStyleSheet("color: rgb(147, 161, 161);")
        self.Tab2Text3.setObjectName("Tab2Text3")
        self.bLabel = QtWidgets.QLabel(self.IzhikevichParameters)
        self.bLabel.setGeometry(QtCore.QRect(10, 150, 16, 25))
        self.bLabel.setObjectName("bLabel")
        self.cLabel = QtWidgets.QLabel(self.IzhikevichParameters)
        self.cLabel.setGeometry(QtCore.QRect(10, 312, 16, 25))
        self.cLabel.setObjectName("cLabel")
        self.dLabel = QtWidgets.QLabel(self.IzhikevichParameters)
        self.dLabel.setGeometry(QtCore.QRect(10, 400, 16, 25))
        self.dLabel.setObjectName("dLabel")
        self.SaveNeuronPushButton = QtWidgets.QPushButton(self.IzhikevichParameters)
        self.SaveNeuronPushButton.setEnabled(True)
        self.SaveNeuronPushButton.setGeometry(QtCore.QRect(210, 530, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.SaveNeuronPushButton.setFont(font)
        self.SaveNeuronPushButton.setStyleSheet("color: rgb(147, 161, 161);")
        self.SaveNeuronPushButton.setObjectName("SaveNeuronPushButton")
        self.Tab2Title = QtWidgets.QLabel(self.TabNeuronGenerator)
        self.Tab2Title.setGeometry(QtCore.QRect(10, 1, 611, 31))
        self.Tab2Title.setStyleSheet("color: rgb(147, 161, 161);")
        self.Tab2Title.setObjectName("Tab2Title")
        self.Tab2Text1 = QtWidgets.QTextBrowser(self.TabNeuronGenerator)
        self.Tab2Text1.setGeometry(QtCore.QRect(10, 50, 581, 201))
        self.Tab2Text1.setStyleSheet("color: rgb(147, 161, 161);")
        self.Tab2Text1.setObjectName("Tab2Text1")
        self.Tab2Text2 = QtWidgets.QTextBrowser(self.TabNeuronGenerator)
        self.Tab2Text2.setGeometry(QtCore.QRect(10, 595, 800, 50))
        self.Tab2Text2.setStyleSheet("color: rgb(147, 161, 161);")
        self.Tab2Text2.setObjectName("Tab2Text2")
        self.BadenLabLogoTab2 = QtWidgets.QLabel(self.TabNeuronGenerator)
        self.BadenLabLogoTab2.setGeometry(QtCore.QRect(10, 645, 170, 45))
        self.BadenLabLogoTab2.setText("")
        self.BadenLabLogoTab2.setPixmap(QtGui.QPixmap("Pictures & Logos/Lab Logo.png"))
        self.BadenLabLogoTab2.setScaledContents(True)
        self.BadenLabLogoTab2.setObjectName("BadenLabLogoTab2")
        self.TrendLogoTab2 = QtWidgets.QLabel(self.TabNeuronGenerator)
        self.TrendLogoTab2.setGeometry(QtCore.QRect(390, 648, 51, 41))
        self.TrendLogoTab2.setText("")
        self.TrendLogoTab2.setPixmap(QtGui.QPixmap("Pictures & Logos/TReND Logo 2.png"))
        self.TrendLogoTab2.setScaledContents(True)
        self.TrendLogoTab2.setObjectName("TrendLogoTab2")
        self.ONLogoTab2 = QtWidgets.QLabel(self.TabNeuronGenerator)
        self.ONLogoTab2.setGeometry(QtCore.QRect(170, 655, 201, 21))
        self.ONLogoTab2.setText("")
        self.ONLogoTab2.setPixmap(QtGui.QPixmap("Pictures & Logos/ON Logo.png"))
        self.ONLogoTab2.setScaledContents(True)
        self.ONLogoTab2.setObjectName("ONLogoTab2")
        self.IzhikImage = QtWidgets.QLabel(self.TabNeuronGenerator)
        self.IzhikImage.setGeometry(QtCore.QRect(590, 50, 221, 191))
        self.IzhikImage.setText("")
        self.IzhikImage.setPixmap(QtGui.QPixmap("Pictures & Logos/izhik.png"))
        self.IzhikImage.setScaledContents(True)
        self.IzhikImage.setObjectName("IzhikImage")
        self.IzhikImage.raise_()
        self.Tab2Text1.raise_()
        self.TrendLogoTab2.raise_()
        self.LicenseTab2.raise_()
        self.Oscilloscope2.raise_()
        self.IzhikevichParameters.raise_()
        self.Tab2Title.raise_()
        self.Tab2Text2.raise_()
        self.BadenLabLogoTab2.raise_()
        self.ONLogoTab2.raise_()
        self.tabWidget.addTab(self.TabNeuronGenerator, "")
        self.TabStimulusGenerator = QtWidgets.QWidget()
        self.TabStimulusGenerator.setObjectName("TabStimulusGenerator")
        self.LicenseTab3 = QtWidgets.QLabel(self.TabStimulusGenerator)
        self.LicenseTab3.setGeometry(QtCore.QRect(0, 650, 1270, 20))
        self.LicenseTab3.setObjectName("LicenseTab3")
        self.Oscilloscope_3 = QtWidgets.QWidget(self.TabStimulusGenerator)
        self.Oscilloscope_3.setGeometry(QtCore.QRect(0, 70, 850, 480))
        self.Oscilloscope_3.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.Oscilloscope_3.setObjectName("Oscilloscope_3")
        self.tabWidget.addTab(self.TabStimulusGenerator, "")
        self.TabDataAnalysis = QtWidgets.QWidget()
        self.TabDataAnalysis.setObjectName("TabDataAnalysis")
        self.tabWidget.addTab(self.TabDataAnalysis, "")
        self.TabAbout = QtWidgets.QWidget()
        self.TabAbout.setStyleSheet("background-color: rgb(7, 54, 66);")
        self.TabAbout.setObjectName("TabAbout")
        self.tabWidget.addTab(self.TabAbout, "")
        Spikeling.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Spikeling)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background-color: rgb(7, 54, 66);")
        self.menubar.setObjectName("menubar")
        Spikeling.setMenuBar(self.menubar)

        self.retranslateUi(Spikeling)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Spikeling)





        self.SelectPortComboBox.currentIndexChanged.connect(lambda: self.ChangePort())

        self.radioButton.clicked.connect(lambda:self.ReadSerial())

        self.FolderNameLabel = QtWidgets.QLabel(self.DataRecordingBox)
        self.FolderNameLabel.setObjectName("FolderNameLabel")

        self.Oscilloscope1.setBackground(DarkSolarized[0])
        self.Oscilloscope2.setBackground(DarkSolarized[0])
        self.DisplayNeuronPushButton.clicked.connect(lambda: self.DrawNeuron())

        self.RecordFolderValue.textChanged.connect(lambda: self.RecordFolderText())
        self.RecordFolderDirPushButton.clicked.connect(lambda: self.BrowseRecordFolder())

        self.StimFreCheckBox.toggled.connect(lambda: self.ActivateStimFre())
        self.StimStrCheckBox.toggled.connect(lambda: self.ActivateStimStr())
        self.CustomStimulusCheckBox.toggled.connect(lambda: self.ActivateCustomStimulus())
        self.PhotoGainCheckBox.toggled.connect(lambda: self.ActivatePhotoGain())
        self.PRDecayCheckBox.toggled.connect(lambda: self.ActivatePRDecay())
        self.PRRecoveryCheckBox.toggled.connect(lambda: self.ActivatePRRecovery())

        self.MembranePotentialCheckBox.toggled.connect(lambda: self.ActivateMembranePotential())
        self.NoiseLevelCheckBox.toggled.connect(lambda: self.ActivateNoiseLevel())
        self.SynapticGain1CheckBox.toggled.connect(lambda: self.ActivateSynapticGain1())
        self.Synapse1DecayCheckBox.toggled.connect(lambda: self.ActivateSynapse1Decay())
        self.Synapse1RecoveryCheckBox.toggled.connect(lambda: self.ActivateSynapse1Recovery())
        self.SynapticGain2CheckBox.toggled.connect(lambda: self.ActivateSynapticGain2())
        self.Synapse2DecayCheckBox.toggled.connect(lambda: self.ActivateSynapse2Decay())
        self.Synapse2RecoveryCheckBox.toggled.connect(lambda: self.ActivateSynapse2Recovery())

    def retranslateUi(self, Spikeling):
        _translate = QtCore.QCoreApplication.translate
        Spikeling.setWindowTitle(_translate("Spikeling", "MainWindow"))
        self.NeuronParametersBox.setTitle(_translate("Spikeling", "Neuron parameters"))
        self.Synapse1Label.setText(_translate("Spikeling", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 1</span></p></body></html>"))
        self.Synapse2Label.setText(_translate("Spikeling", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Synapse 2</span></p></body></html>"))
        self.VoltageClampLabel.setText(_translate("Spikeling", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Voltage Clamp</span></p></body></html>"))
        self.MembranePotentialValue.setText(_translate("Spikeling", "-70"))
        self.Synapse1DecayCheckBox.setText(_translate("Spikeling", "Decay"))
        self.Synapse1RecoveryCheckBox.setText(_translate("Spikeling", "Recovery"))
        self.Synapse2RecoveryCheckBox.setText(_translate("Spikeling", "Recovery"))
        self.Synapse2DecayCheckBox.setText(_translate("Spikeling", "Decay"))
        self.Synapse2RecoveryValue.setText(_translate("Spikeling", "0.990"))
        self.Synapse2DecayValue.setText(_translate("Spikeling", "0.001"))
        self.SynapticGain2CheckBox.setText(_translate("Spikeling", "Synaptic Gain"))
        self.MembranePotentialCheckBox.setText(_translate("Spikeling", "Membrane potential "))
        self.SynapticGain1CheckBox.setText(_translate("Spikeling", "Synaptic Gain"))
        self.label_6.setText(_translate("Spikeling", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Noise</span></p></body></html>"))
        self.NoiseLevelCheckBox.setText(_translate("Spikeling", "Noise Level"))
        self.mVLabel.setText(_translate("Spikeling", "mV"))
        self.Noise0Label.setText(_translate("Spikeling", "0"))
        self.NoiseMaxLabel.setText(_translate("Spikeling", "max"))
        self.Synapse1DecayValue.setText(_translate("Spikeling", "0.001"))
        self.Synapse1RecoveryValue.setText(_translate("Spikeling", "0.995"))
        self.LicenseTab1.setText(_translate("Spikeling", "<html><head/><body><p align=\"right\">This project is licensed under the GNU General Public License v3.0</p></body></html>"))
        self.StimulationParametersBox.setTitle(_translate("Spikeling", "Stimulation parameters"))
        self.StimulusLabel.setText(_translate("Spikeling", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Stimulus</span></p></body></html>"))
        self.PhotoReceptorLabel.setText(_translate("Spikeling", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Photo-Receptor</span></p></body></html>"))
        self.CustomStimulusCheckBox.setText(_translate("Spikeling", "Custom Stimulus"))
        self.StimStrCheckBox.setText(_translate("Spikeling", "Stimulus Strenght"))
        self.StimFreCheckBox.setText(_translate("Spikeling", "Stimulus Frequency"))
        self.PhotoGainCheckBox.setText(_translate("Spikeling", "Photo-Gain"))
        self.PRRecoveryCheckBox.setText(_translate("Spikeling", "Recovery"))
        self.PRDecayCheckBox.setText(_translate("Spikeling", "Decay"))
        self.PRRecoveryValue.setText(_translate("Spikeling", "0.025"))
        self.PRDecayValue.setText(_translate("Spikeling", "0.001"))
        self.StimStr0Label.setText(_translate("Spikeling", "0"))
        self.Osc1VmCheckbox.setText(_translate("Spikeling", "Vm"))
        self.Osc1InputCurrentCheckbox.setText(_translate("Spikeling", "Input Current"))
        self.Osc1StimulusCheckbox.setText(_translate("Spikeling", "Stimulus"))
        self.Osc1Syn1VmCheckbox.setText(_translate("Spikeling", "Synapse 1 Vm"))
        self.Osc1Syn1InputCheckbox.setText(_translate("Spikeling", "Synapse 1 Input"))
        self.Osc1Syn2VmCheckbox.setText(_translate("Spikeling", "Synapse 2 Vm"))
        self.Osc1Syn1InputCheckbox_2.setText(_translate("Spikeling", "Synapse 2 Input"))
        self.DataRecordingBox.setTitle(_translate("Spikeling", "Data Recording"))
        self.RecordingComboBox.setItemText(0, _translate("Spikeling", "Live "))
        self.RecordingComboBox.setItemText(1, _translate("Spikeling", "Loop"))
        self.RecordPushButton.setText(_translate("Spikeling", "Record"))
        self.RecordFolderDirPushButton.setText(_translate("Spikeling", "Dir."))
        self.SelectRecordFolderLabel.setText(_translate("Spikeling", "Data Logging: Filename"))
        self.pushButton.setText(_translate("Spikeling", "Browse"))
        self.NumberOfLoopsLabel.setText(_translate("Spikeling", "Number of loops :"))
        self.SelectPortComboBox.setItemText(0, _translate("Spikeling", "Select a COM port:"))
        self.SelectPortLabel.setText(_translate("Spikeling", "Select Port :"))
        self.radioButton.setText(_translate("Spikeling", "Connected"))
        self.NeuronBrowsePushButton.setText(_translate("Spikeling", "Browse"))
        self.NeuronModeLabel.setText(_translate("Spikeling", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Neuron Mode</span></p></body></html>"))
        self.NeuronModeComboBox.setItemText(0, _translate("Spikeling", "Tonic Spiking"))
        self.NeuronModeComboBox.setItemText(1, _translate("Spikeling", "Phasic Spiking"))
        self.NeuronModeComboBox.setItemText(2, _translate("Spikeling", "Tonic Bursting"))
        self.NeuronModeComboBox.setItemText(3, _translate("Spikeling", "Phasic Bursting"))
        self.NeuronModeComboBox.setItemText(4, _translate("Spikeling", "Mixed Mode"))
        self.NeuronModeComboBox.setItemText(5, _translate("Spikeling", "Spike Frequency Adaptation"))
        self.NeuronModeComboBox.setItemText(6, _translate("Spikeling", "Class 1 Excitable"))
        self.NeuronModeComboBox.setItemText(7, _translate("Spikeling", "Class 2 Excitable"))
        self.NeuronModeComboBox.setItemText(8, _translate("Spikeling", "Spike Latency"))
        self.NeuronModeComboBox.setItemText(9, _translate("Spikeling", "Subthreshold Oscillations"))
        self.NeuronModeComboBox.setItemText(10, _translate("Spikeling", "Resonator"))
        self.NeuronModeComboBox.setItemText(11, _translate("Spikeling", "Integrator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabSpikeling), _translate("Spikeling", "Spikeling"))
        self.LicenseTab2.setText(_translate("Spikeling", "<html><head/><body><p align=\"right\">This project is licensed under the GNU General Public License v3.0</p></body></html>"))
        self.Osc2StimulusCheckbox_2.setText(_translate("Spikeling", "Stimulus"))
        self.Osc2VmCheckbox.setText(_translate("Spikeling", "Vm"))
        self.IzhikevichParameters.setTitle(_translate("Spikeling", "Izhikevich parameters"))
        self.aLabel.setText(_translate("Spikeling", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">a</span></p></body></html>"))
        self.a_Izhikevich.setText(_translate("Spikeling", "0.02"))
        self.b_Izhikevich.setText(_translate("Spikeling", "0.2"))
        self.c_Izhikevich.setText(_translate("Spikeling", "-65"))
        self.d_Izhikevich.setText(_translate("Spikeling", "2"))
        self.DisplayNeuronPushButton.setText(_translate("Spikeling", "Display Neuron"))
        self.Tab2Text3.setHtml(_translate("Spikeling", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The parameter<span style=\" font-size:12pt; font-weight:700;\"> a</span> describes the time scale of the recovery variable u. </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Smaller values result in slower recovery. </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">A typical value is a = 0.02.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The parameter <span style=\" font-size:12pt; font-weight:700;\">b</span> describes the sensitivity of the recovery variable u to the subthreshold fluctuations of the membrane potential v.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Greater values couple v and u more strongly resulting in possible subthreshold oscillations and low-threshold spiking dynamics. </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">A typical value is b = 0.2. </span>The case b &lt; a(b &gt; a) corresponds to saddle-node (Andronov–Hopf) bifurcation of the resting state</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The parameter <span style=\" font-size:12pt; font-weight:700;\">c</span> describes the after-spike reset value of the membrane potential v caused by the fast high-threshold K+ conductances. </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">A typical value is c = -65 (mV).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The parameter <span style=\" font-size:12pt; font-weight:700;\">d</span> describes after-spike reset of the recovery variable u caused by slow high-threshold Na+ and K+ conductances.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">A typical value is d = 2.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p></body></html>"))
        self.bLabel.setText(_translate("Spikeling", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">b</span></p></body></html>"))
        self.cLabel.setText(_translate("Spikeling", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">c</span></p></body></html>"))
        self.dLabel.setText(_translate("Spikeling", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">d</span></p></body></html>"))
        self.SaveNeuronPushButton.setText(_translate("Spikeling", "Save Neuron"))
        self.Tab2Title.setText(_translate("Spikeling", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Spikeling is built on the Izhikevich model</span></p></body></html>"))
        self.Tab2Text1.setHtml(_translate("Spikeling", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Bifurcation methodologies enable us to reduce many biophysically accurate Hodgkin–Huxley-type neuronal models to a two-dimensional (2-D) system of ordinary differential equations of the form:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">v\' = 0.04v</span><span style=\" font-size:11pt; font-weight:700; vertical-align:super;\">2</span><span style=\" font-size:11pt; font-weight:700;\"> + 5v + 140 - u + I                    </span><span style=\" font-size:11pt;\">&amp;</span><span style=\" font-size:11pt; font-weight:700;\">                    u\' = a(bv - u)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">with the auxiliary after-spike resetting:       if </span><span style=\" font-size:11pt; font-weight:700;\">v &gt;= 30 mV</span><span style=\" font-size:10pt;\">, then </span><span style=\" font-size:11pt; font-weight:700;\">v = c</span><span style=\" font-size:10pt;\"> and</span><span style=\" font-size:11pt;\"> </span><span style=\" font-size:11pt; font-weight:700;\">u = u + d</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:700;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Here, </span><span style=\" font-size:11pt; font-weight:700;\">v</span><span style=\" font-size:10pt;\"> and </span><span style=\" font-size:11pt; font-weight:700;\">u</span><span style=\" font-size:10pt;\"> are dimensionless variables, and </span><span style=\" font-size:11pt; font-weight:700;\">a</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:11pt; font-weight:700;\">b</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:11pt; font-weight:700;\">c</span><span style=\" font-size:10pt;\">, and </span><span style=\" font-size:11pt; font-weight:700;\">d</span><span style=\" font-size:10pt;\"> are dimensionless parameters, and </span><span style=\" font-size:11pt; font-weight:700;\">\'= d/dt</span><span style=\" font-size:10pt;\">, where </span><span style=\" font-size:11pt; font-weight:700;\">t</span><span style=\" font-size:10pt;\"> is the time. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The variable v represents the membrane potential of the neuron and </span><span style=\" font-size:11pt; font-weight:700;\">u</span><span style=\" font-size:10pt;\"> represents a membrane recovery variable, which accounts for the activation of K+ ionic currents and inactivation of Na+ ionic currents, and it provides negative feedback to </span><span style=\" font-size:11pt; font-weight:700;\">v</span><span style=\" font-size:10pt;\">. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">After the spike reaches its apex (+30 mV), the membrane voltage and the recovery variable are reset. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Synaptic currents or injected DC-currents are delivered via the variable</span><span style=\" font-size:10pt; font-weight:700;\"> </span><span style=\" font-size:11pt; font-weight:700;\">I</span><span style=\" font-size:10pt;\">.</span></p></body></html>"))
        self.Tab2Text2.setHtml(_translate("Spikeling", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">As most real neurons, the model does not have a fixed threshold: Depending on the history of the membrane potential prior to the spike, the threshold potential can be as low as -55 mV or as high as -40mV</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabNeuronGenerator), _translate("Spikeling", "Neuron mode generator"))
        self.LicenseTab3.setText(_translate("Spikeling", "<html><head/><body><p align=\"right\">This project is licensed under the GNU General Public License v3.0</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabStimulusGenerator), _translate("Spikeling", "Stimulus generator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabDataAnalysis), _translate("Spikeling", "Data Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabAbout), _translate("Spikeling", "About"))

        self.RecordFolderValue.setPlaceholderText(_translate("Spikeling", "Select a directory folder "))
        self.NumberOfLoopsValue.setPlaceholderText(_translate("Spikeling", "#"))
        for i in range(len(ports)):
            self.SelectPortComboBox.addItem("")
        for i in range (len(ports)):
            self.SelectPortComboBox.setItemText(i+1, _translate("Spikeling", str(portList[i])))


    def DrawNeuron(self):
            self.Oscilloscope2.clear()
            a = float(self.a_Izhikevich.text())
            b = float(self.b_Izhikevich.text())
            c = float(self.c_Izhikevich.text())
            d = float(self.d_Izhikevich.text())
            t = 0.0
            time = 250
            time1 = 50
            time2 = 200
            dt = 1.0 / 200.0
            ntime = int(time/dt)+1
            ntime1 = int(time1/dt)
            ntime2 = int(time2/dt)
            v = -65.0
            v_thresh = 30.0
            I_dc = 15.0
            u = 0.0
            vs = []
            nt = numpy.linspace(0, time, ntime)
            while t < time:
                    vs.append(v)
                    dv = (0.04 * v * v) + (5.0 * v) + 140.0 - u
                    du = a * ((b * v) - u)
                    if t > 50.0 and t < 200:
                            dv += I_dc
                    v += dv * dt
                    u += du * dt
                    if v >= v_thresh:
                            v = c
                            u = u + d
                    t += dt

            nstim = numpy.zeros(ntime)
            nstim[:] = -80
            nstim[ntime1:ntime2] = -20

            self.Oscilloscope2.plot(nt, nstim, pen=(DarkSolarized[3]))
            self.Oscilloscope2.plot(nt, vs, pen=(DarkSolarized[2]))
            self.Oscilloscope2.setBackground(DarkSolarized[0])
            self.Oscilloscope2.showGrid(x=True,y=True)

    def ChangePort(self):
            COM = self.SelectPortComboBox.currentText()
            serial_port = serial.Serial(COM, BaudRate)
            if serial_port.is_open:
                self.radioButton.setEnabled(True)
                serial_port.close()



    def ReadSerial(self):
            self.Oscilloscope1.clear()
            COM = self.SelectPortComboBox.currentText()
            serial_port = serial.Serial(port=COM,baudrate=BaudRate)

            sampleinterval = 0.01
            timewindow = 10.
            min_range = -90
            max_range = 30
            stimrange = ((-min_range) + max_range)/2

            self._interval = int(sampleinterval * 1000)
            self._bufsize = int(timewindow / sampleinterval)

            self.databuffer0 = collections.deque([0.0] * self._bufsize, self._bufsize)
            self.databuffer1 = collections.deque([0.0] * self._bufsize, self._bufsize)
            self.databuffer2 = collections.deque([0.0] * self._bufsize, self._bufsize)

            self.x = numpy.linspace(-timewindow, 0.0, self._bufsize)
            self.y0 = numpy.zeros(self._bufsize, dtype=float)
            self.y1 = numpy.zeros(self._bufsize, dtype=float)
            self.y2 = numpy.zeros(self._bufsize, dtype=float)

            self.Oscilloscope1.showGrid(x=True, y=True)
            self.Oscilloscope1.setRange(yRange=[-90,30])
            self.Oscilloscope1.setLabel('left', 'Membrane potential', 'mV')
            self.Oscilloscope1.setLabel('bottom', 'time', 'ms')
            self.Oscilloscope1.setLabel('right', 'Current Input', 'a.u.')

            self.p2 = pyqtgraph.ViewBox()
            self.Oscilloscope1.scene().addItem(self.p2)
            self.p2.setXLink(self.Oscilloscope1)
            self.p2.setRange(yRange=[-75,75])
            self.Oscilloscope1.getAxis("right").linkToView(self.p2)



            #self.curve2 = self.Oscilloscope1.plot(self.x, self.y2, pen=(DarkSolarized[4]))
            self.curve1 = self.Oscilloscope1.plot(self.x, self.y1, pen=(DarkSolarized[3]))
            self.curve0 = self.Oscilloscope1.plot(self.x, self.y0, pen=(DarkSolarized[2]))

            self.curve2 = pyqtgraph.PlotCurveItem(self.x, self.y2, pen=(DarkSolarized[4]))
            self.p2.addItem(self.curve2)
            def updateViews():
                    #global self.p2
                    self.p2.setGeometry(self.Oscilloscope1.getViewBox().sceneBoundingRect())
                    self.p2.linkedViewChanged(self.Oscilloscope1.getViewBox(), self.p2.XAxis)

            updateViews()
            self.Oscilloscope1.getViewBox().sigResized.connect(updateViews)

            def getdata0():
                    rx = serial_port.readline()
                    rx_serial = str(rx, 'utf8').strip()
                    data = rx_serial.split(',')
                    v = data[0]
                    return v
            def getdata1():
                    rx = serial_port.readline()
                    rx_serial = str(rx, 'utf8').strip()
                    data = rx_serial.split(',')
                    s = data[1]
                    return s
            def getdata2():
                    rx = serial_port.readline()
                    rx_serial = str(rx, 'utf8').strip()
                    data = rx_serial.split(',')
                    i = data[2]
                    return i


            def updateplot():
                    self.databuffer0.append(getdata0())
                    self.databuffer1.append(getdata1())
                    self.databuffer2.append(getdata2())

                    self.y0[:] = self.databuffer0
                    self.y1[:] = self.databuffer1
                    self.y2[:] = self.databuffer2

                    self.curve0.setData(self.x, self.y0)
                    self.curve1.setData(self.x, self.y1 * stimrange - 80)
                    self.curve2.setData(self.x, self.y2)
            # QTimer
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(lambda:updateplot())
            self.timer.start(self._interval)




    def BrowseRecordFolder(self):
            FolderName = QFileDialog.getExistingDirectory(self, 'Hey! Select the folder where your experiment will be saved')
            if FolderName:
                    self.SelectedFolderLabel.setText(FolderName)
                    self.FolderNameLabel.setText(FolderName)
                    self.RecordFolderValue.setEnabled(True)
                    self.RecordFolderValue.setPlaceholderText("Enter a file name")

    def RecordFolderText(self):
            FolderName = self.FolderNameLabel.text()
            FileName = self.RecordFolderValue.text()
            self.SelectedFolderLabel.setText(FolderName + '/' + FileName)

    def ActivateStimFre(self):
            if self.StimFreCheckBox.isChecked():
                    self.StimFreSlider.setEnabled(True)
            else:
                    self.StimFreSlider.setEnabled(False)
                    self.StimFreSlider.setValue(0)

    def ActivateStimStr(self):
            if self.StimStrCheckBox.isChecked():
                    self.StimStrSlider.setEnabled(True)
            else:
                    self.StimStrSlider.setEnabled(False)
                    self.StimStrSlider.setValue(0)

    def ActivateCustomStimulus(self):
            if self.CustomStimulusCheckBox.isChecked():
                    self.CustomStimuluComboBox.setEnabled(True)
            else:
                    self.CustomStimuluComboBox.setEnabled(False)

    def ActivatePhotoGain(self):
            if self.PhotoGainCheckBox.isChecked():
                    self.PhotoGainSlider.setEnabled(True)
            else:
                    self.PhotoGainSlider.setEnabled(False)
                    self.PhotoGainSlider.setValue(0)

    def ActivatePRDecay(self):
            if self.PRDecayCheckBox.isChecked():
                    self.PRDecayValue.setEnabled(True)
            else:
                    self.PRDecayValue.setEnabled(False)
                    self.PRDecayValue.setText("0.001")

    def ActivatePRRecovery(self):
            if self.PRRecoveryCheckBox.isChecked():
                    self.PRRecoveryValue.setEnabled(True)
            else:
                    self.PRRecoveryValue.setEnabled(False)
                    self.PRRecoveryValue.setText("0.025")

    def ActivateMembranePotential(self):
            if self.MembranePotentialCheckBox.isChecked():
                    self.MembranePotentialValue.setEnabled(True)
            else:
                    self.MembranePotentialValue.setEnabled(False)
                    self.MembranePotentialValue.setText("-70")

    def ActivateNoiseLevel(self):
            if self.NoiseLevelCheckBox.isChecked():
                    self.NoiseLevelSlider.setEnabled(True)
            else:
                    self.NoiseLevelSlider.setEnabled(False)
                    self.NoiseLevelSlider.setValue(0)

    def ActivateSynapticGain1(self):
            if self.SynapticGain1CheckBox.isChecked():
                    self.SynapticGain1Slider.setEnabled(True)
            else:
                    self.SynapticGain1Slider.setEnabled(False)
                    self.SynapticGain1Slider.setValue(0)

    def ActivateSynapse1Decay(self):
            if self.Synapse1DecayCheckBox.isChecked():
                    self.Synapse1DecayValue.setEnabled(True)
            else:
                    self.Synapse1DecayValue.setEnabled(False)
                    self.Synapse1DecayValue.setText("0.001")

    def ActivateSynapse1Recovery(self):
            if self.Synapse1RecoveryCheckBox.isChecked():
                    self.Synapse1RecoveryValue.setEnabled(True)
            else:
                    self.Synapse1RecoveryValue.setEnabled(False)
                    self.Synapse1RecoveryValue.setText("0.995")

    def ActivateSynapticGain2(self):
            if self.SynapticGain2CheckBox.isChecked():
                    self.SynapticGain2Slider.setEnabled(True)
            else:
                    self.SynapticGain2Slider.setEnabled(False)
                    self.SynapticGain2Slider.setValue(0)

    def ActivateSynapse2Decay(self):
            if self.Synapse2DecayCheckBox.isChecked():
                    self.Synapse2DecayValue.setEnabled(True)
            else:
                    self.Synapse2DecayValue.setEnabled(False)
                    self.Synapse2DecayValue.setText("0.001")

    def ActivateSynapse2Recovery(self):
            if self.Synapse2RecoveryCheckBox.isChecked():
                    self.Synapse2RecoveryValue.setEnabled(True)
            else:
                    self.Synapse2RecoveryValue.setEnabled(False)
                    self.Synapse2RecoveryValue.setText("0.990")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Spikeling = QtWidgets.QMainWindow()
    ui = Ui_Spikeling()
    ui.setupUi(Spikeling)
    Spikeling.show()
    sys.exit(app.exec())
