import csv
import pandas as pd
import matplotlib.pyplot as plt

#read the data in the file and store them in a tabel, shoudl have the columes: Country, code, year, life expectancy
life_expectancy = pd.read_csv("/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/life-expectancy/life-expectancy.csv")
#only keep data points from 1950 to 2023, before 1950 tha dat set showes mayn missing data points, which would influence avergae and standard deviation 
life_expectancy = life_expectancy[(life_expectancy["Year"]>= 1950) & (life_expectancy["Year"] <=2023)]

#for the 195 countires the ISO-3 code and the continet its on
country_continent = {
    # Africa
    "DZA": "Africa", "AGO": "Africa", "BEN": "Africa", "BWA": "Africa",
    "BFA": "Africa", "BDI": "Africa", "CPV": "Africa", "CMR": "Africa",
    "CAF": "Africa", "TCD": "Africa", "COM": "Africa", "COD": "Africa",
    "COG": "Africa", "CIV": "Africa", "DJI": "Africa", "EGY": "Africa",
    "GNQ": "Africa", "ERI": "Africa", "SWZ": "Africa", "ETH": "Africa",
    "GAB": "Africa", "GMB": "Africa", "GHA": "Africa", "GIN": "Africa",
    "GNB": "Africa", "KEN": "Africa", "LSO": "Africa", "LBR": "Africa",
    "LBY": "Africa", "MDG": "Africa", "MWI": "Africa", "MLI": "Africa",
    "MRT": "Africa", "MUS": "Africa", "MAR": "Africa", "MOZ": "Africa",
    "NAM": "Africa", "NER": "Africa", "NGA": "Africa", "RWA": "Africa",
    "STP": "Africa", "SEN": "Africa", "SYC": "Africa", "SLE": "Africa",
    "SOM": "Africa", "ZAF": "Africa", "SSD": "Africa", "SDN": "Africa",
    "TZA": "Africa", "TGO": "Africa", "TUN": "Africa", "UGA": "Africa",
    "ZMB": "Africa", "ZWE": "Africa",

    # Asia
    "AFG": "Asia", "ARM": "Asia", "AZE": "Asia", "BHR": "Asia",
    "BGD": "Asia", "BTN": "Asia", "BRN": "Asia", "KHM": "Asia",
    "CHN": "Asia", "CYP": "Asia", "GEO": "Asia", "IND": "Asia",
    "IDN": "Asia", "IRN": "Asia", "IRQ": "Asia", "ISR": "Asia",
    "JPN": "Asia", "JOR": "Asia", "KAZ": "Asia", "KWT": "Asia",
    "KGZ": "Asia", "LAO": "Asia", "LBN": "Asia", "MYS": "Asia",
    "MDV": "Asia", "MNG": "Asia", "MMR": "Asia", "NPL": "Asia",
    "PRK": "Asia", "OMN": "Asia", "PAK": "Asia", "PSE": "Asia", "PHL": "Asia",
    "QAT": "Asia", "SAU": "Asia", "SGP": "Asia", "KOR": "Asia",
    "LKA": "Asia", "SYR": "Asia", "TJK": "Asia", "THA": "Asia",
    "TLS": "Asia", "TUR": "Asia", "TKM": "Asia", "ARE": "Asia",
    "UZB": "Asia", "VNM": "Asia", "YEM": "Asia",

    # Europe
    "ALB": "Europe", "AND": "Europe", "AUT": "Europe", "BLR": "Europe",
    "BEL": "Europe", "BIH": "Europe", "BGR": "Europe", "HRV": "Europe",
    "CZE": "Europe", "DNK": "Europe", "EST": "Europe", "FIN": "Europe",
    "FRA": "Europe", "DEU": "Europe", "GRC": "Europe", "HUN": "Europe",
    "ISL": "Europe", "IRL": "Europe", "ITA": "Europe", "LVA": "Europe",
    "LIE": "Europe", "LTU": "Europe", "LUX": "Europe", "MLT": "Europe",
    "MDA": "Europe", "MCO": "Europe", "MNE": "Europe", "NLD": "Europe",
    "MKD": "Europe", "NOR": "Europe", "POL": "Europe", "PRT": "Europe",
    "ROU": "Europe", "RUS": "Europe", "SMR": "Europe", "SRB": "Europe",
    "SVK": "Europe", "SVN": "Europe", "ESP": "Europe", "SWE": "Europe",
    "CHE": "Europe", "UKR": "Europe", "GBR": "Europe", "VAT": "Europe",

    # North America
    "ATG": "North America", "BHS": "North America", "BRB": "North America",
    "BLZ": "North America", "CAN": "North America", "CRI": "North America",
    "CUB": "North America", "DMA": "North America", "DOM": "North America",
    "SLV": "North America", "GRD": "North America", "GTM": "North America",
    "HTI": "North America", "HND": "North America", "JAM": "North America",
    "MEX": "North America", "NIC": "North America", "PAN": "North America",
    "KNA": "North America", "LCA": "North America", "VCT": "North America",
    "TTO": "North America", "USA": "North America",

    # South America
    "ARG": "South America", "BOL": "South America", "BRA": "South America",
    "CHL": "South America", "COL": "South America", "ECU": "South America",
    "GUY": "South America", "PRY": "South America", "PER": "South America",
    "SUR": "South America", "URY": "South America", "VEN": "South America",

    # Oceania
    "AUS": "Oceania", "FJI": "Oceania", "KIR": "Oceania",
    "MHL": "Oceania", "FSM": "Oceania", "NRU": "Oceania",
    "NZL": "Oceania", "PLW": "Oceania", "PNG": "Oceania",
    "WSM": "Oceania", "SLB": "Oceania", "TON": "Oceania",
    "TUV": "Oceania", "VUT": "Oceania"
}

