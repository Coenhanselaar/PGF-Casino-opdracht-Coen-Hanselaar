#Constanten

ENTRANCE_FEE = 15.0
CONSUMPTION_COST = 2.5
COST_PER_GAME = 5.0

#Onafhankelijke Variabelen

first_name =input('voer hier uw voornaam in: ').strip().capitalize()
last_name = input('voer hier uw achternaam in: ').strip().capitalize()
date_of_birth = input('Voer hier uw geboortedatum in (dd-mm-yyyy): ')
gender = input('Voer hier uw geslacht in M/V/X: ').strip().upper()
starting_budget = float(input('Wat is uw startbudget: €').strip())
number_of_games = int(input('Hoe veel spellen gaat u spelen (€5,- per spel): ').strip())

# Testwaardes

# first_name ='John'
# last_name = 'Doe'
# date_of_birth = '10-10-2001'
# gender = 'M'

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
#TODO toegang nog uit te breiden met leeftijdscontrole

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