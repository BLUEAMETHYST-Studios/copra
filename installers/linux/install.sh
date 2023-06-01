#!/bin/bash

if [ "$(id -u)" != "0" ]
then

echo -e "\e[31mPlease execute as root (sudo)!\e[0m"
exit

fi

read -p "Are you sure? (N/y): " confirm

if [[ ${confirm} != "y" && ${confirm} != "Y" ]]; then
    echo -e "\e[31mInstallation cancelled.\e[0m"
    exit 1
fi

echo "STARTING"

echo "Making project's directory ..."
mkdir /usr/bin/.copra

echo "Copying files ..."
cp -a application/main/copra.py /usr/bin/.copra/copra.py
cp application/start/copra /usr/bin

echo "Making Copra executable ..."
chmod +x /usr/bin/copra

echo -e "\e[32mInstallation completed!\e[0m"

