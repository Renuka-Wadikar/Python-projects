from flask import Flask, render_template
import pandas as pd 

app = Flask(__name__)

stations = pd.read_csv('Web Api\data_small\stations.txt', skiprows= 17)
stations = stations[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html/", data = stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = 'Web Api\data_small\TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, 
                     skiprows = 20,
                     parse_dates=["    DATE"] )
    temprature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10
    return {
        'date': date,
        'station': station,
        'temprature': temprature
    }

@app.route("/api/v1/<station>")
def stationData(station):
    filename = 'Web Api\data_small\TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, 
                     skiprows = 20,
                     parse_dates=["    DATE"] )
    result = df.to_dict(orient='records')
    return result

@app.route("/api/v1/year/<station>/<year>")
def oneYear(station, year):
    filename = 'Web Api\data_small\TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, 
                     skiprows = 20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))]
    return result.to_dict(orient= 'records')

if __name__ == "__main__":
    app.run(debug =True)