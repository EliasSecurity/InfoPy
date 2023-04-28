from os import system
import platform
import builtwith as Bw
import pyfiglet
from colorama import init, Fore
import whois

init()


def Check_terminal():
    if platform.uname()[0] == 'Windows':
        system('cls')
    else:
        system('clear')


def HomeScaner():
    Check_terminal()
    print(pyfiglet.figlet_format(text='Info . Py', font='standard',))
    print(f'''{Fore.WHITE}Welcom in how to script version{Fore.RED} 1.0
{"-"*31}
    ''')
    print(f'{Fore.WHITE}Example ( {Fore.RED}google.com{Fore.WHITE} )')

    url = input(f'{Fore.MAGENTA}\nEneter url :{Fore.WHITE} ').split()
    for i in url:
        http = 'https://'+i

    # Exteracing info web

    bw = Bw.parse(http)

    list1 = []

    print(Fore.WHITE +
          f"\n\tinformations {Fore.RED}'host and server and languages and framework ' \n")
    for inn in bw:
        list1.append(inn)
        for i in list1:
            res = bw.get(i)
        for i in res:
            myres = i
            print(Fore.CYAN + 'info received + ' + Fore.RED + myres)

    try:
        inUrl = whois.whois(url[0])
    except TimeoutError:
        raise 'Time Ote Error check in internet'
    a = inUrl.get("domain_name")
    b = inUrl.get("registrar")
    c = inUrl.get("whois_server")
    d = inUrl.get("referral_url")
    e = inUrl.get("updated_date")
    f = inUrl.get("creation_date")
    g = inUrl.get("expiration_date")
    h = inUrl.get("name_servers")
    i = inUrl.get("status")
    q = inUrl.get("emails")
    l = inUrl.get("name")
    n = inUrl.get("org")
    y = inUrl.get("address")
    o = inUrl.get("city")
    u = inUrl.get("state")
    p = inUrl.get("registrant_postal_code")
    m = inUrl.get("country")

    print(Fore.WHITE +
          f"\n\tinformations {Fore.RED}'whois in web site' \n")

    print(f"""
{Fore.WHITE}Domain :  {Fore.GREEN}{a}
{Fore.WHITE}registrar : {Fore.GREEN}{b}
{Fore.WHITE}server : {Fore.GREEN}{c}
{Fore.WHITE}referral url : {Fore.GREEN}{d}
{Fore.WHITE}updated date : {Fore.GREEN}{e}
{Fore.WHITE}creation date : {Fore.GREEN}{f}
{Fore.WHITE}expiration date : {Fore.GREEN}{g}
{Fore.WHITE}name servers : {Fore.GREEN}{h}
{Fore.WHITE}status : {Fore.GREEN}{i}
{Fore.WHITE}emails : {Fore.GREEN}{q}
{Fore.WHITE}name : {Fore.GREEN}{l}
{Fore.WHITE}org : {Fore.GREEN}{n}
{Fore.WHITE}address : {Fore.GREEN}{y}
{Fore.WHITE}city : {Fore.GREEN}{o}
{Fore.WHITE}state : {Fore.GREEN}{u}
{Fore.WHITE}registrant postal code : {Fore.GREEN}{p}
{Fore.WHITE}country : {Fore.GREEN}{m}
    """)


def menu():
    Check_terminal()
    print(Fore.LIGHTMAGENTA_EX+'\nwel menu optinos Scrip <)')
    print(Fore.MAGENTA+'''
enter url for info website [ 1 ]
help [ 2 ]
exit [ 3 ]
    ''')
    user = int(input(Fore.WHITE+'Enter number : '+Fore.LIGHTWHITE_EX))

    if (user > 3):
        print('Number notTrue :(')
    elif (user < 1):
        print('Number notTrue :(')
    elif (user == 1):
        HomeScaner()
    elif (user == 2):
        Check_terminal()
        print('You can enter the data collection section by entering 1,\n and you can enter several sites in a row,\n the tool will start scanning.')
        input()
        menu()
    elif (user == 3):
        print('Godbay')
        quit()
    else:
        print(' [-] nottrue bro')


menu()
