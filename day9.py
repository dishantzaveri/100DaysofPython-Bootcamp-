dict={
    "a":"1",
    "b":"2",
    "c":"3",
    "d":"4",
}

print(dict["a"])

dict["e"]="5"

print(dict)

dict={}


print(dict)

dict["a"]="5"

print(dict)

for key in dict:
    print(key)
    print(dict[key])

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for student in student_scores:
    score=student_scores[student]
    if score > 90:
        student_grades[student]="A"
    elif score > 80:
        student_grades[student]="B" 
    elif score > 70:
        student_grades[student]="C"
    else :
        student_grades[student]="D"

print(student_grades)

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])


programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}


programming_dictionary = {}
print(programming_dictionary)
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])


capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(capitals)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited , times_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["country"]=times_visited
    new_country["country"]=cities_visited
    travel_log.append(new_country)

add_new_country("Russia",5,["Moscow","Kazan","Novosibirsk"])

print(travel_log)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)

 

