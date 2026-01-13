import csv
import json

INPUT_CSV = "vehicles_data.csv"
OUTPUT_JSON = "vehicles_grouped_by_battery.json"


def get_battery_range(battery):
    if 1 <= battery <= 10:
        return "1-10"
    elif 11 <= battery <= 20:
        return "11-20"
    elif 21 <= battery <= 30:
        return "21-30"
    elif 31 <= battery <= 40:
        return "31-40"
    elif 41 <= battery <= 50:
        return "41-50"
    elif 51 <= battery <= 60:
        return "51-60"
    elif 61 <= battery <= 70:
        return "61-70"
    elif 71 <= battery <= 80:
        return "71-80"
    elif 81 <= battery <= 90:
        return "81-90"
    elif 91 <= battery <= 100:
        return "91-100"
    else:
        return "Invalid"


def transform_vehicles_on_battery_percentage(csv_file):
    grouped = {}

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            battery = int(row["battery_percentage"])
            range_key = get_battery_range(battery)

            vehicle = {
                "vehicle_id": row["vehicle_id"],
                "vehicle_name": row["vehicle_name"],
                "battery_percentage": battery
            }

            if range_key not in grouped:
                grouped[range_key] = []

            grouped[range_key].append(vehicle)

    return grouped


def write_json(data, json_file):
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    grouped_data = transform_vehicles_on_battery_percentage(INPUT_CSV)
    write_json(grouped_data, OUTPUT_JSON)
