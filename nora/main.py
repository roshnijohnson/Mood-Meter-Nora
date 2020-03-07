from flask import Flask, request, render_template
import pickle
# coding=utf8
m=[]
m=[["Depressed","Exhausted","Drained","Sleepy","Peaceful","Carefree"],
["Pessimistic","Sad","Bored","Relaxed","Satisfied","Balanced"],
["Disguisted","Disappointed","Apathetic","Easygoing","Content","Fulfilled"],
["Anxious","Worried","Annoyed","Happy","Focused","Thrilled"],
["Furious","Frustrated","Restless","Energized","Motivated","Excited"],
["Enraged","Stressed","Shocked","Surprised","Exhileratied","Ecstatic"]]


ldict={}
ldict["Depressed"]=["https://www.alwayswellwithin.com/blog/find-peace-of-mind","https://www.psychologytoday.com/intl/basics/optimism","https://www.helpguide.org/articles/depression/coping-with-depression.htm"]
ldict["Exhausted"]=["https://www.healthline.com/health/mental-exhaustion#overview","https://www.healthline.com/health/emotional-exhaustion","https://www.forbes.com/sites/nomanazish/2018/09/25/how-to-overcome-mental-fatigue-according-to-an-expert/#59c14c161644"]
ldict["Drained"]=["https://hackspirit.com/emotionally-drained-8-clear-signs-and-7-useful-remedies/","https://www.aconsciousrethink.com/5552/8-glaring-signs-mentally-emotionally-drained/"]       
ldict["Pessimistic"]=["https://www.forbes.com/sites/travisbradberry/2016/08/23/3-powerful-ways-to-stay-positive/#5f4aeeeb19c9","https://www.huffpost.com/entry/how-to-stay-optimistic-du_b_7655138","https://dariusforoux.com/stay-positive/"]
ldict["Sad"]=["https://www.lifehack.org/819337/how-to-not-be-sad","https://thiswayup.org.au/how-do-you-feel/sad/","https://au.reachout.com/articles/why-am-i-sad-all-the-time"]
ldict["Bored"]=["https://www.psychologytoday.com/us/blog/making-change/201507/how-beat-boredom","https://www.betterhelp.com/advice/depression/boredom-and-depression:-can-one-lead-to-the-other/"]
ldict["Annoyed"]=["https://www.lifehack.org/articles/communication/20-things-when-you-feel-extremely-angry.html","https://www.buzzfeed.com/stephhallett/how-to-calm-down-when-angry"]
ldict["Enraged"]=["https://www.lifehack.org/articles/communication/20-things-when-you-feel-extremely-angry.html","https://www.buzzfeed.com/stephhallett/how-to-calm-down-when-angry"]
ldict["Frustrated"]=["https://www.positivityblog.com/overcome-frustration/","https://blog.iqmatrix.com/overcome-frustration"]

app = Flask(__name__, template_folder='C://Users//JOEL//Desktop//apptest//final//templates')

@app.route("/")
def home():
    return render_template("page1.html")
@app.route("/name",methods=["POST"])
def name():
	if request.method=="POST":
	    text = request.form["nickname"]
	    return render_template("page2.html",text=text)
@app.route("/mood_meter",methods=["POST"])
def mood_meter():
    option=request.form["mood"]
    p=int(request.form["pleasant"])
    e=int(request.form["energy"])
    if option=="good":
	#p=int(input("On scale of 0 to 100 enter your pleasantness\n"))
	#e=int(input("On scale of 0 to 100 enter your energy\n"))
        a=15+((p*15)/100)
        b=(e*30)/100
    elif option=="bad":
		#p1=int(input("On scale of 0 to 100 enter your pleasantness\n"))
		#e1=int(input("On scale of 0 to 100 enter your energy\n"))
        a=15-((p*15)/100)
        b=(e*30)/100
    filename="finalized_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[b,a]])
    rslt=result[0]
    for i in range(6):
        for j in range(6):
            if m[i][j]==rslt:
                if i<1:
                    if j<1:
                        rslt1=m[i+1][j+1]
                        rslt2=m[i+1][j]
                        rslt3=m[i][j+1]
                    elif j>4:
                        rslt1=m[i+1][j-1]
                        rslt2=m[i+1][j]
                        rslt3=m[i][j-1]
                    else:
                        rslt1=m[i+1][j+1]
                        rslt2=m[i+1][j]
                        rslt3=m[i][j+1]
                elif i>4:
                    if j<1:
                        rslt1=m[i-1][j+1]
                        rslt2=m[i-1][j]
                        rslt3=m[i][j+1]
                    elif j>4:
                        rslt1=m[i-1][j-1]
                        rslt2=m[i-1][j]
                        rslt3=m[i][j-1]
                    else:
                        rslt1=m[i-1][j+1]
                        rslt2=m[i-1][j]
                        rslt3=m[i][j+1]
                else:
                    rslt1=m[i-1][j]
                    rslt2=m[i+1][j]
                    rslt3=m[i][j+1]
    return render_template("page3.html", rslt=rslt,rslt1=rslt1,rslt2=rslt2,rslt3=rslt3)
@app.route("/last/<rslt>",methods=["POST"])
def last(rslt):
    v=[]
    v=ldict.get(rslt)
    vlen=len(v)    
    return render_template("page4(1).html",v=v)
    #return mood    
if __name__ == "__main__":  
	app.run(debug=True)
