import requests

myrequest = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?i=beef")
datajson = myrequest.json()

str.replace("\\", "", "")

outfile = open("food.html", "w")
outfile.write("<body style='margin:0;opacity:1.5;'> <img src='food.png' width=100%></body>")
outfile.write("<h1>""There are " + str(len(datajson['meals'])) + " " + "foods available to make:""</h1>")
outfile.write("<br>")
for i in range(len(datajson['meals'])):
	outfile.write(datajson["meals"][i]["strMeal"] + "<img src=" + datajson['meals'][i]['strMealThumb'] + " height=50%>")
outfile.write("<br>")

#outfile.write("<img src=" + datajson['meals'][0]["strMealThumb"] + " height=50%>")
#for x in range(len(datajson['meals'])):
	#outfile.write("<img src=" + datajson['meals'][x]['strMealThumb'] + " height=50%>")
outfile.close()
