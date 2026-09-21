"""
======================================================
Searching for Low Latency Data from the SOAR with Fido
======================================================

This example demonstrates how to search for and download Solar Orbiter
Low Latency (LL) data from the Solar Orbiter Archive (SOAR) using `sunpy.net.Fido`.

Solar Orbiter provides two primary categories of data products:

* **Science Data:** Standard science data products (Level 1, Level 2, Level 3) undergo
  rigorous ground calibration and validation by the respective instrument teams,
  which typically takes weeks to months following downlink.
* **Low Latency (LL) Data:** Low Latency data is downlinked rapidly (typically within
  hours to a few days) to facilitate mission planning, instrument health monitoring, and
  pointing decisions. They are automatically processed with preliminary calibrations,
  making them ideal for near-real-time observations and space-weather awareness.

The SOAR classifies Low Latency data into the following levels:

* ``LL01``: Raw telemetry packets converted into engineering units.
* ``LL02``: Calibrated quick-look data (such as preliminary imaging or flux rates).
* ``LL03``: Higher-level quick-look products derived from LL02 (such as flare lightcurves
  or summary solar wind parameters).

To search for Low Latency data from the SOAR, the `~sunpy.net.attrs.Level` attribute
must be explicitly specified with a Low Latency level (e.g., ``"LL02"`` or ``"LL03"``).
"""

# sphinx_gallery_tags = ["Acquiring Data", "SOAR", "Solar Orbiter"]

import sunpy.net.attrs as a
from sunpy.net import Fido

###############################################################################
# Searching for Calibrated Quick-Look Data (LL02)
# -----------------------------------------------
# In this first example, we search for Low Latency Level 2 (``LL02``) quick-look
# images from the Extreme Ultraviolet Imager (EUI) on board Solar Orbiter.

time_range = a.Time("2020-10-21 10:00", "2020-10-21 10:30")
instrument = a.Instrument("EUI")
level = a.Level("LL02")

results_eui = Fido.search(time_range & instrument & level)
results_eui

###############################################################################
# Searching for Derived Quick-Look Science Products (LL03)
# --------------------------------------------------------
# Low Latency Level 3 (``LL03``) data consists of higher-level data products
# computed quickly after downlink.
# Here, we search for quick-look flare lightcurves (``stix-ql-lightcurve``) from
# the Spectrometer/Telescope for Imaging X-rays (STIX).

time_range_stix = a.Time("2026-03-11", "2026-03-12")
results_stix = Fido.search(time_range_stix & a.Instrument("STIX") & a.Level("LL03"))
results_stix

###############################################################################
# Downloading the Data
# --------------------
# Once you have identified the files you need from the query results, you can
# download them using `~sunpy.net.Fido.fetch`.
#
# (This line is commented out to avoid downloading files during the documentation build.)

# downloaded_files = Fido.fetch(results_eui)
