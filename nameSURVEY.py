import webbrowser as wb

food = input ("whats your faavirote food")

if food == "chicken":
    print("hmm , like that too.")
    wb.open("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-190808-baked-drumsticks-0217-landscape-pf-1567089281.jpg?crop=1.00xw:0.752xh;0,0.171xh&resize=")
elif food == "fish":
    print("not my choice!")
    wb.open("https://www.peta.org/wp-content/uploads/2014/01/goldfish-sxc.hu_.jpg")

elif food == "fruits":
    print ("Healthy choice")
    wb.open("https://upload.wikimedia.org/wikipedia/commons/2/2f/Culinary_fruits_front_view.jpg")
else:
    print("your favirote food is " + food)

country = input ("whats your faavirote country ? ")

if country == "singapore":
    print("a buetiful country am i right ?")
    wb.open("https://scandasia.com/wp-content/uploads/2020/01/image001.jpg")
elif country == "russia":
    print("what a BIG choice")
    wb.open("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpQPgRc2W45Edn-_NxQEYwNz1-Ml4Ej1JaUA&usqp=CAU")
elif country == "india":
    print ("Awesome choice !")
    wb.open("https://www.costacruises.eu/content/dam/costa/inventory-assets/countries/RUS/RUS.jpg.image.750.563.low.jpg")
else:
    print("your favirote cointry is  " + country)




    
