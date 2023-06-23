# View-Adaptive Streaming of Point Cloud Scenes through combined Decomposition and Video-based Coding

Accompaning repository to the [paper](https://dl.acm.org/doi/abs/10.1145/3552457.3555732).

This repository is based on [mpeg-tmc2](https://github.com/MPEGGroup/mpeg-pcc-tmc2).
Configurations are designed for the [8i VFB v2](http://plenodb.jpeg.org/pc/8ilabs/) dataset.

## Building
The repository was built and tested on Ubuntu 22.04 using gcc/g++-9.

You can run the installation script directly using
```
    ./build.sh
```


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




