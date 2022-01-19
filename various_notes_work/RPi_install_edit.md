====== RPi Interface setup ======

Setup a RPi to autostart the interface and run with a static IP
This project is build and tested for RPis on Python 3.7.x
versions earlier than 3.6 are not supported.

===== Enabling I2C =====

Raspi-config
- enable I2C
- enable Serial Port (serial GPIO)

open ''sudo nano /etc/modules'' and append
>i2c-bcm2708
>i2c-dev

to verify the I2C functioning correctly install
>sudo apt-get install i2c-tools

and verify connection with the PCF8574 by checking addresses with.
This may be done by connecting the RPi GPIOs directly to PCFs if troubleshooting requires it
>i2cdetect -y 1


==== RPI setup from scratch ====

1. Download and install [Image](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip) to Micro-SD card

2. Place empty file with filename `ssh` on **boot** partition

3. edit ''config.txt'' on **boot** partition:

   1. add

      ```yaml
      # Disable Bluetooth
      dtoverlay=disable-bt
      ```

4. Set fixed IP address by editing the `/etc/dhcpcd.conf` on the **rootfs** partition as `sudo`:

   ```bash
   interface eth0
   static ip_address=192.168.xxx.yyy/24
   static routers=192.168.xxx.zzz
   static domain_name_servers=192.168.xxx.zzz 8.8.8.8 fd51:42f8:caae:d92e::1
   ```

5. Card in Pi -> boot -> login via ssh

6. ''passwd'' -> set new password

7. ''sudo raspi-config''

   1. Interface Options -> I2C -> enable

   2. Interface Options -> Serial -> disable login shell, enable serial port hardware

   3. Interface Options -> Remote GPIO -> enable

8. reboot

9. ''sudo nano /etc/modules''

10. add (if not existing)

    ```bash
    i2c-bcm2708
    i2c-dev
    ```

10. ''sudo apt update -y && sudo apt upgrade -y''

11. ''sudo apt install i2c-tools git python-pip python3-pip python3-venv python3-dev python3-rpi.gpio -y''

12. ''i2cdetect -y 1'' check if addresses 38 and 3f are available

13. ''wget https://raw.githubusercontent.com/Electroscape/Tools/master/setup_repo.sh''

14. ''sudo chmod +x setup_repo.sh''

15. ''./setup_repo.sh <your_username>Â  <username@email.com>''

16. ''cd /home/pi/TE/Electroscape-Interface''

17. ''rm -rf env''

18. ''python3 -m venv /home/pi/TE/Electroscape-Interface/env''

19. ''source env/bin/activate''

20. ''pip3 install -r requirements_updated.txt''

21. ''deactivate''

22. ''./init-server.sh''