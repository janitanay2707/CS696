
import os
import urllib.request as ur

class Scrape_Saver:

    def _init_(self, base_url, save_location):
        self.base_url = base_url
        self.save_location = save_location
        return

    def retrieve(self, item):
        if item in os.listdir(self.save_location):
            with open(self.save_location + item,"r") as infile:
                return infile.read()
        else:
            string = ur.urlopen(self.base_url.format(item)).read().decode()
            with open(self.save_location + item, 'w') as outfile:
                outfile.write(string)
        return string

    def _str_(self):  
        return str(os.listdir(self.save_location))


if __name__ == '_main_':
    url = "http://www.uniprot.org/uniprot/{}.fasta"
    item = 'P69892'
    x = Scrape_Saver(url, 'saves/')
    print(x.retrieve(item))
    print (x)