# Small-Size NVIS Fan Dipole

## 80m + 40m Dual-Band | Center-Loaded Compact Design

---

## 1. Design Objective

This antenna minimises physical footprint while maintaining dual-band 80m/40m NVIS capability. Center-loading coils allow 50% element shortening, reducing the span from 39 m (full-size) to just 19 m -- fitting easily on a suburban lot. A lightweight 8 m push-up mast and #14 AWG stranded wire keep the system portable and affordable.

### Target Applications

- Suburban amateur radio operators with limited space
- Portable/field NVIS deployment (EMCOMM, ARES/RACES)
- Emergency preparedness stations on small lots
- First HF antenna for new operators on a budget
- Camping/field day operations with push-up mast

### Design Philosophy

> Prioritise smallest footprint and lowest cost while still achieving usable NVIS coverage on both bands. Accept reduced efficiency and bandwidth as trade-offs for compactness.

---

## 2. System Overview

```
                       Apex: 8 m
                         /|\
                        / | \
                  80m  /  |  \  80m
                 elem /   |   \ elem
                     / [COIL]  \
               4.6m /     |     \ 4.6m
                   /  40m |40m   \
                  / elem [C]elem  \
            6.3m /       |||       \ 6.3m
                /        |||        \
   ============/=========|||=========\============  Ground
   <-- 9.4m -->    <-- 9.4m -->
   <---------- 18.8m (80m span) ---------->

   Included angle: 140 deg (20 deg droop each side)
   [COIL] = Center-loading coil (at midpoint of each half-element)

   Ground screen: 4 x 4 m mesh + 8 radials x 5 m
   ================================================
```

### Feed System

```
     Antenna Elements
           |
     [Single FT-240-43 Balun]
           |
     RG-58 Coax (50 ohm)
           |
     [Transceiver / Tuner]

     Note: Antenna tuner RECOMMENDED, especially on 80m
```

---

## 3. Physical Specifications

| Parameter | Value |
|-----------|-------|
| Type | Inverted-V fan dipole (dual-band, center-loaded) |
| Bands | 80 m (3.5--3.8 MHz) + 40 m (7.0--7.3 MHz) |
| Apex height | 8 m |
| Included angle | 140 deg |
| Droop angle | 20 deg from horizontal |
| 80m element length | 2 x 10.0 m = 20.0 m total (50% shortened) |
| 40m element length | 2 x 5.0 m = 10.0 m total (50% shortened) |
| 80m horizontal span | 18.8 m |
| 40m horizontal span | 9.4 m |
| 80m wire-end height | 4.6 m |
| 40m wire-end height | 6.3 m |
| Wire gauge | #14 AWG (1.63 mm diameter) |
| Wire type | Stranded copper |
| Loading coils | 4 x air-wound on PVC formers |
| Feed impedance | ~50 ohm (at band center) |
| Feed cable | RG-58, 50 ohm |
| Balun | Single FT-240-43 (1:1 current) |
| Power handling | 500 W PEP |
| Ground screen | 4 x 4 m galvanised mesh |
| Radials | 8 x 5 m, 45 deg spacing |
| Overall footprint | 19 x 8 m |

---

## 4. Performance Summary

| Freq (MHz) | Gain (dBi) | Efficiency (%) | VSWR | Bandwidth (kHz) | h/lambda |
|------------|-----------|----------------|------|-----------------|----------|
| 3.500 | +1.8 | 70 | 1.8 | 45 | 0.093 |
| 3.650 | +2.5 | 75 | 1.3 | 50 | 0.097 |
| 3.800 | +2.8 | 77 | 2.0 | 50 | 0.101 |
| 7.000 | +5.0 | 83 | 1.5 | 80 | 0.187 |
| 7.150 | +5.5 | 86 | 1.2 | 90 | 0.191 |
| 7.300 | +5.8 | 86 | 1.6 | 90 | 0.195 |

### Performance Highlights

- **80m band**: +2.5 dBi peak gain at zenith, 75% efficiency, ~50 kHz usable bandwidth
- **40m band**: +5.5 dBi peak gain at zenith, 86% efficiency, ~90 kHz usable bandwidth
- **VSWR**: < 2.0:1 at band centres; rises toward band edges
- **Coverage**: 0--250 km NVIS footprint
- **Antenna tuner recommended** for 80m full-band coverage (only ~50 kHz native BW)
- **40m usable without tuner** for most of the band

