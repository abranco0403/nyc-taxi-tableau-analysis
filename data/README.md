# Data dictionary

## Files

- `sample.csv`: the first 100 trips (plus the header) from the full file, for testing the calculations and the workbook.
- The full file is not stored in this repository. Download the NYC Taxi and Limousine Commission yellow taxi trip records and use the cleaned sample file with 764,854 trips, covering 21 days (seven each in January, February, and March 2016).

## Columns

| Column | Type | Meaning | Notes |
|---|---|---|---|
| VendorID | integer | Technology vendor that recorded the trip | 1 = Vendor 1, 2 = Vendor 2 |
| tpep_pickup_datetime | datetime | Pickup date and time | Format m/d/yyyy H:mm |
| tpep_dropoff_datetime | datetime | Dropoff date and time | Same format as pickup |
| passenger_count | integer | Passengers on the trip | Reported by the driver |
| trip_distance | decimal | Trip distance | Miles |
| pickup_longitude | decimal | Pickup longitude | Decimal degrees |
| pickup_latitude | decimal | Pickup latitude | Decimal degrees |
| dropoff_longitude | decimal | Dropoff longitude | Decimal degrees |
| dropoff_latitude | decimal | Dropoff latitude | Decimal degrees |
| trip_duration | integer | Trip length | **Seconds** in this file. Divide by 60 for minutes. |

## Units check

The first trip in the file runs from 0:00 to 0:18 and records a `trip_duration` of 1110, which is 18.5 minutes. The maximum value in the file is about 7,100 seconds (118.5 minutes). All reported durations in the project are converted to minutes.

## Derived fields used in the analysis

- **Duration in minutes:** `trip_duration / 60`.
- **Pickup hour:** the hour of `tpep_pickup_datetime`, from 0 to 23.
- **Trips per day:** trip count in a month divided by the number of distinct pickup dates in that month (always 7 in this sample).
- **Grid cell:** pickup latitude and longitude, each rounded to two decimals, which groups pickups into squares of roughly 1 km.
