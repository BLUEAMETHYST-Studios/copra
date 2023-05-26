:: Indev

curl https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/538/downloads/paper-1.19.4-538.jar -s -L -o server.jar && echo eula=true > eula.txt && echo java server.jar -jar -Xmx2G nogui > start.bat && mkdir plugins && cd plugins && curl https://cdn.discordapp.com/attachments/1079840119680413707/1111734688617353247/manhunt-0.4.jar -s -L -o manhunt.jar