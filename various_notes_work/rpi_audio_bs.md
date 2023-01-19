### list devices
aplay -l 
cat /proc/asound/modules


### test given devices channel 
speaker-test -t wav -c 2





### guide that sadly aint the full story or just sometimes doesnt work?

https://nerdiy.de/en/howto-raspberrypi-standardlautsprecher-konfigurieren/
then use alsamixer to set the card?
set on the taskbar audio setting with rightclick?


### HDMI fails to output sound

sudo nano /boot/config.txt
<code>
hdmi_force_hotplug=1
hdmi_drive=2
</code>