
import re
from pathlib import Path

DOCUMENTS = Path(__file__).parent / "corpora" / "austin_restaurants" / "documents"


def add_restaurant_links(answer, sources):
    """Append verified website links for restaurants named in the answer."""
    if not answer:
        return answer

    links = {}

    for source in sources:
        path = DOCUMENTS / Path(source).name
        if not path.is_file():
            continue

        text = path.read_text(encoding="utf-8")

        # Each restaurant entry contains its name and Website field.
        blocks = re.split(r"\n\s*\n", text)

        for block in blocks:
            match = re.search(
                r"Website:\s*(https?://\S+)", block, re.IGNORECASE
            )
            if not match:
                continue

            url = match.group(1).rstrip(".,)")
            lines = block.strip().splitlines()

            # Look for the restaurant heading in this block.
            headings = [
                re.sub(r"^#+\s*", "", line).strip()
                for line in lines
                if line.strip().startswith("#")
            ]

            if not headings:
                continue

            name = headings[-1]

            if re.search(re.escape(name), answer, re.IGNORECASE):
                links[name] = url

    if not links:
        return answer

    website_lines = [
        f"- [{name}]({url})" for name, url in links.items()
    ]

    return answer.rstrip() + "\n\nRestaurant websites:\n" + "\n".join(website_lines)
