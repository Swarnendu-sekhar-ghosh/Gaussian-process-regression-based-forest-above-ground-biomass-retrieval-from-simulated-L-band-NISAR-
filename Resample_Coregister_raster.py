
from osgeo import gdal

# open reference file and get resolution

referenceFile = "reference file path"

reference = gdal.Open(referenceFile, 0)  # this opens the file in only reading mode
referenceTrans = reference.GetGeoTransform()

x_res = referenceTrans[1]

y_res = -referenceTrans[5]  # make sure this value is positive

# specify input and output filenames

inputFile = "input file which needs to be resampled"

outputFile = "path and name of output file after getting resampled "

# call gdal Warp

kwargs = {"format": "GTiff", "xRes": x_res, "yRes": y_res}
ds = gdal.Warp(outputFile, inputFile, **kwargs)



