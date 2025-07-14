import xarray as xr
import numpy as np
import pandas as pd
import os
from glob import glob

def preprocess_data():
    # Load and merge netCDF files
    files = glob("../data/raw/*.nc")
    ds = xr.open_mfdataset(files, combine='by_coords')
    
    # Data cleaning
    ds = ds.where(ds.chlor_a > 0, drop=True)  # Remove negative values
    ds['log_chl'] = np.log(ds['chlor_a'])     # Log-transform
    
    # Feature engineering
    ds['chl_anomaly'] = ds['chlor_a'] - ds['chlor_a'].mean(dim='time')
    
    # Convert to DataFrame
    df = ds.to_dataframe().reset_index()
    df = df[['time', 'latitude', 'longitude', 'chlor_a', 'log_chl', 'chl_anomaly']]
    df.dropna(inplace=True)
    
    # Save processed data
    df.to_parquet("../data/processed/chlorophyll_data.parquet", index=False)
    return df

if __name__ == "__main__":
    preprocess_data()