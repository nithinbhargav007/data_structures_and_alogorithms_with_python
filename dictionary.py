d = {"Name": "Nithin" , "Age":27, "Location":"Bangalore"}
print(d.items())
def print_dict():
    for key,value in d.items():
        print(f" key and value is {key} and {value}") 

d["pin code"] = 562163
print_dict()