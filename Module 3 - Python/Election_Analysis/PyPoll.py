#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 

import csv
filename =  "Resources/election_results.csv" 

#import the datetime class form the datetime module
import datetime as dt

#use the now() attribute on the datetime class to get the present time.
now=dt.datetime.now()

#print the present time.
print("the time right now is ",now)

#add our dependencies
import csv
import os

#Assign a variable for the file load and the path
file_to_load=os.path.join("Resources","election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

#1. Initialize a total vote counter.
total_votes=0

#candidate options and candidate votes
candidate_options= []

#1.Declare the empty dictionary.
candidate_votes={}

# 1. county list and dictionary with county votes
county_list = []
county_votes={}

#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#2. Initialize empty string, county name wuth largest turnout
county_largest_turnout=""
county_largest_turnout_votes=0


#Open the election results and read the file
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
        
    #Read the header row
    headers = next(file_reader)
       
   #Print each row in the CSV file
    for row in file_reader:
       #2. Add the total vote count
        total_votes += 1
       
#Print the candidate name from each row.
        candidate_name=row[2]
        
#3. Loop with county name from each row
         county_name=row[1]
    

#if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options: 
    #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
    
    #4A. write a decision statement with a logical operator to check if the county name acquired in Step 3 is in the county list (step1)
        if county_name not in county_list
    #4B. 
    
#2. Begin tracking that candidate??s vote count
            candidate_votes[candidate_name] = 0

#add a vote to that candidate??s count
        candidate_votes[candidate_name] += 1
       
        # Save the results to our text file.
   
with open(file_to_save, "w") as txt_file:
        
        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
        
        #Determine the percentage of votes for each candidate by looping through the counts.
        #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
            #3. Calculate the percentage of votes.
        vote_percentage=float(votes)/ float(total_votes)*100
            
            #To do: Print out each candidate??s name, vote count, and percentage of
            #Votes to the terminal
            
            #4. Print the candidate name and percentage of votes
        candidate_results= (
             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
            #Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
            #Determine winning vote count and candidate
            #Determine if the votes is greater than the winning count
            
        if (votes>winning_count) and (vote_percentage>winning_percentage):
                #If true then set winning_count= votes and winning_percentage=
                #vote_percentage.
            winning_count=votes
            winning_percentage=vote_percentage
                #And, set the winning_candidate equal to the candidate??s name.
            winning_candidate=candidate_name
                
                #to do: print out the winning candidate, vote count and percentage to
                #terminal
             
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
    
    
    
#using the () open function with the "w" mode we will write data to the file.
open(file_to_save,"w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file
    txt_file.write("Counties in the Election")
    txt_file.write("\n-----------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
   


            