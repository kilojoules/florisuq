
# coding: utf-8

# # Build 30 s dataset

# In[8]:

## Build up datasets of 30 sec 


# In[9]:

# %matplotlib inline
import os
import computeDEL
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import matplotlib.gridspec as gridspec
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import scipy.io as spio
import wrapFunctions #import wrap180, wrap360, wrapList
import glob
import pandas as pd


# ## Parameters

# In[10]:

justOne = False #for debugging, try just one file?

# Inputs
dataRoot = 'Y:\\Wind\\Confidential\\Projects\\Cert\\D-Z\\Field Testing\\GE 1.5SLE\\Tests\\FY16\\NextEra Yaw Error Project\\Wind Vane Misalignment - SRDana\\Data\\FT_Formatted Fast Data'
Fs = 50. #Hz
fileLength = 600. #s

# Outputs
interval = 30 #s
dataOut = 'data30_redo'

# Limit range
powLim = 50. #kW (making at least some power)
yawLim = [225., 25.] #note this is an or


# In[11]:

#Long Version
signalList = [
 'OPC_In_RotorSpd',
 'Air_Press_1',
 'Mainshaft_Downwind_Bend_0',
 'BL1_FlapMom',
 'Azimuth',
 'Blade_1_Edge',
 'TowerBaseTorque',
 'Yaw_Encoder',
 'TB_ForeAft',
 'WS1_90m',
 'LSSDW_Mz',
 'LSSDW_My',
 'TTTq',
 'TT_ForeAft',
 'MainShaftBending_0',
 'Temp1',
 'WindSpeed_80m',
 'LSSDW_M90',
 'ScanErrors',
 'MSExcelTimestamp',
 'Pitch_Blade1',
 'LSSDW_Tq',
 'TT_SideSide',
 'ApparentPower',
 'apparantVane',
 'MainShaftTorque',
 'WD_Nacelle',
 'LateScans',
 'BL1_EdgeMom',
 'Mainshaft_Downwind_Torque',
 'LidarOffset',
 'LabVIEWTimestamp',
 'Blade_1_Flap',
 'Mainshaft_Downwind_Bend_90',
 'TowerTopTorque',
 'WD1_87m',
 'MainShaftTorqueNew',
 'TBTq',
 'TB_SideSide']

angularSignalList = ['Azimuth','Yaw_Encoder','Pitch_Blade1','WD_Nacelle','apparantVane','WD1_87m']

m10list = ['BL1_FlapMom','BL1_EdgeMom'] # list of loads which use an m-value of 10, the rest are 4


# In[12]:

#Condensed Version
signalList = [
 'OPC_In_RotorSpd',
 'BL1_FlapMom',
 'Azimuth',
 'TowerBaseTorque',
 'Yaw_Encoder',
 'TB_ForeAft',
 'WS1_90m',
 'LSSDW_Mz',
 'LSSDW_My',
 'WindSpeed_80m',
 'TTTq',
 'TT_ForeAft',
 'Pitch_Blade1',
 'LSSDW_Tq',
 'TT_SideSide',
 'ApparentPower',
 'apparantVane',
 'WD_Nacelle',
 'BL1_EdgeMom',
 'Mainshaft_Downwind_Torque',
 'LidarOffset',
 'LabVIEWTimestamp',
 'Mainshaft_Downwind_Bend_90',
 'TowerTopTorque',
 'WD1_87m',
 'TBTq',
 'TB_SideSide']
 
angularSignalList = ['Azimuth','Yaw_Encoder','Pitch_Blade1','WD_Nacelle','apparantVane','WD1_87m']

m10list = ['BL1_FlapMom','BL1_EdgeMom'] # list of loads which use an m-value of 10, the rest are 4


# In[13]:

# Calculated parameters
numBins = int(fileLength/interval)
binEdge = range(0,int(fileLength*Fs) +int(interval * Fs) ,int(interval * Fs))
binEdge[0] = -1
#binEdge


# ## Load and process data

# In[14]:

# Get list of folders to process
dateFolders = os.listdir(dataRoot)


# In[15]:

# Set up output files
outputFile = os.path.join(dataOut,'dataFile.csv')
filenameFile = os.path.join(dataOut,'filenames.txt')


# In[16]:

# Set up a load file functions

# From http://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries

def loadmat(filename):
    '''
    this function should be called instead of direct spio.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    '''
    try:
        data = spio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    except:
        print 'some issue loading'
        return False
    return _check_keys(data)

def _check_keys(dict):
    '''
    checks if entries in dictionary are mat-objects. If yes
    todict is called to change them to nested dictionaries
    '''
    for key in dict:
        if isinstance(dict[key], spio.matlab.mio5_params.mat_struct):
            dict[key] = _todict(dict[key])
    return dict        

