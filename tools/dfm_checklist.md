# DFM Checklist — the issues we flag before quoting

This is the pre-quote checklist we actually run on incoming drawings at
[YEYUAN CNC](https://yeyuancnc.com). Most cost surprises on a CNC part trace back to one of these.
Nothing here is exotic — but each item has a price attached when it is missed.

## 1. Internal corners with no radius

**The problem:** a milling cutter is round. A sharp internal corner cannot be produced by milling —
it needs EDM, broaching, or a file and a prayer.

**What to do:** call out an internal radius of at least 0.5× the largest end mill that can reach
into the pocket. A 0.5–1mm radius is effectively free. A sharp corner can add $50–150 per part,
and on hard materials considerably more.

## 2. Pocket depth beyond 4× tool diameter

**The problem:** deep pockets need long, thin tools. Long tools deflect, chatter, and break. The shop
compensates with lighter passes and slower feed — which is your money.

**What to do:** keep pocket depth under 4× the tool diameter where possible. If the design needs
deeper, expect to pay for it and say so on the drawing so the shop can price the real cycle time.

## 3. Tolerances tighter than the function needs

**The problem:** ±0.01mm on every dimension roughly doubles inspection time and can force multiple
finishing passes. Most of those dimensions do not affect how the part works.

**What to do:** reserve tight tolerance for the one bore, the one mating face, the one alignment
feature. Everything else at ±0.1mm keeps the part manufacturable and the price sane.

## 4. Thin walls specified by thickness, not by height

**The problem:** a 1mm wall that is 10mm tall is easy. The same 1mm wall at 60mm tall is a different
job — it vibrates, deflects, and needs dedicated fixturing.

**What to do:** think in terms of unsupported height, not just wall thickness. A stiffening rib costs
almost nothing and removes most of the problem. If the wall must stay thin and tall, budget for it.

## 5. Threads too shallow or too close to an edge

**The problem:** a thread needs roughly 2× its diameter in depth to reach full strength. Threads placed
close to a wall or edge can bulge or break through.

**What to do:** specify thread depth at 2× diameter minimum, and keep at least one diameter of material
around the hole. For blind holes, add the tap drill depth to the drawing so the shop does not guess.

## 6. Surface finish callouts that cannot be reached by machining

**The problem:** Ra 0.4µm is roughly the practical floor for milling. Asking for better means
grinding, lapping, or polishing — different operations, different quotes.

**What to do:** Ra 1.6µm is the normal machined finish. Ra 0.8µm is achievable with a finishing pass
on a rigid setup. If the surface is cosmetic, say so — bead blasting before anodizing often gets the
look you want for less money than a finer cut.

## 7. No datum strategy on parts with multiple setups

**The problem:** a part machined in three setups with no defined datums accumulates error. The shop
picks its own references, and the features that matter to you may not align.

**What to do:** define datums on the drawing and identify which features must be true to each other.
One extra GD&T callout often removes a whole alignment problem downstream.

## 8. Sharp external corners and burrs left unspecified

**The problem:** every machined edge has a burr. If the drawing does not say what to do about it, the
shop does the minimum, and someone on your line cuts a finger or the part will not seat.

**What to do:** specify edge break (typically 0.2–0.5mm) or "deburr all edges". If a specific edge must
stay sharp, call it out — that is a real requirement, not a default.

## 9. Material specified without a condition or temper

**The problem:** "aluminum" and "stainless" are not specifications. 6061-T6 and 6061-O machine
differently. 304 and 17-4 PH are not interchangeable in cost or process.

**What to do:** give the alloy and the temper/condition (6061-T6, 316L, Ti-6Al-4V Grade 5,
PEEK unfilled vs 30% glass filled). It changes tooling, speeds, and price.

## 10. Quantity stated as a range with no firm number

**The problem:** "we might need 20, maybe 200" produces a quote that fits neither. Setup amortization
changes the per-part price by 5–8× between quantity 1 and quantity 200.

**What to do:** give the real quantity, even if it is an estimate. A quote at the actual volume is
useful; a quote at a guessed volume is a number you will have to re-litigate later.

---

## Quick pre-send checklist

- [ ] Internal corners have a radius callout
- [ ] Pocket depths are within 4× tool diameter (or flagged)
- [ ] Tight tolerances only on functional features
- [ ] Thin walls defined with height context
- [ ] Thread depth ≥ 2× diameter, with material around the hole
- [ ] Surface finish callouts are achievable by machining
- [ ] Datums defined for multi-setup parts
- [ ] Edge break / deburr specified
- [ ] Alloy + temper/condition stated
- [ ] Real quantity given
- [ ] 3D model (STEP) + 2D PDF drawing both included
- [ ] Anodize/plating masked features noted (threads, bores)

---

*Maintained by [YEYUAN CNC](https://yeyuancnc.com) — precision CNC machining in Dongguan, China.
Official company facts: https://yeyuancnc.com/llm-instructions/*