---

## 5. Loading Coil Theory

### Why Center Loading?

A half-wave dipole for 80m requires ~40 m of wire (20 m each side). By inserting inductors (loading coils) at the center of each half-element, we can electrically lengthen a physically shorter wire to resonate at the same frequency. Center loading offers the best compromise between size reduction and efficiency loss.

### Loading Coil Positions

Loading coils are placed at the **midpoint** of each half-element:

```
Feedpoint --- 5.0 m wire --- [80m COIL] --- 5.0 m wire --- Tip
Feedpoint --- 2.5 m wire --- [40m COIL] --- 2.5 m wire --- Tip
```

Center loading requires more inductance than base loading but distributes current more uniformly along the remaining wire, preserving more radiation efficiency.

### Required Inductance

The inductance needed to compensate for the missing wire length:

```
80m: Full half-element = 20.0 m, shortened to 10.0 m (50%)
     Required L ≈ 30 µH (compensates for 10 m missing wire)

40m: Full half-element = 10.0 m, shortened to 5.0 m (50%)
     Required L ≈ 8 µH (compensates for 5 m missing wire)
```

### Coil Q and Efficiency Impact

Loading coil loss is the dominant efficiency reduction in this design:

```
Coil loss resistance: R_loss = 2*pi*f*L / Q

80m (3.65 MHz, 30 µH, Q=200):
  R_loss = 2*pi * 3.65e6 * 30e-6 / 200 = 3.44 ohm per coil
  Two coils: 6.88 ohm
  With radiation resistance ~25 ohm (shortened dipole):
  Efficiency = 25 / (25 + 6.88) = 78%

40m (7.15 MHz, 8 µH, Q=250):
  R_loss = 2*pi * 7.15e6 * 8e-6 / 250 = 1.44 ohm per coil
  Two coils: 2.88 ohm
  With radiation resistance ~35 ohm:
  Efficiency = 35 / (35 + 2.88) = 92% (wire: ~86% system)
```

Higher coil Q directly improves efficiency. Air-wound coils on PVC achieve Q of 150--300.

---

## 6. Loading Coil Construction

### 80m Loading Coils (2 required)

| Parameter | Value |
|-----------|-------|
| Inductance | ~30 µH |
| Former | 50 mm (2 inch) PVC pipe |
| Wire | #14 AWG enamelled copper |
| Turns | 35 close-wound |
| Coil length | ~55 mm |
| Estimated Q | 200 |
| Position | Center of each 80m half-element (5 m from feedpoint) |

### 40m Loading Coils (2 required)

| Parameter | Value |
|-----------|-------|
| Inductance | ~8 µH |
| Former | 40 mm (1.5 inch) PVC pipe |
| Wire | #14 AWG enamelled copper |
| Turns | 18 close-wound |
| Coil length | ~30 mm |
| Estimated Q | 250 |
| Position | Center of each 40m half-element (2.5 m from feedpoint) |

### Construction Steps

1. Cut PVC pipe to length (80mm for 80m coils, 60mm for 40m coils -- allow 10mm margin each end)
2. Drill small holes at each end for wire feed-through
3. Wind specified turns close-wound (turns touching, no spacing)
4. Thread antenna wire through end holes and solder to coil wire ends
5. Secure winding with a thin layer of clear lacquer or super glue
6. Weatherproof the assembly with self-amalgamating tape or heat shrink over the entire coil
7. Attach to antenna wire with strain relief (cable ties through additional holes)

### Coil Tuning

The calculated turn counts are starting points. Final adjustment is done with an antenna analyser:

- **Too high in frequency**: Add 1--2 turns (increases L, lowers resonance)
- **Too low in frequency**: Remove 1 turn or spread turns slightly (decreases L)
- **Fine tuning**: Adjust element tip lengths ±10 cm

---

## 7. Physics and Array Factor

### Height-to-Wavelength Ratios

| Band | Centre Freq | Wavelength | h/lambda | Array Factor |
|------|------------|------------|----------|-------------|
| 80 m | 3.650 MHz | 82.1 m | 0.097 | 1.17 |
| 40 m | 7.150 MHz | 41.9 m | 0.191 | 1.72 |