# Keep only rows that have a country code from the table 
life_expectancy = life_expectancy.dropna(subset=["Code"])

# Keep only the 195 countries thaqt match the dictionary of the uploaded country code - continent list
life_expectancy = life_expectancy[life_expectancy["Code"].isin(country_continent.keys())].copy()


#add the contitnet column to the tabel based on the ISo-3 code of each country
life_expectancy["Continent"] = life_expectancy["Code"].map(country_continent)

#check how many countries are in the list, and only got 194, so i looked for Palistane and Vatican city as these are the onyl two countires that are not in the UN and therefore might be missing
print(life_expectancy["Code"].nunique())
print(len(country_continent))
#missed Palestine in the list for the ISO-3 code and continen list
print(life_expectancy[life_expectancy["Entity"] == "Palestine"][["Entity", "Code"]].drop_duplicates())

#make a tabel with the mean and std for each contintetn and year, where the std represents the spread of life expectations on one continent
continent_stats = (
    life_expectancy.groupby(["Continent", "Year"])["Life expectancy"]
      .agg(["mean", "std"])
      .reset_index()
)

#plot the figure as a line plot with error bars 

plt.figure(figsize= (12,7))

#define each conitnent as one line for the graph
continents = continent_stats["Continent"].unique()

for continent in continents:
    data = continent_stats[continent_stats["Continent"] == continent]
    plt.errorbar(
        data["Year"],
        data["mean"],
        yerr= data["std"],
        fmt='-',
        capsize=2,
        label=continent
    )

plt.xlabel("year")
plt.ylabel("life expectancy (in years)")
plt.title("Average Life Expectancy by Continent, 1950-2023")
#define the range of teh axis
plt.yticks(range(30, 86, 5))
plt.xlim(1950,2023)

#add legend and grid
plt.legend()
plt.grid(True)
plt.tight_layout()

#svae graph
plt.savefig("average_life_expectancy_errorbars.png")
plt.show()
plt.close()

#the errorbars were hard to see, so i plotted a new graph with shaded boxes instead
plt.figure(figsize=(12, 7))

continents = continent_stats["Continent"].unique()

