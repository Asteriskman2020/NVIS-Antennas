# NVIS Dual-Band Fan Dipole Antenna: 3.5-7.3 MHz Balanced Design

> **Design Class:** Ground-up NVIS (Near-Vertical Incidence Skywave)
> **Antenna Type:** Dual-band fan dipole (inverted-V configuration)
> **Bands:** 80 m (3.500-3.800 MHz) and 40 m (7.000-7.300 MHz)
> **Apex Height:** 10.0 m | **Wire:** #14 AWG stranded copper
> **Coverage:** 0-500 km regional, peak radiation at zenith
> **Efficiency:** 95-97% on both bands

---

## Table of Contents

1. [Design Objective](#1-design-objective)
2. [Why Fan Dipole for NVIS](#2-why-fan-dipole-for-nvis)
3. [System Diagram](#3-system-diagram)
4. [Antenna Dimensions](#4-antenna-dimensions)
5. [Performance Tables](#5-performance-tables)
6. [3D Radiation Pattern](#6-3d-radiation-pattern)
7. [NVIS Configuration](#7-nvis-configuration)
8. [Height Optimisation](#8-height-optimisation)
9. [Link Budget](#9-link-budget)
10. [Balun and Feed System](#10-balun-and-feed-system)
11. [Construction Guide](#11-construction-guide)
12. [Ground Screen](#12-ground-screen)
13. [Safety](#13-safety)
14. [Comparison: Fan Dipole vs Magnetic Loop](#14-comparison-fan-dipole-vs-magnetic-loop)
15. [Bill of Materials](#15-bill-of-materials)
16. [Key Formulae](#16-key-formulae)
17. [Validation Checklist](#17-validation-checklist)
- [Appendix A: Quick Reference Card](#appendix-a-quick-reference-card)
- [Appendix B: NVIS Frequency Planning Guide](#appendix-b-nvis-frequency-planning-guide)

---

## 1. Design Objective

### 1.1 NVIS-First Design Philosophy

This antenna is designed **from the ground up** for Near-Vertical Incidence Skywave (NVIS) propagation. The dual-band fan dipole in inverted-V configuration provides reliable regional coverage from 0 to 500 km by launching signals at steep angles (45-90 degrees elevation) into the F2-layer ionosphere. Every parameter -- apex height, wire lengths, included angle, and feed system -- has been optimised for maximum radiation at zenith.

NVIS propagation exploits the F2-layer of the ionosphere (typically 250-350 km altitude) as a mirror for signals transmitted at high elevation angles. The signal travels nearly straight up, refracts back down, and illuminates a circular area centred on the transmitter. This provides reliable regional coverage immune to terrain shadowing, requires no line-of-sight, and fills the "skip zone" gap that plagues low-angle DX antennas.

### 1.2 The Balanced Approach

The fan dipole strikes a deliberate balance between performance, physical size, and practicality:

| Attribute | Choice | Rationale |
|-----------|--------|-----------|
| Type | Inverted-V fan dipole | Maximum NVIS gain with single-mast support |
| 80m efficiency | 95-96% | Near-lossless; wire antenna advantage |
| 40m efficiency | 96-97% | Near-lossless; excellent performance |
| Apex height | 10 m | Optimal for 40m NVIS; good for 80m |
| Wire span | ~40 m (80m) / ~20 m (40m) | Moderate footprint; fits many properties |
| Bandwidth | 150-210 kHz | Covers full sub-bands without retuning |
| Cost | $153-285 | Accessible to most amateur operators |
| Complexity | Low | Wire + rope + mast; no tuning capacitor |

### 1.3 Target Applications

- **Emergency communications (EMCOMM):** Reliable in-country or in-region coverage from a portable or fixed station.
- **Regional nets:** 80 m LSB and 40 m SSB nets covering a 200-500 km radius.
- **Military/NGO field deployment:** Deployable with minimal tools and materials.
- **Rural HF linking:** Connecting stations across mountainous or jungle terrain.
- **Amateur radio contesting (domestic):** Strong short-skip performance on 40 m and 80 m.
- **Base station NVIS:** Permanent installation for 24/7 regional HF coverage.

---

## 2. Why Fan Dipole for NVIS

### 2.1 The Inverted-V Advantage for NVIS

A horizontal dipole mounted below lambda/4 height produces maximum radiation at zenith -- exactly what NVIS requires. The inverted-V variant requires only a single centre support (mast or tree) and naturally produces a slightly broader NVIS pattern compared to a flat horizontal dipole.

At 10 m apex height:
- **80 m band:** h/lambda = 0.12, well below lambda/4. The ground reflection reinforces zenith radiation, producing a clean NVIS lobe.
- **40 m band:** h/lambda = 0.23, near the optimal lambda/4 point. Ground reinforcement is near-maximum, producing excellent NVIS gain.

### 2.2 Fan Dipole Multi-Band Capability

A fan dipole uses multiple dipole element pairs fed from a single feedpoint. Each pair resonates on its design frequency. The non-resonant elements present high impedance and draw minimal current, so interference between element pairs is small -- provided the wires are adequately spaced (30-50 cm near the feedpoint).

Advantages over other multi-band approaches:

| Approach | Pros | Cons |
|----------|------|------|
| Fan dipole | Simple, wideband, no traps, full efficiency | Requires multiple wires |
| Trapped dipole | Single wire, shorter span | Trap losses (1-3 dB), narrow bandwidth |
| Linked dipole | Full-size on each band | Must physically change links |
| Off-centre-fed dipole | Multi-band from single wire | VSWR issues, needs tuner |
| **This design** | **Full efficiency, wide BW, dual-band, simple** | **Needs 40 m span** |

### 2.3 Comparison with Magnetic Loop for NVIS

The fan dipole and magnetic loop represent opposite ends of the size-vs-efficiency trade-off:

| Property | Fan Dipole | Magnetic Loop (2 m) |
|----------|------------|---------------------|
| Footprint | 40 m span | 2 m diameter |
| 80m gain (NVIS) | +5.9 dBi | -8 to -7 dBi |
| 40m gain (NVIS) | +6.3 dBi | +0 to +1 dBi |
| Bandwidth | 150-210 kHz | 1.7-5 kHz |
| Efficiency | 95-97% | 8.5-55% |
| Noise rejection | Moderate | Excellent (deep nulls) |
| Stealth | Poor | Excellent |

**When to use each:** Use the fan dipole when space permits and maximum NVIS performance is the priority. Use the magnetic loop when space is severely limited, stealth is required, or noise rejection is more important than raw gain.

---

## 3. System Diagram

### 3.1 Overall NVIS Installation

```
                         N
                         ^
                         |
                    [Broadside]
                         |
     ============ NVIS Radiation Pattern ============

              * * * * * * * * * *          F2-layer (~300 km)
            *                     *
          *    Refracted signals     *
        *      return to Earth        *
      *              |                  *
               \     |     /
                 \   |   /        Coverage radius: 0-500 km
                   \ | /
                    \|/
                     |  <-- Zenith radiation (peak)
                     |
               80m   |   80m
              /      |      \
             /   40m | 40m   \
            /   /    |    \   \
           /   /     |     \   \
          /   /      |      \   \
         /   / Feedpoint     \   \
        /   /   (10 m)        \   \
       /   /     ||            \   \
      /   /      ||  1:1 Balun  \   \
     /   /       ||              \   \
    v   v        ||               v   v
  (80m end)   RG-213 coax     (80m end)
   ~3-5 m     to station       ~3-5 m
   height                      height

   Ground  ------||-------------------------------
   Level         ||
           [=====||=====]   6 m x 6 m ground screen
           [=====||=====]   (optional, +1-2 dB)
           [=====||=====]
                 ||
                 +--- RG-213 coax to station (50 ohm)
```

### 3.2 Plan View (Top Down)

```
                         N
                         |
                         |
         80m wire        |        80m wire
      <-- ~20 m -----[FEED]------ ~20 m -->
                        /|\
         40m wire      / | \      40m wire
      <-- ~10 m -----/  |  \---- ~10 m -->
                     /   |   \
                    /    |    \
                   /     |     \
                  /      |      \    30-50 cm spacing
                 /       |       \   near feedpoint
                /        |        \
               /         S         \
```

### 3.3 Side View (East-West Cross Section)

```
                    Feedpoint at 10 m
                        /|\
                       / | \     Apex angle ~120 deg
                      /  |  \
              40m    /   |   \    40m
              wire  /    |    \   wire
                   /  80m|80m  \
                  /  wire|wire  \
                 /       |       \
                /      Mast       \
               /     (10 m)        \
              v         |           v
    End height         |          End height
     ~3-5 m            |           ~3-5 m
    =========|=========|=========|==========  Ground
             |   Ground Screen   |
             +-------------------+
                     6 x 6 m
```

### 3.4 Feedpoint Detail

```
     80m wire (left) ----+---- 80m wire (right)
                          |
     40m wire (left) --+--+--+-- 40m wire (right)
                       |  |  |
                    30-50 cm spacing
                       (plastic spreader)
                          |
                    +-----+-----+
                    |   1:1     |   Weatherproof
                    |  Current  |   junction box
                    |   Balun   |
                    | (FT-240-43)|
                    +-----+-----+
                          |
                       SO-239
                          |
                       RG-213
                      to station
```

---

## 4. Antenna Dimensions

### 4.1 Element Lengths

The theoretical half-wave dipole length is shortened by approximately 5% to account for end effects:

```
L_half = (143 / f_MHz) metres   (each side of feedpoint)
```

| Band | Centre Freq (MHz) | lambda (m) | L_half (m) | Total Element (m) |
|------|-------------------|-----------|-----------|-------------------|
| 80 m | 3.650 | 82.13 | 19.59 | 39.18 |
| 40 m | 7.150 | 41.93 | 19.93* | 39.86* |

*Note: 40 m at 7.150 MHz gives L_half = 143/7.15 = 20.0 m theoretical. With inverted-V correction (multiply by 0.98): L_half ~ 19.6 m. However, the fan dipole interaction requires empirical trimming.

**Recommended starting lengths (before trimming):**

| Element | Each Side | Total | Trim Allowance |
|---------|-----------|-------|----------------|
| 80 m | 20.5 m | 41.0 m | +1.5 m (0.75 m each end) |
| 40 m | 10.3 m | 20.6 m | +0.6 m (0.3 m each end) |

### 4.2 Physical Configuration

| Parameter | Value |
|-----------|-------|
| Apex height | 10.0 m |
| Included angle | ~120 degrees |
| Wire end height (80 m) | ~3.0-4.0 m above ground |
| Wire end height (40 m) | ~5.5-6.5 m above ground |
| Horizontal span (80 m) | ~35 m |
| Horizontal span (40 m) | ~17 m |
| Wire spacing at feedpoint | 30-50 cm |
| Wire gauge | #14 AWG (1.63 mm diameter) |
| Wire type | Stranded copper (THHN or bare) |

### 4.3 Wire Selection

| Wire Type | Pros | Cons | Recommended |
|-----------|------|------|-------------|
| #14 AWG stranded copper | Flexible, low loss, affordable | Heavier, stretches | Yes (primary) |
| #14 AWG copper-clad steel | Strong, light, low stretch | Slightly higher loss | Yes (portable) |
| #12 AWG stranded copper | Very low loss, strong | Heavy, expensive | For permanent only |
| #18 AWG stranded copper | Very light, cheap | Higher loss, fragile | Emergency only |

---

## 5. Performance Tables

### 5.1 Complete Performance Table

| Parameter | 3.500 MHz | 3.650 MHz | 3.800 MHz | 7.000 MHz | 7.150 MHz | 7.300 MHz |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **Wavelength (m)** | 85.71 | 82.13 | 78.89 | 42.86 | 41.93 | 41.10 |
| **h/lambda** | 0.117 | 0.122 | 0.127 | 0.233 | 0.239 | 0.243 |
| **Gain (dBi, NVIS)** | +5.8 | +5.9 | +6.0 | +6.2 | +6.3 | +6.4 |
| **Efficiency (%)** | 95 | 95 | 96 | 96 | 97 | 97 |
| **VSWR** | 1.3:1 | 1.1:1 | 1.4:1 | 1.5:1 | 1.2:1 | 1.6:1 |
| **Bandwidth -3 dB (kHz)** | 150 | 160 | 160 | 200 | 210 | 210 |
| **Feed Z (ohm)** | ~45 | ~50 | ~48 | ~52 | ~50 | ~48 |
| **Take-off angle** | 90 deg | 90 deg | 90 deg | 90 deg | 90 deg | 90 deg |
| **-3 dB beamwidth** | 50-90 deg | 50-90 deg | 50-90 deg | 45-90 deg | 45-90 deg | 45-90 deg |
| **NVIS coverage (km)** | 0-400 | 0-400 | 0-400 | 0-500 | 0-500 | 0-500 |

### 5.2 Bandwidth

The fan dipole has inherently wide bandwidth because the full-size wire elements have low Q:

| Band | -2:1 SWR Bandwidth | Covers |
|------|---------------------|--------|
| 80 m | ~300 kHz | Full 3.5-3.8 MHz allocation |
| 40 m | ~400 kHz | Full 7.0-7.3 MHz allocation |

**No retuning is required** when changing frequency within either band. This is a major operational advantage over the narrow-band magnetic loop.

### 5.3 NVIS Elevation Pattern

The normalised elevation pattern in the broadside direction at 10 m apex height:

| Elevation | 80 m (3.65 MHz) | 80 m (dB) | 40 m (7.15 MHz) | 40 m (dB) |
|-----------|-----------------|-----------|-----------------|-----------|
| 90 deg (zenith) | 1.000 | 0.0 | 1.000 | 0.0 |
| 80 deg | 0.990 | -0.1 | 0.985 | -0.1 |
| 70 deg | 0.960 | -0.4 | 0.945 | -0.5 |
| 60 deg | 0.905 | -0.9 | 0.875 | -1.2 |
| 50 deg | 0.825 | -1.7 | 0.780 | -2.2 |
| 45 deg | 0.775 | -2.2 | 0.720 | -2.9 |
| 30 deg | 0.560 | -5.0 | 0.480 | -6.4 |
| 20 deg | 0.370 | -8.6 | 0.300 | -10.5 |
| 10 deg | 0.185 | -14.7 | 0.150 | -16.5 |
| 0 deg (horizon) | 0.000 | null | 0.000 | null |

---

## 6. 3D Radiation Pattern

### 6.1 Pattern Description

The 3D radiation pattern of the inverted-V fan dipole at 10 m height over ground shows:

1. **Primary lobe at zenith (90 degrees elevation):** Maximum radiation directed straight up, ideal for NVIS illumination of the F2-layer ionosphere.

2. **Broad -3 dB beamwidth:** The NVIS cone extends from approximately 45-50 degrees to 90 degrees elevation, covering ground distances from 0 to approximately 300-400 km.

3. **Horizon null:** Radiation at the horizon is zero (null), which suppresses interference to/from distant stations and concentrates power in the NVIS direction.

4. **Azimuthal pattern:** Broadside (perpendicular to wire axis) is slightly stronger than endfire (along wire axis) at intermediate elevation angles. The difference narrows as elevation approaches zenith.

### 6.2 Pattern Characteristics by Band

| Property | 80 m (3.65 MHz) | 40 m (7.15 MHz) |
|----------|-----------------|-----------------|
| Pattern peak | Zenith | Zenith |
| -3 dB beamwidth (elev.) | 50 deg - 90 deg | 45 deg - 90 deg |
| -6 dB beamwidth (elev.) | 30 deg - 90 deg | 25 deg - 90 deg |
| Array factor at zenith | 1.34 | 1.96 |
| Ground reinforcement | Moderate | Strong (near lambda/4) |
| Azimuthal variation at 70 deg | < 2 dB | < 3 dB |

### 6.3 Visualisation

The poster file `Dualband_Balanced.png` and PDF file `Dualband_Balanced.pdf` contain rendered 3D radiation patterns for both bands, showing the characteristic mushroom-shaped NVIS lobe directed at zenith with the ground plane visible below. The patterns were computed using:

- Inverted-V element factor (modified half-wave dipole with droop)
- Ground reflection (image theory, PEC ground model)
- Array factor: AF(alpha) = 2|sin(kh * sin(alpha))|

---

## 7. NVIS Configuration

### 7.1 Mounting Geometry

| Parameter | Value |
|-----------|-------|
| Configuration | Inverted-V (drooping dipole) |
| Wire orientation | Broadside perpendicular to wire axis |
| Recommended alignment | Wire axis N-S, broadside E-W |
| Apex height | 10.0 m above ground |
| Wire end height (80 m) | 3.0-4.0 m |
| Wire end height (40 m) | 5.5-6.5 m |
| Included angle at apex | ~120 degrees |
| Mast type | Fibreglass, timber, or rope-over-tree |

### 7.2 Height-to-Wavelength Ratios

| Band | Frequency | lambda (m) | h/lambda | kh (rad) | AF(zenith) |
|------|-----------|-----------|----------|----------|------------|
| 80 m | 3.500 MHz | 85.71 | 0.117 | 0.734 | 1.338 |
| 80 m | 3.650 MHz | 82.13 | 0.122 | 0.766 | 1.390 |
| 80 m | 3.800 MHz | 78.89 | 0.127 | 0.797 | 1.432 |
| 40 m | 7.000 MHz | 42.86 | 0.233 | 1.467 | 1.960 |
| 40 m | 7.150 MHz | 41.93 | 0.239 | 1.499 | 1.974 |
| 40 m | 7.300 MHz | 41.10 | 0.243 | 1.529 | 1.986 |

The 40 m band is near the optimal h/lambda = 0.25 (AF = 2.0), providing excellent ground reinforcement. The 80 m band, at h/lambda ~ 0.12, still has good NVIS gain with AF of 1.3-1.4.

### 7.3 NVIS Coverage Geometry

Assuming F2-layer reflection at 300 km altitude:

| Elevation Angle | Ground Radius (km) | Application |
|-----------------|---------------------|-------------|
| 90 deg (zenith) | 0 | Directly overhead |
| 80 deg | 53 | City-wide |
| 70 deg | 109 | Regional |
| 60 deg | 173 | Inter-city |
| 50 deg | 247 | Provincial |
| 45 deg | 300 | Extended regional |
| 30 deg | 520 | NVIS outer limit |

### 7.4 Broadside vs. Endfire

For an inverted-V aligned North-South:

- **Broadside (East-West):** Strongest radiation at all elevation angles. Place the broadside direction toward the primary coverage area.
- **Endfire (North-South):** Slightly weaker radiation at intermediate angles but still good for NVIS. The inverted-V droop reduces the endfire null compared to a flat dipole.

For maximum omnidirectional NVIS coverage, the distinction is small above 60 degrees elevation.

---

## 8. Height Optimisation

### 8.1 Height vs. Array Factor

| Height (m) | h/lambda (80 m) | AF (80 m) | h/lambda (40 m) | AF (40 m) | Notes |
|------------|-----------------|-----------|-----------------|-----------|-------|
| 5 | 0.058 | 0.72 | 0.117 | 1.34 | Minimum practical |
| 7 | 0.082 | 1.00 | 0.163 | 1.68 | Good for portable |
| 8 | 0.093 | 1.11 | 0.187 | 1.81 | Good dual-band |
| **10** | **0.117** | **1.34** | **0.234** | **1.96** | **Recommended** |
| 10.7 | 0.125 | 1.41 | 0.250 | 2.00 | Optimal for 40 m |
| 12 | 0.140 | 1.55 | 0.280 | 1.95 | 40 m past peak |
| 15 | 0.175 | 1.76 | 0.350 | 1.90 | 80 m climbing |
| 21.4 | 0.250 | 2.00 | 0.500 | 0.00 | Optimal 80 m; 40 m NULL |

### 8.2 Key Insight

The 10 m height is the sweet spot for dual-band operation:
- 40 m is near-optimal (AF = 1.96, just shy of 2.00 at 10.7 m)
- 80 m has good gain (AF = 1.34)
- Avoids the 21.4 m catastrophic point where 40 m has a zenith null
- Single 10 m mast is practical for one-person erection

---

## 9. Link Budget

### 9.1 40 m Band, 100 W, 300 km Path (Daytime)

| Parameter | Value | Unit |
|-----------|-------|------|
| Transmit power | 100 / +50.0 | W / dBm |
| TX antenna gain (NVIS) | +6.3 | dBi |
| EIRP | +56.3 | dBm |
| Free-space path loss | -125.0 | dB |
| Ionospheric absorption | -10.0 | dB |
| Polarisation mismatch | -1.0 | dB |
| Ground reflection loss | -2.0 | dB |
| RX antenna gain (NVIS) | +6.3 | dBi |
| **Received signal** | **-75.4** | **dBm** |
| Noise floor (40 m, 4 kHz) | -100.0 | dBm |
| **SNR** | **+24.6** | **dB** |

### 9.2 80 m Band, 100 W, 200 km Path (Night-time)

| Parameter | Value | Unit |
|-----------|-------|------|
| Transmit power | +50.0 | dBm |
| TX antenna gain (NVIS) | +5.9 | dBi |
| EIRP | +55.9 | dBm |
| Path loss | -120.0 | dB |
| Ionospheric absorption | -5.0 | dB |
| Ground reflection loss | -2.0 | dB |
| RX antenna gain (NVIS) | +5.9 | dBi |
| **Received signal** | **-65.2** | **dBm** |
| Noise floor (80 m, 4 kHz) | -90.0 | dBm |
| **SNR** | **+24.8** | **dB** |

### 9.3 Link Budget Summary

| Scenario | Band | Power | Distance | Est. SNR | Assessment |
|----------|------|-------|----------|----------|------------|
| 40 m, day | 40 m | 100 W | 300 km | +25 dB | Excellent |
| 40 m, day | 40 m | 100 W | 500 km | +18 dB | Very good |
| 80 m, night | 80 m | 100 W | 200 km | +25 dB | Excellent |
| 80 m, day | 80 m | 100 W | 200 km | +10 dB | Good |
| 40 m, day, QRP 5 W | 40 m | 5 W | 300 km | +12 dB | Good (SSB) |
| 80 m, night, QRP 5 W | 80 m | 5 W | 200 km | +12 dB | Good (SSB) |

The fan dipole provides dramatically better link margins than the magnetic loop, particularly on 80 m where the efficiency advantage is 10-12 dB.

---

## 10. Balun and Feed System

### 10.1 1:1 Current Balun

A current balun (choke balun) is essential to prevent common-mode currents on the feedline, which would distort the radiation pattern and increase noise pickup.

| Parameter | Value |
|-----------|-------|
| Type | 1:1 current balun (choke) |
| Core | FT-240-43 ferrite toroid |
| Winding | 10 bifilar turns |
| Wire | #14 AWG PTFE-insulated |
| Impedance | 50 ohm |
| Common-mode impedance | > 1000 ohm (3-8 MHz) |
| Power rating | 500 W continuous |

### 10.2 Construction

```
        FT-240-43 Toroid Core
         (OD 61 mm, ID 35 mm)

              ___________
             /    10     \
            /   bifilar   \
           |    turns      |
           |               |
            \    #14 AWG  /
             \___________/
                  |  |
          Wire A  |  |  Wire B
                  |  |
         +--------+  +--------+
         |                     |
     Antenna                 Antenna
     Side A                  Side B
     (80m+40m left)          (80m+40m right)
         |                     |
         +--------+  +--------+
                  |  |
              Feedline
             (RG-213)
```

### 10.3 Feedline

| Parameter | Recommendation |
|-----------|---------------|
| Type | RG-213 or LMR-400, 50 ohm |
| Length | 10-20 m typical |
| Connectors | PL-259 / SO-239 |
| Additional choke | 6 turns of feedline on FT-240-43 at station end |
| Grounding | Shield bonded to station ground at entry point |

---

## 11. Construction Guide

### 11.1 Materials Preparation

1. Cut wire elements with trim allowance:
   - 80 m: Two lengths of 20.5 m each
   - 40 m: Two lengths of 10.3 m each
   - Label each wire clearly (80L, 80R, 40L, 40R)

2. Prepare feedpoint hardware:
   - Wind 1:1 balun on FT-240-43 (10 bifilar turns)
   - Mount balun in weatherproof junction box
   - Install SO-239 connector on box

3. Prepare end hardware:
   - Attach egg or dog-bone insulators to each wire end
   - Prepare Dacron support rope (4 lengths, each 10-15 m)

### 11.2 Assembly

1. **Connect wires to balun:**
   - Solder 80L and 40L wires to one terminal
   - Solder 80R and 40R wires to the other terminal
   - Use ring lugs or direct solder connections
   - Verify continuity with multimeter

2. **Install wire spreaders:**
   - At 0.5 m from feedpoint: plastic cross-spreader (30-50 cm)
   - At 2 m from feedpoint: second spreader
   - Purpose: keep 80 m and 40 m wires separated to reduce coupling

3. **Erect the mast:**
   - Raise feedpoint to 10 m using fibreglass mast or rope-over-tree
   - The feedpoint should hang freely or be secured to the mast

4. **Deploy wires:**
   - Run each wire outward and downward at ~30-degree droop angle
   - Secure wire ends to ground stakes, trees, or fence posts
   - Use Dacron rope from insulators to anchor points
   - Wire ends should be 3-5 m above ground

### 11.3 Tuning and Trimming

1. **Connect antenna analyser** at the feedpoint (or at the end of the feedline)
2. **Check 40 m first** (trim shorter wires first):
   - Measure VSWR sweep across 6.8-7.5 MHz
   - Find the resonant frequency (lowest VSWR)
   - If resonance is below target: trim 2 cm from each 40 m wire end
   - If resonance is above target: add wire (fold back the excess)
   - Target: VSWR < 1.5:1 at 7.15 MHz
3. **Check 80 m:**
   - Measure VSWR sweep across 3.3-4.0 MHz
   - Trim if needed (usually less trimming required)
   - Target: VSWR < 1.5:1 at 3.65 MHz
4. **Recheck 40 m** after adjusting 80 m (usually no change)

---

## 12. Ground Screen

### 12.1 Purpose

An optional ground screen below the antenna improves NVIS performance by:
1. Improving ground reflectivity (closer to PEC behaviour)
2. Reducing ground absorption losses
3. Typical improvement: +1 to +2 dB in NVIS gain

### 12.2 Specifications

| Parameter | Primary Option | Alternative |
|-----------|---------------|-------------|
| Type | Chicken wire (poultry netting) | Radial wires |
| Dimensions | 6 m x 6 m | 8 radials, 10 m each |
| Material | Galvanised steel | #14 AWG copper |
| Placement | On ground, centred below feedpoint | On ground |
| Bonding | Connect to station ground | Connect to station ground |

### 12.3 Construction

For the chicken wire option:
1. Lay out a 6 x 6 m sheet centred below the feedpoint
2. Pin with landscape staples every 0.5 m around perimeter
3. Bond to station ground with #10 AWG or heavier wire
4. May be covered with thin soil or mulch

---

## 13. Safety

### 13.1 RF Exposure

The fan dipole operates at much lower voltages and currents than the magnetic loop:

| Parameter | Fan Dipole | Magnetic Loop |
|-----------|------------|---------------|
| Feedpoint voltage (100 W) | ~70 V | ~6,000 V |
| Maximum current | ~1.4 A | ~39 A |
| RF burn risk | Low | Extreme |
| Minimum clearance | 2 m during TX | 2 m during TX |

With wire ends at 3-5 m above ground, adequate clearance for pedestrians is maintained.

### 13.2 Lightning Protection

1. Install coaxial lightning arrester at station entry
2. Bond ground screen and mast base to station ground
3. Disconnect feedline from equipment during thunderstorms
4. Wire antenna is not a significant lightning attractor at 10 m, but mast may be the highest point -- consider a lightning rod

### 13.3 Mechanical Safety

- Wire ends at 3-5 m above ground for pedestrian clearance
- Use high-visibility flagging tape on wire ends near walkways
- Inspect ropes and wire annually for UV damage and corrosion
- If using a guyed mast, use non-conductive Dacron or nylon rope

---

## 14. Comparison: Fan Dipole vs Magnetic Loop

| Parameter | Fan Dipole (this design) | Magnetic Loop (balanced) |
|-----------|--------------------------|--------------------------|
| **Footprint** | 40 m span | 2 m diameter |
| **80m Efficiency** | 95-96% | 8.5-11% |
| **40m Efficiency** | 96-97% | 51-55% |
| **80m Gain (dBi, NVIS)** | +5.8 to +6.0 | -8 to -7 |
| **40m Gain (dBi, NVIS)** | +6.2 to +6.4 | +0 to +1 |
| **Bandwidth (-3 dB)** | 150-210 kHz | 1.7-5 kHz |
| **Retuning Required** | No (full band coverage) | Every 1-5 kHz |
| **Feed Voltage at 100 W** | ~70 V | 5,000-6,400 V |
| **Tuning Complexity** | Cut-and-trim once | Vacuum variable capacitor |
| **Stealth / Low Profile** | Poor (40 m wire span) | Excellent (2 m circle) |
| **Noise Rejection** | Moderate | Excellent (deep nulls) |
| **Wind Resistance** | Excellent (wire flexes) | Good (rigid loop) |
| **Portability** | Fair (bulky wire, ropes) | Good (compact, rigid) |
| **Cost** | $153-285 | $313-712 |
| **Construction Skill** | Beginner | Intermediate |
| **Best For** | Max NVIS gain, wide BW | Limited space, stealth, noise |

**Recommendation:** The fan dipole is the superior NVIS antenna when space permits. It provides 12-14 dB more gain on 80 m and 5-6 dB more on 40 m, with much wider bandwidth and lower cost. Use the magnetic loop when the fan dipole's 40 m wire span is not feasible.

---

## 15. Bill of Materials

| # | Item | Specification | Qty | Est. Cost (USD) |
|---|------|--------------|-----|-----------------|
| 1 | Antenna wire | #14 AWG stranded copper, 70 m | 1 | $15-25 |
| 2 | Balun core | FT-240-43 ferrite toroid | 1 | $8-15 |
| 3 | Balun wire | #14 AWG PTFE, 3 m | 1 | $5-8 |
| 4 | Coaxial cable | RG-213, 50 ohm, 20 m | 1 | $30-50 |
| 5 | Connectors | PL-259, SO-239, barrel | 4-6 | $8-15 |
| 6 | Mast | Fibreglass telescoping, 10 m | 1 | $40-80 |
| 7 | Insulators | Egg or dog-bone, ceramic/HDPE | 6 | $5-10 |
| 8 | Support rope | Dacron (polyester), UV-resistant, 50 m | 1 | $10-20 |
| 9 | Wire spreaders | Plastic rod/tube, 30-50 cm | 4 | $5-10 |
| 10 | Junction box | IP65 weatherproof, for balun | 1 | $5-10 |
| 11 | Lightning arrester | Gas-discharge coaxial type | 1 | $15-25 |
| 12 | Ground screen | #14 AWG wire, 6x6 m (optional) | 1 | $15-25 |
| | **Total** | | | **$161-293** |

### 15.1 Cost-Saving Options

| Substitution | Saving | Trade-off |
|--------------|--------|-----------|
| Trees instead of mast | $40-80 | Requires suitable trees |
| Bare copper wire | $5-10 | Less UV-resistant jacket |
| Paracord instead of Dacron | $5-10 | Stretches more; less durable |
| Skip ground screen | $15-25 | Lose 1-2 dB NVIS gain |

---

## 16. Key Formulae

### 16.1 Dipole Length

```
L_half = 143 / f_MHz   [metres, each side of feedpoint]
```

With inverted-V correction (5% droop factor):

```
L_half_inv_V = 143 / f_MHz * 0.98
```

### 16.2 Array Factor (Horizontal Antenna over Ground)

```
AF(alpha) = 2 * |sin(kh * sin(alpha))|
```

where:
- `k = 2*pi/lambda`
- `h` = antenna height above ground (m)
- `alpha` = elevation angle (0 = horizon, 90 deg = zenith)

### 16.3 Free-Space Path Loss

```
FSPL (dB) = 20 * log10(4*pi*d/lambda)
```

### 16.4 NVIS Coverage Radius

```
R_ground = 2 * h_iono / tan(alpha)
```

where `h_iono` ~ 300 km (F2-layer height).

### 16.5 Wavelength

```
lambda = 300 / f_MHz   [metres]
```

### 16.6 Feed Impedance (Inverted-V)

The feedpoint impedance of an inverted-V dipole at the apex is approximately:

```
Z_feed ~ 50 ohm  (for 120-degree included angle)
```

The inverted-V droop lowers the impedance from the theoretical 73 ohm of a flat half-wave dipole in free space. The ~120-degree included angle conveniently brings the feedpoint impedance close to 50 ohm, providing a natural match to standard coax without a matching network.

---

## 17. Validation Checklist

### 17.1 Pre-Assembly

- [ ] All wire lengths cut with trim allowance
- [ ] Wires labelled (80L, 80R, 40L, 40R)
- [ ] Balun wound and tested (continuity, isolation)
- [ ] Junction box sealed with cable glands
- [ ] Insulators and rope attached to wire ends
- [ ] Mast erected and stable

### 17.2 Electrical Checks

- [ ] 80 m VSWR < 1.5:1 at 3.65 MHz (or target frequency)
- [ ] 40 m VSWR < 1.5:1 at 7.15 MHz (or target frequency)
- [ ] 80 m SWR bandwidth covers 3.5-3.8 MHz at < 2:1
- [ ] 40 m SWR bandwidth covers 7.0-7.3 MHz at < 2:1
- [ ] No spurious resonances between bands
- [ ] Common-mode choke installed on feedline

### 17.3 NVIS-Specific

- [ ] Feedpoint at 10 m (+/- 1 m)
- [ ] Wire ends at 3-5 m above ground
- [ ] Included angle approximately 120 degrees
- [ ] Wire spacing 30-50 cm near feedpoint
- [ ] Ground screen installed (if using)
- [ ] Feedline exits at 90 degrees to wire axis

### 17.4 On-Air Verification

- [ ] Signal reports from 50-300 km stations consistent with NVIS
- [ ] Signals from > 500 km weak or absent (NVIS pattern confirmed)
- [ ] Both bands operable without retuning
- [ ] Noise level acceptable on both bands
- [ ] SWR stable under all weather conditions

### 17.5 Safety

- [ ] All wire ends above 3 m from ground
- [ ] Lightning arrester installed
- [ ] Feedline disconnect accessible
- [ ] Mast guying adequate for local wind conditions
- [ ] No RF exposure hazard at ground level

---

## Appendix A: Quick Reference Card

```
+=======================================================================+
|          NVIS DUAL-BAND FAN DIPOLE - QUICK REFERENCE                  |
+=======================================================================+
|                                                                       |
|  TYPE:  Inverted-V fan dipole | WIRE: #14 AWG stranded copper        |
|  FEED:  1:1 current balun (FT-240-43) + RG-213 50 ohm coax          |
|  HEIGHT: 10 m apex | ANGLE: ~120 deg | GROUND: 6x6 m screen (opt.)  |
|                                                                       |
+-----------------------------------------------------------------------+
|  BAND  | ELEMENT  | GAIN   | EFF  | BW     | VSWR   | COVERAGE      |
+--------+----------+--------+------+--------+--------+---------------+
|  80 m  | 20 m/side| +5.9   | 95%  | 160 kHz| <1.5:1 | 0-400 km      |
|  40 m  | 10 m/side| +6.3   | 97%  | 210 kHz| <1.5:1 | 0-500 km      |
+--------+----------+--------+------+--------+--------+---------------+
|                                                                       |
|  NVIS PEAK: Zenith (90 deg) | -3 dB cone: 45-90 deg elevation        |
|  COVERAGE: 0-500 km via F2-layer reflection at ~300 km altitude       |
|                                                                       |
|  OPERATING SCHEDULE:                                                  |
|    06-09h: 80m or 40m  |  09-17h: 40m  |  17-20h: transition         |
|    20-06h: 80m only (foF2 < 7 MHz at night)                          |
|                                                                       |
|  COST: $161-293  |  CONSTRUCTION: Beginner-friendly                   |
|                                                                       |
+=======================================================================+
```

---

## Appendix B: NVIS Frequency Planning Guide

### B.1 Band-by-Band NVIS Planning

**80 m Band (3.500-3.800 MHz):**

| Time of Day | Season | Solar Activity | NVIS Reliability |
|-------------|--------|----------------|------------------|
| Day | Summer | High | Excellent |
| Day | Winter | High | Good to Excellent |
| Night | Summer | High | Good |
| Night | Winter | Low | Poor (foF2 may drop below 3.5) |

**40 m Band (7.000-7.300 MHz):**

| Time of Day | Season | Solar Activity | NVIS Reliability |
|-------------|--------|----------------|------------------|
| Day | Summer | High | Excellent |
| Day | Winter | Low | Fair |
| Night | Any | Low | Fail (foF2 < 7 MHz) |

### B.2 Operating Schedule

| Time (Local) | Band | Notes |
|--------------|------|-------|
| 06:00-09:00 | 80 m or 40 m | 80 m for certainty; 40 m once foF2 rises |
| 09:00-17:00 | 40 m preferred | Higher gain, lower noise |
| 17:00-20:00 | 40 m or 80 m | Transition period |
| 20:00-06:00 | 80 m only | foF2 below 7 MHz at night |

### B.3 Seasonal NVIS Calendar (Mid-Latitudes)

```
         J   F   M   A   M   J   J   A   S   O   N   D
80m Day  |===|===|===|===|===|===|===|===|===|===|===|===|  Always
80m Nite |== |== |===|===|===|===|===|===|===|== |== |== |  Mostly
40m Day  |=  |== |===|===|===|===|===|===|===|== |=  |=  |  Spring-Autumn
40m Nite |   |   |   |=  |=  |== |== |=  |=  |   |   |   |  Summer only

Legend: === Excellent  == Good  = Fair  (blank) Poor/Fail
Note: Solar maximum conditions assumed.
```

---

## Document Information

| Field | Value |
|-------|-------|
| Design class | Ground-up NVIS, balanced size/efficiency |
| Antenna type | Dual-band fan dipole (inverted-V) |
| Bands | 80 m (3.500-3.800 MHz), 40 m (7.000-7.300 MHz) |
| Primary mode | NVIS (0-500 km regional coverage) |
| Apex height | 10.0 m |
| Ground enhancement | 6x6 m screen (optional) |
| Companion design | [Magnetic Loop (balanced)](3-7Mhz-balanced.md) |
| Poster | [Dualband_Balanced.png](Dualband_Balanced.png) |
| PDF datasheet | [Dualband_Balanced.pdf](Dualband_Balanced.pdf) |

---

*End of document.*
