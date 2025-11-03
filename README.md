# Web Crawler
[![](https://mermaid.ink/img/pako:eNp1j8EOgjAMhl-F9ASJHvBIjCffQE8yY8pWHHFsZGwaQnx3BzhNTNxp39-__dsRuBEEBdTKPLhE65LjnukkPJ5v1-sdbspUK3dLRJWdlwLOhWoTbRPkC_S-ulrsZMItPhTZRa3y9M3Z3FhGvHyHkhY_I6bUGLis0JO9N5yyea1_bb6Je6Xd4KTRQcl-zLCClmyLjQiXj5PGwElqiUERvoJq9MoxYPoZrOidOQyaQ-GspxVY468SihpVH8h3Ah3tGwzx7UftUJ-Mifx8AfEXcRQ?type=png)](https://mermaid.live/edit#pako:eNp1j8EOgjAMhl-F9ASJHvBIjCffQE8yY8pWHHFsZGwaQnx3BzhNTNxp39-__dsRuBEEBdTKPLhE65LjnukkPJ5v1-sdbspUK3dLRJWdlwLOhWoTbRPkC_S-ulrsZMItPhTZRa3y9M3Z3FhGvHyHkhY_I6bUGLis0JO9N5yyea1_bb6Je6Xd4KTRQcl-zLCClmyLjQiXj5PGwElqiUERvoJq9MoxYPoZrOidOQyaQ-GspxVY468SihpVH8h3Ah3tGwzx7UftUJ-Mifx8AfEXcRQ)

# Prerequisites for installation
- Have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- Optional: Have [Git](https://git-scm.com/downloads) installed

# Install and Run
- Install X Server - [VcXsrv](https://vcxsrv.com/) for Windows, [XQuartz](https://www.xquartz.org/) for MacOS, [X11 Server](https://help.ubuntu.com/community/ServerGUI#X11_Server_Installation) for Linux. Since I use Windows, the following instructions are tailored for Windows

- Search xlaunch in start menu, launch it, don't change any of the options except disable access control - make sure that is checked. You can save the configuration for later use. Additionally, you can download the config from this repo (config.xlaunch) and run that file instead. You'll see the icon in your tray:
![](/assets/x-server-icon.png)

- Clone the repo using `git clone https://github.com/Denkata-Iliev/WebCrawlerCoursework.git`

- Go in the folder through the terminal using `cd WebCrawlerCoursework`

- Run `ipconfig`, and check your IPv4 - ex: 192.168.1.100

- Use [this tutorial](https://www.youtube.com/watch?v=Z2k7ZBMZT3Y) to set an environment variable called DISPLAY (needed for the app to be able to display the UI) - `DISPLAY=192.168.1.100:0`. **Note the `:0` after your IPv4!**

- Launch Docker Desktop

- Then you can run `docker-compose up -d --build` which should start the app and you'll see the UI after it's done
    - **Note: it may take a little while, depending on your internet connection**
