from virtualizarr import open_virtual_dataset

def generate_virtual_dataset(file_url):
    storage_options = {
        "anon": True,
        "default_fill_cache": False,
        "default_cache_type": "none"
    }
    vds = open_virtual_dataset(
        file_url,
        indexes={},
        filetype="tiff",
        reader_options={
            "remote_options": {"anon": True},
            "storage_options": storage_options,
        },
    )
    return vds

# Example usage
file_url = "s3://your-bucket-name/path/to/your-file.tif"
virtual_dataset = generate_virtual_dataset(file_url) 