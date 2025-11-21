from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = False
yaml.indent(mapping=2, sequence=4, offset=2)

# Load the specification
with open("specification.yaml", "r", encoding="utf-8") as f:
    spec = yaml.load(f)

# Build hierarchy
pillars = {}
for s in spec["specification"]:
    p = s["pillar"]
    c = s["capability_index"]
    r = s["requirement_index"]
    if p not in pillars:
        pillars[p] = {}
    if c not in pillars[p]:
        pillars[p][c] = []
    pillars[p][c].append({
        k: v for k, v in s.items() if k in (
            "requirement_index", "statement", "guidance", "importance", "architecture_url",
        )
    })

# Convert to list format
pillars2 = []
for n, pk in enumerate(pillars.keys()):
    pillar = {"pillar_index": n + 1, "pillar": pk, "capabilities": []}
    for ck in pillars[pk]:
        pillar["capabilities"].append({"capability_index": ck, "statements": pillars[pk][ck]})
    pillars2.append(pillar)

# Write to YAML
with open("specification-pillars.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"specification": pillars2}, f)

print(f"Created specification-pillars.yaml with {len(pillars2)} pillars")
