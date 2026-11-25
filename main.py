import random
#volledige random module geïmporteerd. mogelijk meer functies uit deze module nodig.

#Constanten

ENTRANCE_FEE = 15.0
CONSUMPTION_COST = 2.5
COST_PER_GAME = 5.0
MIN_AGE = 18
CURRENT_YEAR = 2026

# Testwaardes

# first_name ='John'
# last_name = 'Doe'
# date_of_birth = '10-10-2001'
# gender = 'M'

#Onafhankelijke Variabelen

first_name =input('voer hier uw voornaam in: ').strip().capitalize()
last_name = input('voer hier uw achternaam in: ').strip().capitalize()
date_of_birth = input('Voer hier uw geboortedatum in (dd-mm-yyyy): ').strip()
birth_day, birth_month, birth_year = date_of_birth.split("-")
birth_day = int(birth_day)
birth_month = int(birth_month)
birth_year = int(birth_year)
age = CURRENT_YEAR - birth_year
#TODO hoe kan ik hier de invoer valideren?
#TODO uitvinden hoe je een date.today() ophaald in python. voorlopig opgelost met een constante
gender = input('Voer hier uw geslacht in M/V/X: ').strip().upper()
starting_budget = float(input('Wat is uw startbudget: €').strip())
number_of_games = int(input('Hoe veel spellen gaat u spelen (€5,- per spel): ').strip())

#afhankelijke variabelen
buy_in_costs = COST_PER_GAME * number_of_games
total_fixed_costs = ENTRANCE_FEE + CONSUMPTION_COST + buy_in_costs
remaining_balance = starting_budget - total_fixed_costs

#TODO: Maximaal 5 spellen toestaan.

if remaining_balance > 0:
    greeting = "Welkom, "
    message = "Veel plezier!"
else:
    greeting = "Beste, "
    message = "Uw toegang is geweigerd"
if gender == 'M':
    salutation = 'meneer '
elif gender == 'V':
    salutation = 'mevrouw '
else:
    salutation = ''
#expres geen/lege aanhef bij elk andere invoer dan M of V.
if age < MIN_AGE:
    print(f'Toegang geweigerd. U bent onder de 18.')
    exit(1)

print(
    '\n'
    'Casino de Gouden Driehoek\n'
    '\n'
    '-------------------------\n'
)

print(

    f"{greeting}{salutation}"
    f'{first_name} {last_name}\n'
    '\n'
    f'Startbudget: €{starting_budget:.2f}\n'
    f'Vaste kosten: €{total_fixed_costs:.2f}\n'
    f'Saldo: €{remaining_balance:.2f}\n'
    '\n'
    f'{message}'
    '\n'
)

#Aparte overview voor alle gegevens. Vond ik zelf netter in een los overzicht.
overview_costs = input('Wilt u nog een apart kostenoverzicht (Y/N)?').strip().upper()
print(
    '\n'
    'Uw persoonlijk kostenoverzicht\n'
    '\n'
    '------------------------------\n'
    '\n'
    f'{first_name.upper()} {last_name.upper()}\n'
    f'{date_of_birth}\n'
    '\n'
    f'Entree: €{ENTRANCE_FEE:.2f}\n'
    f'Verplichte consumptie: €{CONSUMPTION_COST:.2f}\n'
    f'Buy-in kosten: €{buy_in_costs:.2f} - {number_of_games} spellen\n'
    if overview_costs == 'Y'
    else ''
)
#todo meerdere spellen toevoegen. Koppelen aan gekozen aantal spellen? Anders een nieuwe constante kiezen
if remaining_balance <= 0:
    exit(1)
print(
    'Welkom bij de Roulette tafel\n'
)
round_number = 1

while True:
    if remaining_balance <= 0:

        print("U heeft geen saldo meer. Het spel wordt beëindigd")
        break
    choice = int(input('Maak uw keuze: \n'
                '1 - rood\n'
                '2 - zwart\n'
                '3 - even\n'
                '4 - oneven\n'
                '0 - Stop met spelen\n'
    ).strip())

    match choice:
        case 0:
            print("Tot ziens!")
            break
        case 1:
            print("U kiest rood.")
        case 2:
            print("U kiest zwart.")
        case 3:
            print("U kiest even.")
        case 4:
            print("U Kiest oneven.")
        case _:
            print("ongeldige keuze")
            continue

    bet_amount = float(input("Hoe veel wilt u inzetten: €"))
    #TODO traceback error. lege waarde kan niet omgezet worden naar float

    if bet_amount > 0 and remaining_balance >= bet_amount:
        spin = random.randint(0, 36)

        odd_even = 'geen' if spin == 0 else ('even' if spin % 2 == 0 else 'oneven')

        if spin == 0:
            color = 'groen'
        elif 1 <= spin <= 18:
            color = 'zwart' if odd_even == 'even' else 'rood'
        else:
           color = 'rood' if odd_even == 'even' else 'zwart'

        won = False

        if choice == 1 and color == 'rood':
            won = True
        elif choice == 2 and color == 'zwart':
            won = True
        elif choice == 3 and odd_even == 'even':
            won = True
        elif choice == 4 and odd_even == 'oneven':
            won = True
        profit = bet_amount * 2 if won else 0
        remaining_balance = remaining_balance - bet_amount + profit
        print(f"De bal valt op {color} ({spin})")

        round_number += 1
        print('Gefeliciteerd, u heeft gewonnen!' if won else 'Helaas, u heeft verloren.')
        print(f"Uw nieuwe saldo is: €{remaining_balance:.2f}")

    else:
        print("Ongeldige invoer of onvoldoende saldo voor deze inzet")
        continue
print(f"Uw definitieve eindsaldo is: €{remaining_balance:.2f}")