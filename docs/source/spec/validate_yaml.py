from ruamel.yaml import YAML

yaml = YAML()

# Load and validate specification.yaml
with open("specification.yaml", "r", encoding="utf-8") as f:
    data = yaml.load(f)

items = data['specification']
print(f"Total items: {len(items)}")

# Check for missing fields
required_fields = ['pillar', 'capability_index', 'requirement_index', 'statement', 'guidance', 'importance', 'architecture_url']

for i, item in enumerate(items):
    missing = [field for field in required_fields if field not in item]
    if missing:
        print(f"Item {i} (requirement {item.get('requirement_index', 'unknown')}): Missing fields: {missing}")

print("Validation complete!")
