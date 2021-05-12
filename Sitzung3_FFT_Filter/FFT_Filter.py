#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:45:50 2021

@author: marius
"""

##wir beginnen damit, einige Packages zu importieren, die wir brauchen werden, und unsere Beispieldaten zu laden
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

dat=np.load("timeseries.npy") 
dat_all = dat.copy()
dat = dat[:20000]
#es handelt sich um Ruhe-EEG-Daten von einem zentralen Kanal (Cz), 
#die wir vor einigen Wochen im Institut aufgezeichnet haben
#wir plotten die Zeitreihe, um einen ersten Eindruck zu bekommen:

plt.figure()
plt.plot(dat)


#%% Diskrete Sinus-Transformation

#eine Grundannahme der Fourier-Analysis besagt, dass jedes zeitdiskrete Signal
#als gewichtete Summe komplexer Sinuswellen dargestellt werden kann. 


#Ein Signal kann informationserhaltend vom Zeitraum in den Frequenzraum ueberfuehrt werden, indem
#fuer jede moegliche Frequenz ein Sinus gleicher Laenge erzeugt und das Signal
#mit diesem gefaltet (engl. convolution - algebraisch einfach das Punkt-Produkt 
#der Vektoren) wird (Diskrete Fourier-Transformation, DFT).


#wir versuchen eine erste Implementierung.
t = np.linspace(0,1,len(dat)) #Hilfs-Vektor in Laenge des Signals erzeugen
sine_coefficients = np.zeros(len(dat),dtype='float') #leeren Koeffizientenvektor erzeugen, der vom Loop gefuellt wird
for freq in np.arange(len(dat)): #Erzeuge so viele verschiedene Sinus, wie es Zeitpunkte im Signal gibt
    sinewave = np.sin(2*np.pi*freq*t) #wir erzeugen einen Sinus in gleicher Laenge wie das Signal
    sine_coefficients[freq] = sinewave.dot(dat) #Punktprodukt


#wir plotten die so erzeugten Koeffizienten. Was faellt Ihnen auf?
plt.figure()
plt.plot(sine_coefficients)
"""
Aufgabe 1: Diese Implementierung ist sehr ineffizient (braucht auf meinem Rechner ca. 5 Minuten).
Zum Glueck gibt es die Fast Fourier Transformation (FFT), einen deutlich effizienteren
Algorithmus, der bereits auf C.F. Gauss zurueckgeht, aber erst im Zeitalter der
Computer sinnvoll implementierbar war.

a) recheerchieren Sie, wie Sie in Numpy eine FFT durchfuehren koennen. Berechnen 
    Sie sie und speichern Sie das Ergebnis in einer neuen Variable fft_coefficients.
b) Stellen Sie die Arrays sine_coefficients und fft_coefficients in einer
    gemeinsamen Abbildung dar. Was faellt Ihnen auf?
c) Auf der X-Achse Ihres Plots ist die Frequenz abgetragen, allerdings nicht
    in Hertz oder einer anderen bekannten Einheit. Ermitteln Sie die Frequenzen in
    Hertz und stellen Sie sie auf der X-Achse dar.
"""

fft_coefficients = np.fft.fft(dat)
plt.plot(np.abs(fft_coefficients))
freqs = np.fft.fftfreq(len(fft_coefficients), d = 1/1000)
"""Musterlösung
#a)
fft_coefficients = np.fft.fft(dat)
#b)
plt.plot(np.abs(fft_coefficients))
#c)
#höchste abbildbare Frequenz ist die Nyquist-Frequenz = halbe Samplingfrequenz.
#die zweite Hälfte des Spektrums ist symmetrisch zur ersten und kann, für reell-
#wertige Ausgangssignale, ignoriert werden. Die Frequenzen in Hertz ergeben sich dann als 
#lineare Sequenz zwischen 0 und der Nyquist-Frequenz (500 Hz)
frequencies = np.zeros(len(fft_coefficients))
frequencies[:int(len(frequencies)/2)+1] = np.linspace(0,500,int(len(frequencies)/2)+1)
frequencies[int(len(frequencies)/2):] = np.linspace(-500,0,int(len(frequencies)/2)+1)[:-1]
"""




#%% Diskrete Fourier-Transformation

"""
Aufgabe 2: Da unsere 'von Hand' erzeugten Koeffizienten den FFT-Koeffizienten zwar
sehr aehnlich, aber nicht identisch waren, haben wir wohl in unserem obigen Loop noch
keine vollstaendige Fourier-Transformation implementiert. Der Grund ist, dass wir nur
reellwertige und keine komplexen Sinuswellen erzeugt haben.

