from kerchunk.combine import MultiZarrToZarr

# List of GeoTIFFs
tiff_files = ["s3://my-bucket/tile1.tif", "s3://my-bucket/tile2.tif"]

# Generate references for each file
refs = [kerchunk.rasterio.RasterioToZarr(f).translate() for f in tiff_files]

# Merge references
mzz = MultiZarrToZarr(refs)
merged_ref = mzz.translate()

# Save merged reference
with fsspec.open("merged_geotiffs.json", "w") as f:
    json.dump(merged_ref, f)


with fsspec.open("merged_geotiffs.json") as f:
    merged_ref = json.load(f)

mapper = fsspec.get_mapper("reference://", fo=merged_ref, target_options={})
ds = xr.open_zarr(mapper, consolidated=False)

print(ds)
