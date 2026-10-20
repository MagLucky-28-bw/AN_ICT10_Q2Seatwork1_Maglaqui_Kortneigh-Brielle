from pyscript import when, web

club_members = [
    "Khloe Pineda",
    "Joseph Reto",
    "Mandi Smith",
    "Mark Silverstone",
    "Diego Silang"
    ]


@when("submit", "#member-form")
def check_member(event):
    event.preventDefault()

    first_name = web.page["first-name"].value.strip().title()
    last_name = web.page["last-name"].value.strip().title()
    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    web.page["result"].innerText = messages[is_member]
