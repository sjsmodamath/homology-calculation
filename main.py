# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
import datetime
import dionysus as d
import numpy as np
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = numpy.loadtxt('car4.txt')
    print(a.shape)
    starttime = datetime.datetime.now()
    f = d.fill_rips(a, 4, 1.1)
    endtime = datetime.datetime.now()
    print(f)
    k=(endtime - starttime).seconds
    print(k)
    starttime = datetime.datetime.now()
    m = d.homology_persistence(f)
    endtime = datetime.datetime.now()
    k=(endtime - starttime).seconds
    print(k)
    dgms = d.init_diagrams(m, f)
    d.plot.plot_bars(dgms[0], show=True)
    d.plot.plot_bars(dgms[1], show=True)
