""" Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

  """

def bmi(weight, height):
    calc = weight / (height * height) #this can be written height **2 i suppose this means squared

    bmi_dictionary = {
        18.5 : "Underweight",
        25 : "Normal",
        30 : "Overweight"
    }

    for weight in bmi_dictionary:
        if calc <= weight:
            return bmi_dictionary[weight]
        
    return "Obese"