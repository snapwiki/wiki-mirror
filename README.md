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
.