def _todict(matobj):
    '''
    A recursive function which constructs from matobjects nested dictionaries
    '''
    dict = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, spio.matlab.mio5_params.mat_struct):
            dict[strg] = _todict(elem)
        else:
            dict[strg] = elem
    return dict

# Finally the load file function

def loadGEfile(filename):

    data = loadmat(filename)
    if data:
        data = data['data_out']

        # Add the apparant vane signal
        data['apparantVane'] = dict()
        data['apparantVane']['processed'] =  np.array(wrapFunctions.wrapList(data['WD1_87m']['processed'] - data['Yaw_Encoder']['processed'] ))
    
    return data


# In[17]:

# Angular mean and standard deviation helper and del helper function

import math

def mixedMean(ser):
    
    #print ser.name
    
    #agg = pd.DataFrame()
    #for col in df.columns:
    if ser.name in angularSignalList:
        #print  ser.name + ' is angular'
        xAng += np.cos(ser*(np.pi/180.))
        yAng += np.sin(ser*(np.pi/180.))

        sMean = math.atan2(yAng,xAng)*(180./np.pi)
        
    else:
        sMean = np.mean(ser)
    return sMean

def mixedDEL(ser):
    
    if ser.name in m10list:
        return computeDEL.computeDEL(ser,1./Fs,10.)
    else:
        return computeDEL.computeDEL(ser,1./Fs,4.)
            


# In[24]:

# Get a list of already processed files
processedFiles = []
with open(filenameFile) as f:
    contents = f.readlines()
for i in contents:
    processedFiles.append(i.rstrip('\n'))
#print processedFiles


# In[ ]:

#os.remove(outputFile)



for dateFolder in dateFolders:
    print 'Processing ' + dateFolder
    
    folder = os.path.join(dataRoot,dateFolder)
    
    # Get a list of mat files
    files = os.listdir(folder)
    files = [f for f in files if '.mat' in f]
    
    for f in files:
        
        # Check if we've allready processed this one
        if f in processedFiles:
            print 'File ' + f + ' is already processed'
            continue
        
        fullFile = os.path.join(folder,f)
        print '... file ' + f
        
        # Load the file
        data = loadGEfile(fullFile)
        
        if not data:
            'skipping file due to badness'
            continue
        
        #Simplify into a dataframe
        dataCon = pd.DataFrame()
        for s in signalList:
            dataCon[s] = data[s]['processed'] 
            
        # Ensure there are 30000 rows
        if dataCon.shape[0] != int(Fs * fileLength):
            print 'ill-sized dataframe'
            continue
        
        # Group the data into intervals
        dataCon['interval'] = pd.cut(dataCon.index,binEdge)
        grouped = dataCon.groupby('interval')
        
        # Compute the mean
        gMean = grouped.aggregate(mixedMean)
        gMean.columns = [c + '_mean' for c in gMean.columns]
        
        # Compute the std
        gStd = grouped.aggregate(np.std)
        gStd.columns = [c + '_std' for c in gStd.columns]
        
        # Compute the min
        gMin = grouped.aggregate(np.min)
        gMin.columns = [c + '_min' for c in gMin.columns]
        
        # Compute the max
        gMax = grouped.aggregate(np.max)
        gMax.columns = [c + '_max' for c in gMax.columns]
        
        # Compute the del
        gDEL = grouped.aggregate(mixedDEL)
        gDEL.columns = [c + '_del' for c in gDEL.columns]
        
        # Merge the dataframes
        merged = pd.concat([gMean,gStd,gMin,gMax,gDEL],axis=1)
        
        # Filter down by power and wind direction
        merged = merged[merged.ApparentPower_mean > powLim]
        merged = merged[(merged.WD1_87m_mean > yawLim[0]) | (merged.WD1_87m_mean < yawLim[1])]
        
        # Add a data column
        merged['date'] = dateFolder
        
        #Record this filename
        with open(filenameFile, 'a') as ff:
            ff.write(f + '\n')
        
        
        if (merged.shape[0] == 0):
            print '..... no rows meet criteria, skipping'
            if justOne:
                break
            continue
            
        
        
        # Write to file
        if not os.path.isfile(outputFile):
            print 'creating file'
            with open(outputFile,'w') as ff:
                merged.to_csv(ff, header=True, index=False)
        else:
            print '...... WRITE TO FILE'
            with open(outputFile, 'a') as ff:
                merged.to_csv(ff, header=False,index=False)
                

        
        if justOne:
            break
    
    if justOne:
        break


# In[23]:

justOne=False

