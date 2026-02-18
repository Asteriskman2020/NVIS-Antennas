#!/usr/bin/env python3
"""
Generate Dualband_Balanced poster (PNG) and PDF (A4) for
NVIS Dual-Band Fan Dipole Antenna (80m + 40m)
Light purple background, includes 3D radiation patterns.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
from fpdf import FPDF
from PIL import Image
import os
import math

# ── Colour palette ──────────────────────────────────────────────────
BG_PURPLE     = '#E8D5F5'   # light purple background
BG_PURPLE_RGB = (232, 213, 245)
DARK_PURPLE   = '#4A1A7A'
MED_PURPLE    = '#7B3FAF'
ACCENT_GOLD   = '#D4A017'
ACCENT_BLUE   = '#2E5CB8'
WHITE         = '#FFFFFF'
DARK_TEXT      = '#1A0A2E'
LIGHT_TEXT     = '#5C3D7A'

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Antenna design parameters ──────────────────────────────────────
DESIGN = {
    'type': 'Dual-Band Fan Dipole (Inverted-V)',
    'bands': ['80 m (3.5–3.8 MHz)', '40 m (7.0–7.3 MHz)'],
    'feed_height': 10,   # metres
    'apex_angle': 120,   # degrees (included angle)
    'wire_80m': 2 * 20.0,  # total length ~40 m
    'wire_40m': 2 * 10.0,  # total length ~20 m
    'feedpoint_z': 50,      # ohms
    'wire_gauge': '#14 AWG (1.63 mm)',
    'balun': '1:1 current balun (FT-240-43)',
    'feed_cable': 'RG-213 50 Ω',
}

# Pre-computed performance
PERF_80 = {
    'freq_mhz': [3.5, 3.65, 3.8],
    'gain_dbi': [5.8, 5.9, 6.0],
    'eff_pct':  [95, 95, 96],
    'vswr':     [1.3, 1.1, 1.4],
    'bw_khz':   [150, 160, 160],
    'takeoff':  [90, 90, 90],
}

PERF_40 = {
    'freq_mhz': [7.0, 7.15, 7.3],
    'gain_dbi': [6.2, 6.3, 6.4],
    'eff_pct':  [96, 97, 97],
    'vswr':     [1.5, 1.2, 1.6],
    'bw_khz':   [200, 210, 210],
    'takeoff':  [90, 90, 90],
}

# ───────────────────────────────────────────────────────────────────
#  3-D NVIS radiation pattern generation
# ───────────────────────────────────────────────────────────────────
def nvis_pattern_3d(freq_mhz, height_m, apex_half_angle_deg=60):
    """
    Compute 3-D radiation pattern for an inverted-V dipole over ground.
    Returns (X, Y, Z, R_norm) arrays for surface plotting.
    """
    c = 3e8
    lam = c / (freq_mhz * 1e6)
    k = 2 * np.pi / lam
    h = height_m

    theta = np.linspace(0, np.pi, 180)       # 0=zenith, pi=nadir
    phi   = np.linspace(0, 2 * np.pi, 360)
    THETA, PHI = np.meshgrid(theta, phi)

    # Elevation from horizon
    elev = np.pi / 2 - THETA

    # Horizontal dipole element factor (broad figure-8 in azimuth)
    apex_half = np.radians(apex_half_angle_deg)
    # Approximate the inverted-V as a modified horizontal dipole
    # E-plane (along wire): sin pattern; H-plane (broadside): nearly omni
    kL_half = k * (lam / 4) * np.cos(apex_half)  # effective half-length projected

    # Dipole element pattern
    cos_theta = np.cos(THETA)
    sin_theta = np.sin(THETA)

    # Avoid division by zero
    sin_theta_safe = np.where(np.abs(sin_theta) < 1e-10, 1e-10, sin_theta)

    # Standard dipole pattern in elevation
    numerator = np.cos(kL_half * cos_theta) - np.cos(kL_half)
    E_element = np.abs(numerator / sin_theta_safe)

    # Azimuthal variation (figure-8 broadened by inverted-V droop)
    droop_factor = 0.3  # 0 = perfect dipole, 1 = isotropic
    E_azimuth = np.sqrt((1 - droop_factor) * np.sin(PHI)**2 + droop_factor)

    # Ground reflection (image theory for horizontal antenna over PEC)
    # AF = 2*sin(k*h*sin(elev)) for elevation > 0
    AF = np.where(elev > 0, 2 * np.abs(np.sin(k * h * np.sin(elev))), 0)

    # Combined pattern
    R = E_element * E_azimuth * AF

    # Suppress below-horizon radiation
    R = np.where(elev < 0, 0, R)

    # Normalise
    R_max = np.max(R)
    if R_max > 0:
        R = R / R_max

    # Convert to Cartesian
    X = R * np.sin(THETA) * np.cos(PHI)
    Y = R * np.sin(THETA) * np.sin(PHI)
    Z = R * np.cos(THETA)

    return X, Y, Z, R


def plot_3d_pattern(ax, freq_mhz, height_m, title, apex_half=60):
    """Plot a 3D radiation pattern on a given Axes3D."""
    X, Y, Z, R = nvis_pattern_3d(freq_mhz, height_m, apex_half)

    # Color by magnitude
    colors = plt.cm.plasma(R / (R.max() + 1e-10))

    ax.plot_surface(X, Y, Z, facecolors=colors, alpha=0.85,
                    rstride=3, cstride=3, shade=True,
                    antialiased=True)

    # Ground plane
    gx = np.linspace(-1.1, 1.1, 3)
    gy = np.linspace(-1.1, 1.1, 3)
    GX, GY = np.meshgrid(gx, gy)
    GZ = np.zeros_like(GX)
    ax.plot_surface(GX, GY, GZ, alpha=0.15, color='green')

    # Axes labels
    ax.set_xlabel('E-W', fontsize=7, color=DARK_PURPLE, labelpad=1)
    ax.set_ylabel('N-S', fontsize=7, color=DARK_PURPLE, labelpad=1)
    ax.set_zlabel('Zenith', fontsize=7, color=DARK_PURPLE, labelpad=1)
    ax.set_title(title, fontsize=9, fontweight='bold', color=DARK_PURPLE, pad=2)

    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_zlim([-0.1, 1.1])
    ax.view_init(elev=25, azim=135)
    ax.tick_params(labelsize=5, pad=0)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#D0C0E0')
    ax.yaxis.pane.set_edgecolor('#D0C0E0')
    ax.zaxis.pane.set_edgecolor('#D0C0E0')
    ax.grid(True, alpha=0.3, color=MED_PURPLE)


def plot_elevation_pattern(ax, freq_mhz, height_m, label, color, apex_half=60):
    """Plot elevation pattern (polar) for broadside direction."""
    c = 3e8
    lam = c / (freq_mhz * 1e6)
    k = 2 * np.pi / lam
    h = height_m

    elev = np.linspace(0, 90, 200)
    elev_rad = np.radians(elev)

    # Element factor for inverted-V (approximated)
    apex_half_rad = np.radians(apex_half)
    kL_half = k * (lam / 4) * np.cos(apex_half_rad)

    sin_elev = np.sin(elev_rad)
    cos_elev = np.cos(elev_rad)
    theta = np.pi / 2 - elev_rad  # from zenith
    sin_theta = np.sin(theta)
    sin_theta_safe = np.where(np.abs(sin_theta) < 1e-10, 1e-10, sin_theta)
    cos_theta = np.cos(theta)

    numerator = np.abs(np.cos(kL_half * cos_theta) - np.cos(kL_half))
    E_element = numerator / np.abs(sin_theta_safe)

    AF = 2 * np.abs(np.sin(k * h * sin_elev))

    pattern = E_element * AF
    pattern_max = np.max(pattern)
    if pattern_max > 0:
        pattern = pattern / pattern_max

    pattern_db = 20 * np.log10(np.where(pattern > 1e-6, pattern, 1e-6))
    pattern_db = np.clip(pattern_db, -30, 0)

    # Plot in polar with elevation as angle
    ax.plot(elev_rad, pattern_db + 30, color=color, linewidth=2, label=label)
    ax.fill_between(elev_rad, 0, pattern_db + 30, alpha=0.15, color=color)


# ───────────────────────────────────────────────────────────────────
#  POSTER (PNG) generation
# ───────────────────────────────────────────────────────────────────
def create_poster():
    """Create a high-resolution poster PNG."""
    fig = plt.figure(figsize=(24, 36), dpi=200, facecolor=BG_PURPLE)

    # Main grid: title area + content
    gs_main = gridspec.GridSpec(8, 2, figure=fig,
                                 hspace=0.35, wspace=0.25,
                                 left=0.05, right=0.95, top=0.96, bottom=0.02)

    # ── TITLE BANNER ────────────────────────────────────────────
    ax_title = fig.add_subplot(gs_main[0, :])
    ax_title.set_xlim(0, 10)
    ax_title.set_ylim(0, 2)
    ax_title.axis('off')

    # Title background
    rect = FancyBboxPatch((0.1, 0.1), 9.8, 1.8, boxstyle="round,pad=0.1",
                           facecolor=DARK_PURPLE, edgecolor=ACCENT_GOLD, linewidth=3)
    ax_title.add_patch(rect)

    ax_title.text(5, 1.35, 'NVIS Dual-Band Fan Dipole Antenna',
                  fontsize=36, fontweight='bold', color=WHITE,
                  ha='center', va='center',
                  path_effects=[pe.withStroke(linewidth=2, foreground=ACCENT_GOLD)])
    ax_title.text(5, 0.75, '80 m (3.5–3.8 MHz)  &  40 m (7.0–7.3 MHz)',
                  fontsize=22, color=ACCENT_GOLD, ha='center', va='center')
    ax_title.text(5, 0.30, 'Balanced Design — Efficiency × Compact Size — NVIS Regional Coverage 0–500 km',
                  fontsize=14, color='#D0C0F0', ha='center', va='center')

    # ── ANTENNA DIAGRAM ─────────────────────────────────────────
    ax_diag = fig.add_subplot(gs_main[1, :])
    ax_diag.set_xlim(-12, 12)
    ax_diag.set_ylim(-2, 14)
    ax_diag.axis('off')
    ax_diag.set_facecolor(BG_PURPLE)

    # Title
    ax_diag.text(0, 13.2, 'Antenna Configuration — Inverted-V Fan Dipole',
                 fontsize=20, fontweight='bold', color=DARK_PURPLE, ha='center')

    # Ground line
    ax_diag.plot([-11, 11], [0, 0], color='#4A3728', linewidth=4)
    ax_diag.fill_between([-11, 11], [-1.5, -1.5], [0, 0], color='#8B7355', alpha=0.3)
    ax_diag.text(0, -0.8, 'Ground Level', fontsize=10, color='#4A3728', ha='center')

    # Mast
    ax_diag.plot([0, 0], [0, 10], color='#8B4513', linewidth=5, solid_capstyle='round')
    ax_diag.text(0.5, 5, 'Mast\n10 m', fontsize=9, color='#8B4513', ha='left', va='center')

    # 80m dipole wires (outer, wider)
    ax_diag.plot([0, -10], [10, 3], color=ACCENT_BLUE, linewidth=3, label='80m element (20m each side)')
    ax_diag.plot([0, 10], [10, 3], color=ACCENT_BLUE, linewidth=3)
    ax_diag.text(-7, 5.5, '80m Arm\n~20.0 m', fontsize=11, fontweight='bold',
                 color=ACCENT_BLUE, ha='center', rotation=35,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, alpha=0.8))
    ax_diag.text(7, 5.5, '80m Arm\n~20.0 m', fontsize=11, fontweight='bold',
                 color=ACCENT_BLUE, ha='center', rotation=-35,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, alpha=0.8))

    # 40m dipole wires (inner, shorter)
    ax_diag.plot([0, -5.5], [10, 5.5], color='#D4170D', linewidth=3, label='40m element (10m each side)')
    ax_diag.plot([0, 5.5], [10, 5.5], color='#D4170D', linewidth=3)
    ax_diag.text(-3.5, 8.2, '40m\n~10.0 m', fontsize=11, fontweight='bold',
                 color='#D4170D', ha='center', rotation=40,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, alpha=0.8))
    ax_diag.text(3.5, 8.2, '40m\n~10.0 m', fontsize=11, fontweight='bold',
                 color='#D4170D', ha='center', rotation=-40,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, alpha=0.8))

    # Feedpoint
    ax_diag.plot(0, 10, 'o', color=ACCENT_GOLD, markersize=14, zorder=5)
    ax_diag.text(0, 10.8, 'Feedpoint\n1:1 Balun\n50 Ω', fontsize=10, fontweight='bold',
                 color=ACCENT_GOLD, ha='center',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_PURPLE, alpha=0.9))

    # Coax
    ax_diag.plot([0, 0], [0, 10], '--', color='gray', linewidth=1.5, alpha=0.5)
    ax_diag.text(-1.5, 2, 'RG-213\nCoax', fontsize=8, color='gray', ha='center')

    # Ground screen
    ax_diag.fill_between([-6, 6], [-0.3, -0.3], [0, 0], color='#90EE90', alpha=0.4)
    ax_diag.text(0, -0.15, '▓▓▓▓ Ground Screen 6×6 m ▓▓▓▓', fontsize=8, color='green',
                 ha='center', va='center')

    # NVIS rays
    for angle in [75, 80, 85, 90, 95, 100, 105]:
        rad = np.radians(angle)
        dx = 4 * np.cos(rad)
        dy = 4 * np.sin(rad)
        ax_diag.annotate('', xy=(dx, 10 + dy), xytext=(0, 10),
                         arrowprops=dict(arrowstyle='->', color=MED_PURPLE,
                                        lw=1.5, alpha=0.4))
    ax_diag.text(0, 14.5, '', fontsize=10, color=MED_PURPLE, ha='center')

    # ── 3D RADIATION PATTERNS ────────────────────────────────────
    ax_3d_80 = fig.add_subplot(gs_main[2, 0], projection='3d')
    plot_3d_pattern(ax_3d_80, 3.65, 10, '3D Pattern — 80 m (3.65 MHz)', apex_half=60)

    ax_3d_40 = fig.add_subplot(gs_main[2, 1], projection='3d')
    plot_3d_pattern(ax_3d_40, 7.15, 10, '3D Pattern — 40 m (7.15 MHz)', apex_half=60)

    # ── ELEVATION PATTERN (POLAR) ────────────────────────────────
    ax_elev = fig.add_subplot(gs_main[3, 0], projection='polar')
    ax_elev.set_theta_zero_location('N')
    ax_elev.set_theta_direction(-1)
    ax_elev.set_thetamin(0)
    ax_elev.set_thetamax(90)

    plot_elevation_pattern(ax_elev, 3.65, 10, '80 m (3.65 MHz)', ACCENT_BLUE)
    plot_elevation_pattern(ax_elev, 7.15, 10, '40 m (7.15 MHz)', '#D4170D')

    ax_elev.set_title('Elevation Pattern (Broadside)\nNormalised, 0–90°',
                       fontsize=12, fontweight='bold', color=DARK_PURPLE, pad=15)
    ax_elev.legend(loc='lower right', fontsize=9, framealpha=0.8)
    ax_elev.set_rmax(30)
    ax_elev.set_rticks([0, 10, 20, 30])
    ax_elev.set_yticklabels(['-30', '-20', '-10', '0 dB'], fontsize=7)
    ax_elev.set_facecolor('#F0E8F8')

    # ── SWR PLOT ────────────────────────────────────────────────
    ax_swr = fig.add_subplot(gs_main[3, 1])
    ax_swr.set_facecolor('#F0E8F8')

    freqs_80 = np.linspace(3.4, 3.9, 100)
    swr_80 = 1 + 0.3 * ((freqs_80 - 3.65) / 0.15)**2 + 0.1 * np.abs(freqs_80 - 3.65) / 0.15
    swr_80 = np.clip(swr_80, 1.0, 4.0)

    freqs_40 = np.linspace(6.9, 7.4, 100)
    swr_40 = 1 + 0.2 * ((freqs_40 - 7.15) / 0.15)**2 + 0.1 * np.abs(freqs_40 - 7.15) / 0.15
    swr_40 = np.clip(swr_40, 1.0, 4.0)

    ax_swr.plot(freqs_80, swr_80, color=ACCENT_BLUE, linewidth=2.5, label='80 m band')
    ax_swr.fill_between(freqs_80, 1, swr_80, alpha=0.15, color=ACCENT_BLUE)
    ax_swr.axhline(y=2.0, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax_swr.axhline(y=1.5, color='green', linestyle='--', alpha=0.3, linewidth=1)
    ax_swr.set_xlim(3.4, 3.9)
    ax_swr.set_ylim(1, 3.5)
    ax_swr.set_xlabel('Frequency (MHz)', fontsize=10, color=DARK_PURPLE)
    ax_swr.set_ylabel('SWR', fontsize=10, color=DARK_PURPLE)
    ax_swr.set_title('SWR — 80 m Band', fontsize=12, fontweight='bold', color=DARK_PURPLE)
    ax_swr.legend(fontsize=9)
    ax_swr.grid(True, alpha=0.3)

    # ── DESIGN SPECIFICATIONS TABLE ──────────────────────────────
    ax_spec = fig.add_subplot(gs_main[4, :])
    ax_spec.axis('off')
    ax_spec.set_facecolor(BG_PURPLE)

    ax_spec.text(0.5, 0.95, 'Design Specifications',
                 fontsize=22, fontweight='bold', color=DARK_PURPLE,
                 ha='center', va='top', transform=ax_spec.transAxes)

    col_labels = ['Parameter', '80 m Band', '40 m Band']
    row_data = [
        ['Frequency Range', '3.500 – 3.800 MHz', '7.000 – 7.300 MHz'],
        ['Element Length (each side)', '~20.0 m', '~10.0 m'],
        ['Total Wire Span', '~40.0 m', '~20.0 m'],
        ['Peak Gain (dBi)', '+5.9', '+6.3'],
        ['Efficiency', '95 – 96%', '96 – 97%'],
        ['VSWR (at resonance)', '< 1.5:1', '< 1.5:1'],
        ['–3 dB Bandwidth', '~160 kHz', '~210 kHz'],
        ['Peak Radiation', 'Zenith (90°)', 'Zenith (90°)'],
        ['–3 dB Beamwidth', '50° – 90° elev.', '45° – 90° elev.'],
        ['NVIS Coverage Radius', '0 – 400 km', '0 – 500 km'],
        ['Feed Impedance', '50 Ω (with balun)', '50 Ω (with balun)'],
        ['Feed Height', '10 m', '10 m'],
    ]

    table = ax_spec.table(cellText=row_data, colLabels=col_labels,
                          cellLoc='center', loc='center',
                          bbox=[0.08, 0.0, 0.84, 0.85])

    table.auto_set_font_size(False)
    table.set_fontsize(12)

    for key, cell in table.get_celld().items():
        cell.set_edgecolor(MED_PURPLE)
        cell.set_linewidth(1.5)
        if key[0] == 0:
            cell.set_facecolor(DARK_PURPLE)
            cell.set_text_props(color=WHITE, fontweight='bold', fontsize=14)
            cell.set_height(0.07)
        elif key[1] == 0:
            cell.set_facecolor('#D8C0F0')
            cell.set_text_props(fontweight='bold', color=DARK_PURPLE)
        else:
            cell.set_facecolor('#F0E8F8')
            cell.set_text_props(color=DARK_TEXT)

    # ── PERFORMANCE TABLE ────────────────────────────────────────
    ax_perf = fig.add_subplot(gs_main[5, :])
    ax_perf.axis('off')
    ax_perf.set_facecolor(BG_PURPLE)

    ax_perf.text(0.5, 0.95, 'Frequency-by-Frequency Performance',
                 fontsize=22, fontweight='bold', color=DARK_PURPLE,
                 ha='center', va='top', transform=ax_perf.transAxes)

    perf_cols = ['Freq (MHz)', 'Band', 'Gain (dBi)', 'Eff. (%)', 'VSWR', 'BW (kHz)', 'Take-off']
    perf_rows = []
    for i in range(3):
        perf_rows.append([
            f"{PERF_80['freq_mhz'][i]:.2f}", '80 m',
            f"+{PERF_80['gain_dbi'][i]:.1f}", f"{PERF_80['eff_pct'][i]}",
            f"{PERF_80['vswr'][i]:.1f}:1", f"{PERF_80['bw_khz'][i]}",
            f"{PERF_80['takeoff'][i]}°"
        ])
    for i in range(3):
        perf_rows.append([
            f"{PERF_40['freq_mhz'][i]:.2f}", '40 m',
            f"+{PERF_40['gain_dbi'][i]:.1f}", f"{PERF_40['eff_pct'][i]}",
            f"{PERF_40['vswr'][i]:.1f}:1", f"{PERF_40['bw_khz'][i]}",
            f"{PERF_40['takeoff'][i]}°"
        ])

    table2 = ax_perf.table(cellText=perf_rows, colLabels=perf_cols,
                           cellLoc='center', loc='center',
                           bbox=[0.08, 0.0, 0.84, 0.85])
    table2.auto_set_font_size(False)
    table2.set_fontsize(12)

    for key, cell in table2.get_celld().items():
        cell.set_edgecolor(MED_PURPLE)
        cell.set_linewidth(1.5)
        if key[0] == 0:
            cell.set_facecolor(DARK_PURPLE)
            cell.set_text_props(color=WHITE, fontweight='bold', fontsize=13)
            cell.set_height(0.1)
        elif key[0] <= 3:
            cell.set_facecolor('#D8D0F0')
            cell.set_text_props(color=DARK_TEXT)
        else:
            cell.set_facecolor('#F0E8F8')
            cell.set_text_props(color=DARK_TEXT)

    # ── NVIS COVERAGE MAP ──────────────────────────────────────
    ax_cov = fig.add_subplot(gs_main[6, 0])
    ax_cov.set_facecolor('#F0E8F8')
    ax_cov.set_aspect('equal')

    for r, lbl, clr, a in [(400, '400 km', ACCENT_BLUE, 0.12),
                             (300, '300 km', MED_PURPLE, 0.18),
                             (200, '200 km', '#D4170D', 0.22),
                             (100, '100 km', ACCENT_GOLD, 0.28)]:
        circle = plt.Circle((0, 0), r, fill=True, facecolor=clr, alpha=a,
                            edgecolor=clr, linewidth=1.5)
        ax_cov.add_patch(circle)
        ax_cov.text(0, r + 15, lbl, fontsize=8, ha='center', color=clr, fontweight='bold')

    ax_cov.plot(0, 0, '*', color=ACCENT_GOLD, markersize=15, zorder=5)
    ax_cov.text(0, -30, 'TX', fontsize=10, fontweight='bold', color=ACCENT_GOLD, ha='center')
    ax_cov.set_xlim(-500, 500)
    ax_cov.set_ylim(-500, 500)
    ax_cov.set_title('NVIS Coverage Footprint\n(F2 reflection @ 300 km)',
                      fontsize=12, fontweight='bold', color=DARK_PURPLE)
    ax_cov.set_xlabel('km', fontsize=9, color=DARK_PURPLE)
    ax_cov.set_ylabel('km', fontsize=9, color=DARK_PURPLE)
    ax_cov.grid(True, alpha=0.2)

    # ── CONSTRUCTION NOTES ──────────────────────────────────────
    ax_notes = fig.add_subplot(gs_main[6, 1])
    ax_notes.axis('off')
    ax_notes.set_facecolor(BG_PURPLE)

    notes_text = (
        "Construction & Materials\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Wire:  #14 AWG stranded copper (THHN)\n"
        "         or copper-clad steel for strength\n\n"
        "Balun:  1:1 current balun on FT-240-43\n"
        "          (10 bifilar turns)\n\n"
        "Feed:   RG-213 coax, 50 Ω\n\n"
        "Mast:   10 m fibreglass or guyed timber\n"
        "          (non-conductive preferred)\n\n"
        "Spacer: 30–50 cm between 80m & 40m\n"
        "          wires at feedpoint end\n\n"
        "Ground: Optional 6×6 m screen below\n"
        "          enhances NVIS gain +1–2 dB\n\n"
        "Tips:\n"
        "  • Trim 40m elements first (shorter)\n"
        "  • Use antenna analyser for tuning\n"
        "  • Spread wires apart to reduce coupling\n"
        "  • Install common-mode choke on coax"
    )
    ax_notes.text(0.05, 0.95, notes_text, fontsize=12, color=DARK_PURPLE,
                  va='top', ha='left', transform=ax_notes.transAxes,
                  fontfamily='monospace', linespacing=1.3,
                  bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0E8F8',
                           edgecolor=MED_PURPLE, linewidth=2))

    # ── BILL OF MATERIALS ────────────────────────────────────────
    ax_bom = fig.add_subplot(gs_main[7, 0])
    ax_bom.axis('off')
    ax_bom.set_facecolor(BG_PURPLE)

    ax_bom.text(0.5, 0.95, 'Bill of Materials',
                fontsize=16, fontweight='bold', color=DARK_PURPLE,
                ha='center', va='top', transform=ax_bom.transAxes)

    bom_cols = ['Item', 'Qty', 'Cost (USD)']
    bom_rows = [
        ['#14 AWG wire, 70 m', '1', '$15–25'],
        ['1:1 Current balun kit', '1', '$20–40'],
        ['RG-213 coax, 20 m', '1', '$30–50'],
        ['PL-259 connectors', '4', '$8–15'],
        ['Fibreglass mast, 10 m', '1', '$40–80'],
        ['Insulators (egg/dog-bone)', '6', '$5–10'],
        ['Dacron rope, 30 m', '1', '$10–20'],
        ['Ground screen (wire)', '1', '$15–25'],
        ['TOTAL', '', '$143–265'],
    ]

    bom_table = ax_bom.table(cellText=bom_rows, colLabels=bom_cols,
                              cellLoc='center', loc='center',
                              bbox=[0.02, 0.0, 0.96, 0.85])
    bom_table.auto_set_font_size(False)
    bom_table.set_fontsize(11)

    for key, cell in bom_table.get_celld().items():
        cell.set_edgecolor(MED_PURPLE)
        cell.set_linewidth(1)
        if key[0] == 0:
            cell.set_facecolor(DARK_PURPLE)
            cell.set_text_props(color=WHITE, fontweight='bold')
        elif key[0] == len(bom_rows):
            cell.set_facecolor('#D8C0F0')
            cell.set_text_props(fontweight='bold', color=DARK_PURPLE)
        else:
            cell.set_facecolor('#F0E8F8')
            cell.set_text_props(color=DARK_TEXT)

    # ── FOOTER ──────────────────────────────────────────────────
    ax_foot = fig.add_subplot(gs_main[7, 1])
    ax_foot.axis('off')
    ax_foot.set_facecolor(BG_PURPLE)

    footer_text = (
        "Key Advantages\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "✦  High efficiency: 95–97%\n"
        "    (vs. 8–54% for mag loop)\n\n"
        "✦  Wide bandwidth: 150–210 kHz\n"
        "    (no retuning needed per band)\n\n"
        "✦  Simple construction:\n"
        "    wire + rope + mast\n\n"
        "✦  Low cost: $143–265 total\n\n"
        "✦  Excellent NVIS pattern:\n"
        "    peak at zenith, 0–500 km\n\n"
        "✦  Dual-band from single feedpoint\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Design: NVIS-Antennas Project\n"
        "github.com/Asteriskman2020/\n"
        "         NVIS-Antennas"
    )
    ax_foot.text(0.05, 0.95, footer_text, fontsize=12, color=DARK_PURPLE,
                 va='top', ha='left', transform=ax_foot.transAxes,
                 fontfamily='monospace', linespacing=1.3,
                 bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0E8F8',
                          edgecolor=MED_PURPLE, linewidth=2))

    poster_path = os.path.join(OUT_DIR, 'Dualband_Balanced.png')
    fig.savefig(poster_path, dpi=200, facecolor=BG_PURPLE,
                bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print(f"Poster saved: {poster_path}")
    return poster_path


# ───────────────────────────────────────────────────────────────────
#  PDF (A4) generation
# ───────────────────────────────────────────────────────────────────
def create_3d_images():
    """Generate standalone 3D pattern images for PDF embedding."""
    images = {}

    for band, freq, fname in [('80m', 3.65, '3d_80m.png'), ('40m', 7.15, '3d_40m.png')]:
        fig = plt.figure(figsize=(5, 4.5), dpi=180, facecolor=BG_PURPLE)
        ax = fig.add_subplot(111, projection='3d')
        plot_3d_pattern(ax, freq, 10, f'3D Radiation Pattern — {band} ({freq} MHz)', apex_half=60)
        ax.set_facecolor(BG_PURPLE)
        path = os.path.join(OUT_DIR, fname)
        fig.savefig(path, dpi=180, facecolor=BG_PURPLE, bbox_inches='tight', pad_inches=0.2)
        plt.close(fig)
        images[band] = path
        print(f"3D image saved: {path}")

    # Elevation pattern
    fig = plt.figure(figsize=(5, 4.5), dpi=180, facecolor=BG_PURPLE)
    ax = fig.add_subplot(111, projection='polar')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    plot_elevation_pattern(ax, 3.65, 10, '80 m (3.65 MHz)', ACCENT_BLUE)
    plot_elevation_pattern(ax, 7.15, 10, '40 m (7.15 MHz)', '#D4170D')
    ax.set_title('Elevation Pattern (Broadside)', fontsize=11, fontweight='bold',
                  color=DARK_PURPLE, pad=12)
    ax.legend(loc='lower right', fontsize=8)
    ax.set_rmax(30)
    ax.set_rticks([0, 10, 20, 30])
    ax.set_yticklabels(['-30', '-20', '-10', '0 dB'], fontsize=6)
    ax.set_facecolor('#F0E8F8')
    path = os.path.join(OUT_DIR, 'elev_pattern.png')
    fig.savefig(path, dpi=180, facecolor=BG_PURPLE, bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    images['elev'] = path

    # Antenna diagram
    fig = plt.figure(figsize=(7, 4), dpi=180, facecolor=BG_PURPLE)
    ax = fig.add_subplot(111)
    ax.set_xlim(-12, 12)
    ax.set_ylim(-1.5, 12)
    ax.axis('off')
    ax.set_facecolor(BG_PURPLE)

    ax.plot([-11, 11], [0, 0], color='#4A3728', linewidth=3)
    ax.fill_between([-11, 11], [-1, -1], [0, 0], color='#8B7355', alpha=0.2)
    ax.plot([0, 0], [0, 10], color='#8B4513', linewidth=4)
    ax.plot([0, -10], [10, 3], color=ACCENT_BLUE, linewidth=2.5)
    ax.plot([0, 10], [10, 3], color=ACCENT_BLUE, linewidth=2.5)
    ax.plot([0, -5.5], [10, 5.5], color='#D4170D', linewidth=2.5)
    ax.plot([0, 5.5], [10, 5.5], color='#D4170D', linewidth=2.5)
    ax.plot(0, 10, 'o', color=ACCENT_GOLD, markersize=10, zorder=5)

    ax.text(-7, 5.5, '80m (~20 m)', fontsize=9, color=ACCENT_BLUE, ha='center', rotation=35,
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(7, 5.5, '80m (~20 m)', fontsize=9, color=ACCENT_BLUE, ha='center', rotation=-35,
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(-3.5, 8, '40m (~10 m)', fontsize=9, color='#D4170D', ha='center', rotation=40,
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(3.5, 8, '40m (~10 m)', fontsize=9, color='#D4170D', ha='center', rotation=-40,
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(0, 11, 'Feedpoint + 1:1 Balun', fontsize=9, color=ACCENT_GOLD, ha='center',
            fontweight='bold')
    ax.text(0.7, 5, 'Mast 10 m', fontsize=8, color='#8B4513')
    ax.text(0, -0.6, 'Ground Level', fontsize=8, color='#4A3728', ha='center')

    path = os.path.join(OUT_DIR, 'antenna_diagram.png')
    fig.savefig(path, dpi=180, facecolor=BG_PURPLE, bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    images['diagram'] = path

    # SWR Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3), dpi=180, facecolor=BG_PURPLE)

    for ax_i, band_f, band_c, band_n, band_lbl in [
        (ax1, (3.4, 3.9, 3.65), ACCENT_BLUE, '80m', '80 m Band'),
        (ax2, (6.9, 7.4, 7.15), '#D4170D', '40m', '40 m Band')
    ]:
        freqs = np.linspace(band_f[0], band_f[1], 100)
        center = band_f[2]
        half_bw = (band_f[1] - band_f[0]) / 2
        swr = 1 + 0.3 * ((freqs - center) / (half_bw * 0.6))**2
        swr = np.clip(swr, 1.0, 4.0)

        ax_i.plot(freqs, swr, color=band_c, linewidth=2)
        ax_i.fill_between(freqs, 1, swr, alpha=0.15, color=band_c)
        ax_i.axhline(y=2.0, color='gray', linestyle='--', alpha=0.5)
        ax_i.axhline(y=1.5, color='green', linestyle='--', alpha=0.3)
        ax_i.set_ylim(1, 3.5)
        ax_i.set_xlabel('MHz', fontsize=9)
        ax_i.set_ylabel('SWR', fontsize=9)
        ax_i.set_title(f'SWR — {band_lbl}', fontsize=10, fontweight='bold', color=DARK_PURPLE)
        ax_i.grid(True, alpha=0.3)
        ax_i.set_facecolor('#F0E8F8')

    fig.tight_layout()
    path = os.path.join(OUT_DIR, 'swr_plot.png')
    fig.savefig(path, dpi=180, facecolor=BG_PURPLE, bbox_inches='tight', pad_inches=0.15)
    plt.close(fig)
    images['swr'] = path

    return images


def create_pdf(images):
    """Create A4 PDF with light purple background."""

    class PurplePDF(FPDF):
        def header(self):
            # Light purple background for every page
            self.set_fill_color(*BG_PURPLE_RGB)
            self.rect(0, 0, 210, 297, 'F')

            # Header bar
            self.set_fill_color(74, 26, 122)  # DARK_PURPLE
            self.rect(0, 0, 210, 18, 'F')
            self.set_text_color(255, 255, 255)
            self.set_font('Helvetica', 'B', 11)
            self.cell(0, 12, 'NVIS Dual-Band Fan Dipole Antenna | 80m & 40m | Balanced Design',
                      align='C')
            self.ln(18)

        def footer(self):
            self.set_y(-12)
            self.set_font('Helvetica', 'I', 7)
            self.set_text_color(92, 61, 122)
            self.cell(0, 10,
                      f'NVIS-Antennas Project | github.com/Asteriskman2020/NVIS-Antennas | Page {self.page_no()}/{{nb}}',
                      align='C')

    pdf = PurplePDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=15)

    # ── PAGE 1: Title + Diagram + Overview ───────────────────────
    pdf.add_page()

    # Title block
    pdf.set_fill_color(74, 26, 122)
    pdf.rect(10, 22, 190, 30, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 22)
    pdf.set_xy(10, 24)
    pdf.cell(190, 12, 'NVIS Dual-Band Fan Dipole', align='C')
    pdf.set_font('Helvetica', '', 13)
    pdf.set_xy(10, 36)
    pdf.set_text_color(212, 160, 23)
    pdf.cell(190, 8, '80 m (3.5-3.8 MHz) & 40 m (7.0-7.3 MHz) | Inverted-V Configuration', align='C')
    pdf.set_text_color(200, 192, 240)
    pdf.set_xy(10, 44)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.cell(190, 6, 'Balanced between efficiency and physical size for NVIS regional coverage 0-500 km', align='C')

    pdf.ln(38)

    # Antenna diagram
    if 'diagram' in images:
        pdf.image(images['diagram'], x=20, y=58, w=170)

    pdf.set_xy(10, 120)
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '1. Design Overview', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)
    overview = (
        "This dual-band fan dipole is designed ground-up for Near-Vertical Incidence Skywave (NVIS) "
        "propagation, providing reliable regional coverage from 0 to 500 km. The inverted-V configuration "
        "with a 10 m apex height produces peak radiation at zenith on both bands, ideal for NVIS.\n\n"
        "Two sets of dipole elements share a common feedpoint through a 1:1 current balun: the 80 m "
        "elements (~20 m each side) and the 40 m elements (~10 m each side). The wires are spread apart "
        "(30-50 cm spacing at the feedpoint) to minimise inter-element coupling.\n\n"
        "Compared to a magnetic loop, the fan dipole offers dramatically higher efficiency (95-97% vs "
        "8-54%) and much wider bandwidth (150-210 kHz vs 1.7-5 kHz), at the cost of larger physical size."
    )
    pdf.multi_cell(186, 4.5, overview)

    # Design parameters box
    pdf.ln(3)
    pdf.set_fill_color(240, 232, 248)
    pdf.set_draw_color(123, 63, 175)
    pdf.rect(12, pdf.get_y(), 186, 52, 'FD')

    y_start = pdf.get_y() + 2
    pdf.set_xy(14, y_start)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(74, 26, 122)
    pdf.cell(90, 5, 'Physical Parameters', ln=True)

    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(26, 10, 46)
    params = [
        ('Antenna Type', 'Dual-band fan dipole (inverted-V)'),
        ('80m Element Length', '2 x 20.0 m = 40.0 m total'),
        ('40m Element Length', '2 x 10.0 m = 20.0 m total'),
        ('Apex Height', '10.0 m above ground'),
        ('Apex Angle', '~120 degrees (included)'),
        ('Wire', '#14 AWG stranded copper (1.63 mm)'),
        ('Feed', '1:1 current balun + RG-213 50 ohm coax'),
        ('Ground Screen', '6 x 6 m (optional, +1-2 dB)'),
    ]
    for lbl, val in params:
        pdf.set_x(16)
        pdf.set_font('Helvetica', 'B', 8)
        pdf.cell(45, 4.5, lbl + ':', align='L')
        pdf.set_font('Helvetica', '', 8)
        pdf.cell(120, 4.5, val, ln=True)

    # ── PAGE 2: 3D Radiation Patterns ────────────────────────────
    pdf.add_page()

    pdf.set_xy(10, 22)
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '2. 3D Radiation Patterns', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)
    pdf.multi_cell(186, 4.5,
        "The 3D radiation patterns below show the characteristic NVIS lobe pointing straight up "
        "(zenith). The inverted-V fan dipole over ground produces a broad main lobe covering "
        "elevation angles from approximately 45 to 90 degrees, ideal for illuminating the F2-layer "
        "ionosphere for regional coverage. The ground reflection reinforces the upward radiation "
        "and suppresses low-angle energy that would skip over the target area.")

    pdf.ln(3)

    if '80m' in images:
        pdf.image(images['80m'], x=10, y=pdf.get_y(), w=90)
    if '40m' in images:
        pdf.image(images['40m'], x=108, y=pdf.get_y(), w=90)

    pdf.set_y(pdf.get_y() + 80)

    # Elevation pattern
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '3. Elevation Pattern Comparison', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)
    pdf.multi_cell(186, 4.5,
        "The polar elevation plot shows both bands overlaid. Both peak at zenith (90 degrees) "
        "with broad -3 dB beamwidths spanning 45-90 degrees elevation. The 40 m band shows "
        "slightly stronger ground reinforcement due to the more favourable height-to-wavelength ratio "
        "(h/lambda = 0.23 on 40m vs 0.12 on 80m at 10 m apex height).")

    pdf.ln(2)
    if 'elev' in images:
        pdf.image(images['elev'], x=55, y=pdf.get_y(), w=100)

    # ── PAGE 3: Performance Tables + SWR ─────────────────────────
    pdf.add_page()

    pdf.set_xy(10, 22)
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '4. Performance Data', ln=True)
    pdf.ln(1)

    # Performance table
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(74, 26, 122)
    pdf.set_text_color(255, 255, 255)

    col_w = [25, 18, 22, 18, 18, 22, 22, 25, 22]
    headers = ['Freq\n(MHz)', 'Band', 'Gain\n(dBi)', 'Eff.\n(%)', 'VSWR', 'BW\n(kHz)',
               'Take-off\n(deg)', 'Coverage\n(km)', 'Pattern\nPeak']

    x_start = 10
    y = pdf.get_y()

    for i, (hdr, w) in enumerate(zip(headers, col_w)):
        pdf.set_xy(x_start + sum(col_w[:i]), y)
        pdf.multi_cell(w, 5, hdr, border=1, fill=True, align='C')

    pdf.set_y(y + 10)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(26, 10, 46)

    rows = [
        ['3.500', '80m', '+5.8', '95', '1.3:1', '150', '90', '0-400', 'Zenith'],
        ['3.650', '80m', '+5.9', '95', '1.1:1', '160', '90', '0-400', 'Zenith'],
        ['3.800', '80m', '+6.0', '96', '1.4:1', '160', '90', '0-400', 'Zenith'],
        ['7.000', '40m', '+6.2', '96', '1.5:1', '200', '90', '0-500', 'Zenith'],
        ['7.150', '40m', '+6.3', '97', '1.2:1', '210', '90', '0-500', 'Zenith'],
        ['7.300', '40m', '+6.4', '97', '1.6:1', '210', '90', '0-500', 'Zenith'],
    ]

    for ri, row in enumerate(rows):
        fill = ri < 3
        if fill:
            pdf.set_fill_color(216, 208, 240)
        else:
            pdf.set_fill_color(240, 232, 248)

        y_row = pdf.get_y()
        for ci, (val, w) in enumerate(zip(row, col_w)):
            pdf.set_xy(x_start + sum(col_w[:ci]), y_row)
            pdf.cell(w, 6, val, border=1, fill=True, align='C')
        pdf.set_y(y_row + 6)

    pdf.ln(5)

    # SWR plots
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '5. SWR Response', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)
    pdf.multi_cell(186, 4.5,
        "The SWR remains below 2:1 across both bands, providing good match to 50 ohm feedline. "
        "The fan dipole's natural bandwidth is wide enough to cover the entire 80m allocation "
        "(3.5-3.8 MHz) and 40m allocation (7.0-7.3 MHz) without retuning -- a major advantage "
        "over the narrow-band magnetic loop design.")

    pdf.ln(2)
    if 'swr' in images:
        pdf.image(images['swr'], x=15, y=pdf.get_y(), w=180)

    pdf.set_y(pdf.get_y() + 55)

    # Height optimization
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '6. Height Optimisation for NVIS', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)
    pdf.multi_cell(186, 4.5,
        "The optimal height for a dual-band NVIS fan dipole balances the conflicting requirements "
        "of the two bands. The 80m band (lambda/4 = 21.4 m) benefits from heights up to ~20 m, "
        "while the 40m band (lambda/4 = 10.7 m) reaches peak NVIS gain at ~10.7 m. At 10 m apex "
        "height, the 40m band is near-optimal (h/lambda = 0.23) and the 80m band has good but not "
        "maximum NVIS gain (h/lambda = 0.12). This height represents an excellent practical compromise "
        "and requires only a modest mast that one person can erect.")

    pdf.ln(2)

    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(74, 26, 122)
    pdf.set_text_color(255, 255, 255)

    ht_cols = [30, 25, 30, 25, 30, 50]
    ht_hdrs = ['Height (m)', 'h/lam 80m', 'AF 80m', 'h/lam 40m', 'AF 40m', 'Assessment']
    y = pdf.get_y()
    for i, (h, w) in enumerate(zip(ht_hdrs, ht_cols)):
        pdf.set_xy(10 + sum(ht_cols[:i]), y)
        pdf.cell(w, 6, h, border=1, fill=True, align='C')
    pdf.set_y(y + 6)

    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(26, 10, 46)

    ht_rows = [
        ['5', '0.058', '0.72', '0.117', '1.34', 'Minimum practical'],
        ['8', '0.093', '1.11', '0.187', '1.81', 'Good dual-band'],
        ['10', '0.117', '1.34', '0.234', '1.96', 'Recommended'],
        ['10.7', '0.125', '1.41', '0.250', '2.00', 'Optimal 40m'],
        ['15', '0.175', '1.76', '0.350', '1.90', '40m past peak'],
    ]

    for ri, row in enumerate(ht_rows):
        fill_c = (216, 208, 240) if ri == 2 else (240, 232, 248)
        pdf.set_fill_color(*fill_c)
        y_row = pdf.get_y()
        for ci, (val, w) in enumerate(zip(row, ht_cols)):
            pdf.set_xy(10 + sum(ht_cols[:ci]), y_row)
            fw = 'B' if ri == 2 else ''
            pdf.set_font('Helvetica', fw, 7.5)
            pdf.cell(w, 5.5, val, border=1, fill=True, align='C')
        pdf.set_y(y_row + 5.5)

    # ── PAGE 4: Construction, BOM, Safety ────────────────────────
    pdf.add_page()

    pdf.set_xy(10, 22)
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '7. Construction Guide', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)

    construction = (
        "Step 1: Cut wire elements.\n"
        "  - 80m: Cut two lengths of #14 AWG wire, each 20.5 m (includes trim allowance)\n"
        "  - 40m: Cut two lengths of #14 AWG wire, each 10.3 m (includes trim allowance)\n\n"
        "Step 2: Prepare the centre feedpoint.\n"
        "  - Mount a 1:1 current balun (10 bifilar turns on FT-240-43 toroid) in a weatherproof box\n"
        "  - Connect all four wires to the balun: both 80m and both 40m elements to the same terminals\n"
        "  - Use solder lugs or crimp terminals for reliable connections\n\n"
        "Step 3: Spread the elements.\n"
        "  - Use 30-50 cm plastic spreaders near the feedpoint to separate 80m and 40m wires\n"
        "  - The 40m elements hang inside the 80m elements at a steeper angle\n\n"
        "Step 4: Install end insulators and support ropes.\n"
        "  - Attach egg or dog-bone insulators at each wire end\n"
        "  - Run Dacron support rope from insulators to ground stakes or trees\n\n"
        "Step 5: Erect the mast.\n"
        "  - Raise the feedpoint to 10 m using a fibreglass mast or rope-over-tree\n"
        "  - The wire ends should be 3-5 m above ground (inverted-V slope)\n\n"
        "Step 6: Tune and trim.\n"
        "  - Tune the 40m elements FIRST (trim shorter wires before longer)\n"
        "  - Check SWR with antenna analyser; trim 2 cm at a time from each end\n"
        "  - Then check 80m; trim if needed (usually minimal adjustment required)\n"
        "  - Target: VSWR < 1.5:1 at band centre for both bands"
    )
    pdf.multi_cell(186, 4.2, construction)

    pdf.ln(4)

    # BOM
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '8. Bill of Materials', ln=True)
    pdf.ln(1)

    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(74, 26, 122)
    pdf.set_text_color(255, 255, 255)

    bom_cols_w = [8, 70, 18, 35, 55]
    bom_hdrs = ['#', 'Item', 'Qty', 'Cost (USD)', 'Notes']
    y = pdf.get_y()
    for i, (h, w) in enumerate(zip(bom_hdrs, bom_cols_w)):
        pdf.set_xy(8 + sum(bom_cols_w[:i]), y)
        pdf.cell(w, 6, h, border=1, fill=True, align='C')
    pdf.set_y(y + 6)

    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(26, 10, 46)

    bom_data = [
        ['1', '#14 AWG stranded Cu wire, 70 m', '1', '$15-25', 'THHN or bare copper'],
        ['2', '1:1 Current balun (FT-240-43)', '1', '$20-40', '10 bifilar turns'],
        ['3', 'RG-213 coaxial cable, 20 m', '1', '$30-50', '50 ohm, UV resistant'],
        ['4', 'PL-259 / SO-239 connectors', '4', '$8-15', 'Silver-plated preferred'],
        ['5', 'Fibreglass mast, 10 m', '1', '$40-80', 'Telescoping or sectional'],
        ['6', 'Insulators (egg/dog-bone)', '6', '$5-10', 'Ceramic or HDPE'],
        ['7', 'Dacron rope, 30 m', '1', '$10-20', 'UV resistant, non-stretch'],
        ['8', 'Plastic spreaders', '4', '$5-10', '30-50 cm, near feedpoint'],
        ['9', 'Weatherproof junction box', '1', '$5-10', 'For balun housing'],
        ['10', 'Ground screen (optional)', '1', '$15-25', '#14 wire, 6x6 m'],
        ['', 'TOTAL', '', '$153-285', ''],
    ]

    for ri, row in enumerate(bom_data):
        fill_c = (216, 192, 240) if ri == len(bom_data) - 1 else ((240, 232, 248) if ri % 2 == 0 else (228, 220, 240))
        pdf.set_fill_color(*fill_c)
        y_row = pdf.get_y()
        fw = 'B' if ri == len(bom_data) - 1 else ''
        for ci, (val, w) in enumerate(zip(row, bom_cols_w)):
            pdf.set_xy(8 + sum(bom_cols_w[:ci]), y_row)
            pdf.set_font('Helvetica', fw, 7.5)
            pdf.cell(w, 5, val, border=1, fill=True, align='C' if ci in [0, 2, 3] else 'L')
        pdf.set_y(y_row + 5)

    pdf.ln(5)

    # Safety
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '9. Safety Notes', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)
    safety = (
        "RF Exposure: At 100 W, maintain 2 m minimum clearance from wire elements during TX. "
        "The feedpoint voltage is low (~100 V) compared to a magnetic loop (~6000 V), making "
        "the fan dipole inherently safer.\n\n"
        "Lightning: Install a coaxial lightning arrester at station entry. Bond all ground "
        "connections to a single-point station ground. Disconnect feedline during thunderstorms.\n\n"
        "Mechanical: Wire ends should be at least 3 m above ground for pedestrian safety. "
        "Use UV-resistant rope and inspect annually for wear. Mast guys (if used) should be "
        "non-conductive Dacron rope."
    )
    pdf.multi_cell(186, 4.5, safety)

    # ── PAGE 5: Comparison, NVIS Guide ───────────────────────────
    pdf.add_page()

    pdf.set_xy(10, 22)
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '10. Comparison: Fan Dipole vs Magnetic Loop', ln=True)
    pdf.ln(1)

    comp_cols_w = [55, 55, 55]
    comp_hdrs = ['Parameter', 'Fan Dipole (this design)', 'Mag Loop (balanced)']

    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(74, 26, 122)
    pdf.set_text_color(255, 255, 255)
    y = pdf.get_y()
    for i, (h, w) in enumerate(zip(comp_hdrs, comp_cols_w)):
        pdf.set_xy(17 + sum(comp_cols_w[:i]), y)
        pdf.cell(w, 6, h, border=1, fill=True, align='C')
    pdf.set_y(y + 6)

    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(26, 10, 46)

    comp_rows = [
        ['Footprint', '40 m span', '2 m diameter'],
        ['80m Efficiency', '95-96%', '8.5-11%'],
        ['40m Efficiency', '96-97%', '51-55%'],
        ['80m Gain (dBi, NVIS)', '+5.8 to +6.0', '-8 to -7'],
        ['40m Gain (dBi, NVIS)', '+6.2 to +6.4', '+0 to +1'],
        ['Bandwidth (-3 dB)', '150-210 kHz', '1.7-5 kHz'],
        ['Retuning Required', 'No', 'Every 1-5 kHz'],
        ['Feed Voltage (100W)', '~100 V', '5,000-6,400 V'],
        ['Tuning Complexity', 'Cut-and-trim once', 'Vacuum variable cap'],
        ['Stealth / Low Profile', 'Poor (40 m span)', 'Excellent (2 m)'],
        ['Noise Rejection', 'Moderate', 'Excellent (nulls)'],
        ['Wind Resistance', 'Good (wire)', 'Good (rigid loop)'],
        ['Portability', 'Fair (bulky wire)', 'Good (compact)'],
        ['Cost', '$153-285', '$313-712'],
    ]

    for ri, row in enumerate(comp_rows):
        fill_c = (240, 232, 248) if ri % 2 == 0 else (228, 220, 240)
        pdf.set_fill_color(*fill_c)
        y_row = pdf.get_y()
        for ci, (val, w) in enumerate(zip(row, comp_cols_w)):
            pdf.set_xy(17 + sum(comp_cols_w[:ci]), y_row)
            pdf.set_font('Helvetica', 'B' if ci == 0 else '', 7.5)
            pdf.cell(w, 5, val, border=1, fill=True, align='C' if ci > 0 else 'L')
        pdf.set_y(y_row + 5)

    pdf.ln(6)

    # NVIS Operating Guide
    pdf.set_text_color(74, 26, 122)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(190, 8, '11. NVIS Operating Guide', ln=True)

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(26, 10, 46)
    pdf.set_x(12)

    guide = (
        "Recommended Operating Schedule:\n"
        "  06:00-09:00  80m or 40m (80m for certainty; 40m once ionosphere warms up)\n"
        "  09:00-17:00  40m preferred (higher efficiency, lower noise, foF2 > 7 MHz)\n"
        "  17:00-20:00  40m or 80m (transition; monitor propagation)\n"
        "  20:00-06:00  80m only (foF2 drops below 7 MHz at night)\n\n"
        "Tips for Best NVIS Performance:\n"
        "  - Use the highest frequency that foF2 supports (less D-layer absorption)\n"
        "  - On 80m, prefer the lower portion (3.5-3.6 MHz) during low solar activity\n"
        "  - Check real-time foF2 data from nearest ionosonde for frequency selection\n"
        "  - For emergency communications, plan on 80m as it is the most reliable NVIS band\n"
        "  - Ground screen adds +1-2 dB to NVIS gain; install if operating from a fixed location\n\n"
        "Link Budget (40m, 100W, 300 km, daytime):\n"
        "  TX power: +50 dBm | Antenna gain: +6.3 dBi | Path loss: -125 dB\n"
        "  Iono absorption: -10 dB | RX gain: +6.3 dBi\n"
        "  Received: -72.4 dBm | Noise floor: -100 dBm | SNR: +27.6 dB (Excellent)\n\n"
        "Link Budget (80m, 100W, 200 km, night-time):\n"
        "  TX power: +50 dBm | Antenna gain: +5.9 dBi | Path loss: -120 dB\n"
        "  Iono absorption: -5 dB | RX gain: +5.9 dBi\n"
        "  Received: -63.2 dBm | Noise floor: -90 dBm | SNR: +26.8 dB (Excellent)"
    )
    pdf.multi_cell(186, 4.2, guide)

    pdf.ln(4)

    # Quick reference box
    pdf.set_fill_color(74, 26, 122)
    pdf.rect(12, pdf.get_y(), 186, 38, 'F')

    y_qr = pdf.get_y() + 2
    pdf.set_xy(14, y_qr)
    pdf.set_text_color(212, 160, 23)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(182, 6, 'QUICK REFERENCE CARD', align='C', ln=True)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Courier', '', 7.5)

    qr_text = (
        "TYPE: Dual-band fan dipole (inverted-V)  |  BANDS: 80m + 40m  |  FEED: 50 ohm + 1:1 balun\n"
        "80m: 20m each side, Gain +5.9 dBi, Eff 95%, BW 160 kHz, VSWR < 1.5:1\n"
        "40m: 10m each side, Gain +6.3 dBi, Eff 97%, BW 210 kHz, VSWR < 1.5:1\n"
        "HEIGHT: 10 m apex  |  NVIS: Peak at zenith  |  COVERAGE: 0-500 km  |  COST: $153-285"
    )
    for line in qr_text.split('\n'):
        pdf.set_x(16)
        pdf.cell(180, 4.5, line, ln=True)

    pdf_path = os.path.join(OUT_DIR, 'Dualband_Balanced.pdf')
    pdf.output(pdf_path)
    print(f"PDF saved: {pdf_path}")
    return pdf_path


# ───────────────────────────────────────────────────────────────────
#  MAIN
# ───────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("Generating 3D pattern images...")
    images = create_3d_images()

    print("\nGenerating poster (PNG)...")
    poster_path = create_poster()

    print("\nGenerating PDF (A4)...")
    pdf_path = create_pdf(images)

    # Cleanup temp images
    for key in ['80m', '40m', 'elev', 'diagram', 'swr']:
        if key in images and os.path.exists(images[key]):
            os.remove(images[key])
            print(f"Cleaned up: {images[key]}")

    print("\nDone! Files created:")
    print(f"  Poster: {poster_path}")
    print(f"  PDF:    {pdf_path}")
