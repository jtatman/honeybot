# -*- coding: utf-8 -*-
"""
[countries.py]
Country-Capital Plugin

[Author]
Phil Beld

[About]
Show the capital of a given country.

[Commands]
>>> .country <country>
returns the associated capital
"""


class Plugin:
    def __init__(self):
        pass

    def __country(input_country):

        data = [
            "Afghanistan",
            "Kabul",
            "Albania",
            "Tirana",
            "Algeria",
            "Algiers",
            "Andorra",
            "Andorra la Vella",
            "Angola",
            "Luanda",
            "Antigua and Barbuda",
            "Saint John’s",
            "Argentina",
            "Buenos Aires",
            "Armenia",
            "Yerevan",
            "Australia",
            "Canberra",
            "Austria",
            "Vienna",
            "Azerbaijan",
            "Baku",
            "The Bahamas",
            "Nassau",
            "Bahrain",
            "Manama",
            "Bangladesh",
            "Dhaka",
            "Barbados",
            "Bridgetown",
            "Belarus",
            "Minsk",
            "Belgium",
            "Brussels",
            "Belize",
            "Belmopan",
            "Benin",
            "Porto-Novo",
            "Bhutan",
            "Thimphu",
            "Bolivia",
            "La Paz, Sucre",
            "Bosnia and Herzegovina",
            "Sarajevo",
            "Botswana",
            "Gaborone",
            "Brazil",
            "Brasilia",
            "Brunei",
            "Bandar Seri Begawan",
            "Bulgaria",
            "Sofia",
            "Burkina Faso",
            "Ouagadougou",
            "Burundi",
            "Bujumbura",
            "Cambodia",
            "Phnom Penh",
            "Cameroon",
            "Yaounde",
            "Canada",
            "Ottawa",
            "Cape Verde",
            "Praia",
            "Central African Republic",
            "Bangui",
            "Chad",
            "N’Djamena",
            "Chile",
            "Santiago",
            "China",
            "Beijing",
            "Colombia",
            "Bogota",
            "Comoros",
            "Moroni",
            "Congo",
            "Republic of the, Brazzaville",
            "Congo",
            "Democratic Republic of the Kinshasa",
            "Costa Rica",
            "San Jose",
            "Cote d’Ivoire",
            "Yamoussoukro",
            "Croatia",
            "Zagreb",
            "Cuba",
            "Havana",
            "Cyprus",
            "Nicosia",
            "Czech Republic",
            "Prague",
            "Denmark",
            "Copenhagen",
            "Djibouti",
            "Djibouti",
            "Dominica",
            "Roseau",
            "Dominican Republic",
            "Santo Domingo",
            "East Timor",
            "Dili",
            "Ecuador",
            "Quito",
            "Egypt",
            "Cairo",
            "El Salvador",
            "San Salvador",
            "Equatorial Guinea",
            "Malabo",
            "Eritrea",
            "Asmara",
            "Estonia",
            "Tallinn",
            "Ethiopia",
            "Addis Ababa",
            "Fiji",
            "Suva",
            "Finland",
            "Helsinki",
            "France",
            "Paris",
            "Gabon",
            "Libreville",
            "The Gambia",
            "Banjul",
            "Georgia",
            "Tbilisi",
            "Germany",
            "Berlin",
            "Ghana",
            "Accra",
            "Greece",
            "Athens",
            "Grenada",
            "Saint George’s",
            "Guatemala",
            "Guatemala City",
            "Guinea",
            "Conakry",
            "Guinea-Bissau",
            "Bissau",
            "Guyana",
            "Georgetown",
            "Haiti",
            "Port-au-Prince",
            "Honduras",
            "Tegucigalpa",
            "Hungary",
            "Budapest",
            "Iceland",
            "Reykjavik",
            "India",
            "New Delhi",
            "Indonesia",
            "Jakarta",
            "Iran",
            "Tehran",
            "Iraq",
            "Baghdad",
            "Ireland",
            "Dublin",
            "Israel",
            "Telaviv",
            "Italy",
            "Rome",
            "Jamaica",
            "Kingston",
            "Japan",
            "Tokyo",
            "Jordan",
            "Amman",
            "Kazakhstan",
            "Astana",
            "Kenya",
            "Nairobi",
            "Kiribati",
            "Tarawa Atoll",
            "Korea",
            "North, Pyongyang",
            "Korea",
            "South, Seoul",
            "Kosovo",
            "Pristina",
            "Kuwait",
            "Kuwait City",
            "Kyrgyzstan",
            "Bishkek",
            "Laos",
            "Vientiane",
            "Latvia",
            "Riga",
            "Lebanon",
            "Beirut",
            "Lesotho",
            "Maseru",
            "Liberia",
            "Monrovia",
            "Libya",
            "Tripoli",
            "Liechtenstein",
            "Vaduz",
            "Lithuania",
            "Vilnius",
            "Luxembourg",
            "Luxembourg",
            "Macedonia",
            "Skopje",
            "Madagascar",
            "Antananarivo",
            "Malawi",
            "Lilongwe",
            "Malaysia",
            "Kuala Lumpur",
            "Maldives",
            "Male",
            "Mali",
            "Bamako",
            "Malta",
            "Valletta",
            "Marshall Islands",
            "Majuro",
            "Mauritania",
            "Nouakchott",
            "Mauritius",
            "Port Louis",
            "Mexico",
            "Mexico City",
            "Micronesia",
            "Federated States of, Palikir",
            "Moldova",
            "Chisinau",
            "Monaco",
            "Monaco",
            "Mongolia",
            "Ulaanbaatar",
            "Montenegro",
            "Podgorica",
            "Morocco",
            "Rabat",
            "Mozambique",
            "Maputo",
            "Myanmar",
            "Naypyidaw",
            "Namibia",
            "Windhoek",
            "Nauru",
            "Yaren District",
            "Nepal",
            "Kathmandu",
            "Netherlands",
            "Amsterdam",
            "New Zealand",
            "Wellington",
            "Nicaragua",
            "Managua",
            "Niger",
            "Niamey",
            "Nigeria",
            "Abuja",
            "Norway",
            "Oslo",
            "Oman",
            "Muscat",
            "Pakistan",
            "Islamabad",
            "Palau",
            "Melekeok",
            "Panama",
            "Panama City",
            "Papua New Guinea",
            "Port Moresby",
            "Paraguay",
            "Asuncion",
            "Peru",
            "Lima",
            "Philippines",
            "Manila",
            "Poland",
            "Warsaw",
            "Portugal",
            "Lisbon",
            "Qatar",
            "Doha",
            "Romania",
            "Bucharest",
            "Russia",
            "Moscow",
            "Rwanda",
            "Kigali",
            "Saint Kitts and Nevis",
            "Basseterre",
            "Saint Lucia",
            "Castries",
            "Saint Vincent and the Grenadines",
            "Kingstown",
            "Samoa",
            "Apia",
            "San Marino",
            "San Marino",
            "Sao Tome and Principe",
            "Sao Tome",
            "Saudi Arabia",
            "Riyadh",
            "Senegal",
            "Dakar",
            "Serbia",
            "Belgrade",
            "Seychelles",
            "Victoria",
            "Sierra Leone",
            "Freetown",
            "Singapore",
            "Singapore",
            "Slovakia",
            "Bratislava",
            "Slovenia",
            "Ljubljana",
            "Solomon Islands",
            "Honiara",
            "Somalia",
            "Mogadishu",
            "South Africa",
            "Pretoria",
            "South Sudan",
            "Juba",
            "Spain",
            "Madrid",
            "Sri Lanka, Colombo",
            "Sri Jayewardenepura Kotte",
            "Sudan",
            "Khartoum",
            "Suriname",
            "Paramaribo",
            "Swaziland",
            "Mbabane",
            "Sweden",
            "Stockholm",
            "Switzerland",
            "Bern",
            "Syria",
            "Damascus",
            "Taiwan",
            "Taipei",
            "Tajikistan",
            "Dushanbe",
            "Tanzania",
            "Dodoma",
            "Thailand",
            "Bangkok",
            "Togo",
            "Lome",
            "Tonga",
            "Nuku’alofa",
            "Trinidad and Tobago",
            "Port-of-Spain",
            "Tunisia",
            "Tunis",
            "Turkey",
            "Ankara",
            "Turkmenistan",
            "Ashgabat",
            "Tuvalu",
            "Funafuti",
            "Uganda",
            "Kampala",
            "Ukraine",
            "Kyiv",
            "United Arab Emirates",
            "Abu Dhabi",
            "United Kingdom",
            "London",
            "United States of America",
            "Washington D.C.",
            "Uruguay",
            "Montevideo",
            "Uzbekistan",
            "Tashkent",
            "Vanuatu",
            "Port-Vila",
            "Vatican City",
            "Vatican City",
            "Venezuela",
            "Caracas",
            "Vietnam",
            "Hanoi",
            "Yemen",
            "Sanaa",
            "Zambia",
            "Lusaka",
            "Zimbabwe",
            "Harare",
        ]

        city = None
        for ii in range(len(data)):
            if str(input_country) == data[ii]:
                city = data[ii + 1]
            else:
                pass
        return city

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"]
            input_country = str(msgs[1][9:])

            if info["command"] == "PRIVMSG" and info["args"][1][1:8] == "country":
                methods["send"](info["address"], Plugin.__country(input_country))
        except Exception as e:
            print("woops plugin error: ", e)
