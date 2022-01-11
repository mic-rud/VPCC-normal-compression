gdb --args ./bin/PccAppDecoder \
	--compressedStreamPath=S26C03R03.bin \
	--videoDecoderOccupancyPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderGeometryPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderAttributePath=../external/HM/bin/TAppDecoderStatic \
	--colorSpaceConversionPath=../external/HDRTools/bin/HDRConvert \
	--inverseColorSpaceConversionConfig=cfg/hdrconvert/yuv420torgb444.cfg \
	--reconstructedDataPath=S26C03R03_dec_%04d.ply \
	--uncompressedDataFolder=../../../mpeg_datasets/CfP/datasets/Dynamic_Objects/People/