### Array Factor Calculation

The ground reflection doubles the vertical pattern:

```
AF(alpha) = 2 * |sin(k * h * sin(alpha))|

where:
    k     = 2*pi / lambda
    h     = antenna height (8 m)
    alpha = elevation angle
```

At zenith (alpha = 90 deg):

- **80m**: AF = 2 * |sin(2*pi * 8 / 82.1)| = 2 * 0.584 = 1.17
- **40m**: AF = 2 * |sin(2*pi * 8 / 41.9)| = 2 * 0.862 = 1.72

The low h/lambda on 80m significantly reduces the array factor gain, which is the main reason for lower 80m performance compared to the full-size design.

### Wire End Heights

```
End height = Apex - L_half * sin(droop_angle)

80m: 8 - 10.0 * sin(20 deg) = 8 - 3.42 = 4.6 m
40m: 8 -  5.0 * sin(20 deg) = 8 - 1.71 = 6.3 m
```

### Horizontal Span

```
Span = 2 * L_half * cos(droop_angle)

80m: 2 * 10.0 * cos(20 deg) = 2 * 9.40  = 18.8 m
40m: 2 *  5.0 * cos(20 deg) = 2 * 4.70  =  9.4 m
```

---

## 8. Radiation Patterns

### 3D Pattern Characteristics

Both bands produce upward (zenith-directed) radiation lobes for NVIS, but with reduced gain compared to the full-size design:

- **80m (3.65 MHz)**: Broad lobe peaking near zenith, +2.5 dBi. The very low h/lambda = 0.097 produces a wide, low-gain pattern. The shortened elements and loading coils further reduce peak gain by ~4.5 dB compared to the efficient design.

- **40m (7.15 MHz)**: Stronger lobe peaking at zenith, +5.5 dBi. The h/lambda = 0.191 is closer to optimal. Performance is only ~2.3 dB below the full-size design, making 40m the stronger band for this antenna.

### Elevation Pattern

- 80m: Peak near zenith, 3 dB beamwidth approximately 90 deg (very broad)
- 40m: Peak at zenith, 3 dB beamwidth approximately 60 deg
- Both bands have nulls at the horizon

### Bandwidth Limitation

The center-loading coils store energy in reactive fields, which dramatically narrows the operating bandwidth:

- **80m**: Only ~50 kHz between 2:1 VSWR points (vs 180 kHz full-size)
- **40m**: ~90 kHz between 2:1 VSWR points (vs 240 kHz full-size)

An antenna tuner is **strongly recommended**, especially on 80m, to cover the full amateur allocation.

---

## 9. Comparison with Efficient Design

| Parameter | Efficient (full-size) | Small-Size (this design) | Trade-off |
|-----------|----------------------|--------------------------|-----------|
| Apex height | 12 m | 8 m | Shorter mast, easier to erect |
| Included angle | 160 deg | 140 deg | Steeper droop = smaller footprint |
| 80m half-element | 20 m (full) | 10 m (50% shortened) | Loading coils compensate |
| 40m half-element | 10 m (full) | 5 m (50% shortened) | Loading coils compensate |
| Wire gauge | #10 AWG hard-drawn | #14 AWG stranded | Lighter, more flexible |
| Loading coils | None | 4 x air-wound PVC | Key size enabler |
| Ground screen | 10x10 m + 20 radials | 4x4 m + 8 radials x 5 m | Minimal ground |
| Balun | Triple-core FT-240-43 | Single FT-240-43 | 500 W sufficient |
| Feed cable | LMR-400 | RG-58 | Lightweight, portable |
| 80m gain | +7.0 dBi | +2.5 dBi | -4.5 dB (significant) |
| 40m gain | +7.8 dBi | +5.5 dBi | -2.3 dB (moderate) |
| Efficiency | 97--99% | 72--86% | Coil Q limits |
| 80m bandwidth | 180 kHz | 50 kHz | Tuner needed |
| 40m bandwidth | 240 kHz | 90 kHz | Mostly OK |
| Coverage | 0--500 km | 0--250 km | Reduced gain |
| Footprint | 39 x 12 m | 19 x 8 m | ~60% reduction |
| Cost | $280--$450 | $80--$150 | ~70% savings |

