
from water_flow import water_column_height, pressure_gain_from_water_height, psi_form_kPa, \
    pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
from pytest import approx
import pytest

def test_water_column_height ():
    assert water_column_height (0, 0) == approx (0) 
    assert water_column_height (0, 10) == approx (7.5) 
    assert water_column_height (25, 0) == approx (25) 
    assert water_column_height (48.3, 12.8) == approx (57.9) 

def test_pressure_gain_from_water_height ():
    assert pressure_gain_from_water_height (0, 998.2, 9.80665) == approx (0, abs = 0.001)
    assert pressure_gain_from_water_height (30.2, 998.2, 9.80665) == approx (295.628, abs = 0.001)
    assert pressure_gain_from_water_height (50, 998.2, 9.80665) == approx (489.450, abs = 0.001)

def test_pressure_loss_from_pipe ():
    assert pressure_loss_from_pipe (0.048692, 0, 0.018, 1.75, 998.2) == approx (0, abs = 0.001)
    assert pressure_loss_from_pipe (0.048692, 200, 0, 1.75, 998.2) == approx (0, abs = 0.001)
    assert pressure_loss_from_pipe (0.048692, 200, 0.018, 0, 998.2) == approx (0, abs = 0.001)
    assert pressure_loss_from_pipe (0.048692, 200, 0.018, 1.75, 998.2) == approx (-113.008, abs = 0.001)
    assert pressure_loss_from_pipe (0.048692, 200, 0.018, 1.65, 998.2) == approx (-100.462, abs = 0.001)
    assert pressure_loss_from_pipe (0.28687, 1000, 0.013, 1.65, 998.2) == approx (-61.576, abs = 0.001)
    assert pressure_loss_from_pipe (0.28687, 1800.75, 0.013, 1.65, 998.2) == approx (-110.884, abs = 0.001)

def test_pressure_loss_from_fittings ():
    assert pressure_loss_from_fittings (0, 3, 998.2) == approx (0, abs = 0.001)
    assert pressure_loss_from_fittings (1.65, 0, 998.2) == approx (0, abs = 0.001)
    assert pressure_loss_from_fittings (1.65, 2, 998.2) == approx (-0.109, abs = 0.001)
    assert pressure_loss_from_fittings (1.75, 2, 998.2) == approx (-0.122, abs = 0.001)
    assert pressure_loss_from_fittings (1.75, 5, 998.2) == approx (-0.306, abs = 0.001)

def test_reynolds_number ():
    assert reynolds_number (0.048692, 0, 998.2, 0.0010016) == approx (0, abs = 1)
    assert reynolds_number (0.048692, 1.65, 998.2, 0.0010016) == approx (80069, abs = 1)
    assert reynolds_number (0.048692, 1.75, 998.2, 0.0010016) == approx (84922, abs = 1)
    assert reynolds_number (0.28687, 1.65, 998.2, 0.0010016) == approx (471729, abs = 1)
    assert reynolds_number (0.28687, 1.75, 998.2, 0.0010016) == approx (500318, abs = 1)

def test_pressure_loss_from_pipe_reduction ():
    assert pressure_loss_from_pipe_reduction (0.28687, 0, 1, 0.048692, 998.2) == approx (0, abs = 0.001)
    assert pressure_loss_from_pipe_reduction (0.28687, 1.65, 471729, 0.048692, 998.2) == approx (-163.744,	abs = 0.001)
    assert pressure_loss_from_pipe_reduction (0.28687, 1.75, 500318, 0.048692, 998.2) == approx (-184.182,	abs = 0.001)
    
#Exceeding the Requirements
def test_psi_form_kPa ():
    assert psi_form_kPa (1, 0.145038) == approx (0.145038, abs = 0.001)
    assert psi_form_kPa (6.895, 0.145038) == approx (1, abs = 0.001)
    assert psi_form_kPa (33.7, 0.145038) == approx (4.88778, abs = 0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])