gdb --args ./bin/PccAppDecoder \
	--compressedStreamPath=S26C03R03O_5.bin \
	--reconstructedDataPath=S26C03R03_dec_%04d_O5.ply \
	--videoDecoderOccupancyPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderGeometryPath=../external/HM/bin/TAppDecoderStatic \
	--videoDecoderAttributePath=../external/HM/bin/TAppDecoderStatic \
	--colorSpaceConversionPath=../external/HDRTools/bin/HDRConvert \
	--inverseColorSpaceConversionConfig=cfg/hdrconvert/yuv420torgb444.cfg \
	--uncompressedDataFolder=../../../mpeg_datasets/CfP/datasets/Dynamic_Objects/People/ \
	--numInStreams=1