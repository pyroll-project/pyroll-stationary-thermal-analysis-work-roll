import logging
import webbrowser
from pathlib import Path

from pyroll.core import Profile, PassSequence, RollPass, Roll, CircularOvalGroove, Transport, RoundGroove
from pyroll.report import report


def test_solve(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    import pyroll.stationary_thermal_analysis_work_roll

    in_profile = Profile.round(
        diameter=30e-3,
        temperature=1200 + 273.15,
        strain=0,
        material=["C45", "steel"],
        flow_stress=100e6,
        density=7.5e3,
        specific_heat_capacity=690,
    )

    sequence = PassSequence([
        RollPass(
            label="Oval I",
            roll=Roll(
                material="CR75",
                groove=CircularOvalGroove(
                    depth=8e-3,
                    r1=6e-3,
                    r2=40e-3
                ),
                nominal_radius=160e-3,
                rotational_frequency=1,
                cooling_sections=[
                    [25, 240]
                ],
                temperature=50 + 273.15,
                thermal_conductivity=110,
                density=13.5e3,
                specific_heat_capacity=200,
            ),
            gap=2e-3,
            coulomb_friction_coefficient=0.4,
        ),
        Transport(
            label="I => II",
            duration=1
        ),
        RollPass(
            label="Round II",
            roll=Roll(
                material="SS2242",
                groove=RoundGroove(
                    r1=1e-3,
                    r2=12.5e-3,
                    depth=11.5e-3
                ),
                nominal_radius=160e-3,
                rotational_frequency=1,
                cooling_sections=[
                    [25, 240]
                ],
                temperature=50 + 273.15,
                thermal_conductivity=23,
                density=7.5e3,
                specific_heat_capacity=670,
            ),
            gap=2e-3,
            coulomb_friction_coefficient=0.4,
        ),
    ])

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    report_file = tmp_path / "report.html"

    rendered = report(sequence)
    print()

    report_file.write_text(rendered, encoding="utf-8")

    webbrowser.open(report_file.as_uri())
