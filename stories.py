"""Every story on the Tuesday 24 November 2026 page.

Rule for getting in: the event happened, or was first reported, on 24 November 2026
in some time zone. Anything older goes to DATE_CHECK instead.

Fields: n (pin number), region, head (bold headline), detail (one line of facts),
label (CONFIRMED / OFFICIAL / REPORTED / SCHEDULED), src (short source credit),
lon/lat (map pin).
"""

LABELS = {
    "CONFIRMED": "several outlets or official data agree",
    "OFFICIAL": "government, agency or company statement",
    "REPORTED": "one wire or outlet so far",
    "SCHEDULED": "set for 24 Nov; result came after this page",
}

# Four lead stories across the top
LEADS = [
    dict(n=1, region="ASIA", big="+9%", unit="TAIEX",
         head="Asia surges as Huang returns to Nvidia",
         detail="Kospi +6.5% to 5,014.41 (sidecar triggered), Nikkei +3.9% to 58,654.40; TSMC, MediaTek near +10%. Intraday.",
         label="CONFIRMED", src="AP, Longbridge", lon=121.5, lat=25.0),
    dict(n=2, region="EUROPE", big="2", unit="KILLED",
         head="Russian strike on Zaporizhzhia",
         detail="22 wounded, two of them children, local officials say.",
         label="CONFIRMED", src="Reuters", lon=35.1, lat=47.8),
    dict(n=3, region="ASIA", big="1st", unit="FOREIGNER",
         head="Shenzhou-24 cleared to fly with a Pakistani",
         detail="CMSA: crew Tang Hongbo, Wu Yi, Zeeshan Ali; launch from Jiuquan set for 00:18 UTC 25 Nov.",
         label="OFFICIAL", src="CMSA", lon=98.5, lat=39.7),
    dict(n=4, region="ASIA", big="16 Dec", unit="RETURN DATE",
         head="Sheikh Hasina says she will fly home",
         detail="Spokesman tells Reuters she wants a Biman flight back to Bangladesh on Victory Day; she faces a death sentence.",
         label="CONFIRMED", src="Reuters, TBS", lon=90.4, lat=23.8),
]

