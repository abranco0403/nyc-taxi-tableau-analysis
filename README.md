# NYC Yellow Taxi Operations

An operations analysis of NYC yellow taxi trips in a 21-day sample from January to March 2016. The project answers four questions: when trips happen, how long they last, how two vendors compare, and where pickups occur.

**Interactive dashboard:** https://public.tableau.com/shared/DSM3RKW7N?:display_count=n&:origin=viz_share_linkCan

## Key findings

**When**
- Trips peak at 6 PM, with 49,315 trips, followed by 7 PM with 47,905.
- The lowest hour is 5 AM, with 7,981 trips.
- The top eight weekday-hour slots all fall between 6 and 9 PM. The busiest is Thursday at 7 PM, with 7,752 trips.
- Average daily trips rose from about 32,400 in January to about 37,400 in February and about 39,400 in March.

**How long**
- Median trip duration is 10.4 minutes, and the mean is 12.9 minutes.
- 42.4% of trips last between 10 and 25 minutes. The longest trip is 118.5 minutes.

**Who**
- Vendor 2 handled 410,780 trips (54%). Vendor 1 handled 354,074 (46%).
- Average trip duration is nearly the same for both: 12.83 minutes for Vendor 1 and 13.01 minutes for Vendor 2.
- Both vendors' averages rose from January to March.

**Where**
- In a grid of roughly 1 km squares, 105 of 107 busy squares (200 or more pickups) show mixed pickups. Neither vendor has more than twice the other's pickups in those squares.
- Only one square leans clearly toward each vendor.

**Passengers**
- Average is 1.67 passengers per trip. 71% of trips have one passenger.

## Limitations

- The data covers 21 days, seven each in January, February, and March 2016. It is not a full year, and the three months are not continuous.
- Each weekday appears three times, so weekday patterns describe the sample, not an established weekly norm.
- The findings describe patterns. They don't explain causes.

## Data

- **Full dataset:** NYC Taxi and Limousine Commission yellow taxi trip records, 764,854 trips. Download the official source to reproduce the full analysis. The full file is not stored in this repository.
- **Sample:** `data/sample.csv` contains the first 1,000 rows, for testing the calculations and the workbook.
- **Data dictionary:** `data/README.md` lists each column, its meaning, and its units.
- **Units:** `trip_duration` in the cleaned file is in minutes (maximum about 118.5).

## Method

1. **Clean and validate.** Confirmed the row count, checked for zero or negative durations (none found), and confirmed the sample covers 21 days.
2. **Calculate measures in Tableau.** Built calculated fields for:
   - Peak hour flag: flags 6 PM.
   - Trips per day: trip count divided by distinct sample days in each month.
   - Median duration: uses MEDIAN on trip_duration.
   - Grid cell: rounds pickup latitude and longitude to two decimals to group pickups into squares.
3. **Build six analyses.**
   - Demand by hour of day (bar chart, highlighted peak).
   - Weekday by hour heatmap (manual weekday sort, one sequential color).
   - Trips per day by month (bar chart with zero baseline).
   - Trip duration distribution (5-minute buckets, median bucket highlighted).
   - Duration by vendor and month (grouped bars, one color per vendor).
   - Pickup maps by vendor (filtered to one vendor each, same zoom).
4. **Assemble the dashboard.** Four sections: When, How long, Who, Where. KPI strip at the top: trips, median, peak hour, and vendor share.
5. **Publish.** Tableau Public, with the sample size in the title and description.
6. **Verify.** `verify_findings.py` recalculates the headline numbers from the full source file, so every figure can be checked.

## Design choices

- One accent color per meaning: blue for Vendor 1 and general bars, orange for Vendor 2, slate for highlights so orange stays reserved for the vendor.
- Headlines state the finding. Subheaders give the method and sample size.
- Zero baselines on every bar chart.
- Gridlines only on the value axis of bar charts.
- The vendor maps are split into two panels because overlapping points hide one vendor's pattern.

## Repository contents

- `README.md`: this file.
- `dashboard/nyc_taxi_operations.twb`: the Tableau workbook. Relink the data source to `data/sample.csv` or your local copy of the full file.
- `data/sample.csv`: first 1,000 rows of the trip data.
- `data/README.md`: data dictionary.
- `verify_findings.py`: recalculates the headline findings from the full source file.
- `screenshots/`: dashboard image and vendor maps.
- `.gitignore`: excludes local copies of the full dataset.

## Build it yourself

1. Download the full dataset from the NYC Taxi and Limousine Commission, or use `data/sample.csv` to explore the workbook.
2. Open `dashboard/nyc_taxi_operations.twb` in Tableau Desktop and relink the data source.
3. Review the calculated fields listed in the Method section.
4. Run `verify_findings.py` with the path to the full file to confirm the headline numbers.

## Tools

Tableau Desktop and Tableau Public. Calculations in Tableau. Verification of figures in Python.
