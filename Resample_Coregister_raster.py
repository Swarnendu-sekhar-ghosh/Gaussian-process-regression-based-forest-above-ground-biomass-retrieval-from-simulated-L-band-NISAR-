#!/usr/bin/env python
# coding: utf-8

# In[60]:


from osgeo import gdal



# In[61]:


# open reference file and get resolution

#referenceFile = "F:\\DATASETS\\UAVSAR_LENO\\NISARP_03112_CHM_2019.tif"

referenceFile = "reference file path"

reference = gdal.Open(referenceFile, 0)  # this opens the file in only reading mode
referenceTrans = reference.GetGeoTransform()


# In[62]:


x_res = referenceTrans[1]


# In[63]:


x_res


# In[64]:


y_res = -referenceTrans[5]  # make sure this value is positive


# In[65]:


y_res


# In[59]:


# specify input and output filenames

inputFile = "input file which needs to be resampled"

#inputFile = "F:\\DATASETS\\UAVSAR_LENO\\NISARP_03112_19044_009_190703_L090_CX_129_02.h5_20m_utm.tif"


outputFile = "path and name of output file after getting resampled "

# call gdal Warp
kwargs = {"format": "GTiff", "xRes": x_res, "yRes": y_res}
ds = gdal.Warp(outputFile, inputFile, **kwargs)



