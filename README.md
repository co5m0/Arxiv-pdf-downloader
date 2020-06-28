This is a simple Python script to obtain direct links for download pdf from Arxiv archive.

# How it works

The script will generate:

1.  `index.txt` ( file contains a list of links )
2.  `subjects.csv` ( file contains a list of subjects with their occurency )
3.  `INPUT` (folder in wich download the files)

# How to run

## Obtain links

`pyhton3 app.py number_of_links_you_want_to_donwload`

Es. `python3 app.py 1000`
It will download 1000 pdf links

> The script downs't require external libs

## Download files into INPUT folder

`wget -i index.txt -P ./INPUT`

> INPUT folder is created by the script
