import csv
import json


class VehicleBatteryTransformation:
    def __init__(self, input_csv, output_json):
        self.input_csv = input_csv
        self.output_json = output_json

    def get_battery_range(self, battery):
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

    def transform_vehicles_on_battery_percentage(self):
        grouped = {}

        with open(self.input_csv, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                battery = int(row["battery_percentage"])
                range_key = self.get_battery_range(battery)

                vehicle = {
                    "vehicle_id": row["vehicle_id"],
                    "vehicle_name": row["vehicle_name"],
                    "battery_percentage": battery
                }

                if range_key not in grouped:
                    grouped[range_key] = []

                grouped[range_key].append(vehicle)

        return grouped

    def write_json(self, data):
        with open(self.output_json, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def group_data(self):
        grouped_data = self.transform_vehicles_on_battery_percentage()
        self.write_json(grouped_data)


if __name__ == "__main__":
    transformed_data = VehicleBatteryTransformation("vehicles_data.csv", "vehicles_grouped_by_battery.json")
    transformed_data.group_data()