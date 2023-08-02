from flask import Flask, request
import urllib.request


tursted_sources = {"book":"1","the address":"2"}
@app.route('/image', methods=['POST','GET'])
def image():
    try:
        images = request.get_json()
        source = request.headers['source']
        
        front_url = images["front_image"]
        back_url = images["back_image"]

        front_image = urllib.request.urlretrieve(front_url)
        back_image = urllib.request.urlretrieve(back_url)

        if  source in tursted_sources.keys():
            source_id =  tursted_sources["source"]
        else:
            return "not trusted source"
    return     
    except Exception as e:
        print(e)