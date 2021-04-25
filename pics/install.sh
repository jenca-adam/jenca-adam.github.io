#!/usr/bin/bash
APPSRC="https://raw.githubusercontent.com/jenca-adam/microbit/master/recaptcha"
DSKSRC="https://raw.githubusercontent.com/jenca-adam/microbit/master/rec.desktop"
IMGSRC="https://pbs.twimg.com/profile_images/566388455265931264/dVHQiE0t.png"
cd ~
echo "Downloading sources"
curl $APPSRC>recaptcha
chmod a+x recaptcha
echo "installing python"
yay -S python
echo "Installing Python libraries"
pip install whitenoise_player
pip install art
echo "syncing db"
sleep 1
echo "Creating desktop file"
curl $DSKSRC >Desktop/rc.desktop
cd ~
echo "Downloading icon"
curl $IMGSRC >rc.png
clear;
konsole -e ./recaptcha &
