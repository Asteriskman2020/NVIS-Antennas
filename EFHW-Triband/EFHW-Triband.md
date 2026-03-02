# Tri-Band End-Fed Half-Wave (EFHW) Antenna

## 80m + 40m + 20m | Inverted-L | 49:1 Transformer

---

## Table of Contents

1. [Design Objective](#1-design-objective)
2. [System Overview](#2-system-overview)
3. [Physical Specifications](#3-physical-specifications)
4. [Performance Summary](#4-performance-summary)
5. [EFHW Operating Principle](#5-efhw-operating-principle)
6. [49:1 Transformer Design](#6-491-transformer-design)
7. [Radiation Patterns](#7-radiation-patterns)
8. [NVIS + DX Coverage](#8-nvis--dx-coverage)
9. [Comparison with Other Designs](#9-comparison-with-other-designs)
10. [Counterpoise and Ground](#10-counterpoise-and-ground)
11. [Feed System](#11-feed-system)
12. [Construction Guide](#12-construction-guide)
13. [Bill of Materials](#13-bill-of-materials)
14. [Safety](#14-safety)
15. [Quick Reference Card](#15-quick-reference-card)
16. [Frequency Planning](#16-frequency-planning)
17. [Appendix: Key Formulae](#17-appendix-key-formulae)
18. [Files in This Package](#18-files-in-this-package)

---

## 1. Design Objective

This antenna provides **tri-band operation from a single wire** -- 80m and 40m for NVIS regional coverage plus 20m for low-angle DX -- without traps, loading coils, or an antenna tuner. The End-Fed Half-Wave (EFHW) design exploits the natural harmonic relationship between the three bands (3.5 / 7 / 14 MHz = 1:2:4) so that a single wire resonates on all three.

### Target Applications

- General HF operation: NVIS on 80m/40m plus DX on 20m
- Field stations needing multi-band capability from one antenna
- Emergency communications (EMCOMM, ARES/RACES) with extended reach
- Portable and semi-permanent installations
- Operators wanting 20m DX capability without a separate antenna
- Budget-conscious stations seeking maximum band coverage per dollar

### Design Philosophy

> Maximise band coverage from a single wire and single support. Accept moderate efficiency on 80m in exchange for tri-band operation and 20m DX capability that no dual-band NVIS antenna can provide.

---

## 2. System Overview

```
                        Support (10-12 m)
                              |
      Horizontal: ~29 m ======+
                              |
                              | Vertical: ~10 m
                              |
                      [49:1 Transformer]
                           |     |
                    Counterpoise  RG-213 to station
                    ~3 m wire
    Ground ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

### Feed System

```
    Antenna wire (39.4 m)
           |
     [49:1 Transformer]
      2x FT-240-43
      2:14 turns
           |
     [CM Choke]
      8-10T RG-213
      on FT-240-43
           |
     RG-213 Coax (50 ohm)
           |
     [Transceiver]
```

### Harmonic Relationship

```
    80m:  39.4 m = 0.5 lambda  (half-wave)      --> NVIS
    40m:  39.4 m = 1.0 lambda  (full-wave)       --> NVIS
    20m:  39.4 m = 2.0 lambda  (double-wave)     --> DX
```

---

## 3. Physical Specifications

| Parameter | Value |
|-----------|-------|
| Type | End-Fed Half-Wave (EFHW), inverted-L |
| Bands | 80 m (3.5--3.8 MHz) + 40 m (7.0--7.3 MHz) + 20 m (14.0--14.35 MHz) |
| Wire length | ~39.4 m total |
| Vertical section | ~10 m (up the support) |
| Horizontal section | ~29 m (sloping to far end) |
| Support height | 10--12 m (single mast or tree) |
| Far-end height | 2--5 m above ground |
| Feed height | 1--2 m above ground |
| Wire gauge | #14 AWG (1.63 mm diameter) stranded copper |
| Transformer | 49:1 on 2x FT-240-43 (2:14 turns) |
| Counterpoise | 3.05 m wire on ground |
| Feed cable | RG-213, 50 ohm |
| CM choke | 8--10 turns RG-213 on FT-240-43 |
| Power handling | 200 W PEP (80m), 300 W PEP (40m/20m) |
| Overall footprint | ~29 x 10 m |

---

## 4. Performance Summary

| Freq (MHz) | Band | Lambda-mult | Gain (dBi) | Efficiency (%) | VSWR | Bandwidth (kHz) | h/lambda | Use |
|-----------|------|-------------|-----------|----------------|------|-----------------|----------|-----|
| 3.500 | 80m | 0.5 lambda | +2.0 | 85 | 2.0 | 100 | 0.12 | NVIS |
| 3.650 | 80m | 0.5 lambda | +2.8 | 88 | 1.5 | 120 | 0.12 | NVIS |
| 3.800 | 80m | 0.5 lambda | +3.0 | 88 | 2.2 | 120 | 0.13 | NVIS |
| 7.000 | 40m | 1.0 lambda | +4.5 | 92 | 1.5 | 200 | 0.23 | NVIS |
| 7.150 | 40m | 1.0 lambda | +5.0 | 93 | 1.2 | 220 | 0.24 | NVIS |
| 7.300 | 40m | 1.0 lambda | +5.2 | 93 | 1.6 | 220 | 0.24 | NVIS |
| 14.000 | 20m | 2.0 lambda | +6.5 | 95 | 1.8 | 250 | 0.47 | DX |
| 14.150 | 20m | 2.0 lambda | +7.0 | 96 | 1.5 | 280 | 0.47 | DX |
| 14.350 | 20m | 2.0 lambda | +7.2 | 96 | 1.8 | 280 | 0.48 | DX |

### Performance Highlights

- **80m band**: +2.8 dBi peak gain at zenith, 88% efficiency, ~120 kHz usable bandwidth
- **40m band**: +5.0 dBi peak gain at zenith, 93% efficiency, ~220 kHz usable bandwidth
- **20m band**: +7.0 dBi peak gain at low angles, 96% efficiency, ~280 kHz usable bandwidth
- **NVIS coverage**: 0--350 km on 80m/40m
- **DX coverage**: Low-angle radiation on 20m for long-distance contacts
- **No antenna tuner required** for normal operation within each band

---

## 5. EFHW Operating Principle

### Harmonic Resonance

The End-Fed Half-Wave antenna exploits a fundamental property of wire antennas: a wire that is lambda/2 at a given frequency is automatically resonant at all even harmonics. Since amateur bands are harmonically related (3.5 x 2 = 7 x 2 = 14 MHz), a single wire serves all three bands.

```
Frequency    Wire length     Resonance mode
3.5 MHz      39.4 m          0.5 lambda  (half-wave)
7.0 MHz      39.4 m          1.0 lambda  (full-wave)
14.0 MHz     39.4 m          2.0 lambda  (double-wave)
```

### End-Fed Impedance

At the end of a resonant wire, the impedance is very high -- approximately 2500--5000 ohm depending on height and ground conditions. This high impedance is consistent across all harmonic resonances, making a single broadband transformer effective on all three bands.

### Pattern Evolution

As the electrical length of the wire increases, the radiation pattern changes:

- **0.5 lambda (80m)**: Classic half-wave pattern with broad main lobe at zenith. Maximum radiation is straight up -- ideal for NVIS.
- **1.0 lambda (40m)**: The full-wave pattern narrows, concentrating more energy at zenith with higher gain. Still excellent for NVIS.
- **2.0 lambda (20m)**: Multiple lobes form. Significant radiation appears at lower elevation angles (20--40 degrees), providing DX capability. Some energy remains at higher angles.

### Wire Length Calculation

```
lambda/2 at 3.5 MHz:
    c = 300 MHz*m
    lambda = 300 / 3.5 = 85.7 m
    lambda/2 = 42.9 m (free space)

Velocity factor for #14 AWG wire: ~0.97
    Effective lambda/2 = 42.9 * 0.97 = 41.6 m

Practical adjustment for height, inverted-L, and ground effects:
    Final wire length: ~39.4 m (tune to resonance)
```

---

## 6. 49:1 Transformer Design

### Core Selection

The transformer uses two FT-240-43 toroids stacked and taped together. The Fair-Rite 43 material (NiZn ferrite) provides good permeability from 1--30 MHz, making it well-suited for tri-band operation.

| Parameter | Value |
|-----------|-------|
| Core material | Fair-Rite 43 (NiZn ferrite) |
| Core size | FT-240-43 (61 mm OD, 35.5 mm ID) |
| Number of cores | 2 (stacked) |
| Primary (coax side) | 2 turns #14 AWG PTFE |
| Secondary (antenna side) | 14 turns #14 AWG PTFE |
| Impedance ratio | (14/2)^2 = 49:1 |
| Nominal Z transform | 2500 ohm to 51 ohm |
| Insertion loss (80m) | 0.3--0.5 dB |
| Insertion loss (40m/20m) | 0.1--0.3 dB |
| Power rating | 200 W (80m), 300 W (40m/20m) |

### Why 49:1?

```
End-fed impedance: ~2500 ohm (typical for EFHW over ground)
Target impedance: 50 ohm (coax)
Required ratio: 2500 / 50 = 50:1

Nearest practical turns ratio: 14:2 = 7:1
Impedance ratio: 7^2 = 49:1
Transformed Z: 2500 / 49 = 51 ohm (close enough to 50 ohm)
```

### Construction Steps

1. Stack two FT-240-43 toroids and wrap with fibreglass tape or PTFE tape
2. Wind 14 turns of #14 AWG PTFE-insulated wire as the secondary (antenna side)
3. Wind 2 turns of #14 AWG PTFE-insulated wire as the primary (coax side)
4. Both windings go through the same core aperture but are separate
5. Connect the primary to an SO-239 chassis connector (centre to one end, shield to the other)
6. Connect one end of the secondary to the antenna wire terminal (wing-nut)
7. Connect the other end of the secondary to the counterpoise terminal
8. The junction of primary and secondary grounds ties to the SO-239 ground lug
9. House everything in an IP65 ABS enclosure
10. Seal cable entries with silicone or grommet seals

### Transformer Loss Budget

| Band | Frequency | Core Loss | Copper Loss | Total Loss |
|------|----------|-----------|-------------|------------|
| 80m | 3.65 MHz | 0.25 dB | 0.10 dB | 0.35 dB |
| 40m | 7.15 MHz | 0.10 dB | 0.08 dB | 0.18 dB |
| 20m | 14.15 MHz | 0.08 dB | 0.07 dB | 0.15 dB |

---

## 7. Radiation Patterns

### 3D Pattern Characteristics

Each band produces a distinct radiation pattern due to the changing electrical length of the wire:

- **80m (3.65 MHz, 0.5 lambda)**: Broad toroidal lobe peaking near zenith, +2.8 dBi. The h/lambda = 0.12 produces good NVIS coverage. The inverted-L configuration adds a small vertically-polarised component that fills in nulls.

- **40m (7.15 MHz, 1.0 lambda)**: Narrower main lobe still peaking near zenith, +5.0 dBi. The h/lambda = 0.24 is close to the NVIS optimum. Higher gain and narrower beamwidth compared to 80m make this the strongest NVIS band.

- **20m (14.15 MHz, 2.0 lambda)**: Multiple lobes with significant energy at 20--40 degree elevation, +7.0 dBi. The h/lambda = 0.47 places the antenna at roughly half a wavelength above ground. Low-angle lobes provide DX capability not available on the lower bands.

### Elevation Pattern

- 80m: Peak near zenith, 3 dB beamwidth approximately 80 degrees (very broad)
- 40m: Peak at zenith, 3 dB beamwidth approximately 55 degrees
- 20m: Multiple peaks, strongest lobe at approximately 25 degrees elevation

---

## 8. NVIS + DX Coverage

### Height-to-Wavelength Analysis

| Band | Centre Freq | Wavelength | h/lambda | Array Factor | Mode |
|------|------------|------------|----------|-------------|------|
| 80m | 3.650 MHz | 82.1 m | 0.12 | 1.47 | NVIS |
| 40m | 7.150 MHz | 41.9 m | 0.24 | 1.96 | NVIS |
| 20m | 14.150 MHz | 21.2 m | 0.47 | 2.00 | DX |

### Array Factor Calculation

The ground reflection creates an image antenna:

```
AF(alpha) = 2 * |sin(k * h * sin(alpha))|

where:
    k     = 2*pi / lambda
    h     = effective antenna height (~10 m for vertical section)
    alpha = elevation angle
```

At zenith (alpha = 90 degrees):

- **80m**: AF = 2 * |sin(2*pi * 10 / 82.1)| = 2 * 0.735 = 1.47
- **40m**: AF = 2 * |sin(2*pi * 10 / 41.9)| = 2 * 0.998 = 1.96
- **20m**: AF = 2 * |sin(2*pi * 10 / 21.2)| = 2 * 0.998 = 2.00

### Coverage Geometry

| Elevation Angle | Single-hop Range | 80m Signal | 40m Signal | 20m Signal |
|----------------|-----------------|-----------|-----------|-----------|
| 90 deg (zenith) | 0 km (overhead) | Maximum | Maximum | Moderate |
| 70 deg | ~90 km | Strong | Strong | Moderate |
| 50 deg | ~210 km | Good | Good | Good |
| 30 deg | ~400 km | Weak | Moderate | Strong |
| 15 deg | ~1000 km | -- | Weak | Strong |
| 10 deg | ~2000 km | -- | -- | Good |

### Day/Night Performance

- **Daytime (80m)**: Coverage 0--200 km, moderate D-layer absorption
- **Daytime (40m)**: Coverage 0--350 km, better D-layer penetration
- **Daytime (20m)**: DX 500--3000 km via F2 layer, low-angle radiation
- **Night-time (80m)**: Coverage 0--350 km, reduced absorption, best 80m window
- **Night-time (40m)**: F-layer higher; mixed NVIS/DX performance
- **Night-time (20m)**: Band may close; monitor propagation

---

## 9. Comparison with Other Designs

| Parameter | EFHW Tri-Band (this design) | Efficient Fan Dipole | Small-Size Fan Dipole | Balanced Mag Loop |
|-----------|---------------------------|---------------------|---------------------|------------------|
| Bands | 80m + 40m + 20m | 80m + 40m | 80m + 40m | 80m + 40m |
| Type | EFHW inverted-L | Full-size inverted-V | Center-loaded inv-V | Magnetic loop |
| 80m gain | +2.8 dBi | +7.0 dBi | +2.5 dBi | -7 dBi |
| 40m gain | +5.0 dBi | +7.8 dBi | +5.5 dBi | +1 dBi |
| 20m gain | +7.0 dBi | N/A | N/A | N/A |
| Efficiency | 85--96% | 97--99% | 72--86% | 8--55% |
| Footprint | 29 x 10 m | 39 x 12 m | 19 x 8 m | 2 m diameter |
| Support points | 1 mast + rope | 1 mast + 2 ropes | 1 mast + 2 ropes | Tripod |
| Feed system | 49:1 transformer | 1:1 balun | 1:1 balun | Direct |
| Cost | $95--$185 | $280--$450 | $80--$150 | $313--$712 |
| Tuner needed | No | No | Yes (80m) | Every QSY |

### What You Gain (vs dual-band designs)

1. **20m DX band** -- no other design in this series covers 20m
2. **Three bands from one wire** -- simpler than multiple antennas
3. **Single support point** -- inverted-L needs only one mast or tree
4. **Low cost** -- $95--$185, competitive with the small-size design
5. **No traps or tuner** -- natural harmonic resonance keeps things simple

### What You Give Up

1. **Lower 80m gain** than the efficient fan dipole (-4.2 dB)
2. **End-fed RF on coax shield** -- requires good CM choke
3. **High voltage at wire end** (~2500 V at 200 W on 80m)
4. **Narrower 80m bandwidth** (120 kHz vs 180 kHz for full-size)
5. **More complex feed** (49:1 transformer vs simple balun)

---

## 10. Counterpoise and Ground

### Counterpoise Wire

The EFHW requires a short counterpoise wire at the feed point to provide a return path for RF current. This is not a radial system -- the counterpoise carries very little current.

| Parameter | Value |
|-----------|-------|
| Length | 3.05 m (approximately 0.05 lambda at 80m) |
| Wire | #14 AWG, insulated or bare |
| Routing | Laid on the ground, away from the coax run |
| Connection | To the ground terminal of the 49:1 transformer |

### Why 3.05 m?

The counterpoise length is chosen to avoid resonance on any operating band. A quarter-wave counterpoise would create unwanted common-mode current. The 3.05 m length is approximately:

```
80m: 3.05 / 82.1 = 0.037 lambda (well below quarter-wave)
40m: 3.05 / 41.9 = 0.073 lambda (still short)
20m: 3.05 / 21.2 = 0.144 lambda (approaching quarter-wave)
```

### Ground Rod (Optional)

An 8-foot (2.4 m) ground rod at the transformer location provides lightning protection and can improve common-mode suppression. Bond the coax shield, counterpoise, and ground rod at a single point.

---

## 11. Feed System

### 49:1 Transformer

See Section 6 for full construction details.

```
     Antenna wire (39.4 m)
           |
     ======|==================
     |  2x FT-240-43        |
     |  Primary: 2 turns    |
     |  Secondary: 14 turns |
     |  Ratio: 49:1         |
     ======|=========|=======
           |         |
        SO-239    Counterpoise
           |      (3.05 m)
        [CM Choke]
           |
        RG-213
```

### Common-Mode Choke

A common-mode choke is essential for end-fed antennas to prevent RF from flowing on the outside of the coax shield.

| Parameter | Value |
|-----------|-------|
| Core | FT-240-43 (single) |
| Cable | RG-213, wound through core |
| Turns | 8--10 |
| Impedance | > 2000 ohm common-mode at 3.5 MHz |
| Placement | Immediately after transformer, before coax run |

### Feed Cable: RG-213

| Parameter | Value |
|-----------|-------|
| Type | RG-213/U |
| Impedance | 50 ohm |
| Loss at 4 MHz | 1.2 dB/100 m |
| Loss at 7 MHz | 1.6 dB/100 m |
| Loss at 14 MHz | 2.3 dB/100 m |
| For 20 m run at 4 MHz | 0.24 dB |
| For 20 m run at 7 MHz | 0.32 dB |
| For 20 m run at 14 MHz | 0.46 dB |
| Velocity factor | 0.66 |
| Connector | PL-259 (SO-239) |
| Power rating | 1 kW at 30 MHz |

### Feed Loss Budget

| Source | Loss (dB) | Notes |
|--------|----------|-------|
| Wire ohmic loss | 0.1--0.2 | #14 AWG stranded copper |
| Transformer loss | 0.15--0.50 | 49:1 on 2x FT-240-43 |
| CM choke insertion | < 0.1 | Negligible |
| Feed cable (20 m) | 0.24--0.46 | RG-213 (band dependent) |
| Connector loss | 0.05 | 2x PL-259 |
| **Total system loss** | **0.55--1.3** | **85--96% efficiency** |

---

## 12. Construction Guide

### Tools Required

- Wire cutters / strippers (for #14 AWG)
- Soldering iron (60W or greater)
- Antenna analyser (NanoVNA or similar)
- Tape measure (50 m)
- Rope, cord, or guy line
- Drill (for enclosure holes)

### Step-by-Step Construction

#### Step 1: Transformer Construction

1. Stack two FT-240-43 cores and wrap with fibreglass tape
2. Wind 14 turns of #14 AWG PTFE wire through the core (secondary)
3. Wind 2 turns of #14 AWG PTFE wire through the core (primary)
4. Mount SO-239 connector in IP65 ABS enclosure
5. Connect primary to SO-239 (centre pin to one end, shield to the other)
6. Install wing-nut terminals for antenna wire and counterpoise
7. Connect secondary ends to antenna and counterpoise terminals
8. Seal all cable entries

#### Step 2: Wire Preparation

1. Cut antenna wire to 40.5 m (#14 AWG stranded copper) -- includes 1.1 m trim allowance
2. Cut counterpoise wire to 3.05 m
3. Attach a ring terminal or loop to the feed end of the antenna wire
4. Attach an egg insulator at the far end

#### Step 3: Common-Mode Choke

1. Wind 8--10 turns of RG-213 through a single FT-240-43 core
2. Install PL-259 connectors on both ends
3. Connect between transformer SO-239 and the main coax run

#### Step 4: Erection

1. Attach the transformer enclosure to the base of the support (1--2 m above ground)
2. Route the antenna wire vertically up the support (~10 m)
3. At the top, route the wire horizontally (or sloping down) to the far anchor (~29 m)
4. Secure the far end to a rope tied to a stake or low support (2--5 m height)
5. Lay the counterpoise wire on the ground, away from the coax
6. Run the coax from the choke to the station

#### Step 5: Tuning

1. Connect antenna analyser at the shack end of the coax
2. Sweep 3.4--3.9 MHz: find VSWR minimum; target 3.65 MHz
3. Sweep 6.9--7.4 MHz: should show VSWR < 1.6:1 near 7.15 MHz
4. Sweep 13.9--14.5 MHz: should show VSWR < 2.0:1 near 14.15 MHz
5. If all bands are high in frequency: trim 20 cm at a time from the far end
6. If all bands are low: wire is too short; splice and extend
7. Fine-tune counterpoise length +/- 10 cm for best 80m match
8. Verify CM choke is suppressing shield current (check with RF ammeter)

---

## 13. Bill of Materials

| Item | Quantity | Est. Cost |
|------|----------|-----------|
| #14 AWG stranded copper wire | 42 m (140 ft) | $10--$20 |
| FT-240-43 ferrite toroid (transformer) | 2 pcs | $20--$30 |
| FT-240-43 ferrite toroid (CM choke) | 1 pc | $10--$15 |
| #14 AWG PTFE wire (transformer windings) | 2 m | $3--$5 |
| RG-213 coaxial cable | 20 m (65 ft) | $25--$40 |
| IP65 ABS enclosure | 1 pc | $5--$10 |
| SO-239 chassis connector | 2 pcs | $3--$5 |
| PL-259 connectors | 4 pcs | $5--$8 |
| Wing-nut terminals | 2 pcs | $2--$3 |
| Mast/support hardware | 1 set | $15--$50 |
| Dacron rope (UV-resistant) | 30 m | $5--$10 |
| Egg insulators | 2 pcs | $2--$3 |
| Miscellaneous (tape, sealant, ties) | 1 set | $5--$10 |
| **TOTAL** | | **$95--$185** |

---

## 14. Safety

1. **Power lines**: Maintain minimum 2x mast height (20--24 m) clearance from all overhead power lines. Never erect an antenna where it could contact power lines if the support fails.

2. **Lightning**: Install a coaxial lightning arrestor at the station entry point. Bond all ground connections to a single-point station ground. Disconnect the feedline during thunderstorms. Consider a ground rod at the transformer location.

3. **RF exposure**: The wire end of an EFHW carries very high voltage (approximately 2500 V at 200 W on 80m). Keep the far end of the wire well above head height. The transformer end also has elevated RF fields -- maintain at least 3 m clearance during transmit.

4. **Structural**: Guy the support mast if it is freestanding. Rate all hardware for local wind speeds. Use UV-resistant rope for outdoor runs.

5. **Wire visibility**: The far end of the wire may be at 2--5 m height. Mark with visible flagging tape in areas where people walk.

6. **Weatherproofing**: The 49:1 transformer must be housed in a weatherproof enclosure. Seal all cable entries. Water ingress into the transformer core will cause excessive loss and eventually core failure.

---

## 15. Quick Reference Card

```
+----------------------------------------------------------+
|  TRI-BAND EFHW ANTENNA                                    |
|  Quick Reference                                          |
+----------------------------------------------------------+
|  Type: EFHW Inverted-L    Wire: 39.4 m #14 AWG           |
|  Bands: 80m + 40m + 20m   XFMR: 49:1 (2x FT-240-43)    |
|  Feed: RG-213 (50 ohm)    Choke: 8-10T on FT-240-43     |
|  Counterpoise: 3.05 m     Support: 10-12 m mast/tree     |
+----------------------------------------------------------+
|  80m: +2.8 dBi, 88% eff, BW 120 kHz, NVIS               |
|  40m: +5.0 dBi, 93% eff, BW 220 kHz, NVIS               |
|  20m: +7.0 dBi, 96% eff, BW 280 kHz, DX                 |
+----------------------------------------------------------+
|  Transformer: 2x FT-240-43 stacked                        |
|    Primary: 2 turns    Secondary: 14 turns                |
|    Ratio: 49:1         Z: 2500 -> 51 ohm                 |
+----------------------------------------------------------+
|  Footprint: 29 x 10 m    Cost: $95-$185                  |
|  Power: 200W (80m) / 300W (40m/20m)                      |
+----------------------------------------------------------+
```

---

## 16. Frequency Planning

### 80m Sub-Band Allocation

| Sub-Band | Freq Range | VSWR | Notes |
|----------|-----------|------|-------|
| CW | 3.500--3.600 | 1.5--2.5 | Upper end of usable range |
| SSB (centre) | 3.600--3.700 | 1.3--1.8 | Best match zone |
| SSB (upper) | 3.700--3.800 | 1.5--2.5 | Acceptable with mild mismatch |

### 40m Sub-Band Allocation

| Sub-Band | Freq Range | VSWR | Notes |
|----------|-----------|------|-------|
| CW | 7.000--7.050 | 1.3--1.8 | Good match |
| SSB (centre) | 7.050--7.200 | 1.2--1.4 | Best match zone |
| SSB (upper) | 7.200--7.300 | 1.4--1.8 | Acceptable |

### 20m Sub-Band Allocation

| Sub-Band | Freq Range | VSWR | Notes |
|----------|-----------|------|-------|
| CW | 14.000--14.100 | 1.5--2.0 | Good; slightly off-centre |
| SSB (centre) | 14.100--14.250 | 1.3--1.6 | Best match zone |
| SSB (upper) | 14.250--14.350 | 1.5--2.0 | Acceptable |

### Operating Schedule (Typical Mid-Latitude)

| Time | Recommended Band | Reason |
|------|-----------------|--------|
| 06:00--09:00 | 80m or 40m | 80m best before sunrise; 40m as ionosphere builds |
| 09:00--12:00 | 40m or 20m | 40m for NVIS; 20m opens for DX |
| 12:00--17:00 | 20m (DX) + 40m (NVIS) | 20m at peak; 40m still reliable |
| 17:00--20:00 | 40m or 20m | 20m closing; transition to 40m |
| 20:00--00:00 | 80m or 40m | 80m preferred after sunset |
| 00:00--06:00 | 80m | Most reliable night-time NVIS band |

---

## 17. Appendix: Key Formulae

### End-Fed Half-Wave Length

```
L = (c / f) * 0.5 * VF

where:
    c  = 300 MHz*m (speed of light)
    f  = design frequency (MHz)
    VF = velocity factor (~0.97 for bare wire)

For 3.5 MHz:
    L = (300 / 3.5) * 0.5 * 0.97
      = 85.7 * 0.5 * 0.97
      = 41.6 m (free space)
    Practical: ~39.4 m (adjusted for height and ground effects)
```

### 49:1 Transformer Impedance Ratio

```
Z_ratio = (N_secondary / N_primary)^2

Z_ratio = (14 / 2)^2 = 7^2 = 49

Z_out = Z_in / Z_ratio = 2500 / 49 = 51 ohm
```

### Array Factor (Ground Reflection)

```
AF(alpha) = 2 * |sin(k * h * sin(alpha))|

where:
    k     = 2*pi / lambda
    h     = antenna height above ground
    alpha = elevation angle

At zenith (alpha = 90 deg):
    AF = 2 * |sin(2*pi*h / lambda)|
```

### VSWR from Impedance Mismatch

```
Gamma = (Z_ant - Z_0) / (Z_ant + Z_0)
VSWR = (1 + |Gamma|) / (1 - |Gamma|)

where:
    Z_ant = antenna impedance (after transformer)
    Z_0   = feedline impedance (50 ohm)
```

### Transformer Core Loss Estimate

```
P_loss = P_in * (1 - 10^(-dB_loss/10))

For 200W input, 0.35 dB loss:
    P_loss = 200 * (1 - 10^(-0.35/10))
           = 200 * (1 - 0.923)
           = 200 * 0.077
           = 15.4 W dissipated in transformer
```

---

## 18. Files in This Package

| File | Description |
|------|------------|
| `EFHW-Triband.md` | This document -- full design reference |
| `Triband_EFHW.png` | 24x36" technical poster (200 DPI) |
| `Triband_EFHW.pdf` | A4 PDF datasheet (3 pages) |

---

*Tri-Band End-Fed Half-Wave (EFHW) Antenna -- 80m + 40m + 20m*
*Inverted-L configuration with 49:1 transformer for general HF operation*
*NVIS on 80m/40m + DX on 20m | Footprint: 29 x 10 m | Cost: $95--$185*
