from flask import Flask
import http.client

app=Flask(__name__)
@app.route('/getKota',methods=['GET','POST'])
def getKota():
  

    conn = http.client.HTTPSConnection("api.rajaongkir.com")

    headers = { 'key': "b5ba3fdc4c012551d4cfac501ba0ca37" }

    conn.request("GET", "/starter/city?id=39&province=5", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return(data.decode("utf-8")) 

if __name__ == '__main__':
    app.run(debug=True,port=5010,host='0.0.0.0')