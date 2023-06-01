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

echo "Deleting Copra folder and its contents ..."
rm -rf /usr/bin/.copra

echo "Deleting Copra Starting script ..."
rm /usr/bin/copra

echo -e "\e[32mUninstall completed!\e[0m"