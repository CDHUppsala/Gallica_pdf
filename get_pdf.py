#Author: Marie Dubremetz @ Center for Digital Humanities Uppsala
#Program to download the PDF of the medical journals 
#from 1890 to 1892 (or whaterver start end date you decide)

#0. Adapt the following variables to your specific case:
startDate = 1959
endDate = 1990
baseUrl = "https://gallica.bnf.fr/services/Issues?ark=ark:/12148/cb34348109k/date&date="#Example for medical journal. adapt the baseURL accordingly
baseName = "BulletinANM_"#whaterver name for your output files
#I. Get the Ark code
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import time
import requests

# For each year between 1890 and 1892 get the list of issues in the form of a list of "ark code"
# store the link to the ark codes in "link"

baseUrl_meta = "https://gallica.bnf.fr/services/OAIRecord?ark="
opener = urllib.request.build_opener()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
for year in range(startDate,endDate):
    arks=[]
    link=baseUrl+str(year)
    #get the document from the link
    document = urllib.request.urlopen(link)
    soup = BeautifulSoup(document, "lxml") 
    tags = soup.find_all("issue")
    #get all the ark codes of the year into a list
    arks= [ark['ark'] for ark in tags]
    days_of_year= [ark['dayofyear'] for ark in tags]
    #get attribute "ark" from the issue in bs
    print("***"+str(year)+"***")
    print("***"+str("number of docs to download:"+str(len(arks)))+"***")
    i=0
    for ark in arks:
        time.sleep(30)
        print("Extracting doc ark no: ",ark)
#II. Get the PDF and its metadata
        #get dc:date and dc:identifier
        url_meta="https://gallica.bnf.fr/services/OAIRecord?ark="+ark
        document_meta = urllib.request.urlopen(url_meta)
        soup_meta = BeautifulSoup(document_meta, "lxml")
        date = soup_meta.find("dc:date").text
        pdf_link=soup_meta.find("dc:identifier").text+".pdf"
        if len(days_of_year) != len(set(days_of_year)):#check if there has not been issues the same day if yes add a number
            i+=1
            file_name=baseName+date+"_"+str(i)
        else:
            file_name=baseName+date
        #save the pdf in a file
        pdf_name=file_name+".pdf"
        print(pdf_name)
        print(pdf_link)
        foldername="PDF"
        #try downloading the pdf and if error 503 wait 10 seconds and try again twice
        try:
            #open the pdf with the opener and save it in a file
            r = requests.get(pdf_link, headers=headers)
            with open(foldername+"/"+pdf_name, 'wb') as f:
                f.write(r.content)
        except urllib.error.HTTPError as e:
            if e.code == 503:
                print("Error 503: Service Unavailable")
                print("Waiting 1000 seconds...")
                time.sleep(1000)
                try:
                    urllib.request.urlretrieve(pdf_link, foldername+"/"+pdf_name,headers=headers)
                except urllib.error.HTTPError as e:
                    if e.code == 503:
                        print("Error 503: Service Unavailable")
                        print("Waiting 3600 seconds...")
                        time.sleep(3600)
                        urllib.request.urlretrieve(pdf_link, foldername+"/"+pdf_name,headers=headers)
                    else:
                        raise



        #save the metadata in a file
        meta_name=file_name+".xml"
        urllib.request.urlretrieve(url_meta, foldername+"/"+meta_name)