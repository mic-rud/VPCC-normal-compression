gdb --args ./bin/PccAppEncoder \
	--configurationFolder=cfg/ \
	--config=cfg/common/ctc-common.cfg \
	--config=cfg/condition/ctc-all-intra.cfg \
	--config=cfg/sequence/longdress_vox10.cfg \
	--config=cfg/rate/ctc-r3.cfg \
	--uncompressedDataFolder=../../../mpeg_datasets/CfP/datasets/Dynamic_Objects/People/ \
	--frameCount=1 \
	--videoencoderoccupancypath=../external/hm/bin/tappencoderstatic \
	--videoencodergeometrypath=../external/hm/bin/tappencoderstatic \
	--videoencoderattributepath=../external/hm/bin/tappencoderstatic \
	--colorspaceconversionpath=../external/hdrtools/bin/hdrconvert \
	--reconstructedDataPath=S26C03R03_rec_%04d.ply \
	--compressedStreamPath=S26C03R03.bin
	--keepIntermediateFiles \
	--additionalProjectionPlaneMode=0 \
	--constrainedPack \
	--packingStrategy=2 \
