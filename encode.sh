gdb --args ./bin/PccAppEncoder \
	--configurationFolder=cfg/ \
	--config=cfg/common/ctc-common.cfg \
	--config=cfg/condition/ctc-all-intra.cfg \
	--config=cfg/sequence/longdress_vox10.cfg \
	--config=cfg/rate/ctc-r5.cfg \
	--uncompressedDataFolder=../../../mpeg_datasets/CfP/datasets/Dynamic_Objects/People/ \
	--frameCount=2 \
	--videoEncoderOccupancyPath=../external/HM/bin/TAppEncoderStatic \
	--videoEncoderGeometryPath=../external/HM/bin/TAppEncoderStatic \
	--videoEncoderAttributePath=../external/HM/bin/TAppEncoderStatic \
	--colorSpaceConversionPath=../external/HDRTools/bin/HDRConvert \
	--reconstructedDataPath=S26C03R03_rec_%04d.ply \
	--compressedStreamPath=S26C03R03.bin \
	--keepIntermediateFiles \
	--additionalProjectionPlaneMode=0 \
	--constrainedPack \
	--orientationSeparation \
	--packingStrategy=2 \
