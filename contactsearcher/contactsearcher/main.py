"""Define the command-line interface for the contact searching program."""

#Import the necessary modules
from contactsearcher import search
from rich.console import Console
from pathlib import Path
import typer


#Set up CLI
console = Console()
cli = typer.Typer()


@cli.command()
def contactsearcher (
    job_description: str = typer.Option(..., prompt=True),
    contacts_file: [Path] = typer.Option(None),
) -> None:
    """Search for either an email address of a contact who has a job in the file."""
    # declare an empty contacts_text
    contacts_text = ""
    # display details about the file provided on the command line
    # --> the file was not specified so we cannot continue using program
    if contacts_file is None:
        typer.echo("No contacts file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if contacts_file.is_file():
        contacts_text = contacts_file.read_text()
        contacts_line_count = len(contacts_text.splitlines())
        typer.echo(
            f"The contacts file contains {contacts_line_count} people in it! Let's get searching!"
        )
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not contacts_file.exists():
        typer.echo("The contacts file does not exist!")
    # display details about the search key for the job provided on the command line
    typer.echo("")
    typer.echo(
        f'  We are looking for contacts who have a job related to "{job_description}":'
    )

    #set a variable equal to the list returned by the search_for_email_given_job function in search.py, when called with the inputs of the job descriptions and the text from the file to be searched
    search_for_email = search.search_for_email_given_job(job_description, contacts_text)
    #for every line/list in search_for_email, output the email (stored at index 0) and the job description (stored at index 1)
    for email in search_for_email:
        typer.echo(f"{email[0]} is {email[1]}")

    typer.echo("")
    typer.echo("Wow, we found some contacts! Email them to learn more about your job!")
