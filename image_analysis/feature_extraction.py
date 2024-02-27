import dask.array as da
from dask_image.ndfilters import gaussian_filter
from joblib import Parallel, delayed

def extract_features_dask(image_chunk, sigmas=[1, 2, 4, 8, 16]):
    """
    Extract features from an image chunk using Gaussian blurring.
    This function applies Gaussian blurring with multiple sigma values.
    
    Parameters:
    - image_chunk: A chunk of the image (dask array).
    - sigmas: A list of sigma values for Gaussian blurring.
    
    Returns:
    - A dask array containing the extracted features for the chunk.
    """
    features = [gaussian_filter(image_chunk, sigma=sigma) for sigma in sigmas]
    return da.stack(features, axis=-1)

def parallel_feature_extraction(image, sigmas=[1, 2, 4, 8, 16], n_jobs=-1):
    """
    Parallel feature extraction across image chunks.
    
    Parameters:
    - image: The full image as a dask array.
    - sigmas: A list of sigma values for Gaussian blurring.
    - n_jobs: The number of jobs to run in parallel. -1 means using all processors.
    
    Returns:
    - A dask array of extracted features.
    """
    # Divide the image into non-overlapping chunks
    chunks = [image.rechunk(image.shape[i:i+1]) for i in range(image.ndim)]
    
    # Apply feature extraction in parallel across chunks
    features_list = Parallel(n_jobs=n_jobs)(
        delayed(extract_features_dask)(chunk, sigmas) for chunk in chunks
    )
    
    # Combine features back into a single dask array
    features = da.concatenate(features_list, axis=0)
    
    return features
