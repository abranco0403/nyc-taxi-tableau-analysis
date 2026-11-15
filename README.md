# NYC Yellow Taxi Operations

An operations analysis of NYC yellow taxi trips in a 21-day sample from January to March 2016. The project answers four questions a fleet planner would ask: when trips happen, how long they last, how two vendors compare, and where pickups occur.

**Interactive dashboard:** https://public.tableau.com/shared/DSM3RKW7N

**Full walkthrough:** [docs/NYC_Yellow_Taxi_Project_Walkthrough.pdf](docs/NYC_Yellow_Taxi_Project_Walkthrough.pdf)

![Dashboard](screenshots/dashboard.png)

## Objectives

1. Identify when demand peaks, by hour and by weekday.
2. Describe how long trips last, and how that varies across trips.
3. Compare the two vendors on volume and trip length.
4. Show where pickups happen, and whether the vendors cover the same areas.

## Key findings

**When**
- Demand peaks at 6 PM (49,315 trips), followed by 7 PM (47,905) and 8 PM (43,836).
- The quietest hour is 5 AM, with 7,981 trips.
- 11 of the 12 busiest weekday-hour slots fall between 6 and 9 PM. The busiest is Thursday at 7 PM (7,752 trips).
- 6 to 9 PM accounts for 24.0% of all trips in the sample.
- Average daily trips rose 21% from January (32,448) to March (39,380).

**How long**
- Median trip duration is 10.4 minutes. The mean is 12.9 minutes.
- 42.4% of trips last between 10 and 25 minutes.
- The longest trip in the sample is 118.5 minutes.

**Who**
- Vendor 2 handled 410,780 trips (53.7%). Vendor 1 handled 354,074 (46.3%).
- Average trip length is nearly the same: 12.83 minutes for Vendor 1 and 13.01 minutes for Vendor 2.
- Both vendors' averages rise from January to March. The gap between them stays between 0.14 and 0.22 minutes each month.

**Where**
- In squares of roughly 1 km, 105 of the 107 busy squares (200 or more pickups) are mixed: neither vendor has more than twice the other's pickups.
- Two squares lean clearly toward one vendor: one toward Vendor 1 (200 pickups against 98) and one toward Vendor 2 (295 against 96).

**Passengers**
- The average trip has 1.67 passengers. 70.9% of trips have one passenger.

## Dataset

- **Source:** NYC Taxi and Limousine Commission yellow taxi trip records, cleaned.
- **Coverage:** 764,854 trips on 21 days, seven each in January, February, and March 2016. The three months are not continuous.
- **Full file:** not stored in this repository. Download it from the source to reproduce the analysis.
- **Sample:** `data/sample.csv` holds the first 100 trips, for exploring the workbook. It does not reproduce the findings.
- **Data dictionary:** `data/README.md` lists each column, its meaning, and its units.
- **Units:** `trip_duration` is in **seconds** in the source file. All durations here are converted to minutes.

## Data validation

Before analysis, the file was checked for common problems:
- Row count confirmed at 764,854.
- No zero or negative durations.
- Recorded trip duration matches dropoff minus pickup time on every trip.
- Vendor IDs are only 1 and 2.
- Duration unit confirmed as seconds from the first trip (1,110 seconds = 18.5 minutes).

## Method

1. **Validate** the data as described above.
2. **Calculate measures** in Tableau:
   - Duration in minutes: `trip_duration / 60`.
   - Median duration: `ROUND(MEDIAN(...) / 60, 1)`, shown as 10.4.
   - Peak hour label, and vendor share label.
   - Duration buckets: 5-minute intervals for the histogram.
   - Grid cell: pickup latitude and longitude rounded to two decimals.
3. **Explore** each question with summaries before choosing a chart.
4. **Build** six analyses: demand by hour, weekday-by-hour heatmap, trips per day by month, trip duration histogram, duration by vendor and month, and pickup maps by vendor.
5. **Assemble** the dashboard in four sections (When, How long, Who, Where), with a KPI strip at the top.
6. **Verify** every headline figure with `verify_findings.py`, which recalculates them from the full file using only the Python standard library.

## Exploratory analysis

The EDA covered hourly and weekday demand, daily volume by month, the shape of the trip duration distribution, vendor comparison by month, pickup concentration on a grid, and passenger counts. The full write-up, including the summaries behind each chart, is in the walkthrough PDF.

Notable points from the EDA:
- Trip duration is right-skewed. Most trips fall between 0 and 20 minutes, with a long tail, so the median (10.4) is reported with the mean (12.9).
- The vendor difference is small in every month, so the two vendors look operationally similar in this sample.

## Visualizations and design choices

- **Hourly demand (bars):** zero baseline, peak highlighted, so the 6 PM peak is easy to compare.
- **Weekday by hour (heatmap):** one sequential color, weekdays in calendar order.
- **Trips per day (bars):** zero baseline, so the 21% change is shown honestly.
- **Trip duration (histogram):** 5-minute buckets with the median bucket highlighted.
- **Vendors by month (grouped bars):** blue for Vendor 1, orange for Vendor 2 only.
- **Pickup maps:** one map per vendor at the same zoom, because overlapping points hide one vendor's pattern.

Color rules: blue for Vendor 1 and general bars, orange for Vendor 2 only, slate for highlights. Headlines state the finding. Subtitles give the measure, unit, and sample size.

## Limitations

- 21 sample days in three non-consecutive months. This is not a full year, and it can't show seasonal trends.
- Each weekday appears three times, so weekday patterns describe this sample, not a settled weekly norm.
- The findings describe patterns. They do not explain causes such as weather, events, or driver supply.

## Repository contents

- `README.md`: this file.
- `docs/NYC_Yellow_Taxi_Project_Walkthrough.pdf`: full walkthrough of the process, EDA, chart rationale, dashboard design, and corrections.
- `dashboard/nyc_taxi_operations.twb`: the Tableau workbook. Relink its data source to your local copy of the full file.
- `data/sample.csv`: first 100 trips.
- `data/README.md`: data dictionary.
- `verify_findings.py`: recalculates the headline figures from the full file.
- `screenshots/`: dashboard image and vendor maps.
- `.gitignore`: excludes local copies of the full dataset.

## Reproduce the results

1. Download the full cleaned dataset from the NYC Taxi and Limousine Commission and save it locally.
2. Run the verification script:

   ```
   python3 verify_findings.py path/to/your/full_file.csv
   ```

3. Open `dashboard/nyc_taxi_operations.twb` in Tableau Desktop and relink the data source to your full file.

## Tools

Tableau Desktop and Tableau Public for analysis and publishing. Python 3 standard library for verification.
