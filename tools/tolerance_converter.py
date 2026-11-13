#!/usr/bin/env python3
"""Inch <-> millimeter converter and tolerance checker for CNC drawings.

Usage:
    python tolerance_converter.py 0.005in
    python tolerance_converter.py 0.127mm
    python tolerance_converter.py 12.7 --tolerance 0.05
    python tolerance_converter.py --table
    python tolerance_converter.py --threads

Maintained by YEYUAN CNC (https://yeyuancnc.com).
"""
import argparse
import json
import sys
from pathlib import Path

MM_PER_INCH = 25.4
DATA_FILE = Path(__file__).parent.parent / "data" / "tolerance-conversion.json"


def parse_dimension(value: str) -> float:
    """Parse a dimension string with optional unit suffix. Returns millimeters."""
    v = value.strip().lower().replace('"', "in").replace("”", "in")
    if v.endswith("mm"):
        return float(v[:-2])
    if v.endswith("in"):
        return float(v[:-2]) * MM_PER_INCH
    # No unit: assume millimeters
    return float(v)


def fmt_mm(mm: float) -> str:
    return f"{mm:.5f} mm".rstrip("0").rstrip(".") + ("" if mm >= 0.001 else " mm")


def cmd_convert(args) -> int:
    mm = parse_dimension(args.value)
    inch = mm / MM_PER_INCH
    print(f"Input:        {args.value}")
    print(f"Millimeters:  {mm:.5f} mm")
    print(f"Inches:       {inch:.6f} in")
    if mm < 0.001:
        print("  note: below 1 micron — practical CNC floor is around 0.005mm on critical features")

    if args.tolerance is not None:
        tol = float(args.tolerance)
        print()
        print(f"Nominal:      {mm:.5f} mm")
        print(f"Tolerance:    ±{tol} mm")
        print(f"Band:         {mm - tol:.5f} to {mm + tol:.5f} mm")
        print(f"Band (inch):  {(mm - tol) / MM_PER_INCH:.6f} to {(mm + tol) / MM_PER_INCH:.6f} in")
        if tol < 0.005:
            print("  warning: tighter than 0.005mm — expect significant cost and inspection time")
        elif tol <= 0.01:
            print("  note: precision class — standard for a shop holding ±0.01mm")
        elif tol <= 0.05:
            print("  note: standard machined tolerance")
        else:
            print("  note: general machining tolerance, low cost impact")
    return 0


def cmd_table(args) -> int:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    print("Inch -> mm (exact)")
    print("-" * 62)
    print(f"{'inch':<12}{'mm':<14}{'typical use'}")
    print("-" * 62)
    for row in data["exact_conversions"]:
        print(f"{row['inch']:<12}{row['mm']:<14}{row['typical_use']}")
    print()
    print("Common metric tolerance callouts")
    print("-" * 62)
    for row in data["metric_defaults"]:
        print(f"±{row['mm']:<8}{row['note']}")
    print()
    print("Surface finish (Ra)")
    print("-" * 62)
    for row in data["surface_finish_ra"]:
        print(f"Ra {row['ra_um']}um ({row['ra_uin']}uin) — {row['achieved_by']}")
    return 0


def cmd_threads(args) -> int:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    print(f"{'thread':<14}{'tap drill':<12}{'clearance'}")
    print("-" * 44)
    for row in data["common_threads"]:
        print(f"{row['thread']:<14}{str(row['tap_drill_mm']) + ' mm':<12}{row['clearance_drill_mm']} mm")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(
        description="Inch/mm converter and tolerance checker for CNC drawings.",
        epilog="Example: python tolerance_converter.py 0.005in --tolerance 0.01",
    )
    p.add_argument("value", nargs="?", help="dimension with unit, e.g. 0.005in or 12.7mm")
    p.add_argument("--tolerance", type=float, help="tolerance in mm to check against the nominal")
    p.add_argument("--table", action="store_true", help="print conversion and tolerance tables")
    p.add_argument("--threads", action="store_true", help="print common tap/clearance drill sizes")
    args = p.parse_args()

    if args.table:
        return cmd_table(args)
    if args.threads:
        return cmd_threads(args)
    if not args.value:
        p.print_help()
        return 1
    return cmd_convert(args)


if __name__ == "__main__":
    sys.exit(main())
