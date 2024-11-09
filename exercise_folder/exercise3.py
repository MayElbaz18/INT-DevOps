# 1. Error handling basics

def my_function (number1, number2, operation):

    allowed_operations = ['add', 'subtract', 'multiply']
    if operation not in allowed_operations:
        return 'Invalid Operation!'
    
    if operation == 'add':
        return number1 + number2
    
    elif operation == 'subtract':
        return number1 - number2
    
    elif operation == 'multiply':
        return number1 * number2
    

result = my_function(2, 2 , 'multiply')
print(result)


# 2. Dictionary

my_dict = { 
    "Toyota" : { "Camry" : {
                           "introduced" : 1983,
                           "seats" : 5,
                           "msrp" : 24925,
                           "category" : "midsize"
                       },
                "Corolla" : {
                          "introduced" : 1966,
                          "seats" : 5,
                          "msrp" : 19325,
                          "category" : "compact"
                       },
                "Tacoma" : {    
                          "introduced" : 1995,
                          "seats" : 5,
                          "msrp" : 31500,
                          "category" : "compact"
                       }
    },
    "Volvo" : { "Xc90" : {
                          "introduced" : 2002,
                          "seats" : 7,
                          "msrp" : 58695,
                          "category" : "midsize"
                       },
                "S80" : {
                          "introduced" : 1998,
                          "seats" : 5,
                          "msrp" : 38705,
                          "category" : "midsize"
                       }
    },
    "Mercedes" : { "Gle" : {
                          "introduced" : 1997,
                          "seats" : 5,
                          "msrp" : 62650,
                          "category" : "midsize"
                       },
                    "Eqe" :{
                          "introduced" : 2022,
                          "seats" : 5,
                          "msrp" : 77900,
                          "category" : "executive"
                       }   

    }
           }

for company in my_dict:
    for model in my_dict[company]:

        if my_dict[company][model]["introduced"] > 1980:
            print(f"{model} was introduced after 1980!")

        if my_dict[company][model]["seats"] >= 7:
            print(f"{model} have 7 seats or more!")

        if my_dict[company][model]["msrp"] < 40000:
            print(f"{model} price is below $40000!")

        if my_dict[company][model]["category"] == "midsize":
            print(f"{company}-{model} is midsize category car!")        
    
       