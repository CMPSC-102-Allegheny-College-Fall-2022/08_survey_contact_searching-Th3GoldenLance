# Contact Searching

## Nahayan Hussain Minhas

## Program Output

### What is the output from running the following commands?


- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```


- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```
from contactsearcher import search
```
This statement is used to import the `search.py` module from the `contactsearcher` directory to be made available for use
in `main.py`. 

#### The source code statement that extracts the current job description for a contact

`current_contact_job = line[1].replace('"',"")`

The variable `current_contact_job` stores the current job description for a contact, by taking the list holding contact at index 0
and job desc. at index 1, for a line and equating the value at index 1 to `current_contact_job`. The `replace()` function is also used
to basically remove the double quotes in the txt file.

#### Invocation of the function called `search_for_email_given_job`

```
search_for_email = search.search_for_email_given_job(job_description, contacts_text)
```
This source code sets the variable `search_for_email` equal to result returned by the `search_for_email_given_job` function inside the imported
`search` module. The function takes a job description keyword, and the text of the file holding all the data to be evaluated, as inputs
and outputs a list where each element is a list.

#### Test case for the function called `search_for_email_given_job`



#### Execute trace of the `contactsearcher` program

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

The program sets up the `contactsearcher` function with the string input `job_description` and path input `contacts_file`.
Then, with `typer.Abort()`, it ends the typer interface that's running if the file was not specified. Then, it uses the
`is_file()` and `exists()` function to check whether the specified file is valid or not. If so, `contacts_text` is set equal to the string
obtained from reading the file using `read_text()`. Then, the file's line count is checked using the `splitlines()` function to
split `contacts_text` into lines so the count of lines can be displayed. Then, the `search_for_email_given_job` function is called from the
imported `search` module using the inputs `job_description` and `contacts_text`. Inside the said function, a list is made from each line in `contacts_text`
using the `splitlines()` and `csv.reader()` functions. Then, for each of these lines' list, the element at index 1 is stored in `current_contact_job` with 
the double quotes removed, when occurring, using the `replace()` function. Then, if the entered `job_description` is found as a part of `current_contact_job`
for that specific line, that line/list is added to `contact_list` with the `append()` function for lists. Finally, the function returns `contact_list`, a list of lists,
which is stored inside the `search_for_email` variable in `main.py`. Finally, the relevant results are displayed.

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

I have really struggled in focusing on my assignments and turning them in on time. Unfortunately, due to circumstances out of my control, personal problems
arose and I fell behind and I could not overcome my lack of focus until now, a very late point in the semester. However, I hope that with my code, I've shown that I do have the potential to be
an academically good and responsible student.

### Based on your experiences with this project, what is one way in which you want to improve?

I want to improve my understanding of Poetry and the use of toml,lock files etc.