# Region blocks, in the order they are drawn
REGIONS = [
    ("ASIA", [
        dict(n=5, head="S. Korea: 3-minute evacuation alert on Ulleung",
             detail="07:52 local, after a Russian aircraft entered its airspace",
             label="CONFIRMED", src="Safety ministry", lon=130.9, lat=37.5),
        dict(n=6, head="M5.3 quake in eastern Nepal, felt in India",
             detail="Koshi province, 10 km deep, near Sikkim; no casualties reported",
             label="CONFIRMED", src="EMSC, USGS", lon=87.3, lat=26.7),
        dict(n=7, head="Indonesia: ex-police chief charged with treason",
             detail="Listyo Sigit Prabowo among 6 suspects in wiretap case",
             label="REPORTED", src="Reuters", lon=106.8, lat=-6.2),
        dict(n=8, head="Indonesia: MPR to verify VP candidates' diplomas",
             detail="Field checks in Makassar and Magelang from 25 Nov",
             label="REPORTED", src="Harianesia", lon=119.4, lat=-5.1),
        dict(n=9, head="Rupiah slips to 18,215 per dollar",
             detail="Turns weaker by midday on hawkish Fed signals",
             label="REPORTED", src="Validnews", lon=110.4, lat=-7.5),
        dict(n=10, head="Japan pulls car suppliers into arms build-up",
             detail="Biggest since WWII; Aster makes drone motors for Anduril",
             label="REPORTED", src="Reuters exclusive", lon=140.6, lat=39.3),
        dict(n=11, head="Japan's 2nd consular visit to reporter held in Russia",
             detail="Tokyo meets detained Japanese journalist again",
             label="REPORTED", src="Wire report", lon=139.7, lat=35.7),
    ]),
    ("EUROPE", [
        dict(n=12, head="Russian drone briefly breaches Polish airspace",
             detail="During overnight strikes on western Ukraine",
             label="REPORTED", src="Polish armed forces", lon=19.0, lat=52.0),
        dict(n=13, head="European Parliament votes in Strasbourg",
             detail="ETS stability reserve, small mid-cap relief, Omnibus IV",
             label="SCHEDULED", src="EP agenda", lon=7.75, lat=48.6),
        dict(n=14, head="WFP: 10m tonnes of grain may miss markets",
             detail="Ukrainian and Russian wheat at risk",
             label="REPORTED", src="WFP", lon=30.7, lat=46.5),
        dict(n=15, head="Champions League matchday 5, nine games",
             detail="Arsenal-Dortmund, Man City-Napoli, Real-PSV",
             label="SCHEDULED", src="UEFA", lon=-0.1, lat=51.5),
    ]),
    ("MIDDLE EAST", [
        dict(n=16, head="Gaza: Israeli strike kills at least 3",
             detail="Near a police post in Khan Younis; 5 hurt, medics say",
             label="REPORTED", src="Reuters", lon=34.3, lat=31.3),
        dict(n=17, head="Qatar pushes to revive US-Iran talks",
             detail="Brent -0.5% to $86.27, near a 3-month low",
             label="REPORTED", src="AP, wires", lon=51.5, lat=25.3),
    ]),
    ("AFRICA", [
        dict(n=18, head="AU launches maternal health roadmap",
             detail="Unveiled by Tanzania's Samia Suluhu Hassan, Addis Ababa",
             label="REPORTED", src="Today News Africa", lon=38.7, lat=9.0),
        dict(n=19, head="Africa CDC: 1 in 6 pregnancies are teenage girls",
             detail="Report presented at CPHIA conference",
             label="REPORTED", src="Africa CDC", lon=40.2, lat=7.6),
        dict(n=20, head="Nigeria: school building collapses in Abia",
             detail="Pupil, 8, killed; Governor Otti orders inquiry",
             label="REPORTED", src="Punch", lon=7.5, lat=5.5),
        dict(n=21, head="Ramaphosa takes NCOP questions on AGOA",
             detail="US 30% tariff on South Africa on the agenda",
             label="SCHEDULED", src="SA briefing", lon=18.4, lat=-33.9),
    ]),
    ("OCEANIA", [
        dict(n=22, head="Australia and Singapore sign first CCS treaty",
             detail="Albanese-Wong summit; AI statement, supply MoU",
             label="OFFICIAL", src="PM of Australia", lon=149.1, lat=-35.3),
        dict(n=23, head="AustralianSuper backs Brookfield's $2.53bn bid",
             detail="Reliance Worldwide +12% to A$5.07, 20-month high",
             label="REPORTED", src="Reuters", lon=151.2, lat=-33.9),
        dict(n=24, head="Fiji to shut every school for 5 days",
             detail="From 30 Nov, as El Nino drought bites",
             label="REPORTED", src="PINA", lon=178.0, lat=-17.8),
        dict(n=25, head="Kiribati: Kanton Island evacuated",
             detail="Residents given one day's notice",
             label="REPORTED", src="PINA", lon=-171.7, lat=-2.8),
        dict(n=26, head="Australian opposition rejects Vanuatu treaty",
             detail="Coalition says it will not back the pact",
             label="REPORTED", src="PINA", lon=168.3, lat=-17.7),
    ]),
    ("NORTH AMERICA", [
        dict(n=27, head="Google rolls Gemini 4 Neon out to Workspace",
             detail="Via the Gemini app, announced 00:09 UTC",
             label="REPORTED", src="Google", lon=-122.1, lat=37.4),
        dict(n=28, head="White House turkey pardon, 14:00 ET",
             detail="Birds named Freedom and Feathers",
             label="SCHEDULED", src="White House", lon=-77.0, lat=38.9),
    ]),
    ("LATIN AMERICA", [
        dict(n=29, head="Brazil: Lula's fiscal package to House vote",
             detail="PLP 299/2026 needs 257 of 513 votes",
             label="SCHEDULED", src="FinFlash", lon=-47.9, lat=-15.8),
        dict(n=30, head="Miss Universe final in San Juan",
             detail="Puerto Rico hosts the crowning night",
             label="SCHEDULED", src="Today News Africa", lon=-66.1, lat=18.4),
    ]),
]

# Hour by hour, UTC, 24 November 2026
TIMELINE = [
    ("22:52*", "Ulleung alert", 5),
    ("00:00", "Asia opens, rally", 1),
    ("00:09", "Gemini 4 Neon", 27),
    ("00:16", "Abia collapse", 20),
    ("00:28", "RWC +12%", 23),
    ("01:32", "M5.3 Nepal", 6),
    ("02:57", "Treason charge", 7),
    ("03:47", "Rupiah 18,215", 9),
    ("17:45", "UCL kick-offs", 15),
    ("19:00", "Turkey pardon", 28),
]
TIMELINE_NOTE = "* 22:52 UTC on 23 Nov = 07:52 on 24 Nov in Korea"

# Earlier-day stories deliberately left off the page
DATE_CHECK = [
    ("Nvidia rehires Huang, shares +31.5%", "Mon 23 Nov (US)"),
    ("Wall St best day since Apr 2025", "Mon 23 Nov"),
    ("COP31 ends without a deal", "Sun 22 Nov"),
    ("Zelensky calls for 4-way talks", "Mon 23 Nov"),
    ("EU 22nd sanctions package", "Mon 23 Nov"),
    ("M6.5 Vanuatu earthquake", "Mon 23 Nov UTC"),
    ("India-NZ 1st Test ends in draw", "Mon 23 Nov"),
]

NUMBERS = [
    ("5,014", "Kospi, first time over 5,000"),
    ("58,654", "Nikkei after Monday holiday"),
    ("$86.27", "Brent, near 3-month low"),
    ("18,215", "rupiah per US dollar"),
]
