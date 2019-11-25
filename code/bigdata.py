#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Math of Big Data
# Generated: Mon Nov 18 11:11:20 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import os
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class bigdata(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Math of Big Data")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Math of Big Data")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "bigdata")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.sig_src = sig_src = 0
        self.samp_rate = samp_rate = 44100
        self.rf_rate = rf_rate = 1000000
        self.fc = fc = 903000000
        self.chooser = chooser = 0
        self.amplitude = amplitude = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._sig_src_options = (0, 1, 2, )
        self._sig_src_labels = ('Silence', 'Recorded', 'Tones', )
        self._sig_src_group_box = Qt.QGroupBox('Audio Source')
        self._sig_src_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._sig_src_button_group = variable_chooser_button_group()
        self._sig_src_group_box.setLayout(self._sig_src_box)
        for i, label in enumerate(self._sig_src_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._sig_src_box.addWidget(radio_button)
        	self._sig_src_button_group.addButton(radio_button, i)
        self._sig_src_callback = lambda i: Qt.QMetaObject.invokeMethod(self._sig_src_button_group,
                                                                       "updateButtonChecked",
                                                                       Qt.Q_ARG("int",
                                                                                self._sig_src_options.index(i)))
        self._sig_src_callback(self.sig_src)
        self._sig_src_button_group.buttonClicked[int].connect(
        	lambda i: self.set_sig_src(self._sig_src_options[i]))
        self.top_layout.addWidget(self._sig_src_group_box)
        self._chooser_options = (0, 1, 2, 3, 4, )
        self._chooser_labels = ('None', '15 KHz', '8 KHz', '4 KHz', '1 KHz', )
        self._chooser_group_box = Qt.QGroupBox('Filter')
        self._chooser_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._chooser_button_group = variable_chooser_button_group()
        self._chooser_group_box.setLayout(self._chooser_box)
        for i, label in enumerate(self._chooser_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._chooser_box.addWidget(radio_button)
        	self._chooser_button_group.addButton(radio_button, i)
        self._chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._chooser_button_group,
                                                                       "updateButtonChecked",
                                                                       Qt.Q_ARG("int",
                                                                                self._chooser_options.index(i)))
        self._chooser_callback(self.chooser)
        self._chooser_button_group.buttonClicked[int].connect(
        	lambda i: self.set_chooser(self._chooser_options[i]))
        self.top_layout.addWidget(self._chooser_group_box)
        self._amplitude_range = Range(0, 1, 0.05, 0.5, 200)
        self._amplitude_win = RangeWidget(self._amplitude_range,
                                          self.set_amplitude, 'Volume', "counter_slider", float)
        self.top_layout.addWidget(self._amplitude_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=rf_rate,
                decimation=44100,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(0, 0.5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(rf_rate)
        self.osmosdr_sink_0.set_center_freq(fc, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(6, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(60, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

#Below the output is cutoff since the list contains a all the filter coefficients.
        self.fft_filter_xxx_1 = filter.fft_filter_ccc(1, ([0.003903353586792946, 0.004398836754262447, 0.004820726346224546, 0.005158012267202139, 0.00540095055475831, 0.005541282705962658, 0.005572437774389982, 0.005489712115377188, 0.005290416534990072, 0.0049739922396838665, 0.004542096983641386, 0.0039986493065953255, 0.003349836217239499, 0.002604085486382246, 0.0017719914903864264, 0.0008662082836963236, -9.869968198472634e-05, -0.0011064403224736452, -0.0021392127964645624, -0.0031779559794813395, -0.004202624782919884, -0.005192489828914404, -0.006126458290964365, -0.006983403582125902, -0.007742506451904774, -0.00838360097259283, -0.0088875163346529, -0.009236408397555351, -0.009414080530405045, -0.009406284429132938, -0.009200994856655598, -0.008788660168647766, -0.00816240906715393, -0.007318231742829084, -0.006255108397454023, -0.004975105170160532, -0.0034834130201488733, -0.0017883480759337544, 9.870219219010323e-05, 0.002163375960662961, 0.004388484172523022, 0.006754200905561447, 0.009238296188414097, 0.011816411279141903, 0.0144623639062047, 0.017148490995168686, 0.019846012815833092, 0.022525422275066376, 0.025156879797577858, 0.027710631489753723, 0.03015742264688015, 0.03246889263391495, 0.03461800515651703, 0.036579396575689316, 0.03832974657416344, 0.03984813764691353, 0.04111631214618683, 0.04211897775530815, 0.04284398630261421, 0.04328254610300064, 0.043429333716630936, 0.04328254610300064, 0.04284398630261421, 0.04211897775530815, 0.04111631214618683, 0.03984813764691353, 0.03832974657416344, 0.036579396575689316, 0.03461800515651703, 0.03246889263391495, 0.03015742264688015, 0.027710631489753723, 0.025156879797577858, 0.022525422275066376, 0.019846012815833092, 0.017148490995168686, 0.0144623639062047, 0.011816411279141903, 0.009238296188414097, 0.006754200905561447, 0.004388484172523022, 0.002163375960662961, 9.870219219010323e-05, -0.0017883480759337544, -0.0034834130201488733, -0.004975105170160532, -0.006255108397454023, -0.007318231742829084, -0.00816240906715393, -0.008788660168647766, -0.009200994856655598, -0.009406284429132938, -0.009414080530405045, -0.009236408397555351, -0.0088875163346529, -0.00838360097259283, -0.007742506451904774, -0.006983403582125902, -0.006126458290964365, -0.005192489828914404, -0.004202624782919884, -0.0031779559794813395, -0.0021392127964645624, -0.0011064403224736452, -9.869968198472634e-05, 0.0008662082836963236, 0.0017719914903864264, 0.002604085486382246, 0.003349836217239499, 0.0039986493065953255, 0.004542096983641386, 0.0049739922396838665, 0.005290416534990072, 0.005489712115377188, 0.005572437774389982, 0.005541282705962658, 0.00540095055475831, 0.005158012267202139, 0.004820726346224546, 0.004398836754262447, 0.003903353586792946]), 1)
        self.fft_filter_xxx_1.declare_sample_delay(0)
        self.fft_filter_xxx_0_1 = filter.fft_filter_ccc(1, ([0.0028788824565708637, 0.0022246302105486393, -0.0054065571166574955, 0.0036008567549288273, 0.0016665795119479299, -0.005552714224904776, 0.004340639337897301, 0.0010164391715079546, -0.005619300529360771, 0.005091989878565073, 0.00027059073909185827, -0.0055961222387850285, 0.005848423112183809, -0.0005751991411671042, -0.005472039803862572, 0.0066032810136675835, -0.0015262352535501122, -0.005234523676335812, 0.007349805440753698, -0.002589553128927946, -0.004868983756750822, 0.00808121357113123, -0.003774885553866625, -0.004357736557722092, 0.008790770545601845, -0.005096122156828642, -0.003678400767967105, 0.009471872821450233, -0.006573567166924477, -0.0028013368137180805, 0.010118113830685616, -0.008237586356699467, -0.0016854042187333107, 0.010723364539444447, -0.0101347416639328, -0.00027065255562774837, 0.011281842365860939, -0.012338690459728241, 0.0015349905006587505, 0.011788173578679562, -0.014970831573009491, 0.0038816523738205433, 0.012237459421157837, -0.018242765218019485, 0.007032625377178192, 0.012625332921743393, -0.02255321852862835, 0.011495769955217838, 0.012948009185492992, -0.028743509203195572, 0.018391413614153862, 0.013202328234910965, -0.03892756253480911, 0.03076619654893875, 0.013385793194174767, -0.06030977517366409, 0.06081909313797951, 0.013496600091457367, -0.14336292445659637, 0.2671947777271271, 0.6766828298568726, 0.2671947777271271, -0.14336292445659637, 0.013496600091457367, 0.06081909313797951, -0.06030977517366409, 0.013385793194174767, 0.03076619654893875, -0.03892756253480911, 0.013202328234910965, 0.018391413614153862, -0.028743509203195572, 0.012948009185492992, 0.011495769955217838, -0.02255321852862835, 0.012625332921743393, 0.007032625377178192, -0.018242765218019485, 0.012237459421157837, 0.0038816523738205433, -0.014970831573009491, 0.011788173578679562, 0.0015349905006587505, -0.012338690459728241, 0.011281842365860939, -0.00027065255562774837, -0.0101347416639328, 0.010723364539444447, -0.0016854042187333107, -0.008237586356699467, 0.010118113830685616, -0.0028013368137180805, -0.006573567166924477, 0.009471872821450233, -0.003678400767967105, -0.005096122156828642, 0.008790770545601845, -0.004357736557722092, -0.003774885553866625, 0.00808121357113123, -0.004868983756750822, -0.002589553128927946, 0.007349805440753698, -0.005234523676335812, -0.0015262352535501122, 0.0066032810136675835, -0.005472039803862572, -0.0005751991411671042, 0.005848423112183809, -0.0055961222387850285, 0.00027059073909185827, 0.005091989878565073, -0.005619300529360771, 0.0010164391715079546, 0.004340639337897301, -0.005552714224904776, 0.0016665795119479299, 0.0036008567549288273, -0.0054065571166574955, 0.0022246302105486393, 0.0028788824565708637]), 1)
        self.fft_filter_xxx_0_1.declare_sample_delay(0)
        self.fft_filter_xxx_0_0 = filter.fft_filter_ccc(1, ([0.0018509112996980548, 0.00425605196505785, 0.0053756218403577805, 0.004805463366210461, 0.0026688403449952602, -0.00040442057070322335, -0.0034613036550581455, -0.00551880057901144, -0.0058774263598024845, -0.004355869721621275, -0.0013690496562048793, 0.002181260846555233, 0.005175653845071793, 0.006626667454838753, 0.006000583525747061, 0.003407776355743408, -0.00040454373811371624, -0.004263333976268768, -0.0069261761382222176, -0.007476193364709616, -0.005631453823298216, -0.001866401406005025, 0.00270229484885931, 0.006640682928264141, 0.00864048395305872, 0.007945320568978786, 0.004623932298272848, -0.00040463957702741027, -0.005615596193820238, -0.009330428205430508, -0.010245315730571747, -0.007873144932091236, -0.002754001412540674, 0.003647102741524577, 0.009343433193862438, 0.012423933483660221, 0.011670381762087345, 0.00700198020786047, -0.00040470805834047496, -0.00838277768343687, -0.014376423321664333, -0.016217505559325218, -0.012852108106017113, -0.0047893403097987175, 0.005889771971851587, 0.01600692979991436, 0.02214829809963703, 0.02169501781463623, 0.013737058266997337, -0.0004047491238452494, -0.017234185710549355, -0.03175058588385582, -0.038605403155088425, -0.03347253054380417, -0.014284832403063774, 0.01799636147916317, 0.05930747836828232, 0.1031637042760849, 0.14196203649044037, 0.1686103790998459, 0.17809565365314484, 0.1686103790998459, 0.14196203649044037, 0.1031637042760849, 0.05930747836828232, 0.01799636147916317, -0.014284832403063774, -0.03347253054380417, -0.038605403155088425, -0.03175058588385582, -0.017234185710549355, -0.0004047491238452494, 0.013737058266997337, 0.02169501781463623, 0.02214829809963703, 0.01600692979991436, 0.005889771971851587, -0.0047893403097987175, -0.012852108106017113, -0.016217505559325218, -0.014376423321664333, -0.00838277768343687, -0.00040470805834047496, 0.00700198020786047, 0.011670381762087345, 0.012423933483660221, 0.009343433193862438, 0.003647102741524577, -0.002754001412540674, -0.007873144932091236, -0.010245315730571747, -0.009330428205430508, -0.005615596193820238, -0.00040463957702741027, 0.004623932298272848, 0.007945320568978786, 0.00864048395305872, 0.006640682928264141, 0.00270229484885931, -0.001866401406005025, -0.005631453823298216, -0.007476193364709616, -0.0069261761382222176, -0.004263333976268768, -0.00040454373811371624, 0.003407776355743408, 0.006000583525747061, 0.006626667454838753, 0.005175653845071793, 0.002181260846555233, -0.0013690496562048793, -0.004355869721621275, -0.0058774263598024845, -0.00551880057901144, -0.0034613036550581455, -0.00040442057070322335, 0.0026688403449952602, 0.004805463366210461, 0.0053756218403577805, 0.00425605196505785, 0.0018509112996980548]), 1)
        self.fft_filter_xxx_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, ([-0.003558691358193755, -0.005211095791310072, -0.0007477444014512002, 0.004758210387080908, 0.004821118898689747, -0.0008297579479403794, -0.005705812945961952, -0.003996317274868488, 0.002521971706300974, 0.0063015613704919815, 0.0027476600371301174, -0.004216135945171118, -0.0064582861959934235, -0.0011154226958751678, 0.005786840803921223, 0.006107581313699484, -0.0008307702955789864, -0.007101939059793949, -0.005204908549785614, 0.00299339578486979, 0.008028782904148102, 0.003733475459739566, -0.0052497913129627705, -0.008440246805548668, -0.0017066110158339143, 0.007455863989889622, 0.00821989867836237, -0.0008315581944771111, -0.0094501543790102, -0.007265483494848013, 0.0038072089664638042, 0.01105731911957264, 0.005489638075232506, -0.007119685877114534, -0.012089499272406101, -0.002816049614921212, 0.010645996779203415, 0.012342825531959534, -0.0008321212371811271, -0.014246711507439613, -0.011583548970520496, 0.005558452103286982, 0.017772935330867767, 0.009511140175163746, -0.011550930328667164, -0.021073974668979645, -0.005664809141308069, 0.01921885833144188, 0.02400524541735649, -0.0008324591908603907, -0.029571404680609703, -0.026435984298586845, 0.012114893645048141, 0.045557666569948196, 0.02825627103447914, -0.035449642688035965, -0.07940889894962311, -0.029383007436990738, 0.12199178338050842, 0.29200705885887146, 0.36633163690567017, 0.29200705885887146, 0.12199178338050842, -0.029383007436990738, -0.07940889894962311, -0.035449642688035965, 0.02825627103447914, 0.045557666569948196, 0.012114893645048141, -0.026435984298586845, -0.029571404680609703, -0.0008324591908603907, 0.02400524541735649, 0.01921885833144188, -0.005664809141308069, -0.021073974668979645, -0.011550930328667164, 0.009511140175163746, 0.017772935330867767, 0.005558452103286982, -0.011583548970520496, -0.014246711507439613, -0.0008321212371811271, 0.012342825531959534, 0.010645996779203415, -0.002816049614921212, -0.012089499272406101, -0.007119685877114534, 0.005489638075232506, 0.01105731911957264, 0.0038072089664638042, -0.007265483494848013, -0.0094501543790102, -0.0008315581944771111, 0.00821989867836237, 0.007455863989889622, -0.0017066110158339143, -0.008440246805548668, -0.0052497913129627705, 0.003733475459739566, 0.008028782904148102, 0.00299339578486979, -0.005204908549785614, -0.007101939059793949, -0.0008307702955789864, 0.006107581313699484, 0.005786840803921223, -0.0011154226958751678, -0.0064582861959934235, -0.004216135945171118, 0.0027476600371301174, 0.0063015613704919815, 0.002521971706300974, -0.003996317274868488, -0.005705812945961952, -0.0008297579479403794, 0.004821118898689747, 0.004758210387080908, -0.0007477444014512002, -0.005211095791310072, -0.003558691358193755]), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/andy/Documents/flight_of_the_bumblebee.wav', True)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(math.pi)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((amplitude, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((0.5, ))
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=sig_src,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=5,
        	num_outputs=1,
        	input_index=chooser,
        	output_index=0,
        )
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 440, 0.4, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 3520, 0.1, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blks2_selector_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.fft_filter_xxx_0_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.fft_filter_xxx_0_1, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.fft_filter_xxx_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_selector_0_0, 2))
        self.connect((self.blocks_complex_to_real_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blks2_selector_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blks2_selector_0, 2))
        self.connect((self.fft_filter_xxx_0_0, 0), (self.blks2_selector_0, 3))
        self.connect((self.fft_filter_xxx_0_1, 0), (self.blks2_selector_0, 1))
        self.connect((self.fft_filter_xxx_1, 0), (self.blks2_selector_0, 4))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_rotator_cc_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bigdata")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def setStyleSheetFromFile(self, filename):
        try:
            if not os.path.exists(filename):
                filename = os.path.join(
                    gr.prefix(), "share", "gnuradio", "themes", filename)
            with open(filename) as ss:
                self.setStyleSheet(ss.read())
        except Exception as e:
            print >> sys.stderr, e

    def get_sig_src(self):
        return self.sig_src

    def set_sig_src(self, sig_src):
        self.sig_src = sig_src
        self._sig_src_callback(self.sig_src)
        self.blks2_selector_0_0.set_input_index(int(self.sig_src))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rf_rate(self):
        return self.rf_rate

    def set_rf_rate(self, rf_rate):
        self.rf_rate = rf_rate
        self.osmosdr_sink_0.set_sample_rate(self.rf_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.osmosdr_sink_0.set_center_freq(self.fc, 0)

    def get_chooser(self):
        return self.chooser

    def set_chooser(self, chooser):
        self.chooser = chooser
        self._chooser_callback(self.chooser)
        self.blks2_selector_0.set_input_index(int(self.chooser))

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.blocks_multiply_const_vxx_0.set_k((self.amplitude, ))


def main(top_block_cls=bigdata, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.setStyleSheetFromFile('/home/andy/math_of_big_data/projector.qss')
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