### What You Gain

1. **60% smaller footprint** (19 x 8 m vs 39 x 12 m)
2. **70% lower cost** ($80--$150 vs $280--$450)
3. **Portable capability** (lighter wire, shorter mast, RG-58)
4. **Easier installation** (one person can erect 8 m mast)
5. **Suburban-friendly** (fits on typical residential lot)

### What You Give Up

1. **4.5 dB on 80m** (equivalent to ~3x power difference)
2. **2.3 dB on 40m** (equivalent to ~1.7x power difference)
3. **Narrow bandwidth** (tuner required for full-band 80m)
4. **Reduced coverage** (250 km vs 500 km reliable range)
5. **Lower power handling** (500 W vs 1.5 kW)

---

## 10. Ground System Design

### Ground Screen

- **Mesh**: 4 x 4 m galvanised welded wire mesh
- **Mesh spacing**: 5 cm (2 inch) openings
- **Placement**: Centred directly under the mast, on or just below ground surface
- **Bonding**: Bond mesh panels with copper strap at overlaps

### Radial System

- **Number**: 8 radials
- **Length**: 5 m each
- **Spacing**: 45 deg (360 / 8)
- **Wire**: #14 AWG bare copper
- **Total radial wire**: 40 m
- **Connection**: All radials bonded to mesh at centre, tied to coax shield

### Ground System Notes

The minimal ground system is a deliberate trade-off for portability. Ground loss is higher than the full-size design, contributing to the overall efficiency reduction. For a permanent installation, expanding to 8 x 8 m mesh with 12--16 radials at 10 m would recover 1--2 dB.

---

## 11. Feed System

### Balun: Single FT-240-43

```
     Antenna terminals
           |   |
     ======|===|======
     |  FT-240-43    |
     |  12 bifilar   |    Single core
     |  turns        |
     ======|===|======
           |   |
     Coax centre / shield
```

**Specifications:**

| Parameter | Value |
|-----------|-------|
| Core material | Fair-Rite 43 (NiZn ferrite) |
| Core size | FT-240-43 (61 mm OD) |
| Number of cores | 1 |
| Winding | 12 turns bifilar |
| Type | 1:1 current balun |
| Impedance | > 1500 ohm common-mode at 3.5 MHz |
| Power rating | 500 W PEP |
| Insertion loss | < 0.1 dB |

### Feed Cable: RG-58

| Parameter | Value |
|-----------|-------|
| Type | RG-58/U or RG-58C/U |
| Impedance | 50 ohm |
| Loss at 4 MHz | 2.2 dB/100 m |
| Loss at 7 MHz | 2.9 dB/100 m |
| For 15 m run at 4 MHz | 0.33 dB |
| For 15 m run at 7 MHz | 0.44 dB |
| Velocity factor | 0.66 |
| Connector | PL-259 (SO-239) |
| Power rating | 500 W at 10 MHz |

### Feed Loss Budget

| Source | Loss (dB) | Notes |
|--------|----------|-------|
| Wire ohmic loss | 0.1--0.2 | #14 AWG stranded copper |
| Loading coil loss | 0.8--1.5 | Dominant loss source (Q=200-250) |
| Balun insertion loss | < 0.1 | Single FT-240-43 |
| Feed cable (15 m) | 0.33--0.44 | RG-58 |
| Connector loss | 0.05 | 2 x PL-259 |
| Ground system loss | 0.2--0.5 | Minimal ground screen |
| **Total system loss** | **1.6--2.8** | **72--86% efficiency** |

---

## 12. NVIS Coverage Geometry

### Coverage vs Elevation Angle

| Elevation Angle | Single-hop Range | Signal Level |
|----------------|-----------------|-------------|
| 90 deg (zenith) | 0 km (overhead) | Maximum |
| 80 deg | ~45 km | Strong |
| 70 deg | ~90 km | Good |
| 60 deg | ~145 km | Good |
| 50 deg | ~210 km | Moderate |
| 40 deg | ~250 km | Weak/usable |

### Day/Night Performance

- **Daytime (80m)**: Coverage 0--150 km, moderate absorption limits range
- **Daytime (40m)**: Coverage 0--250 km, better D-layer penetration
- **Night-time (80m)**: Coverage 0--250 km, reduced absorption, best 80m window
- **Night-time (40m)**: F-layer may be too high; 80m preferred after sunset

