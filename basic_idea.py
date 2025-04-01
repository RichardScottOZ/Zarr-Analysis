pip install rasterio fsspec kerchunk xarray zarr
pip install gcsfs s3fs

import fsspec
import kerchunk.rasterio
import json

# Path to a local or remote GeoTIFF
tiff_path = "s3://my-bucket/my-geotiff.tif"  # or "file:///path/to/local.tif"

# Create the Kerchunk reference
ref_gen = kerchunk.rasterio.RasterioToZarr(tiff_path)
ref = ref_gen.translate()

# Save the reference to a JSON file
with fsspec.open("geotiff_reference.json", "w") as f:
    json.dump(ref, f)

import xarray as xr
import fsspec
import zarr

# Load the reference JSON
with fsspec.open("geotiff_reference.json") as f:
    ref = json.load(f)

# Open as a Zarr dataset
mapper = fsspec.get_mapper("reference://", fo=ref, target_options={})
ds = xr.open_zarr(mapper, consolidated=False)

# Print dataset details
print(ds)