for continent in continents:
    data = continent_stats[continent_stats["Continent"] == continent]

    # Average line
    plt.plot(
        data["Year"],
        data["mean"],
        label=continent
    )

    # Standard deviation area
    plt.fill_between(
        data["Year"],
        data["mean"] - data["std"],
        data["mean"] + data["std"],
        alpha=0.15
    )

#labels adn grid
plt.xlabel("Year")
plt.ylabel("Life expectancy (years)")
plt.title("Average Life Expectancy by Continent, 1950–2023")

plt.yticks(range(30, 86, 5))
plt.xlim(1950,2023)

plt.legend()
plt.grid(True)
plt.tight_layout()

#save graph
plt.savefig("average_life_expectancy_shaded.png")
plt.show()
plt.close()
#----------------------------------------------------------------------------------------------------------

#Global gap = highest country life expectancy − lowest country life expectancy in each year

#sort tabel by year and max / min life expectancy
global_gap = (
    life_expectancy.groupby("Year")["Life expectancy"]
    .agg(["min", "max"])
    .reset_index()
)
#calculate the global gap
global_gap["gap"] = global_gap["max"] - global_gap["min"]

#plot graph
plt.figure(figsize=(12, 7))

plt.plot(
    global_gap["Year"],
    global_gap["gap"],
    color="blue"
)

#label and grid
plt.xlabel("Year")
plt.ylabel("Life expectancy gap (years)")
plt.title("Global Gap in Life Expectancy Between Countries, 1950–2023")
plt.xlim(1950,2023)

plt.grid(True)
plt.tight_layout()
#save graph
plt.savefig("Global_gap.png")
plt.show()
plt.close()

#global average and its standard deviation, this showes a more reliable overview as extrem cases can influence the view in the first graph

#sort data by year and calculate the overall avergae with std
global_variation1 = (
    life_expectancy.groupby("Year")["Life expectancy"]
    .agg(["mean", "std"])
    .reset_index()
)

#plot the graph with error bars
plt.figure(figsize=(12, 7))

plt.errorbar(
    global_variation1["Year"],
    global_variation1["mean"],
    yerr= global_variation1["std"],
    fmt='-',
    color='red',
    ecolor='black',
    capsize=2,
)
#add titles and grid
plt.xlabel("Year")
plt.ylabel("avergae of life expectancy (years)")
plt.title("Variation in Life Expectancy Between Countries, 1950–2023")
plt.xlim(1950,2023)

plt.grid(True, alpha=0.3)
plt.tight_layout()

#safe graph
plt.savefig("Global_average_errorbars.png")
plt.show()
plt.close()

#i want to show both graphs in one graph to outline the extrem cases and shwo a relative view

# Create the graph
fig, ax1 = plt.subplots(figsize=(12, 7))

# Left y-axis: Gap
#plot the graph
ax1.plot(
    global_gap["Year"],
    global_gap["gap"],
    color="blue",
    label="Global Gap"
)
#add label the the left side 
ax1.set_xlabel("Year")
ax1.set_ylabel("Life expectancy gap (years)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(True)

# Right y-axis: average 
ax2 = ax1.twinx()
#plot avergae
ax2.plot(
    global_variation1["Year"],
    global_variation1["mean"],
    color = 'red',
    label="Global Avergae"
    )

# decided agaisnt errorbars as it looked to crowed and show the Standard deviation area as a shaded box
ax2.fill_between(
    global_variation1["Year"],
    global_variation1["mean"] - global_variation1["std"],
    global_variation1["mean"] + global_variation1["std"],
    color = 'red',
    alpha=0.15
    )

#label on the right side in the same color as graph
ax2.set_ylabel(
    "Avergae of life expectancy (years)",
    color="red"
)
ax2.tick_params(axis="y", labelcolor="red")

# Title
plt.title(
    "Global Variation and Gap in Life Expectancy Between Countries, 1950–2023"
)

# Show both legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines1 + lines2,
    labels1 + labels2,
    loc="upper right"
)
plt.xlim(1950,2023)
plt.tight_layout()

#save graph
plt.savefig("global_Veriation_Gap.png")
plt.show()
plt.close()