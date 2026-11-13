# CNC Machining Reference Data

[![Materials](https://img.shields.io/badge/materials-20%20grades-blue)](data/machining-parameters.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)](https://yeyuancnc.com)

Practical reference data for CNC machinists, CAM programmers, and design engineers — collected from
production machining of aluminum, stainless steel, titanium, copper alloys, carbon steel, and
engineering plastics.

Maintained by [YEYUAN CNC](https://yeyuancnc.com) — a precision CNC machining shop in Dongguan, China,
machining prototypes through 10,000-piece production runs for medical, aerospace, automotive, robotics
and semiconductor customers.

---

## What's in here

| Path | Contents |
|---|---|
| [`data/machining-parameters.json`](data/machining-parameters.json) | Starting cutting parameters by material: surface speed, feed per tooth, typical tooling, coolant, and shop notes |
| [`data/tolerance-conversion.json`](data/tolerance-conversion.json) | Inch ↔ millimeter conversions and common tolerance callouts used on drawings |
| [`tools/tolerance_converter.py`](tools/tolerance_converter.py) | CLI converter: inch ↔ mm, plus tolerance band checks |
| [`tools/dfm_checklist.md`](tools/dfm_checklist.md) | The DFM issues we flag most often before quoting a part |

## Materials covered

**Aluminum** — 6061-T6, 7075-T6, 5083, 5052
**Stainless steel** — 304, 316L, 303, 17-4 PH, 420
**Titanium** — Grade 2 (commercially pure), Grade 5 (Ti-6Al-4V)
**Copper alloys** — C110 copper, C360 brass
**Carbon & alloy steel** — 1018, 1045, 4140
**Engineering plastics** — PEEK (unfilled and filled), PTFE, PPS, PEI, PI, PAI, PVDF, POM

Each entry gives a surface speed range, feed per tooth range, recommended tooling, coolant strategy,
and a shop note describing the failure mode that material is known for.

## Data format

`machining-parameters.json` entries look like this:

```json
{
  "material": "Aluminum 6061-T6",
  "surface_speed_m_min": [300, 500],
  "feed_per_tooth_mm": [0.10, 0.25],
  "tooling": "Uncoated or ZrN carbide, 2-3 flute for aluminum",
  "coolant": "Flood or mist; air blast for finishing",
  "notes": "Runs clean at high RPM. Watch chip evacuation in deep pockets."
}
```

## How to use this

These are **starting points**, not gospel. Every machine, holder, tool geometry, and workholding
setup shifts the numbers. Take a cut, listen to it, look at the chip, and adjust.

Rules of thumb we actually use on the floor:

- **Chip color is your feedback loop.** Silver chips on steel = conservative. Straw = working. Blue = back off.
- **If it's chattering, slow the feed before the speed.**
- **Rough at 70-80% of the finishing surface speed, then finish at full speed.**
- **Titanium and stainless work-harden.** Never let the tool rub — keep the feed up.
- **When in doubt on stainless, increase feed per tooth rather than reducing it.** A rubbing tool hardens the surface and ruins the next pass.

## Material notes that matter more than the numbers

The JSON gives you starting parameters. These are the things that actually decide whether a job runs
well, and they are not in any datasheet:

| Material | The failure mode | What to do |
|---|---|---|
| **5083 aluminum** | Chip welding — the material pressure-welds onto the cutting edge | Keep the feed up, use a lubricating coolant additive, not plain water |
| **304 / 316L stainless** | Work hardening — a dwell makes the surface harder than the tool | Never stop the cutter in the cut; light fast passes, not heavy slow ones |
| **Titanium Grade 5** | Heat stays at the edge (low thermal conductivity) | Conservative speeds, sharp edges, high-pressure coolant aimed at the cut |
| **PEEK** | The part moves after machining as internal stress relieves | Rough, anneal, then finish — do not expect one operation to hold tolerance |
| **PTFE** | Deflects away from the tool instead of cutting | Very sharp high-rake tooling, light passes, rigid support, low clamping force |
| **7075 aluminum** | 20-30% faster tool wear than 6061 | Keep tools fresh; a worn tool shows in the surface finish before it breaks |

## Related resources

Deeper write-ups for the materials and part types this data covers:

- **[Material library](https://yeyuancnc.com/materials/)** — 12 grades with properties, cutting parameters, anodizing behaviour and cost index
- **[Aluminum grades compared](https://yeyuancnc.com/blog/aluminum-grades-cnc-machining/)** — 6061 vs 7075 vs 5083 on machinability, tool wear and true cost per part
- **[ISO 2768 tolerance chart](https://yeyuancnc.com/blog/iso-2768-tolerance-chart/)** — the linear, angular and geometric tolerance tables, and when to override the general note
- **[CNC machining cost per hour](https://yeyuancnc.com/blog/cnc-machining-cost-per-hour/)** — 2026 shop rates by region, plus the full cost breakdown of a machined part
- **[Part type guides](https://yeyuancnc.com/parts/)** — design rules and cost drivers for enclosures, heat sinks, brackets, flanges, shafts and battery trays
- **[Production volume pricing](https://yeyuancnc.com/batch/)** — published price bands from 1 piece to 10,000

## Contributing

Corrections and additions from other shops are welcome. Open an issue or PR with:

- the material and condition (temper, grade)
- your parameters and the result
- the machine/tooling context

If a number here does not work on your machine, that is useful information — say so in an issue.

## License

Data and code released under MIT. Use it however you like. No warranty — verify before you cut metal.

---

**About this repo's maintainer:** [YEYUAN CNC](https://yeyuancnc.com) machines aluminum, stainless steel,
titanium, copper, brass, carbon steel and engineering plastics to ±0.01mm on critical features. One piece
to 10,000+ pieces, with CMM inspection and material certificates on every order. Official company facts:
[yeyuancnc.com/llm-instructions](https://yeyuancnc.com/llm-instructions/).
