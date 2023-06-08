# NIFC - Prescribed Burns - 1998-2019

CSV-formatted tabular data detailing prescribed burns in the US by a number of environmental agencies.

Source: (https://www.nifc.gov/fire-information/statistics/prescribed-fire)

Years: 1998-2019. NFS ended prescribed burns in 2019 citing increased risk, likely from climate change.

Agencies:
- BIA: [Bureau of Indian Affairs, U.S. Dept. of the Interior](https://www.bia.gov/)
- BLM: [Bureau of Land Management, U.S. Dept. of the Interior](https://www.blm.gov/)
- USFS: [Forest Service, U.S. Dept. of Agriculture](https://www.fs.usda.gov/)
- FWS: [Fish and Wildlife Service, U.S. Dept. of the Interior](https://www.fws.gov/)
- NPS: [National Park Service, U.S. Dept. of the Interior](https://www.nps.gov/index.htm)
- State/Other: Non-national agencies responsible for state or territory land management.

Required libraries: `pandas`, `lxml`

Creating tables: run `python ./create_data_tables.py` from cloned root directory. Data tables saved into `./data/*.csv` where burn data is separated into `acres.csv` and `fires.csv`, where the former is acreage burned per year and the latter is the number fires per year.

Michael Nolan
2023-06-08