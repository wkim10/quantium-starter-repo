from app import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("header", timeout=10)

def test_visualization(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("graph", timeout=10)

def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("region_picker", timeout=10)