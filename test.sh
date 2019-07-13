#!/data/data/com.termux/files/usr/bin/bash
folder=ubuntu-fs

if [ -d "$folder" ]; then
	first=1
	echo "Skipping downloading.... Please remove older Ubuntu version"
fi
if [ "$first" != 1 ];then
	echo "Download Rootfs, this may take a while base on your internet speed."

	curl "https://github.com/ultrahacx/OpenCV/raw/master/test.tar.gz" -o nul
	
	
	echo "  "
	echo "Decompressing Rootfs, please be patient.."
	echo "  "
	echo "It might take a little longer than expected due to large file size"
	proot --link2symlink tar -xf test.tar.gz||:
	
echo "  "
echo "  "
echo "Removing image for some space"
rm ubunMODV3.tar.gz
echo "You can now launch Ubuntu with the ./start-ubuntu.sh command"

fi


