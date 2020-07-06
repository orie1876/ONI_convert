#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename='experiment-1_sample-1-2_posXY0_channels_t0_posZ0_localizations.csv'   # This is the name of the SR file containing the localisations.
path='/Users/Mathew/Dropbox (Cambridge University)/Ed Code/ONI code/sample-1-2/pos_0/'       # Path to the file

toload=path+filename
fit = pd.read_table(toload,sep=',')       # Load files


# Plot a precision hsitogram
Precision=np.array(fit['X precision (nm)'])
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = "12"
plt.figure(figsize=(8, 6))
plt.hist(Precision, bins = 50,range=[0,100], rwidth=0.9,ec='red',color='#ff0000',alpha=0.3,density=True)
plt.xlabel('Precision (nm)')
plt.ylabel('Number of events')
plt.show()




fit_truncated = fit[['Frame', 'X raw (pix)','Y raw (pix)', 'Photons', 'PSF Sigma Y (pix)','PSF Sigma Y (pix)','Background','Photons','Z raw (pix)','X (pix)', 'Y (pix)','PSF Sigma X (pix)','PSF Sigma Y (pix)','X precision (nm)']].copy()
fit_truncated['X raw (pix)'] = fit_truncated['X raw (pix)'].astype(int)
fit_truncated['Y raw (pix)'] = fit_truncated['Y raw (pix)'].astype(int)

Out=open(path+'/'+'test.txt','w')   # Open file for writing to. 
    
    
    # Write the header of the file
Out.write("""#Localisation Results File
#FileVersion Text.D0.E0.V2
#Name Clustered (LSE)
#Source <gdsc.smlm.ij.IJImageSource><name>Clustered</name><width>428</width><height>512</height><frames>684</frames><singleFrame>0</singleFrame><extraFrames>0</extraFrames><path></path></gdsc.smlm.ij.IJImageSource>
#Bounds x0 y0 w428 h684
#Calibration <gdsc.smlm.results.Calibration><nmPerPixel>117.0</nmPerPixel><gain>55.5</gain><exposureTime>50.0</exposureTime><readNoise>0.0</readNoise><bias>0.0</bias><emCCD>false</emCCD><amplification>0.0</amplification></gdsc.smlm.results.Calibration>
#Configuration <gdsc.smlm.engine.FitEngineConfiguration><fitConfiguration><fitCriteria>LEAST_SQUARED_ERROR</fitCriteria><delta>1.0E-4</delta><initialAngle>0.0</initialAngle><initialSD0>2.0</initialSD0><initialSD1>2.0</initialSD1><computeDeviations>false</computeDeviations><fitSolver>LVM</fitSolver><minIterations>0</minIterations><maxIterations>20</maxIterations><significantDigits>5</significantDigits><fitFunction>CIRCULAR</fitFunction><flags>20</flags><backgroundFitting>true</backgroundFitting><notSignalFitting>false</notSignalFitting><coordinateShift>4.0</coordinateShift><shiftFactor>2.0</shiftFactor><fitRegion>0</fitRegion><coordinateOffset>0.5</coordinateOffset><signalThreshold>0.0</signalThreshold><signalStrength>30.0</signalStrength><minPhotons>0.0</minPhotons><precisionThreshold>400.0</precisionThreshold><precisionUsingBackground>true</precisionUsingBackground><nmPerPixel>117.0</nmPerPixel><gain>55.5</gain><emCCD>false</emCCD><modelCamera>false</modelCamera><noise>0.0</noise><minWidthFactor>0.5</minWidthFactor><widthFactor>1.01</widthFactor><fitValidation>true</fitValidation><lambda>10.0</lambda><computeResiduals>false</computeResiduals><duplicateDistance>0.5</duplicateDistance><bias>0.0</bias><readNoise>0.0</readNoise><amplification>0.0</amplification><maxFunctionEvaluations>2000</maxFunctionEvaluations><searchMethod>POWELL_BOUNDED</searchMethod><gradientLineMinimisation>false</gradientLineMinimisation><relativeThreshold>1.0E-6</relativeThreshold><absoluteThreshold>1.0E-16</absoluteThreshold></fitConfiguration><search>2.5</search><border>1.0</border><fitting>3.0</fitting><failuresLimit>10</failuresLimit><includeNeighbours>true</includeNeighbours><neighbourHeightThreshold>0.3</neighbourHeightThreshold><residualsThreshold>1.0</residualsThreshold><noiseMethod>QUICK_RESIDUALS_LEAST_MEAN_OF_SQUARES</noiseMethod><dataFilterType>SINGLE</dataFilterType><smooth><double>0.5</double></smooth><dataFilter><gdsc.smlm.engine.DataFilter>MEAN</gdsc.smlm.engine.DataFilter></dataFilter></gdsc.smlm.engine.FitEngineConfiguration>
#Frame	origX	origY	origValue	Error	Noise	Background	Signal	Angle	X	Y	X SD	Y SD	Precision

    """)
Out.write(fit_truncated.to_csv(sep = '\t',header=False,index=False))    # Write the columns that are required (without the non-clustered localisations)
    

