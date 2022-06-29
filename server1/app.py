from flask import Flask
app = Flask(__name__)
import http.client
@app.route('/getOngkir', methods=['GET','POST'])
def getOngkir():
    #conn = http.client.HTTPSConnection("api.rajaongkir.com")

   # headers = { 'key': "b5ba3fdc4c012551d4cfac501ba0ca37" }

  #  conn.request("GET", "/starter/city?id=39&province=5", headers=headers)

    conn = http.client.HTTPSConnection("api.rajaongkir.com")

    payload = "origin=501&destination=114&weight=1700&courier=jne"

    headers = {
        'key': "cb38fec811a21fd0d7be524e7586f37f",
        'content-type': "application/x-www-form-urlencoded"
        }

    conn.request("POST", "/starter/cost", payload, headers)
    
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))

if __name__ == '__main__':
    app.run(debug=True,port=5010,host='0.0.0.0')