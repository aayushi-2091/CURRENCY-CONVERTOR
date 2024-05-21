#original code
with open('data.txt') as f:
    lines=f.readlines()
dict={}
for line in lines:
    parsed=line.split("\t")
    dict[parsed[0]]=parsed[1]
amount=int(input("Enter amount in INR: "))
print("Enter the name of the currency you want to convert this amount to? Available options are: \n")
[print (item) for item in dict.keys()]
curr=input("Please enter one of these currency: ")
print(f"{amount} INR = {amount*(float(dict[curr]))} {curr}")




#another elaborate way

# Read currency data from file and populate the dictionary
#currency_dict = {}
#with open('data.txt') as f:
 #   lines = f.readlines()

#for line in lines:
 #   parsed = line.strip().split("\t")
  #  currency_dict[parsed[0].upper()] = float(parsed[1])

# Get user input
#amount = float(input("Enter amount in INR: "))
#print("Enter the name of the currency you want to convert this amount to. Available options are:")
#for currency in currency_dict.keys():
 #   print(currency)

#to_currency = input("Please enter one of these currencies: ").upper()

# Check if the currency code is valid and perform conversion
#if to_currency in currency_dict:
 #   converted_amount = amount * currency_dict[to_currency]
  #  print(f"{amount} INR = {converted_amount:.2f} {to_currency}")
#else:
 #   print(f"Error: Currency code {to_currency} not found.")
