from pluto._internal.dash.exp_and_inc.callbacks import register_callbacks

class DummyDashApp:
    def __init__(self):
        pass
    def callback(self, *args, **kwargs):
        def _c(f):
            return f
        return _c

# TODO: properly test this thing...
def test_register_callbacks():
    register_callbacks(DummyDashApp())
