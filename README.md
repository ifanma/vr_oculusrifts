# vr_oculusrifts

先安装依赖项
sudo apt-get install python-dev cython cython3
pip install Cython
sudo apt install libhidapi-dev libhidapi-libusb0
sudo apt install glew-utils libglew-dev

写配置文件
sudo gedit /etc/udev/rules/83-hmd.rules
写入
SUBSYSTEM=="usb", ATTR{idVendor}=="2833", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="0bb4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="28de", MODE="0666", GROUP="plugdev"
sudo udevadm control --reload-rules

安装OpenHMD
git clone https://github.com/OpenHMD/OpenHMD.git
cd OpenHMD
mkdir build
cd build
cmake ..
make
sudo make install 
sudo ldconfig

然后安装openhmd-ros
sudo python setup.py install
测试：
from rift import PyRift

然后设置a.conf
安装nv驱动后就有nvidia-setting
sudo cp a.conf /usr/share/X11/xorg.conf.d/99-hmd.conf
