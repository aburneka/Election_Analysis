counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties: 
 #   print("El Paso is in the list of counties.")
#else:
 #   print("El Paso is not in the list of counties.")
#if "Arapahoe" in counties and "El Paso" not in counties: 
 #   print("Only Arapahoe is in the list of counties.")
#else: 
 #   print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
#for county in counties: 
 #   print(county)

#for i in range(len(counties)):
 #   print(counties[i])

#counties_tuples = ("Arapahoe","Denver","Jefferson")
#for i in range(len(counties_tuples)):
 #   print(counties_tuples[i])
#    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
 #   for county in counties_dict:
  #      print(county)

#for county in counties_dict.keys():
 #   print(county)

#for voters in counties_dict.values():
 #   print(voters)

#for county in counties_dict:
 #   print(counties_dict[county])

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
 #   print(county, voters)

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
 #               {"county":"Denver", "registered_voters": 463353},
  #              {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
 #   print(county_dict)

#for i in range(len(voting_data)):
 #   print(voting_data[i])

#for county_dict in voting_data:
 #   for value in county_dict.values():
  #      print(value)

#counties dictionary using concatenation
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters} registered voters.")

#multiline f strings to tell candidate how many votes they received
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
 #   f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#skill drill
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#skill drill for voting data 

voting_data = [{'county':'Arapahoe", 'registered_voters': 422829},
               {'county':'Denver', 'registered_voters': 463353},
                {'county':'Jefferson', 'registered_voters': 432438}]
for county, voters in voting_data.items():
    print(f"{county}) county has {voters:,} registered voters.")