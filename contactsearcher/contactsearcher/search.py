"""Search for an email address given a fragment of a job description."""

#Import the necessary modules
from typing import List
import csv

# note: see https://docs.python.org/3/library/csv.html 


#define a function which searched the contacts file for an email given a job descriptions
def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""

    #Create empty list to store contacts
    contact_list = []

    #For each line in the text gathered from the input file, split into two at the comma, when faced with a comma
    for line in csv.reader(
        contacts.splitlines(),
        delimiter = ",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        current_contact_job = line[1].replace('"',"") #set the variable job equal to the contents at the index 1 of line
        #if the job to be searched for is in the job variable above, append the contacts list with the line containing the emails and job descriptions
        #also, remove the inverted commas using the replace() function
        if job_description in current_contact_job:
            contact_list.append(line)

    #the function returns the list
    return contact_list

