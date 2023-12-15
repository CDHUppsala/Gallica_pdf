Gallica_pdf
=======
# Presentation (FR/EN)
Gallica_pdf est un outil écrit en Python permettant de récupérer des documents hébergés sur la bibliothèque numérique 
<a href="http://gallica.bnf.fr/">Gallica</a>. Il permet notamment de constituer rapidement de grands corpus afin d'effectuer des analyses assistées par ordinateur (statistique textuelles, text mining, reconnaissance d'image).

A partir d'ici les instructions seront en anglais.

Gallica_pdf is a tool written in Python made to download documents hosted on the national French library <a href="http://gallica.bnf.fr/">Gallica</a>. That allows for the quick constitution of corpora in order to analyse data with computers.

## Prerequisites with Virtual env
If you use virtual env you can directly run these commands:
```bash
cd path/to/gallica_pdf
#Initiate your environment 
python3 -m venv .env #(only run this command the first time)
source .env/bin/activate  
pip install -r requirements.txt #(only run this command the first time)
#activate your environment
source .env/bin/activate 

```

## Usage 
```bash
python get_pdf.py

```
The output will be stored in the folder "PDF"

## Adapt code to your case
Open "get_pdf.py" with a text editor.
The most important is to change and adapt the baseURL. You can find this variable in the part 0 of the code at the begining.
The most important is to find your baseURL, to do so you need to find the ARKCODE of the periodic you are interested in
 and insert it in this template URL:


https://gallica.bnf.fr/services/Issues?ark=ark:/12148/ARKCODE/date&date=



## Author
* Marie Dubremetz (Engineer at CDHU Uppsala University) github: @mardub1635 gitlab: @mardub For technical questions: marie.dubremetz@abm.uu.se
 or mardubr-github@yahoo.fr . www.mariedubremetz.com
