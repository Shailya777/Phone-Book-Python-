import re, csv
from datetime import datetime

# Functions:
def load_data():
    """
    Loads contacts from a CSV file into a list of dictionaries.

    Parameters:
        filename (str): Path to the CSV file containing contacts data.

    :return:
        list of dict: List containing each contact as a dictionary with keys
                      like 'name', 'phone', and 'email'.
                      Returns an empty list if the file does not exist.

    """

    temp_list = []
    try:
        with open ('PhoneBook.csv', mode= 'r', newline= '') as file:
            reader = csv.DictReader(file)
            for row in reader:
                temp_list.append(row)

        return temp_list
    except FileNotFoundError:
        print('No PhoneBook Found! Starting Fresh.')
        return temp_list


def save_data(data):
    """
    Save the list of contacts into a CSV file.

    :param data: List of Dictionaries, Each Dictionary containing a Single Contact Info eg: {'Name': 'XYZ', 'Contact No': '1234'}

    :return: None
    """

    with open('PhoneBook.csv', mode='w', newline='') as file:
        column_names = ['First Name', 'Last Name', 'Phone Number', 'Email Address', 'Birth Date']
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()

        for dicts in data:
            writer.writerow(dicts)

def add_contact(f_name, l_name, ph_num, email_add, birth_date):
    """
    Takes Varified Contact Information entered by user and saves it to Main List of Dictionaries.

    :param f_name: First Name
    :param l_name: Last Name
    :param ph_num: Phone Number
    :param email_add: Email Address
    :param birth_date: Birth Date

    :return: Single Contact Info Saved in a Dictionary.
    """

    new_contact = dict()
    new_contact['First Name'] = f_name.capitalize()
    new_contact['Last Name'] = l_name.capitalize()
    new_contact['Phone Number'] = ph_num.strip()
    new_contact['Email Address'] = email_add.strip()
    new_contact['Birth Date'] = birth_date
    return new_contact

def display_contacts(contact_list):
    """
    Displays Contacts Currently in The PhoneBook (With changes made by user in current run).

    :param contact_list: List of Dictionary of all contacts.

    :return: None
    """

    if len(contact_list) == 0:
        print('No Contacts Found.')
    else:
        keys = list(contact_list[0].keys())

        print('=' * 125)
        print(f"{'No.':<4} {keys[0]:<20} {keys[1]:<20} {keys[2]:<15} {keys[3]:<40} {keys[4]}")
        print('=' * 125)

        for index, item in enumerate(contact_list, start= 1):
            print(f"{index:<4} {item[keys[0]]:<20} {item[keys[1]]:<20} {item[keys[2]]:<15} {item[keys[3]]:<40} {item[keys[4]]}")
            print('\n')

        print('=' * 125)

def search_contact(contact_list, by, search_chars):
    """
    Searches Contacts Based on Name (Either First or Last Name) / Phone Number / Email / Birth Date.

    :param contact_list: List of Dictionary of All Contacts.
    :param by: Key to Search chosen by User. eg: Name / Phone Number
    :param search_chars: Search String Entered by User.

    :return: List of Dictionary of Contacts Matching the Search.
    """
    temp_list = []

    if by == 'Name':
        key_name = ['First Name', 'Last Name']

        for record in contact_list:
            if search_chars.lower() in record[key_name[0]].lower() or search_chars in record[key_name[1]].lower():
                temp_list.append(record)

    else:
        for record in contact_list:
            if search_chars in record[by]:
                temp_list.append(record)

    return temp_list

def delete_contact(main_contact_list, contact_to_delete):
    """
    Deletes A Contact Chosen by the User (Works Directly on The Main Contact List of program).

    :param main_contact_list: List of Dictionary of All Contacts.
    :param contact_to_delete: Contact to be deleted from Main List chosen by User.

    :return: None
    """

    for index, item in enumerate(main_contact_list):
        if item == contact_to_delete:
            main_contact_list.pop(index)

def check_for_duplicates(contact_list, phone_number, email):
    """
    Checks if Contact already exists in The Main Contact List by Phone Number and Email.
    Either of Phone Number or Email has to be Different from Existing Contacts.

    :param contact_list: List of Dictionaries of All Contacts.
    :param phone_number: Phone Number Entered by The User for Contact.
    :param email: Email Entered by The User for Contact.

    :return: Boolean if the contact already exists or not.
    """

    for item in contact_list:
        if item['Phone Number'] == phone_number and item['Email Address'] == email:
            return False
    return True

