# dict1 ={"1":"hello", 2 :"world"}

# print(dict1["1"])

# student_scores = {
#    "harry" : 81,
#    "Ron":78,
#    "Hermione" : 99,
#    "Draco": 74,
#    "Neville" :62
# }

# student_grade = {}

# for i in student_scores :
#     score = student_scores[i]
#     if score < 70:
#         student_grade[i] = "Fail"
#     elif score< 80:
#         student_grade[i] = "Acceptable"
#     elif score < 90 :
#         student_grade[i] = "Exceed Expectation"
#     else:
#         student_grade[i] = "OUTSTANDING"
# print(student_grade)

# travel_log = [
#    {
#     "country" : "france",
#     "visits" : 5,
#     "cities" :["paris" , "america" ,"india"]
#    },
#    {
#     "country" : "India",
#     "visits" : 2,
#     "cities" :["africa" , "south" ,"pok"]
#    }
#  ] 

# def add_new_country(country_live,times,city_name):
#     new_dict = {}

#     new_dict["country"] = country_live
#     new_dict["visits"] = times
#     new_dict["cities"] = city_name
#     travel_log.append(new_dict)

# add_new_country("Russia" , 2 ,["Moscow" ,"Saint"])  
# print(travel_log)

should_Continue = True

while should_Continue == True :
   
   User = input("What Is Your Name? :")
   New_bid = int(input("What's Your Bid Amount? : $"))
   Anyother = input("Are THere Any Other Bidder ? Type 'Yes' or 'No' .")
   
   Max_Bid = 0
   bid_dict = {}

   bid_dict[User] = New_bid

   for i in bid_dict:
      if Max_Bid < bid_dict[i]:
          Max_Bid = bid_dict[i]


   if Anyother == "No":
     should_Continue = False
     print(f"WINNER OF BIDDING EVENT IS {User} and MAX BIDDING AMOUNT {Max_Bid}")



