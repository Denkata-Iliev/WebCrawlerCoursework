# Web Crawler
[![](https://mermaid.ink/img/pako:eNp1j8EOgjAMhl-F9ASJHvBIjCffQE8yY8pWHHFsZGwaQnx3BzhNTNxp39-__dsRuBEEBdTKPLhE65LjnukkPJ5v1-sdbspUK3dLRJWdlwLOhWoTbRPkC_S-ulrsZMItPhTZRa3y9M3Z3FhGvHyHkhY_I6bUGLis0JO9N5yyea1_bb6Je6Xd4KTRQcl-zLCClmyLjQiXj5PGwElqiUERvoJq9MoxYPoZrOidOQyaQ-GspxVY468SihpVH8h3Ah3tGwzx7UftUJ-Mifx8AfEXcRQ?type=png)](https://mermaid.live/edit#pako:eNp1j8EOgjAMhl-F9ASJHvBIjCffQE8yY8pWHHFsZGwaQnx3BzhNTNxp39-__dsRuBEEBdTKPLhE65LjnukkPJ5v1-sdbspUK3dLRJWdlwLOhWoTbRPkC_S-ulrsZMItPhTZRa3y9M3Z3FhGvHyHkhY_I6bUGLis0JO9N5yyea1_bb6Je6Xd4KTRQcl-zLCClmyLjQiXj5PGwElqiUERvoJq9MoxYPoZrOidOQyaQ-GspxVY468SihpVH8h3Ah3tGwzx7UftUJ-Mifx8AfEXcRQ)

# to work
0. install VcXsrv server, search xlaunch in start menu, launch it, next, next, check disable access control, next, done
1. `ipconfig`, check IPv4 - ex: 192.168.1.100
2. set env var DISPLAY=192.168.1.100:0 through windows ui to make it permanent
3. `docker-compose up -d`, then after done, `docker exec -it coursework-python_app-1 bash`, then `pipenv run python main.py`