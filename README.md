# Web Crawler
[![](https://mermaid.ink/img/pako:eNp1j8EOgjAMhl-F9ASJHvBIjCffQE8yY8pWHHFsZGwaQnx3BzhNTNxp39-__dsRuBEEBdTKPLhE65LjnukkPJ5v1-sdbspUK3dLRJWdlwLOhWoTbRPkC_S-ulrsZMItPhTZRa3y9M3Z3FhGvHyHkhY_I6bUGLis0JO9N5yyea1_bb6Je6Xd4KTRQcl-zLCClmyLjQiXj5PGwElqiUERvoJq9MoxYPoZrOidOQyaQ-GspxVY468SihpVH8h3Ah3tGwzx7UftUJ-Mifx8AfEXcRQ?type=png)](https://mermaid.live/edit#pako:eNp1j8EOgjAMhl-F9ASJHvBIjCffQE8yY8pWHHFsZGwaQnx3BzhNTNxp39-__dsRuBEEBdTKPLhE65LjnukkPJ5v1-sdbspUK3dLRJWdlwLOhWoTbRPkC_S-ulrsZMItPhTZRa3y9M3Z3FhGvHyHkhY_I6bUGLis0JO9N5yyea1_bb6Je6Xd4KTRQcl-zLCClmyLjQiXj5PGwElqiUERvoJq9MoxYPoZrOidOQyaQ-GspxVY468SihpVH8h3Ah3tGwzx7UftUJ-Mifx8AfEXcRQ)

# to work
- install VcXsrv server, search xlaunch in start menu, launch it, next, next, check disable access control, next, done
- clone using `git clone <url>`
- cd in dir `cd <dir>`
- `ipconfig`, check IPv4 - ex: 192.168.1.100
- set env var DISPLAY=192.168.1.100:0 through windows ui to make it permanent
- `docker-compose up -d --build`, wait for it to be done
- `docker compose exec -it gui-app bash`, then `pipenv run python main.py` 