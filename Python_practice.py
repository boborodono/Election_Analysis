counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#if "Arapahoe" in counties or "El Paso" in counties:
#        print("Arapahoe or El Paso are in the list of counties.")
#else:
#        print("Arapahoe or El Paso are not in the list of counties.")
#
#for county in counties:
 #       print(county)

#for county in counties_dict:  
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#        print(county_dict)

#for county_dict in voting_data:
#        for value in county_dict.values():
#                print(value)

#for county_dict in voting_data:
#        print(county_dict['county'])

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#        print(county + " county has " + str(voters) + " registered voters.")

# f Strings
for county, voters in counties_dict.items():
        print(f"{county} county has {voters} registered voters.")

#Will probably need this for assignment!!!
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)      

#Number format in f string
#f'{value:{width}.{precision}}'
# With thousand separator
#f'{value:{width},.{precision}}'
