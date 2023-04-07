from flask import Flask, render_template,request
from scrape import hent_aksje_info
import json


app = Flask(__name__)


fil = open("s&p.json", encoding="utf-8")
stock_lst = json.load(fil)
fil.close()

min_ordbok = {}
@app.route("/",methods=["GET","POST"])
def index():
    
    if request.method == "POST":
        id = request.form["id"]
        
        if id in min_ordbok:
            min_ordbok.pop(id)
        else:
           min_ordbok[id] = hent_aksje_info(id) 
    tech = [hent_aksje_info("AAPL"),hent_aksje_info("META"),hent_aksje_info("MSFT"),hent_aksje_info("AMZN")]
    fs = [hent_aksje_info("JPM"), hent_aksje_info("GS"),hent_aksje_info("BAC"), hent_aksje_info("WFC")]
    rs = [hent_aksje_info("PLD"),hent_aksje_info("AMT"),hent_aksje_info("EQIX"),hent_aksje_info("CCI")]
    hc = [hent_aksje_info("JNJ"), hent_aksje_info("PFE"),hent_aksje_info("UNH"),hent_aksje_info("LLY")]
    energy = {}
    energy["SHEL"] = hent_aksje_info("SHEL")
    energy["EQNR"] = hent_aksje_info("EQNR")
    energy["CVX"] = hent_aksje_info("CVX")
    

      
    return render_template("index.html", min_ordbok = min_ordbok, stock_lst = stock_lst, tech = tech,fs = fs, rs =rs, hc = hc, energy = energy)


