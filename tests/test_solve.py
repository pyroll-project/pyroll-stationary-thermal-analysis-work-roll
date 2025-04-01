import logging
import webbrowser
from pathlib import Path

from pyroll.core import Profile, PassSequence, RollPass, Roll, FalseRoundGroove, CircularOvalGroove
from pyroll.report import report


def test_solve(tmp_path: Path, caplog):
    caplog.set_level(logging.INFO, logger="pyroll")

    import pyroll.stationary_thermal_analysis_work_roll

    in_profile = Profile.from_groove(
        groove=CircularOvalGroove(
            depth=3.5e-3,
            r1=1e-3,
            r2=15.5e-3
        ),
        gap=1.6e-3,
        filling=0.9,
        temperature=1100 + 273.15,
        strain=0,
        material=["C45", "steel"],
        flow_stress=100e6,
        density=7.5e3,
        specific_heat_capacity=690,
    )

    sequence = PassSequence([
        RollPass(
            label="Stand 24",
            orientation="v",
            roll=Roll(
                groove=FalseRoundGroove(
                    depth=4.6e-3,
                    r1=0.2e-3,
                    r2=5.55e-3,
                    flank_angle=70
                ),
                cooling_sections=[
                    [25, 240]
                ],
                temperature=50 + 273.15,
                thermal_conductivity=110,
                density=13.5e3,
                specific_heat_capacity=200,
                nominal_radius=72.75e-3,
            ),
            velocity=65.4,
            gap=1.7e-3,
            coulomb_friction_coefficient=0.4,
        )

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
