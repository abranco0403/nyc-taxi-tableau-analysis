"""Recalculate the headline findings for the NYC yellow taxi sample.

Usage:
    python verify_findings.py path/to/NYC_yellow_taxi_trip_data_clean.csv

Uses only the Python standard library. The source file's trip_duration
column is in seconds; this script converts it to minutes before reporting.
"""
import csv
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime

TIME_FORMAT = "%m/%d/%Y %H:%M"  # e.g. 1/1/2016 0:18
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def main(path):
    n = 0
    durations_min = []
    hour_counts = Counter()
    slot_counts = Counter()          # (weekday, hour) -> trips
    vendor_counts = Counter()
    vendor_durations = defaultdict(list)
    passengers = []
    days_by_month = defaultdict(set)
    trips_by_month = Counter()
    cells = defaultdict(lambda: Counter())  # (lat, lon) -> vendor -> pickups
    bad_durations = 0

    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            n += 1
            pickup = datetime.strptime(row["tpep_pickup_datetime"], TIME_FORMAT)
            seconds = float(row["trip_duration"])
            if seconds <= 0:
                bad_durations += 1
            minutes = seconds / 60
            durations_min.append(minutes)

            hour_counts[pickup.hour] += 1
            slot_counts[(pickup.weekday(), pickup.hour)] += 1

            vendor = int(float(row["VendorID"]))
            vendor_counts[vendor] += 1
            vendor_durations[vendor].append(minutes)

            passengers.append(int(float(row["passenger_count"])))

            days_by_month[pickup.month].add(pickup.date())
            trips_by_month[pickup.month] += 1

            lat = round(float(row["pickup_latitude"]), 2)
            lon = round(float(row["pickup_longitude"]), 2)
            cells[(lat, lon)][vendor] += 1

    print(f"Trips: {n:,}")
    print(f"Zero or negative durations: {bad_durations}")
    print()

    print("WHEN")
    top_hours = hour_counts.most_common(3)
    low_hour = min(hour_counts, key=hour_counts.get)
    print(f"  Top hours: " + ", ".join(f"{h}:00 ({c:,})" for h, c in top_hours))
    print(f"  Lowest hour: {low_hour}:00 ({hour_counts[low_hour]:,})")
    print("  Top weekday-hour slots:")
    for (wd, h), c in slot_counts.most_common(8):
        print(f"    {WEEKDAYS[wd]} {h}:00 ({c:,})")
    print("  Average trips per sample day, by month:")
    for m in sorted(trips_by_month):
        days = len(days_by_month[m])
        print(f"    month {m}: {trips_by_month[m] / days:,.0f} per day over {days} days")
    print()

    print("HOW LONG")
    print(f"  Median: {statistics.median(durations_min):.1f} min")
    print(f"  Mean: {statistics.mean(durations_min):.1f} min")
    share = sum(1 for d in durations_min if 10 <= d <= 25) / n
    print(f"  Share of trips 10 to 25 min: {share:.1%}")
    print(f"  Longest trip: {max(durations_min):.1f} min")
    print()

    print("WHO")
    for v in sorted(vendor_counts):
        share = vendor_counts[v] / n
        avg = statistics.mean(vendor_durations[v])
        print(f"  Vendor {v}: {vendor_counts[v]:,} trips ({share:.1%}), average {avg:.2f} min")
    print()

    print("PASSENGERS")
    print(f"  Average: {statistics.mean(passengers):.2f}")
    print(f"  Share with one passenger: {passengers.count(1) / n:.1%}")
    print()

    print("WHERE (grid of 0.01 degrees, squares with 200+ pickups)")
    busy = {k: v for k, v in cells.items() if sum(v.values()) >= 200}
    dominated = 0
    for v in busy.values():
        c1, c2 = v.get(1, 0), v.get(2, 0)
        if c1 > 2 * c2 or c2 > 2 * c1:
            dominated += 1
    mixed = len(busy) - dominated
    print(f"  Busy squares: {len(busy)}")
    print(f"  Squares where neither vendor has more than twice the other's pickups: {mixed} of {len(busy)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
