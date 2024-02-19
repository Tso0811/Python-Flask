
from flask import Flask #載入 flask
from flask import request  
from flask import redirect
import json
app=Flask(
    __name__,
    static_folder="test",
    static_url_path="/abc"
    ) #建立 Application 物件

@app.route("/zh/")
def zh():
    return json.dumps({
    "status":"ok",
    "text"  :"你好"
},ensure_ascii=False)  #不要用 ascii 編碼處理中文
 

@app.route("/en/")
def en():
    return json.dumps({
    "status":"ok",
    "text":"hello"
}) 

@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("zh"):
        return redirect("/zh/")
    else:
        return redirect("/en/")
       
app.run(port=8080)   #啟動網站伺服器預設為5000,可透過 port 參數指定埠號

