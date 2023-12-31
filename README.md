# View-Adaptive Streaming of Point Cloud Scenes through combined Decomposition and Video-based Coding

Accompaning repository to the [paper](https://dl.acm.org/doi/abs/10.1145/3552457.3555732) **View-Adaptive Streaming of Point Cloud Scenes through combined Decomposition and Video-based Coding**, presented at APCCPA '22: 1st International Workshop on Advances in Point Cloud Compression, Processing and Analysis.

The modification of the V-PCC codec in this repository allows to generate separate bitstreams for each projection direction, allowing view-dependent adaptation of quality in a streaming scenario.

This repository is based on [mpeg-tmc2](https://github.com/MPEGGroup/mpeg-pcc-tmc2). You can find detailed documentation on the V-PCC codec here.
Configurations are designed for the [8i VFB v2](http://plenodb.jpeg.org/pc/8ilabs/) dataset.

## Building
The repository was built and tested on Ubuntu 22.04 using gcc/g++-9.

You can run the installation script directly using
```
    ./build.sh
```

### Verify installation
Verify the correctness of the build:

```
    ./encode.sh
    ./decode.sh
    ./compute_metrics.sh
```

You will need to change the following paths for that:
	*--uncompressedDataFolder=/path/to/8iData/* in *encode.sh*
 	*--uncompressedDataPath=/path/to/8iData/* in *compute_metrics.sh*
  and
  	*--normalDataPath=/path/to/8iNormals/* in *compute_metrics.sh*, if you have normals available. Otherwise, remove this argument.

## Running

Examples for running can be found in [encode.sh](./encode.sh) and [decode.sh](./decode.sh)

### Encoding
For encoding, setting 

```
	--orientationSeparation
```

as an argument will enable the decomposition of the bitstreams according to their projection direction.


Encoding will result in N non-overlapping bitstreams, where the default is N=6. One may experiment with additional projection planes by changing

```
	--additionalProjectionPlaneMode=0
```

according to the mpeg-tmc2 documentation.

### Decoding
For decoding, one can list an arbitrary number of (sub-bitstreams).
Each partial bitstream can be decoded independently or combined with other streams, allowing combined geometry reconstruction and color reassignment during decoding instead of all point clouds after reconstruction.

This allows to combine sections of different quality (e.g. low quality for parts which are not faced by the user and high quality sub-streams for parts facing the user).
One may opt to not use all bitstreams for reconstruction, allowing to reconstruct only parts of the point cloud.

```
	--compressedStreamPath=stream_0.bin,stream_1.bin,stream_2.bin
```