def validate_email(email):
    """
    Validates Email Entered by User by Using Regular Expression.

    :param email: Email Entered by The User.

    :return: Boolean if The Email Matches The Allowed Pattern or Not.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_b_day(b_day):
    """
    Validates Birth Date Entered by User to Make Sure The Birth Date Follows mm/dd/yyyy format precisely.

    :param b_day:  Birth Date entered by The User.

    :return: Boolean if The Birth Date Matches The Allowed Format or Not.
    """
    for item in b_day.split('/'):
        if len(item) < 2:
            return False
    else:
        try:
            datetime.strptime(b_day, '%d/%m/%Y')
            return True
        except ValueError:
            return False
#-----------------------------------------------------------------------------------------------------------------------

def main():
    # Load Data from CSV to List of Dictionaries:
    main_contact_list = load_data()

    print('=======================================================')
    print('Welcome yo Your Phone Book!')

    while True:
        print('Press A: Add Contact | V: View all Contacts | S: Search Contacts | D: Delete A Contact| Q: Quit')
        option = input('How do you want to proceed?: ')
        if option.upper() == 'Q':
            save_data(main_contact_list)
            break

        # Code Block To Add Contact:
        elif option.upper() == "A":
            # Ask for First name, last name, phone number, email and b-date.
            # Asking For First Name and Data Check:
            while True:
                first_name = input('Enter First Name: ')
                if not first_name.isalpha():
                    print('Please Enter Valid First Name.')
                else:
                    break

            # Asking For First Name and Data Check:
            while True:
                last_name = input('Enter Last Name: ')
                if not last_name.isalpha():
                    print('Please Enter Valid Last Name.')
                else:
                    break

            # Asking for Phone Number and Data Check:
            while True:
                phone_number = input('Enter Contact Number(in 10 digit format): ')
                if not phone_number.isnumeric() or len(phone_number) != 10:
                    print('Please Enter Valid Phone Number.')
                else:
                    break

            # Asking for Email and Data Check:
            while True:
                email = input('Enter Email Address: ')
                if not validate_email(email):
                    print('Please Enter Valid Email.')
                else:
                    break

            # Asking for BirthDate and Data Check:
            while True:
                b_day = input('Enter Birth Date (dd/mm/yyyy): ')
                if not validate_b_day(b_day):
                    print('Please Enter Birth Date in Proper Format.')
                else:
                    break

            # Checking if the contact already exists.
            if not check_for_duplicates(main_contact_list, phone_number, email):
                print('Contact Already Exists.')
            else:
                # adding Contact to the Amin List.
                main_contact_list.append(add_contact(first_name, last_name, phone_number, email, b_day))
                print('Contact Added Successfully!')
                print('')

        # Code Block To Display All Contacts:
        elif option.upper() == 'V':
            display_contacts(main_contact_list)

        # Code Block For Contact Search:
        elif option.upper() == 'S':
            search_results = []
            print('Press N: Search by Name | C: Search by Phone Number | E: Search by Email | B: Search by Birth Date/Month/Year | Q: Quit')

            while True:
                choice = input('Option: ')

                if choice.upper() == 'Q':
                    break

                # Search By Name (First Name / Last Name)(Full or partial):
                if choice.upper() == 'N':
                    while True:
                        search_string = input('Enter Name or Character(s): ')

                        if not search_string.isalpha(): # Validating The Input.
                            print('Please Chose Valid Name or Character.')
                        else:
                            search_results.extend(search_contact(main_contact_list, 'Name', search_string))
                            if len(search_results) == 0:
                                print('No Results Found.')
                                break
                            else:
                                display_contacts(search_results)
                                break

                    break

                # Search By Phone Number (Full or Partial):
                elif choice.upper() == 'C':
                    while True:
                        search_string = input('Enter Phone Number (Full / Partial): ')

                        if not search_string.isnumeric(): # Validating The Input.
                            print('Please Enter Valid Phone Number.')
                        else:
                            search_results.extend(search_contact(main_contact_list, 'Phone Number', search_string))
                            if len(search_results) == 0:
                                print('No Results Found.')
                                break
                            else:
                                display_contacts(search_results)
                                break
                    break

                # Search By Email (Full or Partial):
                elif choice.upper() == 'E':
                    search_string = input('Enter Email (Full or Partial): ')
                    search_results.extend(search_contact(main_contact_list, 'Email Address', search_string))
                    if len(search_results) == 0:
                        print('No Results Found.')
                        break
                    else:
                        display_contacts(search_results)
                        break

                # Search By Birth Date (Full or Day / Month / Year):
                elif choice.upper() == 'B':
                    while True:
                        search_string = input('Enter Full Birth Date(dd/mm/yyyy) or Day/Month/Year: ')
                        parts = search_string.split('/') # Checking if the entered Date by user has no Characters.
                        if all(item.isnumeric() for item in parts):
                            search_results.extend(search_contact(main_contact_list, 'Birth Date', search_string))
                            if len(search_results) == 0:
                                print('No Results Found.')
                                break
                            else:
                                display_contacts(search_results)
                                break
                        else:
                            print('Please Enter Valid Date.')

                    break
                else:
                    print('Please Chose Valid Option for Search.')

        # Code Block To Delete a Contact:
        elif option.upper() == 'D':
            search_results = []
            while True:
                search_string = input('Enter Contact Name or Phone Number: ')
                if not search_string.isalpha() and not search_string.isnumeric(): # Checking if Entered String has all characters or all numbers.
                    print('Please Enter valid Name or Phone Number')

                else:
                    # Deciding whether to search by Name or by Phone Number by what User has Entered in Input.
                    search_key = (lambda search_string: 'Name' if search_string.isalpha() else 'Phone Number')(search_string)
                    search_results.extend(search_contact(main_contact_list, search_key, search_string))
                    if len(search_results) == 0:
                        print('No Such Contact(s) Found.')
                        break
                    elif len(search_results) == 1:
                        # If Only one contact found in search, delete it immediately.
                        delete_contact(main_contact_list, search_results[0])
                        print('Contact Successfully Deleted.')
                        break
                    else:
                        display_contacts(search_results)
                        while True:
                            del_choice = input('Enter number of the Contact you want to Delete: ')
                            # Checking Whether user has Entered Proper Number and Not Number Out of Bound or Characters.
                            if not del_choice.isnumeric() or int(del_choice) < 1 or int(del_choice) > len(search_results):
                                print('Please Chose a Valid Number.')
                            else:
                                contact_to_delete = search_results[int(del_choice) - 1] # As Display Number Starts from 1, subtract 1 from User's Choice to get Index of Chosen Contact.
                                delete_contact(main_contact_list, contact_to_delete)
                                print('Contact Successfully Deleted.')
                                break
                break

        else:
            print('Please Chose Valid Option.')

if __name__ == "__main__":
    main()