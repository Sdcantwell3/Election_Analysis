# How many votes did you get"
#my_votes=int(input("How many votes did you get in the election?"))
# Total votes in the election
#total_votes=int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you recieved.
#percentage_votes=(my_votes/total_votes)*100
#print("I received "+str(percentage_votes)+"% of the total votes.")

counties=["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe":369237,"Denver":413229,"Jefferson":390222}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    







