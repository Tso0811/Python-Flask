
from flask import Flask #載入 flask
from flask import request  
import json
app=Flask(
    __name__,
    static_folder="test",
    static_url_path="/abc"
    ) #建立 Application 物件

@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("zh"):
      return json.dumps({
        "status":"ok",
        "text"  :"你好"
      })
    else:
       return json.dumps({
          "status":"ok",
          "text":"hello"
       },ensure_ascii=False) #不要用ascii 編碼處理中文
app.run(port=8080)   #啟動網站伺服器預設為5000,可透過 port 參數指定埠號

