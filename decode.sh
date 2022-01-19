gdb --args ./bin/PccAppDecoder \
	--compressedStreamPath=S26C03R03.bin \
	--reconstructedDataPath=S26C03R03_dec_%04d.ply \
	--videoDecoderOccupancyPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderGeometryPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderAttributePath=../external/HM/bin/TAppDecoderStatic \
	--colorSpaceConversionPath=../external/HDRTools/bin/HDRConvert \
	--inverseColorSpaceConversionConfig=cfg/hdrconvert/yuv420torgb444.cfg \
	--numInStreams=1