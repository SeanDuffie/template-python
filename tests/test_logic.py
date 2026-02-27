""" @file test_logic.py
    @author Sean Duffie
    @brief 
"""
import pytest
from project.logic import process_data, process_user_request
from project.models import CalculationResult

def test_process_data_multiplication():
    """Verify that the engine correctly doubles the input."""
    assert process_data(10) == 20
    assert process_data(0) == 0
    assert process_data(-5) == -10

def test_process_user_request_flow(sample_user):
    """Verify the integration between models and logic."""
    val = 25
    result = process_user_request(sample_user, val)
    
    # Assertions
    assert isinstance(result, CalculationResult)
    assert result.input_value == val
    assert result.output_value == 50
    assert result.timestamp is not None
