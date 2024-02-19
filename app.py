
from flask import Flask #載入 flask
from flask import request  
app=Flask(
    __name__,
    static_folder="test",
    static_url_path="/abc"
    ) #建立 Application 物件

@app.route("/")   
def index():
    print("請求的方法",request.method)
    print("通訊協定",request.scheme)
    print("主機名稱",request.host)
    print("路徑",request.path)
    print("完整網址",request.url)
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))
    lang=request.headers.get("accept-language")
    if lang.startswith("zh"):
        return("你好")
    else:
        return("Hello")
#建立路徑/getsum的處理函式
#利用要求字串 (Query String) 提供彈性:/getsum?min=最小數&max=最大數
    
@app.route("/getsum")
def getSum():
    minNumber=request.args.get("min",0)
    maxNumber=request.args.get("max",100)
    minNumber=int(minNumber)
    maxNumber=int(maxNumber)
    sum=0
    for i in range(minNumber,maxNumber+1):
        sum+=i
    return("總合為:"+str(sum))

app.run(port=8080)   #啟動網站伺服器預設為5000,可透過 port 參數指定埠號

