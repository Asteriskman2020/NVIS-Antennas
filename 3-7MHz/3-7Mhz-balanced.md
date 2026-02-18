# NVIS Magnetic Loop Antenna: 3.5-7.3 MHz Balanced Design

> **Design Class:** Ground-up NVIS (Near-Vertical Incidence Skywave)
> **Loop Diameter:** 2.0 m | **Tube:** 5/8" Type M Copper
> **Bands:** 80 m (3.500-3.800 MHz) and 40 m (7.000-7.300 MHz)
> **Mounting:** Vertical loop, 5.0 m centre height, ground screen below
> **Coverage:** 0-500 km regional, peak radiation at zenith

---

## Table of Contents

1. [Design Objective](#1-design-objective)
2. [Why Magnetic Loop for NVIS](#2-why-magnetic-loop-for-nvis)
3. [System Diagram](#3-system-diagram)
4. [Material Properties](#4-material-properties)
5. [Loop Parameters](#5-loop-parameters)
6. [Tuning Capacitance](#6-tuning-capacitance)
7. [NVIS Configuration](#7-nvis-configuration)
8. [Performance Tables](#8-performance-tables)
9. [Ground Screen](#9-ground-screen)
10. [Height Optimisation](#10-height-optimisation)
11. [Link Budget](#11-link-budget)
12. [Coupling Loop](#12-coupling-loop)
13. [Construction Notes](#13-construction-notes)
14. [Safety](#14-safety)
15. [Design Comparison](#15-design-comparison)
16. [Bill of Materials](#16-bill-of-materials)
17. [Key Formulae](#17-key-formulae)
18. [Validation Checklist](#18-validation-checklist)
- [Appendix A: Quick Reference Card](#appendix-a-quick-reference-card)
- [Appendix B: NVIS Frequency Planning Guide](#appendix-b-nvis-frequency-planning-guide)

---

## 1. Design Objective

### 1.1 NVIS-First Design Philosophy

This antenna is designed **from the ground up** for Near-Vertical Incidence Skywave (NVIS) propagation. It is not a DX antenna adapted for local use, nor a compromise multi-purpose design. Every parameter -- loop diameter, tube gauge, mounting height, ground screen, and coupling method -- has been selected to maximise performance for signals launched at steep angles into the ionosphere and returned to Earth within a 500 km radius.

NVIS propagation exploits the F2-layer of the ionosphere (typically 250-350 km altitude) as a mirror for signals transmitted at elevation angles above approximately 70 degrees. The signal travels nearly straight up, refracts back down, and illuminates a circular area centred on the transmitter. This provides reliable regional coverage that is immune to terrain shadowing, requires no line-of-sight, and fills the "skip zone" gap that plagues conventional HF antennas optimised for low-angle DX.

### 1.2 The Balanced Approach

A small magnetic loop antenna involves a fundamental trade-off between physical size and radiation efficiency. This design strikes a deliberate balance:

| Attribute | Choice | Rationale |
|-----------|--------|-----------|
| Diameter | 2.0 m | One person can construct and erect; fits residential lots |
| Tube | 5/8" (15.875 mm) Type M copper | Good conductivity-to-weight ratio; readily available |
| 80 m efficiency | 8.5% (-10.7 dB) | Modest but usable; 10.8 dB better than a 1 m loop |
| 40 m efficiency | 51.2% (-2.9 dB) | Genuinely competitive; over half the power radiated |
| Weight | ~7 kg (loop only) | Manageable for a single-mast installation at 5-6 m |
| Cost | $265-630 | Accessible to most amateur operators |

The 2.0 m diameter is the sweet spot: doubling from 1 m yields a dramatic efficiency gain (especially on 80 m, where R_rad scales as the fourth power of area), while remaining small enough for practical single-person installation. Going to 3 m would gain further efficiency but at the cost of significantly greater weight, wind load, and mechanical complexity.

### 1.3 Target Applications

- **Emergency communications (EMCOMM):** Reliable in-country or in-region coverage from a single portable or semi-permanent station.
- **Regional nets:** 80 m LSB nets covering a 200-400 km radius, including terrain-obstructed paths.
- **Military/NGO field deployment:** Compact, quickly erected, low visual profile.
- **Rural HF linking:** Connecting stations across mountainous or jungle terrain where VHF/UHF repeaters are impractical.
- **Amateur radio contesting (domestic):** Filling in short-skip contacts on 40 m and 80 m.

---

## 2. Why Magnetic Loop for NVIS

### 2.1 The Vertical Loop Advantage

A small magnetic loop antenna, when mounted with its plane vertical, has its **magnetic moment oriented horizontally**. The free-space radiation pattern of a small loop is a torus (doughnut shape) centred on the magnetic moment axis. Critically, the **zenith direction is perpendicular to this axis**, which means the loop radiates at full strength straight up. There is no zenith null.

This is the opposite behaviour to a vertical dipole or vertical whip, which has a zenith null and radiates best at the horizon -- precisely the wrong pattern for NVIS.

Compare the zenith performance of common antenna types:

| Antenna Type | Zenith Radiation | NVIS Suitability |
|--------------|-----------------|------------------|
| Vertical dipole / whip | Null at zenith | Poor |
| Horizontal dipole at h < lambda/4 | Maximum at zenith | Good |
| Vertical small magnetic loop | Maximum at zenith | Excellent |
| Horizontal small magnetic loop | Null at zenith | Poor |

### 2.2 Ground Reflection Enhancement

When a vertically-mounted small loop is placed over a ground plane at height h, the direct upward radiation and the ground-reflected radiation combine. For a perfect electric conductor (PEC) ground, the array factor is:

```
AF(alpha) = 2|sin(kh * sin(alpha))|
```

where `alpha` is the elevation angle and `k = 2*pi/lambda`. At zenith (alpha = 90 degrees):

```
AF(90 deg) = 2|sin(kh)|
```

For heights well below lambda/4, the sine term is less than 1, so the array factor at zenith is less than the theoretical maximum of 2.0 (which occurs at exactly h = lambda/4). However, the key property is that **the pattern peak remains at zenith** and the horizon is always a null. This is the ideal NVIS pattern: maximum power straight up, suppressed low-angle radiation that would otherwise cause interference or waste power on paths that skip over the target area.

### 2.3 Additional Benefits of the Magnetic Loop for NVIS

1. **Compact footprint:** A 2 m diameter circle versus 20-40 m wire spans for dipoles.
2. **Low noise reception:** The loop's figure-8 pattern (in the plane of the loop) provides nulls that can be steered toward noise sources by rotating the antenna.
3. **No radial field:** Unlike verticals, no extensive radial system is needed for the antenna itself (the ground screen is an enhancement for NVIS pattern shaping, not a requirement for basic operation).
4. **Height flexibility:** Effective NVIS performance at 5 m height, where a horizontal dipole on 80 m would need to be at 10+ m to clear obstacles and still be well below lambda/4.
5. **Narrow bandwidth as a feature:** The high Q provides inherent front-end selectivity, rejecting strong out-of-band signals that can overload receivers -- valuable in the crowded 80 m band.

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
                     |
                 6.0 m  --- Top of loop
                 |   |
                 | O |  <-- 2.0 m dia. copper loop (vertical plane)
                 |   |       Plane oriented N-S for E-W broadside
                 |   |
                 5.0 m  --- Centre of loop
                 |   |
                 | * |  <-- Coupling loop (0.40 m dia.) at bottom
                 |   |
                 4.0 m  --- Bottom of loop
                 |   |
                 |   |   Fibreglass/wood mast (non-conductive)
                 |   |
                 |   |
    Ground  -----+---+---------------------------------------------
    Level        |   |
              [=====|=====]   4 m x 4 m ground screen (chicken wire)
              [=====|=====]   or 8 x 10 m radial wires
              [=====|=====]   centred below loop
              [=====|=====]
                    |
                    +--- RG-213 coax to station (50 ohm)
```

### 3.2 Loop Detail (Front View)

```
                    Vacuum variable capacitor
                    (weather-sealed housing)
                         ___
                        | C |
                   _____|   |_____
                  /               \
                 /                 \
                |                   |
                |    2.0 m dia.     |      5/8" Type M copper tube
                |    (6.283 m       |      Wall: 0.711 mm
                |     circumf.)     |      Weight: ~7 kg
                |                   |
                 \                 /
                  \               /
                   \_____   _____/
                         | |
                     .---+ +---.
                    /   Shield   \      Coupling loop:
                   |   gap (top)  |     0.40 m dia. RG-213
                   |    10-15 mm  |     Faraday shielded
                    \            /
                     '---====---'
                          ||
                       RG-213 to
                       station
```

### 3.3 Side View (Mast Mounting)

```
                  Cap housing
                     [ ]
          ___________| |___________
         /                         \
        /    Loop plane (N-S)       \     <-- View from East
       |            |                |
       |         Mast (vertical)     |
       |            |                |
        \           |               /
         \__________|______________/
                    |
            Coupling loop (bottom)
                    |
         ===========|==========  Cross-arm / standoff
                    |
                    |  Fibreglass mast
                    |
                    |
    ================|================  Ground level
    [  Ground screen 4 m x 4 m  ]
```

---

## 4. Material Properties

### 4.1 Copper Conductor

| Property | Value | Notes |
|----------|-------|-------|
| Material | Type M copper tube | ASTM B88, hard-drawn |
| Outer diameter (OD) | 5/8" = 15.875 mm | Nominal trade size |
| Wall thickness | 0.711 mm (0.028") | Type M standard |
| Inner diameter (ID) | 14.453 mm | OD - 2 * wall |
| Conductivity (sigma) | 5.8 x 10^7 S/m | Annealed copper at 20 deg C |
| Resistivity (rho) | 1.724 x 10^-8 ohm-m | 1/sigma |
| Permeability (mu_0) | 4*pi x 10^-7 H/m | Non-magnetic (mu_r = 1) |
| Density | 8,960 kg/m^3 | |
| Thermal expansion | 16.5 x 10^-6 /K | |
| Melting point | 1,085 deg C | |

### 4.2 Skin Depth

At radio frequencies, current flows only within a thin surface layer of the conductor. The skin depth is:

```
delta = 1 / sqrt(pi * f * mu_0 * sigma)
```

Substituting sigma = 5.8 x 10^7 S/m:

| Frequency (MHz) | Skin Depth delta (um) | Wall Thickness / delta | Current Penetration |
|------------------|-----------------------|------------------------|---------------------|
| 3.500 | 35.1 | 20.3 | Fully developed skin effect |
| 3.650 | 34.4 | 20.7 | Fully developed skin effect |
| 3.800 | 33.7 | 21.1 | Fully developed skin effect |
| 7.000 | 24.8 | 28.7 | Fully developed skin effect |
| 7.100 | 24.7 | 28.8 | Fully developed skin effect |
| 7.200 | 24.5 | 29.0 | Fully developed skin effect |
| 7.300 | 24.3 | 29.3 | Fully developed skin effect |

**Interpretation:** The wall-to-skin-depth ratio exceeds 20 at all operating frequencies. Since RF current is effectively confined within approximately 3-4 skin depths, and the wall provides more than 20 skin depths of material, the tube behaves identically to a solid conductor. The wall thickness is more than adequate and there is no benefit to using thicker-walled tube (Type L or Type K).

### 4.3 Surface Finish and Oxidation

Copper oxide (Cu2O) is a semiconductor with much lower conductivity than pure copper. A heavily oxidised surface will increase loss resistance. Mitigation strategies:

- **New installation:** Clean with fine Scotch-Brite, then apply a thin coat of clear polyurethane or marine varnish within hours of cleaning.
- **Long-term protection:** Wrap with self-amalgamating silicone tape (not PVC electrical tape, which degrades in UV).
- **Joint preparation:** Silver-braze all joints for lowest resistance. Solder joints (even silver solder) introduce tin-based alloys with 5-10x higher resistivity.
- **Do not use:** Conductive grease or anti-oxidant compound on RF-carrying joints -- these compounds have orders-of-magnitude higher resistivity than copper.

---

## 5. Loop Parameters

### 5.1 Physical Dimensions

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Loop diameter | D | 2.000 m |
| Loop radius (centreline) | b | 1.000 m |
| Tube outer diameter | OD | 15.875 mm (5/8") |
| Tube outer radius | a | 7.9375 mm |
| Tube wall thickness | t | 0.711 mm |
| Loop circumference | C_loop | 2*pi*b = 6.283 m |
| Enclosed area | A | pi*b^2 = 3.142 m^2 |
| Tube length required | L_tube | ~6.5 m (loop) + 0.3 m (overlap) = ~7 m |
| Loop weight (copper) | W | ~7 kg |

### 5.2 Inductance Calculation

The inductance of a single-turn circular loop of radius b made from wire/tube of radius a is given by the Neumann formula:

```
L = mu_0 * b * [ln(8b/a) - 2]
```

Step-by-step:

```
b = 1.000 m
a = 0.0079375 m

8b/a = 8 * 1.000 / 0.0079375 = 1007.87

ln(1007.87) = 6.9155

ln(8b/a) - 2 = 6.9155 - 2.0000 = 4.9155

L = 4*pi*10^-7 * 1.000 * 4.9155
  = 1.2566 * 10^-6 * 4.9155
  = 6.176 * 10^-6 H
```

**L = 6.18 uH**

### 5.3 Electrical Size

The electrical size of the loop is characterised by the ratio of circumference to wavelength:

| Frequency (MHz) | Wavelength lambda (m) | C/lambda | Electrical Size |
|------------------|-----------------------|----------|-----------------|
| 3.500 | 85.71 | 0.0733 | Very small (< 0.1 lambda) |
| 3.650 | 82.13 | 0.0765 | Very small |
| 3.800 | 78.89 | 0.0796 | Very small |
| 7.000 | 42.86 | 0.1466 | Small (~ 0.15 lambda) |
| 7.100 | 42.25 | 0.1488 | Small |
| 7.200 | 41.67 | 0.1508 | Small |
| 7.300 | 41.10 | 0.1529 | Small |

At all operating frequencies, the loop circumference is well below one wavelength, confirming that the small-loop approximation (uniform current distribution) is valid. The 40 m band pushes toward 0.15 lambda, where the approximation is still good but second-order effects begin to appear. For this design, the small-loop formulae remain accurate to within a few percent.

### 5.4 Inductive Reactance

| Frequency (MHz) | X_L = 2*pi*f*L (ohm) |
|------------------|-----------------------|
| 3.500 | 135.9 |
| 3.650 | 141.8 |
| 3.800 | 147.6 |
| 7.000 | 271.8 |
| 7.100 | 275.7 |
| 7.200 | 279.5 |
| 7.300 | 283.4 |

These are the reactances that must be cancelled by the tuning capacitor to achieve resonance.

---

## 6. Tuning Capacitance

### 6.1 Required Capacitance

At resonance, the capacitive reactance equals the inductive reactance:

```
X_C = 1/(2*pi*f*C) = X_L = 2*pi*f*L

Solving: C = 1 / (4*pi^2 * f^2 * L)
```

| Frequency (MHz) | C_tune (pF) | X_C (ohm) |
|------------------|-------------|-----------|
| 3.500 | 335.0 | 135.9 |
| 3.650 | 308.2 | 141.8 |
| 3.800 | 283.8 | 147.6 |
| 7.000 | 83.6 | 271.8 |
| 7.100 | 81.3 | 275.7 |
| 7.200 | 79.1 | 279.5 |
| 7.300 | 77.0 | 283.4 |

**Required tuning range: 77 - 335 pF**

### 6.2 Capacitor Selection

The tuning capacitor is the single most critical component in the antenna. It must satisfy three requirements simultaneously:

1. **Capacitance range:** Must cover 77-335 pF (4.35:1 ratio).
2. **Voltage rating:** Must withstand at least 6,438 V peak at 100 W (see Section 14). A 10 kV rating provides adequate margin.
3. **Extremely low loss:** The capacitor's equivalent series resistance (ESR) must be negligible compared to the loop's loss resistance (~60-90 milliohms). Air-variable and vacuum-variable capacitors meet this requirement; ceramic and film capacitors generally do not.

**Recommended: Vacuum variable capacitor, 10-500 pF, 10 kV or higher.**

Suitable types:

| Capacitor | Range (pF) | Voltage (kV) | Notes |
|-----------|-----------|--------------|-------|
| Jennings CSVF-500-0010 | 10-500 | 10 | Ideal; commonly available surplus |
| Jennings UCSL-500 | 5-500 | 15 | Higher voltage margin |
| Russian KP1-4 | 10-500 | 10 | Widely available, affordable |
| Air variable (homebrew) | varies | 3-5 | Only for QRP (< 25 W); plate spacing limits voltage |

**Air-variable capacitors** with standard 1-2 mm plate spacing are limited to approximately 3-5 kV and are therefore only suitable for QRP operation (under 25 W). At 100 W, a vacuum variable is mandatory.

### 6.3 Capacitor Mounting

The capacitor is mounted at the top of the loop, directly across the gap in the tube. This placement:

- Minimises lead length (and associated stray inductance).
- Places the capacitor at the voltage maximum, which is unavoidable but means leads must be as short as possible.
- Allows the coupling loop to be at the bottom, diametrically opposite the capacitor (at the current maximum).

The capacitor should be housed in a weatherproof enclosure (IP65 or better). Use a reduction drive or stepper motor for remote tuning. Direct-drive shafts are acceptable for manual tuning if the operator can safely reach the capacitor.

### 6.4 Stray Capacitance

Typical stray capacitance from mounting hardware, leads, and the capacitor housing adds 5-15 pF. This shifts the tuning range slightly lower and should be accounted for during initial calibration. If the capacitor cannot tune high enough in frequency (cannot reach 77 pF effective), shorten the leads or use a capacitor with a lower minimum value.

---

## 7. NVIS Configuration

### 7.1 Mounting Geometry

| Parameter | Value |
|-----------|-------|
| Loop orientation | Vertical (plane perpendicular to ground) |
| Loop plane alignment | North-South |
| Broadside direction | East-West |
| Centre height above ground | 5.0 m |
| Bottom of loop | 4.0 m above ground |
| Top of loop | 6.0 m above ground |
| Mast type | Fibreglass or wood (non-conductive) |
| Mast minimum height | 6.0 m |
| Mast material | Fibreglass push-up or guyed timber |

### 7.2 Height-to-Wavelength Ratios

The NVIS behaviour of the antenna is governed by the ratio of mounting height to wavelength:

| Band | Frequency | lambda (m) | h/lambda | kh (rad) |
|------|-----------|-----------|----------|----------|
| 80 m | 3.500 MHz | 85.71 | 0.058 | 0.367 |
| 80 m | 3.650 MHz | 82.13 | 0.061 | 0.383 |
| 80 m | 3.800 MHz | 78.89 | 0.063 | 0.398 |
| 40 m | 7.000 MHz | 42.86 | 0.117 | 0.734 |
| 40 m | 7.100 MHz | 42.25 | 0.118 | 0.744 |
| 40 m | 7.200 MHz | 41.67 | 0.120 | 0.754 |
| 40 m | 7.300 MHz | 41.10 | 0.122 | 0.764 |

All values are well below h/lambda = 0.25 (quarter wavelength), confirming that the ground reflection enhances zenith radiation. The 40 m band, at h/lambda ~ 0.12, benefits from stronger ground reinforcement than 80 m at h/lambda ~ 0.06.

### 7.3 Why the Vertical Loop Radiates at Zenith

A vertically mounted small magnetic loop has its **magnetic dipole moment (m)** oriented horizontally, perpendicular to the loop plane. The radiation pattern in free space is:

```
E(theta) proportional to sin(theta)
```

where theta is measured from the magnetic moment axis. The zenith direction is at theta = 90 degrees (perpendicular to the horizontal magnetic moment), giving sin(90 deg) = 1, the pattern maximum. The horizon in the broadside direction is also at theta = 90 degrees (maximum), while the horizon in the endfire direction (along the magnetic moment) is at theta = 0 degrees (null).

When placed over ground, the image theory adds a reflected contribution. For a horizontal magnetic dipole over PEC ground, the image has the **same** polarity (unlike an electric dipole, whose image is inverted). The direct and image fields add in phase at zenith (for any height), giving constructive interference straight up.

### 7.4 Array Factor

The array factor for a horizontal magnetic dipole at height h over PEC ground is:

```
AF(alpha) = 2|sin(kh * sin(alpha))|
```

where alpha is the elevation angle above the horizon (0 deg = horizon, 90 deg = zenith).

**At zenith (alpha = 90 degrees):**

```
AF(90 deg) = 2|sin(kh)|
```

| Band | Frequency | kh (rad) | sin(kh) | AF(zenith) |
|------|-----------|----------|---------|------------|
| 80 m | 3.500 MHz | 0.367 | 0.359 | 0.718 |
| 80 m | 3.800 MHz | 0.398 | 0.388 | 0.776 |
| 40 m | 7.000 MHz | 0.734 | 0.669 | 1.338 |
| 40 m | 7.300 MHz | 0.764 | 0.693 | 1.386 |

**Interpretation:**
- On 80 m, the array factor at zenith is 0.72-0.78 (below the free-space value of 1.0 because the height is very small relative to wavelength). Despite this, the pattern still peaks at zenith.
- On 40 m, the array factor reaches 1.34-1.39, providing actual gain over the free-space pattern at zenith. The ground reflection is working strongly in our favour.

### 7.5 Normalised Elevation Pattern

The normalised elevation pattern in the broadside direction (East-West), with the loop plane North-South, over PEC ground:

```
E_norm(alpha) = sin(kh * sin(alpha)) / sin(kh)
```

This normalises the pattern peak (at zenith) to 1.0 (0 dB):

| Elevation | 80 m (3.5 MHz) | 80 m (dB) | 40 m (7.0 MHz) | 40 m (dB) |
|-----------|----------------|-----------|-----------------|-----------|
| 90 deg (zenith) | 1.000 | 0.0 | 1.000 | 0.0 |
| 80 deg | 0.985 | -0.1 | 0.989 | -0.1 |
| 70 deg | 0.942 | -0.5 | 0.952 | -0.4 |
| 60 deg | 0.872 | -1.2 | 0.887 | -1.0 |
| 50 deg | 0.774 | -2.2 | 0.796 | -2.0 |
| 45 deg | 0.716 | -2.9 | 0.742 | -2.6 |
| 30 deg | 0.509 | -5.9 | 0.536 | -5.4 |
| 20 deg | 0.349 | -9.1 | 0.371 | -8.6 |
| 10 deg | 0.177 | -15.0 | 0.190 | -14.4 |
| 0 deg (horizon) | 0.000 | null | 0.000 | null |

**Key observation:** The pattern is extremely broad around zenith. The -3 dB beamwidth spans from roughly 45 degrees to 90 degrees elevation, which is the ideal NVIS cone.

### 7.6 NVIS Take-Off Angles

| Band | Frequency | Pattern Peak | -3 dB Cone | -6 dB Cone |
|------|-----------|-------------|------------|------------|
| 80 m | 3.500 MHz | 90 deg | 45 deg - 90 deg | 28 deg - 90 deg |
| 80 m | 3.800 MHz | 90 deg | 47 deg - 90 deg | 30 deg - 90 deg |
| 40 m | 7.000 MHz | 90 deg | 44 deg - 90 deg | 27 deg - 90 deg |
| 40 m | 7.300 MHz | 90 deg | 46 deg - 90 deg | 29 deg - 90 deg |

The -3 dB cone encompasses elevation angles from approximately 44-47 degrees up to zenith. This corresponds to NVIS coverage from directly overhead out to approximately 300 km radius, which is precisely the target coverage area.

### 7.7 NVIS Coverage Geometry

Assuming F2-layer reflection at 300 km altitude:

| Elevation Angle | Ground Radius (km) | Round-Trip Path (km) | Application |
|-----------------|---------------------|----------------------|-------------|
| 90 deg | 0 | 600 | Directly overhead (local) |
| 80 deg | 53 | 606 | City-wide coverage |
| 70 deg | 109 | 624 | Regional (adjacent cities) |
| 60 deg | 173 | 660 | Inter-city |
| 50 deg | 247 | 712 | Provincial/state |
| 45 deg | 300 | 735 | Extended regional |
| 30 deg | 520 | 866 | NVIS outer limit |

The ground radius is calculated as:

```
R = 2 * h_iono * cos(alpha) / sin(alpha) = 2 * h_iono / tan(alpha)
```

for a flat-earth approximation (valid for ranges up to ~500 km).

### 7.8 Broadside vs. Endfire

The magnetic loop has a directional pattern in the horizontal plane:

- **Broadside** (perpendicular to loop plane, i.e., East-West if loop is N-S): Full radiation at all elevation angles.
- **Endfire** (in the loop plane, i.e., North-South if loop is N-S): Null at the horizon, but radiation at elevated angles.

For NVIS, the distinction is less important than for DX, because the high-angle radiation is present in all azimuthal directions. However, the broadside direction will have marginally stronger NVIS coverage at intermediate angles (45-70 degrees). Orient the loop plane to place the broadside direction toward the most important coverage area.

---

## 8. Performance Tables

### 8.1 Resistance Components

**Radiation Resistance:**

```
R_rad = 31171 * (A / lambda^2)^2   [ohms]
```

where A = pi * b^2 = 3.142 m^2.

**Loss Resistance:**

```
R_loss = (C_loop / (2*pi*a)) * sqrt(pi*f*mu_0 / sigma)   [ohms]
```

where C_loop = 6.283 m (loop circumference), a = 7.9375 mm (tube outer radius).

### 8.2 Complete Performance Table

| Parameter | 3.500 MHz | 3.650 MHz | 3.800 MHz | 7.000 MHz | 7.100 MHz | 7.200 MHz | 7.300 MHz |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **Wavelength (m)** | 85.71 | 82.13 | 78.89 | 42.86 | 42.25 | 41.67 | 41.10 |
| **C/lambda** | 0.0733 | 0.0765 | 0.0796 | 0.1466 | 0.1488 | 0.1508 | 0.1529 |
| **R_rad (milliohm)** | 5.70 | 6.74 | 7.93 | 91.27 | 96.54 | 102.09 | 107.86 |
| **R_loss (milliohm)** | 61.47 | 62.78 | 64.07 | 86.95 | 87.59 | 88.19 | 88.81 |
| **R_total (milliohm)** | 67.17 | 69.52 | 72.00 | 178.22 | 184.13 | 190.28 | 196.67 |
| **Efficiency (%)** | 8.5 | 9.7 | 11.0 | 51.2 | 52.4 | 53.7 | 54.9 |
| **Efficiency (dB)** | -10.71 | -10.13 | -9.58 | -2.91 | -2.80 | -2.70 | -2.60 |
| **Q factor** | 2023 | 1961 | 1897 | 1525 | 1501 | 1477 | 1450 |
| **Bandwidth -3dB (kHz)** | 1.73 | 1.86 | 2.00 | 4.59 | 4.73 | 4.87 | 5.03 |
| **C_tune (pF)** | 335.0 | 308.2 | 283.8 | 83.6 | 81.3 | 79.1 | 77.0 |
| **V_cap at 100W (V)** | 5244 | 5338 | 5417 | 6438 | 6392 | 6341 | 6287 |

### 8.3 Bandwidth Implications

The -3 dB bandwidth ranges from 1.73 kHz (80 m low end) to 5.03 kHz (40 m high end). For SSB voice (2.4 kHz occupied bandwidth), the antenna must be retuned when moving more than approximately:

| Band | Usable Passband | Retune Interval |
|------|----------------|-----------------|
| 80 m | ~1.7-2.0 kHz | Every 1-2 kHz (~1 channel) |
| 40 m | ~4.6-5.0 kHz | Every 4-5 kHz (~2 channels) |

For CW (500 Hz bandwidth), the antenna can cover approximately 3-10 kHz without retuning.

**Practical consequence:** On 80 m, the operator must retune for virtually every frequency change. On 40 m, a small group of adjacent SSB channels can be covered without retuning. A stepper-motor-driven capacitor with a frequency readout is strongly recommended for convenient operation.

### 8.4 Q Factor Discussion

The high Q values (1450-2023) are a direct consequence of the small loop's low radiation resistance relative to its stored energy. While high Q limits bandwidth, it provides:

1. **Selectivity:** Strong out-of-band signals are attenuated by the antenna itself, reducing receiver intermodulation.
2. **Voltage multiplication:** The tuning capacitor sees thousands of volts even at modest power levels (see Section 14).
3. **Tuning sensitivity:** Small capacitance changes produce large frequency shifts. Fine-resolution tuning drives are essential.

---

## 9. Ground Screen

### 9.1 Purpose

The ground screen serves two functions for NVIS:

1. **Improves ground reflection coefficient:** Real earth (especially dry or rocky soil) is a lossy reflector. A ground screen raises the effective conductivity of the reflecting surface directly below the antenna, making the ground reflection more closely approximate PEC. This increases the array factor at zenith.
2. **Reduces ground losses:** RF currents induced in the ground by the antenna's near field are concentrated in a small area directly below the loop. A conductive screen intercepts these currents and carries them with much lower loss than soil.

### 9.2 Specifications

| Parameter | Primary Option | Alternative |
|-----------|---------------|-------------|
| Type | Chicken wire (poultry netting) | Radial wires |
| Mesh size | 25 mm (1 inch) | N/A |
| Dimensions | 4 m x 4 m | 8 radials, 10 m each |
| Material | Galvanised steel | Bare copper wire (#14 AWG) |
| Placement | On ground surface | On ground surface or buried 2-5 cm |
| Centre point | Directly below loop centre | Directly below loop centre |
| Bonding | Connect to station ground rod | Connect to station ground rod |

### 9.3 Construction

**Chicken wire screen:**
1. Lay out a 4 m x 4 m sheet of 25 mm galvanised chicken wire, centred below the loop.
2. Pin down with landscape staples or tent pegs every 0.5 m around the perimeter.
3. Bond the screen to the station ground system with a short (#10 AWG or heavier) copper wire connected at the centre.
4. If using multiple sheets, overlap by at least 100 mm and bond overlaps with wire ties or clamps at 300 mm intervals.
5. The screen may be left on the surface or covered with a thin layer of soil or mulch for aesthetics. Performance is nearly identical either way.

**Radial wire alternative:**
1. Cut 8 lengths of #14 AWG bare copper wire, each 10 m long.
2. Connect all 8 wires at a central hub (a copper plate or clamp) directly below the loop.
3. Lay radials out at 45-degree intervals (N, NE, E, SE, S, SW, W, NW).
4. Pin down with landscape staples.
5. Bond the central hub to the station ground system.

### 9.4 Ground Screen Size Rationale

The ground screen should extend at least one loop diameter (2 m) beyond the loop footprint in all directions. Since the loop is 2 m in diameter and the bottom is at 4 m height, the Fresnel zone of the ground reflection is relatively compact. A 4 m x 4 m screen captures the primary reflection zone. Larger screens (up to 8 m x 8 m) provide diminishing returns but are beneficial if materials are available.

For the radial wire alternative, 10 m radials extend well beyond the primary reflection zone and provide good performance with less material than a full mesh screen.

---

## 10. Height Optimisation

### 10.1 Height vs. Array Factor

The array factor at zenith, AF(90 deg) = 2|sin(kh)|, varies with height:

| Height (m) | h/lambda (80 m) | AF (80 m) | h/lambda (40 m) | AF (40 m) | Notes |
|------------|-----------------|-----------|-----------------|-----------|-------|
| 2 | 0.023 | 0.293 | 0.047 | 0.578 | Very low; minimal ground gain |
| 3 | 0.035 | 0.436 | 0.070 | 0.852 | Usable but weak on 80 m |
| 4 | 0.047 | 0.578 | 0.093 | 1.105 | Good for 40 m, weak on 80 m |
| **5** | **0.058** | **0.718** | **0.117** | **1.338** | **Recommended compromise** |
| 6 | 0.070 | 0.855 | 0.140 | 1.549 | Better if mast allows |
| 8 | 0.093 | 1.110 | 0.187 | 1.814 | Excellent 40 m; good 80 m |
| 10 | 0.117 | 1.338 | 0.234 | 1.961 | Near-optimal for 40 m |
| 10.7 | 0.125 | 1.414 | 0.250 | 2.000 | **Optimal for 40 m** (lambda/4) |
| 15 | 0.175 | 1.756 | 0.350 | 1.902 | 40 m past peak; 80 m climbing |
| 21.4 | 0.250 | 2.000 | 0.500 | 0.000 | **Optimal 80 m but 40 m null!** |

### 10.2 Analysis

The critical insight from this table is the conflicting height requirements of the two bands:

- **80 m optimal height:** lambda/4 = 21.4 m. At this height, the 40 m array factor is **zero** (destructive interference at zenith). This makes 21.4 m a catastrophic choice for dual-band NVIS.
- **40 m optimal height:** lambda/4 = 10.7 m. At this height, 80 m AF = 1.414, which is good but not optimal.
- **Compromise at 5 m:** Both bands have useful array factors (0.72 and 1.34). Neither is optimal, but both are functional.

### 10.3 Height Selection Rationale

The 5.0 m centre height is recommended for the following reasons:

1. **Dual-band compatibility:** Both bands have positive, useful array factors at zenith.
2. **Practical structure:** A 6 m fibreglass mast is readily available and manageable. Heights of 10+ m require guyed towers or multi-section masts.
3. **Bottom clearance:** With the loop bottom at 4.0 m, there is adequate clearance for people and objects below the antenna. RF safety zones (see Section 14) are satisfied.
4. **Wind loading:** Lower mounting reduces bending moment on the mast by approximately the square of the height reduction.
5. **Portability:** A 6 m mast can be transported in a vehicle and erected by one person with a tilt-over base.

### 10.4 If Greater Height is Available

If a taller mast or tower is available, the following heights are worth considering:

| Scenario | Recommended Height | Rationale |
|----------|-------------------|-----------|
| 40 m only | 10.7 m | Optimal AF = 2.000 at zenith |
| 80 m only | 15-20 m | Approach optimal without going to 21.4 m where 40 m nulls |
| Dual-band (priority 40 m) | 8-10 m | Near-optimal 40 m; good 80 m |
| Dual-band (balanced) | 5-6 m | Good compromise, practical structure |
| Portable / field use | 3-5 m | Minimum practical; 40 m still useful |

---

## 11. Link Budget

### 11.1 NVIS Link Budget: 40 m Band, 100 W, 300 km Path

This link budget estimates the received signal strength for a typical NVIS path on the 40 m band.

**Assumptions:**
- Frequency: 7.000 MHz
- Transmit power: 100 W
- Both stations use identical 2.0 m magnetic loop antennas
- F2-layer reflection height: 300 km
- Path: 300 km ground distance (one hop, 45-degree elevation)
- Time: Daytime, moderate solar activity

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Transmit power | 100 | W | |
| Transmit power | +50.0 | dBm | 10*log10(100/0.001) |
| TX antenna efficiency | -2.9 | dB | 51.2% at 7.0 MHz |
| TX antenna gain at zenith | +2.7 | dBi | Estimated (loop + ground gain) |
| **EIRP** | **+49.8** | **dBm** | |
| Free-space path loss | -125.0 | dB | 20*log10(4*pi*d/lambda), d = 600 km |
| Ionospheric absorption | -10.0 | dB | Typical daytime D-layer absorption |
| Polarisation mismatch | -1.0 | dB | Faraday rotation (statistical average) |
| Ground reflection loss | -2.0 | dB | Real ground (not PEC) |
| RX antenna gain at zenith | +2.7 | dBi | Same antenna |
| RX antenna efficiency | -2.9 | dB | 51.2% at 7.0 MHz |
| **Received signal** | **-88.4** | **dBm** | |
| Noise floor (40 m, 4 kHz BW) | -100.0 | dBm | Typical daytime atmospheric + man-made |
| **Signal-to-Noise Ratio** | **+11.6** | **dB** | |

### 11.2 Simplified Link Budget (Best Case, PEC Ground)

Under more optimistic assumptions (lower ionospheric absorption, PEC ground):

| Parameter | Value |
|-----------|-------|
| Transmit power | +50.0 dBm |
| TX antenna efficiency | -2.9 dB |
| TX antenna gain at zenith | +2.7 dBi |
| EIRP | +52.7 dBm |
| Path loss (600 km F2) | -125 dB |
| Ionospheric absorption | -10 dB |
| RX antenna gain | +2.7 dBi |
| Received signal | -79.6 dBm |
| Noise floor (40 m, 4 kHz) | -100 dBm |
| **SNR** | **+20.4 dB** |

### 11.3 80 m Band Link Budget (100 W, 200 km)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Transmit power | +50.0 dBm | 100 W |
| TX antenna efficiency | -10.7 dB | 8.5% at 3.5 MHz |
| TX antenna gain at zenith | +1.5 dBi | Lower ground gain on 80 m |
| EIRP | +40.8 dBm | |
| Path loss (500 km F2, 70-deg elev.) | -120 dB | Shorter path |
| Ionospheric absorption | -15 dB | Higher on 80 m, especially daytime |
| RX antenna gain | +1.5 dBi | |
| Received signal | -92.2 dBm | |
| Noise floor (80 m, 4 kHz) | -90 dBm | Higher noise on 80 m |
| **SNR** | **-2.2 dB** | Marginal in daytime |

**80 m assessment:** Daytime NVIS on 80 m with this antenna is marginal due to the combination of lower efficiency (8.5%), higher ionospheric absorption, and higher noise floor. Night-time operation (when D-layer absorption drops dramatically) is much more favourable, with SNR improving by 10-15 dB. For reliable 80 m NVIS, night-time operation or higher power (400 W) is recommended.

### 11.4 Link Budget Summary

| Scenario | Band | Power | Distance | Est. SNR | Assessment |
|----------|------|-------|----------|----------|------------|
| 40 m, day, PEC ground | 40 m | 100 W | 300 km | +20 dB | Excellent |
| 40 m, day, real ground | 40 m | 100 W | 300 km | +12 dB | Good (clear SSB) |
| 80 m, night | 80 m | 100 W | 200 km | +13 dB | Good (clear SSB) |
| 80 m, day | 80 m | 100 W | 200 km | -2 dB | Marginal (CW only) |
| 40 m, day, QRP 5 W | 40 m | 5 W | 300 km | +7 dB | Usable (CW) |

---

## 12. Coupling Loop

### 12.1 Design Parameters

| Parameter | Value |
|-----------|-------|
| Type | Faraday-shielded coupling loop |
| Diameter | 0.40 m (D/5 = 2.0/5) |
| Circumference | 1.257 m |
| Material | RG-213 coaxial cable |
| Shield gap | At top of coupling loop, 10-15 mm |
| Position | Bottom of main loop (current maximum) |
| Feed impedance | 50 ohm (nominal) |

### 12.2 Coupling Loop Theory

The coupling loop is a single-turn inductive loop placed inside the main loop at the point of maximum current (diametrically opposite the tuning capacitor). It acts as a transformer: the mutual inductance between the coupling loop and the main loop transfers energy between the 50-ohm feedline and the high-Q resonant main loop.

The coupling loop diameter is chosen as approximately 1/5 of the main loop diameter. This ratio provides a mutual inductance that transforms the very low radiation resistance (milliohms) of the main loop up to approximately 50 ohms at the coupling loop terminals.

### 12.3 Faraday Shield Construction

The Faraday shield prevents capacitive (electric field) coupling between the coupling loop and the main loop, ensuring that only magnetic (inductive) coupling occurs. This improves pattern symmetry and reduces common-mode currents on the feedline.

**Construction using RG-213:**

```
                Shield gap (10-15 mm)
                      |   |
                 _____|   |_____
                /               \
               /                 \     RG-213 coax bent into 0.40 m circle
              |     Coupling      |
              |      loop         |    Shield (braid) acts as Faraday shield
               \                 /     Centre conductor carries the RF signal
                \_______________/
                     |     |
                     |     |
               Centre     Shield
             conductor   (to ground)
                     |     |
                     +--+--+
                        |
                     To TX/RX
                     via RG-213
```

**Step-by-step:**

1. Cut a length of RG-213 coax approximately 1.5 m long (enough for the loop plus pigtails).
2. Form it into a circle of 0.40 m diameter.
3. At the top of the circle (the point farthest from the feedpoint), cut the outer jacket and braid, leaving a gap of 10-15 mm. **Do not cut the centre conductor or dielectric.** The braid must be cleanly separated with no stray strands bridging the gap.
4. Seal the gap with heat-shrink tubing or self-amalgamating tape to weatherproof it.
5. At the feedpoint (bottom of the coupling loop), connect the centre conductor and braid to a female SO-239 connector or directly to the feedline.
6. The braid on one side of the gap connects to the feedline shield; the braid on the other side connects to nothing (it is floating). This ensures the shield acts as a Faraday screen with a single-point ground.

### 12.4 Impedance Matching

The coupling loop diameter (D/5) is a starting point. Fine-tuning may be needed:

| Observation at Resonance | Adjustment |
|--------------------------|------------|
| SWR > 2:1, R < 50 ohm | Increase coupling loop diameter slightly |
| SWR > 2:1, R > 50 ohm | Decrease coupling loop diameter slightly |
| SWR minimum not at resonance | Adjust coupling loop position (tilt or offset) |
| Reactive component at resonance | Check for stray capacitance; adjust gap |

**Target: SWR < 1.5:1 at resonance across both bands.**

In practice, a fixed coupling loop diameter of D/5 typically achieves SWR < 2:1 without adjustment. If both bands must be covered without changing the coupling loop, D/5 is the best starting ratio. The match will be closer to 50 ohms on 40 m (where R_rad is higher) and somewhat lower on 80 m (where R_rad is very low), but the difference is usually within acceptable SWR limits.

### 12.5 Feedline

| Parameter | Recommendation |
|-----------|---------------|
| Type | RG-213 or LMR-400, 50 ohm |
| Length | As short as practical; 10-15 m typical |
| Connectors | PL-259 / SO-239 (adequate at HF) |
| Common-mode choke | 10 turns of feedline on FT-240-43 toroid at station end |
| Grounding | Shield bonded to station ground at entry point |

---

## 13. Construction Notes

### 13.1 Forming the Main Loop

**Materials needed:**
- 7 metres of 5/8" (15.875 mm OD) Type M copper tube
- Tube bender (manual or hydraulic) rated for 5/8" copper
- Silver brazing alloy (BAg-5 or similar, melting point ~620 deg C)
- MAPP gas or oxy-acetylene torch
- Flux (fluoride-based, for silver brazing)

**Procedure:**

1. **Straighten the tube** if it was coiled. Work carefully to avoid kinks. A tube straightener or gentle hand-bending over a padded form works well.

2. **Mark the circumference.** The required length for a 2.0 m diameter circle is pi * 2.0 = 6.283 m. Mark 6.3 m on the tube and add 50-75 mm on each end for the capacitor connection tabs. Total cut length: approximately 6.45 m.

3. **Bend the tube into a circle.** This is the most critical step. Options:
   - **Tube bender:** Use a conduit bender with a 1.0 m radius shoe (if available). Make incremental bends of 10-15 degrees, advancing along the tube.
   - **Form bending:** Build a circular form from plywood (1.0 m radius) and bend the tube around it incrementally.
   - **Free-hand:** For experienced builders. Overbend slightly and spring back. Work in small increments around the entire circumference to maintain circularity.
   - **Fill with sand or use a bending spring** to prevent kinking. Cap one end, fill with dry sand, cap the other end, then bend.

4. **Close the circle.** Bring the two ends together at the top of the loop, leaving a gap of 20-30 mm for the capacitor connection. The ends should be parallel and aligned.

5. **Flatten the connection tabs.** Gently flatten the last 30 mm of each tube end to create flat tabs for bolting to the capacitor terminals. Do not over-flatten; maintain at least 5 mm thickness for mechanical strength.

6. **Braze the support points.** If using a rigid mounting scheme, braze copper strap or bracket attachment points at the 3 o'clock and 9 o'clock positions (the horizontal midpoints of the loop) for cross-arm mounting.

### 13.2 Joining the Loop (If Required)

If the tube must be joined (because 7 m continuous lengths are unavailable):

- **Silver brazing is mandatory.** Tin-lead solder and even silver-bearing soft solder have orders-of-magnitude higher resistivity than copper.
- Clean both surfaces to bright copper immediately before brazing.
- Use a close-fitting sleeve joint (a short section of the next larger tube size, or a machined copper collar).
- The joint must be mechanically rigid and electrically continuous around the full circumference.
- After brazing, clean off all flux residue (it is corrosive and lossy).

### 13.3 Capacitor Housing

The vacuum variable capacitor must be protected from weather:

1. Use an IP65-rated plastic enclosure (polycarbonate or ABS, not metal).
2. Size the enclosure to allow at least 25 mm clearance around the capacitor on all sides.
3. Bring the copper tube ends through weatherproof glands or grommets.
4. If using a stepper motor for remote tuning, mount the motor on the outside of the enclosure with a shaft seal.
5. Include a small packet of silica gel desiccant inside the enclosure.
6. Provide a drain hole (covered with Gore-Tex vent) at the bottom to prevent condensation pooling.

### 13.4 Mast and Mounting

**Mast options:**

| Type | Length | Pros | Cons |
|------|--------|------|------|
| Fibreglass push-up | 6-10 m | Lightweight, non-conductive, portable | Flex in wind |
| Wooden pole | 6-8 m | Inexpensive, non-conductive, rigid | Heavy, may rot |
| Aluminium (with offset) | Any | Strong, available | Must offset loop > 1 m from metal |
| PVC (schedule 80) | 4-6 m | Cheap | Brittle in cold, UV degradation |

**Preferred:** Fibreglass telescoping mast, 6 m minimum.

**Mounting detail:**

1. Mount a non-conductive cross-arm at the top of the mast, perpendicular to the mast axis.
2. Attach the loop at its 3 o'clock and 9 o'clock points to the cross-arm using nylon or PTFE stand-offs (minimum 50 mm standoff from any support structure).
3. The mast passes through or behind the loop at the 6 o'clock position (bottom), where the coupling loop is located.
4. Use nylon cable ties, Dacron cord, or fibreglass straps for securing -- no metal hardware within 0.5 m of the loop.

### 13.5 Guy Wires

If the mast requires guying:

- Use Dacron (polyester) or nylon rope. Never use metal wire or cable.
- If metal guys are unavoidable (e.g., on an existing tower), break them into non-resonant lengths with egg insulators every 2-3 m.
- Attach guys at the 4-5 m level on the mast, anchored at 3-4 m from the base (45-60 degree angle).

### 13.6 Weatherproofing

1. **Copper tube:** Apply a thin coat of clear marine polyurethane or spar varnish. Alternatively, wrap with self-amalgamating silicone tape.
2. **Capacitor housing:** IP65 enclosure as described above.
3. **Coupling loop:** The RG-213 jacket provides UV resistance. Seal the shield gap with heat-shrink and self-amalgamating tape.
4. **Feedline entry:** Use a weatherproof bulkhead connector or drip loop at the station entry.
5. **Lightning:** Install a coaxial lightning arrester (PolyPhaser or equivalent) at the station entry. Bond the antenna ground screen and mast base to the station ground system with #6 AWG or heavier copper.

---

## 14. Safety

### 14.1 Capacitor Voltage

At resonance, the voltage across the tuning capacitor is:

```
V_cap = I_loop * X_C = I_loop / (2*pi*f*C)
```

where the loop current at power P is:

```
I_loop = sqrt(P / R_total)
```

| Frequency (MHz) | R_total (milliohm) | I_loop at 100 W (A) | X_C (ohm) | V_cap (V) |
|------------------|--------------------|----------------------|-----------|-----------|
| 3.500 | 67.17 | 38.59 | 135.9 | 5,244 |
| 3.650 | 69.52 | 37.93 | 141.8 | 5,338 |
| 3.800 | 72.00 | 37.27 | 147.6 | 5,417 |
| 7.000 | 178.22 | 23.69 | 271.8 | 6,438 |
| 7.100 | 184.13 | 23.31 | 275.7 | 6,392 |
| 7.200 | 190.28 | 22.92 | 279.5 | 6,341 |
| 7.300 | 196.67 | 22.55 | 283.4 | 6,287 |

**Maximum voltage: 6,438 V at 7.000 MHz, 100 W.**

The tuning capacitor must be rated for at least **10 kV** to provide adequate margin (1.55x safety factor). At higher power levels, voltages scale as the square root of power:

| Power (W) | V_cap max (V) | Required Rating (kV) |
|-----------|--------------|---------------------|
| 25 | 3,219 | 5 |
| 50 | 4,553 | 7.5 |
| 100 | 6,438 | 10 |
| 200 | 9,104 | 15 |
| 400 | 12,876 | 20 |

### 14.2 RF Exposure

The antenna generates intense electromagnetic fields in its immediate vicinity. At 100 W:

- **Near-field zone:** Within approximately 1 m of the loop, field strengths can exceed FCC/ICNIRP occupational exposure limits.
- **Minimum clearance during TX:** 1.0 m from any part of the loop.
- **Recommended clearance:** 2.0 m from the loop during transmit at 100 W.
- **Bottom of loop at 4.0 m:** Provides adequate clearance from ground-level personnel. No one should stand directly below the antenna during transmission.

**Burns hazard:** Touching the loop or capacitor connections during transmission will cause severe RF burns due to the high circulating current (up to 39 A) and high voltage (up to 6,438 V). The capacitor housing must be locked or physically inaccessible during operation.

### 14.3 Lightning Protection

The antenna and mast should be integrated into the station's lightning protection system:

1. Bond the ground screen to the station ground rod with #6 AWG copper.
2. Install a coaxial lightning arrester (gas-discharge type) on the feedline at the station entry point.
3. Bond the arrester ground to the station ground bus.
4. During thunderstorms, disconnect the feedline from the transceiver and connect it to a grounded bulkhead panel.
5. The antenna itself (being a closed loop of copper) will not attract lightning more than any other structure at the same height, but the mast top at 6 m may be the highest point on the property. Consider a lightning rod extending 0.5 m above the mast top, bonded to the ground system via a dedicated #6 AWG down-conductor.

### 14.4 Mechanical Safety

- **Mast erection:** Use a tilt-over base or gin pole. Never work under a raised mast.
- **Wind loading:** The 2.0 m loop presents approximately 0.03 m^2 of frontal area (tube profile) to the wind. At 100 km/h wind speed, the force on the loop is approximately 20 N (2 kg-force). The mast and mounting must withstand this plus a safety factor of 3x.
- **Weight at height:** The 7 kg loop plus capacitor housing (1-2 kg) creates a 9 kg load at 5-6 m height. Ensure the mast is rated for this eccentric load.

---

## 15. Design Comparison

### 15.1 Three Loop Sizes Compared

| Parameter | Standard (1 m) | This Design (2 m) | Max-Efficiency (3 m) |
|-----------|----------------|-------------------|----------------------|
| **Diameter** | 1.0 m | **2.0 m** | 3.0 m |
| **Tube** | 3/8" (9.525 mm) | **5/8" (15.875 mm)** | 7/8" (22.225 mm) |
| **Circumference** | 3.14 m | **6.28 m** | 9.42 m |
| **Area** | 0.785 m^2 | **3.142 m^2** | 7.069 m^2 |
| **Weight (loop)** | ~3 kg | **~7 kg** | ~12 kg |
| **Inductance** | ~4.1 uH | **6.18 uH** | ~8.0 uH |
| **80 m R_rad** | 0.36 mOhm | **5.70 mOhm** | 19.0 mOhm |
| **80 m R_loss** | ~50 mOhm | **61.5 mOhm** | ~62 mOhm |
| **80 m efficiency** | 0.7% | **8.5%** | 30.5% |
| **80 m efficiency (dB)** | -21.5 dB | **-10.7 dB** | -5.2 dB |
| **40 m R_rad** | 5.7 mOhm | **91.3 mOhm** | 304 mOhm |
| **40 m R_loss** | ~70 mOhm | **87.0 mOhm** | ~88 mOhm |
| **40 m efficiency** | 7.6% | **51.2%** | 83.3% |
| **40 m efficiency (dB)** | -11.2 dB | **-2.9 dB** | -0.8 dB |
| **Practical for 1 person** | Yes | **Yes** | Difficult |
| **Wind survival** | Excellent | **Good** | Marginal |
| **Cost estimate** | $150-350 | **$265-630** | $400-900 |

### 15.2 Gain Relative to Standard 1 m Loop

| Band | This Design (2 m) vs. Standard (1 m) | Max-Eff (3 m) vs. Standard (1 m) |
|------|-------------------------------------|----------------------------------|
| 80 m | **+10.8 dB** | +16.4 dB |
| 40 m | **+8.3 dB** | +10.4 dB |

**Interpretation:** Doubling the loop diameter from 1 m to 2 m yields a **10.8 dB** improvement on 80 m and **8.3 dB** on 40 m. This is an enormous gain -- equivalent to increasing transmitter power by 10-12x on 80 m and 7x on 40 m. Going from 2 m to 3 m yields a further 5.6 dB on 80 m and 2.1 dB on 40 m. The 2 m design captures the majority of the available improvement while remaining practical for single-person construction and installation.

### 15.3 Comparison with Wire Antennas for NVIS

For context, how does this loop compare with common wire antennas used for NVIS?

| Antenna | 80 m NVIS Gain (dBi) | 40 m NVIS Gain (dBi) | Size (m) | Notes |
|---------|----------------------|----------------------|----------|-------|
| Horizontal dipole at 10 m | +5 to +6 | +5 to +6 | 20 (40m) / 40 (80m) | Requires long supports |
| Inverted-V at 10 m | +3 to +5 | +4 to +5 | 20-40 | Single centre support |
| This 2 m loop at 5 m | -8 to -7 | +0 to +1 | 2 dia. | Compact footprint |
| 3 m loop at 5 m | -3 to -2 | +2 to +3 | 3 dia. | Still compact |

The magnetic loop trades 8-13 dB of gain on 80 m relative to a full-size dipole, in exchange for a 20x reduction in physical footprint. On 40 m, the trade-off is only 4-6 dB. Where space permits a full-size wire antenna, the wire antenna will always win on raw gain. The magnetic loop's advantages are compactness, stealth, and directional nulls for noise rejection.

---

## 16. Bill of Materials

### 16.1 Complete Parts List

| # | Item | Specification | Qty | Est. Cost (USD) |
|---|------|--------------|-----|-----------------|
| 1 | Copper tube | 5/8" Type M, hard-drawn, 7 m | 1 | $40-70 |
| 2 | Vacuum variable capacitor | 10-500 pF, >= 10 kV | 1 | $80-250 |
| 3 | Reduction drive or stepper motor | For remote capacitor tuning | 1 | $20-80 |
| 4 | RG-213 coaxial cable | 50 ohm, 15 m (coupling loop + feedline) | 1 | $25-40 |
| 5 | Coaxial connectors | PL-259, SO-239, barrel adapters | 4-6 | $10-20 |
| 6 | Capacitor housing | IP65 polycarbonate box, ~200x200x150 mm | 1 | $15-30 |
| 7 | Fibreglass mast | 6 m telescoping or sectional | 1 | $30-60 |
| 8 | Ground screen | 25 mm chicken wire, 4x4 m OR #14 Cu wire, 80 m | 1 | $15-25 |
| 9 | Mounting hardware | Nylon standoffs, SS bolts, cable ties | Assorted | $15-30 |
| 10 | Silver brazing alloy | BAg-5 or equiv., with flux | 1 kit | $15-25 |
| 11 | Weatherproofing | Silicone tape, heat-shrink, marine varnish | Assorted | $10-20 |
| 12 | Lightning arrester | Gas-discharge coaxial type | 1 | $15-25 |
| 13 | Common-mode choke | FT-240-43 toroid core | 1 | $8-12 |
| 14 | Ground rod and wire | 8 ft copper rod, #6 AWG wire | 1 | $15-25 |
| | **Total** | | | **$313-712** |

### 16.2 Tools Required (Not Included)

| Tool | Purpose |
|------|---------|
| Tube bender (5/8") | Forming the loop |
| MAPP gas or oxy-acetylene torch | Silver brazing joints |
| Multimeter | Checking continuity |
| SWR meter / antenna analyser | Tuning and matching |
| Soldering iron | Connector assembly |
| Drill, hole saw | Enclosure preparation |
| Wrenches, screwdrivers | General assembly |

### 16.3 Cost-Saving Options

| Substitution | Saving | Trade-off |
|--------------|--------|-----------|
| Surplus vacuum cap (hamfest/eBay) | $50-150 | May have limited life; test before use |
| Air variable cap (QRP only, < 25 W) | $40-80 | Cannot run 100 W due to voltage limit |
| Bamboo or wood mast | $0-15 | Shorter life, may need replacement |
| Soldered joints (silver solder) | $10 | Slightly higher loss (~5-10% degradation) |

---

## 17. Key Formulae

### 17.1 Loop Inductance

```
L = mu_0 * b * [ln(8b/a) - 2]
```

where:
- `mu_0 = 4*pi*10^-7 H/m` (permeability of free space)
- `b` = loop radius (m)
- `a` = tube outer radius (m)

### 17.2 Resonant Frequency

```
f = 1 / (2*pi*sqrt(L*C))
```

or equivalently, the tuning capacitance:

```
C = 1 / (4*pi^2 * f^2 * L)
```

### 17.3 Skin Depth

```
delta = 1 / sqrt(pi * f * mu_0 * sigma)
```

where `sigma = 5.8*10^7 S/m` for copper.

### 17.4 Radiation Resistance

```
R_rad = 31171 * (A / lambda^2)^2
```

where:
- `A = pi * b^2` (loop area, m^2)
- `lambda = c / f` (wavelength, m)
- The constant 31171 = 20*pi^2*(2*pi/c)^4 / mu_0 ... simplified to the standard form `R_rad = 31171*(A/lambda^2)^2` ohms.

Note: This is equivalent to `R_rad = 20*pi^2*(C_loop/lambda)^4` for a circular loop.

### 17.5 Loss Resistance

```
R_loss = (C_loop / (2*pi*a)) * R_s
```

where:
- `C_loop = 2*pi*b` (loop circumference, m)
- `a` = tube outer radius (m)
- `R_s = sqrt(pi*f*mu_0/sigma)` = surface resistivity (ohm/square)

Expanded:

```
R_loss = (C_loop / (2*pi*a)) * sqrt(pi*f*mu_0 / sigma)
```

### 17.6 Efficiency

```
eta = R_rad / (R_rad + R_loss)

eta_dB = 10 * log10(eta)
```

### 17.7 Q Factor

```
Q = 2*pi*f*L / (R_rad + R_loss) = X_L / R_total
```

### 17.8 Bandwidth

```
BW = f / Q
```

### 17.9 Capacitor Voltage

```
V_cap = sqrt(P * Q * X_L)
```

or equivalently:

```
I_loop = sqrt(P / R_total)
V_cap = I_loop * X_C = I_loop / (2*pi*f*C)
```

### 17.10 Array Factor (Vertical Loop over Ground)

```
AF(alpha) = 2 * |sin(kh * sin(alpha))|
```

where:
- `k = 2*pi/lambda` (wavenumber)
- `h` = loop centre height above ground (m)
- `alpha` = elevation angle (0 deg = horizon, 90 deg = zenith)

### 17.11 NVIS Coverage Radius

```
R_ground = 2 * h_iono / tan(alpha)
```

where:
- `h_iono` = ionospheric reflection height (~300 km for F2-layer)
- `alpha` = elevation angle

### 17.12 Free-Space Path Loss

```
FSPL (dB) = 20*log10(4*pi*d/lambda)
```

where `d` is the total path length (2 * h_iono for near-vertical incidence).

---

## 18. Validation Checklist

Use this checklist to verify the antenna after construction:

### 18.1 Pre-Assembly Checks

- [ ] Copper tube is free of kinks, dents, and deep scratches
- [ ] Loop circumference measures 6.28 +/- 0.05 m
- [ ] Loop diameter measures 2.00 +/- 0.02 m (check multiple axes)
- [ ] All brazed joints are smooth, shiny, and flux-free
- [ ] Capacitor moves freely through full range without binding
- [ ] Capacitor leads are < 25 mm total length
- [ ] Coupling loop diameter is 0.40 +/- 0.02 m
- [ ] Coupling loop shield gap is clean (no bridging strands)
- [ ] Coupling loop is centred at bottom of main loop

### 18.2 Electrical Checks (Antenna Analyser)

- [ ] Resonance detectable across full 80 m band (3.5-3.8 MHz) by adjusting capacitor
- [ ] Resonance detectable across full 40 m band (7.0-7.3 MHz)
- [ ] SWR < 2.0:1 at resonance on 40 m
- [ ] SWR < 3.0:1 at resonance on 80 m (higher due to lower efficiency)
- [ ] -3 dB bandwidth approximately 1.7-2.0 kHz on 80 m
- [ ] -3 dB bandwidth approximately 4.5-5.0 kHz on 40 m
- [ ] No spurious resonances between 3 and 8 MHz (indicates stray coupling)
- [ ] Resonant frequency changes smoothly with capacitor adjustment (no jumps)

### 18.3 NVIS-Specific Checks

- [ ] Loop mounted vertically, plane oriented N-S (or toward target coverage area)
- [ ] Centre height is 5.0 +/- 0.3 m above ground
- [ ] Ground screen is installed, bonded to station ground
- [ ] No metallic objects within 1 m of the loop (except mast fittings if non-metallic)
- [ ] Feedline runs away from the loop at 90 degrees for at least 3 m before turning
- [ ] Common-mode choke installed on feedline

### 18.4 On-Air Verification

- [ ] Signal reports from stations 50-300 km away are consistent with NVIS propagation
- [ ] Signals from > 500 km are weak or absent (confirming high-angle pattern)
- [ ] Signal strength varies with capacitor tuning (confirming narrow bandwidth)
- [ ] Rotating the loop (if mount allows) produces a null in the direction of the loop plane
- [ ] Received noise level drops when loop null is steered toward a noise source

### 18.5 Safety Verification

- [ ] No arcing or corona audible at the capacitor at 100 W
- [ ] Capacitor housing is sealed and secure
- [ ] Minimum 1.0 m clearance from loop to any accessible area during TX
- [ ] Lightning protection installed and bonded
- [ ] Feedline disconnect accessible for storm protection

---

## Appendix A: Quick Reference Card

```
+=====================================================================+
|             NVIS MAGNETIC LOOP ANTENNA - QUICK REFERENCE             |
+=====================================================================+
|                                                                     |
|  LOOP:  2.0 m dia. | 5/8" Type M Cu | L = 6.18 uH | A = 3.14 m^2 |
|  CAP:   77-335 pF vacuum variable, >= 10 kV                        |
|  FEED:  0.40 m Faraday-shielded coupling loop, 50 ohm              |
|  MOUNT: Vertical, 5.0 m centre height, N-S plane                   |
|  GROUND: 4x4 m chicken wire screen below                           |
|                                                                     |
+---------------------------------------------------------------------+
|  BAND   | FREQ    | C(pF)  | EFF(%) | BW(kHz) | Vcap(V) @ 100W    |
+---------+---------+--------+--------+---------+--------------------+
|  80 m   | 3.500   | 335    |   8.5  |  1.73   |  5,244             |
|  80 m   | 3.650   | 308    |   9.7  |  1.86   |  5,338             |
|  80 m   | 3.800   | 284    |  11.0  |  2.00   |  5,417             |
+---------+---------+--------+--------+---------+--------------------+
|  40 m   | 7.000   |  84    |  51.2  |  4.59   |  6,438             |
|  40 m   | 7.100   |  81    |  52.4  |  4.73   |  6,392             |
|  40 m   | 7.200   |  79    |  53.7  |  4.87   |  6,341             |
|  40 m   | 7.300   |  77    |  54.9  |  5.03   |  6,287             |
+---------+---------+--------+--------+---------+--------------------+
|                                                                     |
|  NVIS COVERAGE (F2 @ 300 km):                                      |
|    90 deg = 0 km     70 deg = 109 km    45 deg = 300 km            |
|    Peak at zenith    -3 dB cone: 44-47 deg to 90 deg               |
|                                                                     |
|  SAFETY: V_cap max = 6,438 V | Min clearance 1.0 m | Cap >= 10 kV |
|                                                                     |
+=====================================================================+
```

---

## Appendix B: NVIS Frequency Planning Guide

### B.1 Understanding NVIS Propagation Windows

NVIS propagation depends on the F2-layer critical frequency (foF2) -- the highest frequency that will be reflected when transmitted vertically. For NVIS to work, the operating frequency must be **below** foF2.

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| foF2 (daytime, solar max) | 8-12 MHz | Both bands supported |
| foF2 (daytime, solar min) | 4-7 MHz | 40 m may fail; 80 m works |
| foF2 (night-time, solar max) | 4-6 MHz | 40 m often fails at night |
| foF2 (night-time, solar min) | 2-4 MHz | Only 80 m (lower portion) |
| MUF(3000) | ~3.0 * foF2 | Maximum usable freq for 3000 km DX |

### B.2 Band-by-Band NVIS Planning

**80 m Band (3.500-3.800 MHz):**

| Time of Day | Season | Solar Activity | NVIS Reliability |
|-------------|--------|----------------|------------------|
| Day | Summer | High | Excellent |
| Day | Summer | Low | Good |
| Day | Winter | High | Good to Excellent |
| Day | Winter | Low | Good |
| Night | Summer | High | Good |
| Night | Summer | Low | Fair |
| Night | Winter | High | Fair |
| Night | Winter | Low | Poor (foF2 may drop below 3.5) |

**80 m is the most reliable NVIS band**, available nearly 24 hours under most conditions. It fails only during deep night-time in winter at solar minimum, when foF2 can drop below 3.5 MHz.

**40 m Band (7.000-7.300 MHz):**

| Time of Day | Season | Solar Activity | NVIS Reliability |
|-------------|--------|----------------|------------------|
| Day | Summer | High | Excellent |
| Day | Summer | Low | Fair to Good |
| Day | Winter | High | Good |
| Day | Winter | Low | Fair |
| Night | Any | High | Poor (foF2 often < 7 MHz) |
| Night | Any | Low | Fail (foF2 < 7 MHz) |

**40 m NVIS is primarily a daytime mode.** At night, the F2-layer critical frequency typically drops below 7 MHz, and signals pass through the ionosphere instead of being reflected. However, during high solar activity, 40 m NVIS can persist for several hours after sunset.

### B.3 Recommended Operating Schedule

| Time (Local) | Recommended Band | Notes |
|--------------|-----------------|-------|
| 06:00-09:00 | 80 m or 40 m | 80 m for certainty; 40 m once foF2 rises |
| 09:00-17:00 | 40 m preferred | Higher efficiency; lower noise; foF2 usually > 7 |
| 17:00-20:00 | 40 m or 80 m | Transition; monitor foF2 |
| 20:00-06:00 | 80 m only | foF2 below 7 MHz in most conditions |

### B.4 Monitoring foF2

To determine real-time NVIS propagation conditions:

1. **Ionosonde data:** Check real-time foF2 from the nearest ionosonde station. Data is available from national space weather services (e.g., NOAA/SWPC, BOM/SWS, DIAS).
2. **Beacon monitoring:** Tune to known NVIS frequencies and listen for beacon stations. If you can hear them, NVIS is working.
3. **Solar indices:** The solar flux index (SFI) and sunspot number (SSN) provide long-term guidance:
   - SFI > 120: Both bands likely supported during day.
   - SFI 80-120: 40 m daytime only; 80 m nearly all day.
   - SFI < 80: 80 m primary; 40 m may fail.

### B.5 NVIS Frequency Selection Tips

1. **Use the highest frequency that foF2 supports.** Higher frequencies have lower D-layer absorption (less signal loss) and the loop antenna has much higher efficiency on 40 m than 80 m.
2. **On 80 m, use the lower portion of the band (3.5-3.6 MHz)** during periods of low solar activity, as foF2 may not support frequencies above 3.8 MHz.
3. **Avoid frequencies near foF2.** Signals at frequencies within 10-15% of foF2 experience increased absorption and fading. If foF2 is 7.5 MHz, operate at 7.0 MHz rather than 7.3 MHz.
4. **For emergency use, plan for 80 m.** It is the most reliable NVIS band across all conditions. The antenna's lower efficiency on 80 m is compensated by its near-universal propagation availability.

### B.6 Seasonal NVIS Calendar (Mid-Latitudes)

```
         J   F   M   A   M   J   J   A   S   O   N   D
80m Day  |===|===|===|===|===|===|===|===|===|===|===|===|  Always
80m Nite |== |== |===|===|===|===|===|===|===|== |== |== |  Mostly
40m Day  |=  |== |===|===|===|===|===|===|===|== |=  |=  |  Spring-Autumn
40m Nite |   |   |   |=  |=  |== |== |=  |=  |   |   |   |  Summer solar max only

Legend: === Excellent  == Good  = Fair  (blank) Poor/Fail
Note: Solar maximum conditions assumed. At solar minimum, reduce all ratings by one level.
```

---

## Document Information

| Field | Value |
|-------|-------|
| Design class | Ground-up NVIS, balanced size/efficiency |
| Loop diameter | 2.0 m |
| Bands | 80 m (3.500-3.800 MHz), 40 m (7.000-7.300 MHz) |
| Primary mode | NVIS (0-500 km regional coverage) |
| Mounting | Vertical loop, 5.0 m centre height |
| Ground enhancement | 4x4 m screen |
| Design basis | Analytical (small-loop theory + image theory) |
| Assumptions | PEC ground for pattern calculations; real copper losses |

---

*End of document.*
