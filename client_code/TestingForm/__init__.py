from ._anvil_designer import TestingFormTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server

class TestingForm(TestingFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
