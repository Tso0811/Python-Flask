
from flask import Flask #載入 flask
app=Flask(
    __name__,
    static_folder="test",
    static_url_path="/abc"
    ) #建立 Application 物件

@app.route("/")
def index():
    return ("this is homepage")

@app.route("/data/<userName>")
def dataPage(userName):
    if userName == "Tso":
        return "Tso is a badass"
    else :
        return 'this is data page '+userName


 

app.run(port=8080)   #啟動網站伺服器預設為5000,可透過 port 參數指定埠號

