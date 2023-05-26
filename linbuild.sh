if [[ $USER == "root" ]] then

echo -e "\e[31mPlease execute as root (sudo)!\e[0m"
exit

fi


echo "Preparing ..."

mkdir "/usr/bin/.copra"

echo "Downloading ..."
curl https://raw.githubusercontent.com/BLUEAMETHYST-Studios/copra/main/linux/copra -s -L -o /usr/bin/copra