[![Continous Integration](https://github.com/snapwiki/wiki-mirror/actions/workflows/lint.yml/badge.svg)](https://github.com/snapwiki/wiki-mirror/actions/workflows/lint.yml)
# Snap<i>!</i> Wiki Mirror
A read-only mirror of the Snap<i>!</i> Wiki

## Adapting for Your Own Use
This repository can be easily adapted following the steps below for any MediaWiki installation that has Parsoid configured.


If you haven't already, clone this repository using the following command-

```Bash
git clone https://github.com/snapwiki/wiki-mirror.git
```
. After that, enter the "wiki-mirror" directory (do not worry, you can rename it) using the following command:
```Bash
cd wiki-mirror
```
. Edit the ``configuration.py`` file inside your favourite editor. Install all the dependencies using PIP with the following command:

```Bash
pip3 install -r requirements.txt
```
. If you want to scrap all pages, run the following command:

```Bash
python3 massgethtml.py
```
. Otherwise, run the following command and respond to all the prompts:

```Bash
python3 gethtml.py
```
. If you want to minify the scraped pages, run the following commands-
```Bash
npm install
npm run minify
```
.

## Legal
Snap! Wiki Mirror - A read-only mirror of the Snap<i>!</i> Wiki

Copyright (C) 2021-2023 GrahamSH and R4356th

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
