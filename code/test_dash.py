import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from dash_chart import update
from dash.testing.application_runners import import_app


def test_header(dash_duo):
    app = import_app("dash_chart")
    dash_duo.start_server(app)

    header = dash_duo.find_element("#header")
    assert header is not None
    assert "Soul Foods" in header.text

def test_graph(dash_duo):
    app = import_app("dash_chart")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#data-graph")
    assert graph is not None


def test_region(dash_duo):
    app = import_app("dash_chart")
    dash_duo.start_server(app)

    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None


def test_update_callback_north():
    output = update('north')
    assert output == 'selected: north'

    output = update('south')
    assert output == 'selected: south'

    output = update('west')
    assert output == 'selected: west'

    output = update('east')
    assert output == 'selected: east'

    output = update('all')
    assert output == 'selected: all'