a) Schreiben Sie den Loop von Zeile 36 ff. um, so dass komplexe statt reeller Sinus
    erzeugt werden. Benutzen Sie dafuer die Eulersche Formel. Benennen Sie den Koeffizientenvektor
    um in dft_coefficients. Beachten Sie, dass Sie das "dtype"-Argument aendern muessen,
    damit der Vektor komplexe Zahlen akzeptiert
    https://de.wikipedia.org/wiki/Eulersche_Formel
b) Stellen Sie unsere oben erzeugten FFT- und die hier erzeugten DFT-Koeffizienten in einer
    gemeinsamen Abbildung dar. Sind die beiden Koeffizientenvektoren jetzt identisch?
c) Zeigen Sie, dass die Fourier-Transformation informationserhaltend ist, indem Sie eine
    inverse FFT durchfuehren.
"""

t = np.linspace(0,1,len(dat)) #Hilfs-Vektor in Laenge des Signals erzeugen
dft_coefficients = np.zeros(len(dat),dtype='complex') #leeren Koeffizientenvektor erzeugen, der vom Loop gefuellt wird
for freq in np.arange(len(dat)): #Erzeuge so viele verschiedene Sinus, wie es Zeitpunkte im Signal gibt
    sinewave = np.exp(-1j*2*np.pi*freq*t) #wir erzeugen einen Sinus in gleicher Laenge wie das Signal
    dft_coefficients[freq] = sinewave.dot(dat) #Punktprodukt


plt.figure()
plt.plot(np.abs(fft_coefficients))
plt.plot(np.abs(dft_coefficients))


"""Musterlösung
#plot 3D
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sinewave = np.exp(-1j*2*np.pi*5*t) #wir erzeugen einen Sinus in gleicher Laenge wie das Signal
ax.plot(t,np.real(sinewave), np.imag(sinewave))
#kopiert von Zeile 36ff.
t = np.linspace(0,1,len(dat)) #Hilfs-Vektor in Laenge des Signals erzeugen
dft_coefficients = np.zeros(len(dat),dtype='complex') #leeren Koeffizientenvektor erzeugen, der vom Loop gefuellt wird
for freq in range(len(dat)): #Erzeuge so viele verschiedene Sinus, wie es Zeitpunkte im Signal gibt
    sinewave = np.exp(-1j*2*np.pi*freq*t) #wir erzeugen einen Sinus in gleicher Laenge wie das Signal
    dft_coefficients[freq] = sinewave.dot(dat) #Punktprodukt

fft_coefficients = np.fft.fft(dat)
plt.plot(np.abs(dft_coefficients))
plt.plot(np.abs(fft_coefficients))

np.allclose(dat, np.fft.ifft(np.fft.fft(dat)))

