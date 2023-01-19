### HDMI failing on newer RPI OS

sudo apt full-upgrade

sudo nano /boot/config.txt

hdmi_safe=1

or

hdmi_force_hotplug=1 
config_hdmi_boost=4