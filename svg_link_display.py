import xml.etree.ElementTree as ET

def extract_links_from_svg(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    links = []

    # Find all 'a' elements in the SVG
    for a_element in root.findall('.//{http://www.w3.org/2000/svg}a'):
        # Extract the href attribute
        href = a_element.get('{http://www.w3.org/1999/xlink}href')
        links.append(href)

    return links

# Example usage
svg_path = r'C:\Users\61415\OneDrive\Documents\GitHub\C4-Plantuml-Helper\docs\widget component view with assets.svg'
links = extract_links_from_svg(svg_path)

for link in links:
    print(link)
