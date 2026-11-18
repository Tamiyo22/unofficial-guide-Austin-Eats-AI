
import csv
import re
from collections import defaultdict
from pathlib import Path

# Location of our restaurant dataset
DOCUMENTS_DIR = Path("corpora/austin_restaurants/documents")
CSV_FILE = DOCUMENTS_DIR / "austin_restaurants_by_neighborhood.csv"


def main():
    restaurants_by_area = defaultdict(list)

    # Read the restaurant CSV
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            area = row["Area"].strip()
            restaurants_by_area[area].append(row)

    # Create one Markdown document per Austin area
    for area, restaurants in sorted(restaurants_by_area.items()):
        filename = re.sub(
            r"[^a-z0-9]+", "_", area.lower()
        ).strip("_") + ".md"

        lines = [
            f"# Austin Eats AI — {area}",
            "",
            "Restaurant information is based on a curated dataset.",
            "Prices are approximate and may change.",
            "",
        ]

        for restaurant in restaurants:
            name = restaurant["Restaurant Name"].strip()
            neighborhood = restaurant["Neighborhood"].strip()
            price = restaurant["Price Tier"].strip()
            website = restaurant["Website URL"].strip()
            highlights = restaurant["Highlights"].strip()

            lines.extend([
                f"## {name}",
                f"Area: {area}",
                f"Neighborhood: {neighborhood}",
                f"Price tier: {price}",
                f"Website: {website}",
                f"Highlights: {highlights}",
                "",
            ])

        output_file = DOCUMENTS_DIR / filename
        output_file.write_text(
            "\n".join(lines), encoding="utf-8"
        )

        print(
            f"Created {filename}: "
            f"{len(restaurants)} restaurants"
        )

    print(
        f"\nDone! Created {len(restaurants_by_area)} "
        "restaurant documents."
    )


if __name__ == "__main__":
    main()
