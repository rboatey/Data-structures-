#list of cars available and their prices
cars ={"Toyota Rav4":60000,"Bugatti":300000,"SUV":50000,"KIA Sorento":36000,\
"Honda civic":12000,"Honda Cr-v":56000,"Toyota camry":12000,"Hyundai accent":12000,\
"Hyundai elantra":650000,"Hyundai i10":18000,"Toyota land cruiser prado":650000,\
"Toyota V8":550000,"Toyota highlander":250000,"Toyota corolla":95000,"Nissan march":32000,\
"Toyota vitz":30000,"Kia morning":19000,"Suzuki swift":55000,"Mercedes-Benz C250":164000,\
"Nissan navara":220000,"Toyota fortuner":765000,"Toyota hilux":765250,"Nissan patrol LE":1399815,\
"Toyota coaster":846850,"Nissan pathfinder":95000,"Toyota avalon":250000,"Kia sportage":100000,\
"Hyundai tucson":120000,"Toyota yaris":95000,"Nissan micra":19500}
carName =input("Enter a car name")
#check if car name is in the list of cars available 
if carName in cars:
    print("Yes")
    #if car name is present, get its price
    car_price =cars[carName]
    print(f"The price of {carName} is GHc{car_price}.")
else:
    #if car name is not present,inform the user
    print(f"Sorry, {carName} is not available.")
    