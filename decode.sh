gdb --args ./bin/PccAppDecoder \
	--compressedStreamPath=results/Binaries/longdress_r5_1frame/S26C03R03O_0.bin,results/Binaries/longdress_r5_1frame/S26C03R03O_1.bin,results/Binaries/longdress_r5_1frame/S26C03R03O_2.bin \
	--reconstructedDataPath=S26C03R03_dec_%04d.ply \
	--videoDecoderOccupancyPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderGeometryPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderAttributePath=../external/HM/bin/TAppDecoderStatic \
	--colorSpaceConversionPath=../external/HDRTools/bin/HDRConvert \
	--inverseColorSpaceConversionConfig=cfg/hdrconvert/yuv420torgb444.cfg \
	--startFrameNumber=42 \
	--numInStreams=6