"""

#%% Filter

#Digitale Zeit-Filter unterdruecken unerwuenschte Frequenzanteile im Signal, um 
#interessierende Frequenzanteile besser sichtbar zu machen.
#Man unterscheidet Filter mit endlicher (Finite Impulse Response, FIR) 
#von solchen mit unendlicher Impulsantwort (Infinite Impulse Response, IIR).
#Um den Unterschied zu demonstrieren, erstellen wir einen einfachen Dirac-Impuls:


dirac = np.zeros(1000)
dirac[500] = 1
plt.figure()
plt.plot(dirac, label = "Original")



#Wir erstellen nun ein FIR- und ein Butterworth-IIR-Filter mit gleich langen
#Filterkernen (erstes Argument der Funktion) und benutzen diese, um die Impulsantwort zu ermitteln.
butterworth = signal.butter(4,.05,btype='low')
fir = signal.firwin(9, .05)

#Die lfilter-Funktion macht im Grunde nichts anderes, als das Signal mit dem Filterkern
#zu falten (fuer FIR-Filter) bzw. das Ausgangssignal und das vorhergehende gefilterte Signal
#rekursiv mit dem Zaehler- und Nennerkern zu falten (IIR-Filter)
filtered_fir = signal.lfilter(fir,1,dirac)
filtered_butterworth = signal.lfilter(*butterworth,dirac)


plt.plot(filtered_fir, label = "FIR")
plt.plot(filtered_butterworth, label = "IIR")
plt.legend()


"""
Aufgabe 3: Betrachten Sie den soeben geoeffneten Plot mit den drei Kurven. Was faellt Ihnen auf?

a) Das Maximum des gefilterten Signals ist, verglichen mit dem Ausgangspuls, nach rechts verschoben.
    Ueberlegen Sie: Woran liegt das? Wie koennte diese Verschiebung behoben werden?
b) Demonstrieren Sie, was mit "endlicher" und "unendlicher" Impulsantwort gemeint ist. Schreiben Sie dazu einen Loop,
    in dem Sie fuer beide Filterarten das Signal mit Filtern unterschiedlicher Ordnung (Filterkernlaengen) filtern. Speichern
    Sie fuer jede Filterordnung, wie lang die Impulsantwort ist (quantifiziert als Anzahl der von Null verschiedenen Stellen des
                                                                 gefilterten Signals). Stellen Sie das Ergebnis graphisch dar.
"""


ir_butter = []
ir_fir = []
kernels = range(1,500)
for kernel in kernels:
    butterworth = signal.butter(kernel,.05,btype='low') #Tiefpassfilter
    fir = signal.firwin(kernel, .05)

    filtered_fir = signal.lfilter(fir,1,dirac)
    filtered_butterworth = signal.lfilter(*butterworth,dirac)
    ir_butter.append(sum(filtered_butterworth != 0))
    ir_fir.append(sum(filtered_fir != 0))


plt.figure()
plt.plot(kernels, ir_butter, label = "IIR")
plt.plot(kernels, ir_fir, label = "FIR")
plt.legend()



"""Musterlösung
#Faltung läuft in Vorwärts-Richtung, daher Verschiebung. Übliche Lösung ist,
#das Signal nochmals rückwärts zu filtern (funktion signal.filtfilt)


ir_butter = []
ir_fir = []
kernels = range(1,50)
for kernel in kernels:
    butterworth = signal.butter(kernel,.05,btype='low')
    fir = signal.firwin(kernel, .05)

    filtered_fir = signal.lfilter(fir,1,dirac)
    filtered_butterworth = signal.lfilter(*butterworth,dirac)
    ir_butter.append(sum(filtered_butterworth != 0))
    ir_fir.append(sum(filtered_fir != 0))


plt.figure()
plt.plot(kernels, ir_butter, label = "IIR")
plt.plot(kernels, ir_fir, label = "FIR")
plt.legend()
"""






#%%

dat = dat_all    

butter = signal.butter(4, (1, 30), fs = 1000, btype = "pass")
notch = signal.butter(4, (48,52), fs = 1000, btype = "stop")
dat_filtered = signal.filtfilt(*butter, dat)
dat_filtered_notch = signal.filtfilt(*notch, dat_filtered)
plt.figure()
plt.plot(dat)
plt.plot(dat_filtered)
plt.plot(dat_filtered_notch)


f, r = signal.freqz(*butter, fs = 1000)
plt.plot(f,np.abs(r))




