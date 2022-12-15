"""Search for an email address given a fragment of a job description."""

from typing import List
import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # TODO: create an empty list of the contacts
    contact_list = []
    # TODO: iterate through the file, parsing it line by line
    for line in csv.reader(
        contacts.splitlines(),
        delimiter = ",",
        quoting = csv.QUOTE_ALL,
        skipinitialspace = True,
    ):
        job = line[1]
        if job_description in job:
            contact_list.append(line)

    return contact_list
    # TODO: refer to the file called input/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    # TODO: iterate through each line of the file and extract the current job
    # ---> TODO: extract the current job for the contact on this line of the CSV
    # ---> TODO: the job description matches and thus we should save it in the list
    # TODO: return the list of the contacts who have a job description that matches
