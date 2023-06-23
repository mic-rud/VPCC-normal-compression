./bin/PccAppDecoder \
	--compressedStreamPath=S26C03R03O_0.bin,S26C03R03O_1.bin,S26C03R03O_2.bin,S26C03R03O_3.bin,S26C03R03O_4.bin,S26C03R03O_5.bin \
	--reconstructedDataPath=S26C03R03_dec_%04d.ply \
	--inverseColorSpaceConversionConfig=cfg/hdrconvert/yuv420torgb444.cfg \
	--startFrameNumber=1051 \
	--numInStreams=6
