
from flask import Flask #載入 flask
from flask import request  
from flask import redirect
from flask import render_template
import json
app=Flask(
    __name__,
    static_folder="test",
    static_url_path="/abc"
    ) #建立 Application 物件

@app.route("/")
def index():
    return render_template("templates",name="小明")
       
app.run(port=8080)   #啟動網站伺服器預設為5000,可透過 port 參數指定埠號