---

## 13. Construction Guide

### Tools Required

- Wire cutters / strippers (for #14 AWG)
- Soldering iron (40W or greater)
- Antenna analyser (NanoVNA or similar)
- Tape measure (25 m)
- Rope, cord, or guy line
- PVC pipe cutter or hacksaw

### Step-by-Step Construction

#### Step 1: Loading Coil Preparation

1. Cut PVC pipe sections: 2 x 80 mm (50 mm diameter) and 2 x 60 mm (40 mm diameter)
2. Drill 2 mm holes at each end for wire feed-through
3. Wind 80m coils: 35 turns #14 AWG enamelled on 50 mm PVC
4. Wind 40m coils: 18 turns #14 AWG enamelled on 40 mm PVC
5. Secure windings with clear lacquer; weatherproof with self-amalgamating tape

#### Step 2: Wire Preparation

1. Cut two 80m half-elements: 10.0 m each, #14 AWG stranded
2. Cut two 40m half-elements: 5.0 m each, #14 AWG stranded
3. Mark the center point of each wire (5.0 m and 2.5 m)
4. Cut each wire at center point to insert loading coil
5. Solder wire ends to loading coil connections
6. Attach egg insulators at the far ends

#### Step 3: Balun Winding

1. Wind 12 bifilar turns on single FT-240-43 core using #14 AWG PTFE wire
2. Connect one pair of ends to antenna terminals
3. Connect the other pair to SO-239 chassis connector
4. Weatherproof with marine sealant

#### Step 4: Feedpoint Assembly

1. Solder 80m elements to balun output (one per terminal)
2. Solder 40m elements parallel to 80m (same terminals)
3. Separate band elements by ~3 cm at feedpoint using a small spreader
4. Seal all joints with self-amalgamating tape

#### Step 5: Ground System

1. Lay 4 x 4 m galvanised mesh under mast location
2. Lay 8 radials at 45 deg intervals from centre, 5 m each
3. Bond all radials to mesh at centre point
4. Connect to coax shield at base of mast

#### Step 6: Mast and Erection

1. Attach balun/feedpoint to mast at 8 m height
2. Run RG-58 down the mast (secure with cable ties)
3. Route 80m and 40m elements to support points
4. Adjust element angles for 140 deg included angle
5. Guy mast at 4 m height if needed

#### Step 7: Tuning

1. Connect antenna analyser at shack end of RG-58
2. Sweep 3.4--3.9 MHz: target VSWR dip at 3.65 MHz
3. Sweep 6.9--7.4 MHz: target VSWR dip at 7.15 MHz
4. Adjust loading coil turns if needed (see Section 6)
5. Fine-tune element tip lengths ±10 cm
6. Verify with antenna tuner for full-band coverage on 80m

---

## 14. Bill of Materials

| Item | Quantity | Est. Cost |
|------|----------|-----------|
| #14 AWG stranded copper wire | 30 m (100 ft) | $10--$15 |
| RG-58 coaxial cable | 20 m (65 ft) | $10--$20 |
| FT-240-43 ferrite core | 1 pc | $10--$15 |
| Galvanised ground mesh (4x4 m) | 16 sq m | $10--$15 |
| #14 AWG bare copper (radials) | 40 m (130 ft) | $5--$8 |
| PVC pipe 50 mm (80m coil formers) | 2 x 10 cm | $2--$3 |
| PVC pipe 40 mm (40m coil formers) | 2 x 8 cm | $2--$3 |
| #14 AWG enamelled wire (coils) | 10 m | $3--$5 |
| Push-up mast (aluminium/fibreglass) | 8 m telescoping | $15--$30 |
| Insulators, connectors, hardware | 1 set | $10--$20 |
| PL-259 connectors | 2 pcs | $3--$5 |
| **TOTAL** | | **$80--$150** |

---

## 15. Safety Considerations

1. **Power lines**: Maintain minimum 2x mast height (16 m) clearance from overhead lines
2. **Lightning**: Install a lightning arrestor at the shack entry; ground the mast
3. **RF exposure**: At 500 W, maintain minimum 5 m distance from antenna during transmit
4. **Structural**: Guy the mast at ~4 m height; rate for local wind speeds
5. **Wire ends**: 80m wire ends are only 4.6 m high -- mark with visible flagging tape
6. **Loading coils**: Ensure weatherproofing to prevent water ingress and coil degradation

---

## 16. Quick Reference Card

```
+----------------------------------------------------------+
|  SMALL-SIZE NVIS FAN DIPOLE                               |
|  Quick Reference                                          |
+----------------------------------------------------------+
|  Apex: 8 m    Angle: 140 deg    Wire: #14 AWG stranded   |
|  80m span: 18.8 m    40m span: 9.4 m                     |
|  Feed: RG-58    Balun: 1x FT-240-43                      |
|  Loading: 4x air-wound PVC coils                          |
+----------------------------------------------------------+
|  80m: +2.5 dBi, 75% eff, BW ~50 kHz (TUNER NEEDED)      |
|  40m: +5.5 dBi, 86% eff, BW ~90 kHz                     |
+----------------------------------------------------------+
|  80m coils: ~30 uH, 35T on 50mm PVC                      |
|  40m coils: ~8 uH, 18T on 40mm PVC                       |
+----------------------------------------------------------+
|  Ground: 4x4 m mesh + 8 radials x 5 m                    |
|  Coverage: 0-250 km    Cost: $80-$150                     |
|  Footprint: 19 x 8 m (fits suburban lot)                  |
+----------------------------------------------------------+
```

---

## 17. Frequency Planning

### 80m Sub-Band Allocation (tuner recommended)

| Sub-Band | Freq Range | VSWR | Notes |
|----------|-----------|------|-------|
| CW | 3.500--3.600 | 1.5--2.5 | Tuner recommended |
| SSB (centre) | 3.600--3.700 | 1.3--1.5 | Best match zone |
| SSB (upper) | 3.700--3.800 | 1.5--2.5 | Tuner recommended |

### 40m Sub-Band Allocation

| Sub-Band | Freq Range | VSWR | Notes |
|----------|-----------|------|-------|
| CW | 7.000--7.050 | 1.3--1.8 | Good match |
| SSB (centre) | 7.050--7.200 | 1.2--1.4 | Best match zone |
| SSB (upper) | 7.200--7.300 | 1.4--1.8 | Acceptable |

---

## 18. Appendix: Loading Coil Formulae

### Single-Layer Air-Core Inductance (Wheeler's Formula)

```
L (µH) = (d^2 * N^2) / (18*d + 40*l)

where:
    d = coil diameter in inches
    N = number of turns
    l = coil length in inches
```

For the 80m coil (50 mm = 1.97 inch diameter, 35 turns, ~55 mm = 2.17 inch length):

```
L = (1.97^2 * 35^2) / (18 * 1.97 + 40 * 2.17)
  = (3.88 * 1225) / (35.46 + 86.8)
  = 4753 / 122.3
  = 38.9 µH (target ~30 µH; adjust to ~30 turns for 30 µH)
```

For the 40m coil (40 mm = 1.57 inch diameter, 18 turns, ~30 mm = 1.18 inch length):

```
L = (1.57^2 * 18^2) / (18 * 1.57 + 40 * 1.18)
  = (2.46 * 324) / (28.26 + 47.2)
  = 797 / 75.5
  = 10.6 µH (target ~8 µH; adjust to ~16 turns for 8 µH)
```

**Note**: These are starting points. Always verify and adjust with an antenna analyser.

### Coil Q Estimation

```
Q = X_L / R_AC

For air-wound coils on PVC formers:
  Q typically 150-300 at HF frequencies
  Higher Q with: larger wire, air-core, wider spacing
  Lower Q with: smaller wire, lossy formers, tight winding
```

---

## 19. Files in This Package

| File | Description |
|------|------------|
| `3-7Mhz-SmallSize.md` | This document -- full design reference |
| `Dualband_SmallSize.png` | 24x36" technical poster (200 DPI) |
| `Dualband_SmallSize.pdf` | A4 PDF datasheet (3 pages) |

---

*Small-Size NVIS Fan Dipole -- 80m + 40m Dual-Band Design*
*Center-loaded compact design for suburban lots and portable deployment*
*Footprint: 19 x 8 m | Cost: $80--$150 | Coverage: 0--250 km*
