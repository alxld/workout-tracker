from ._anvil_designer import SetDetailsTemplate
from anvil import *
import plotly.graph_objects as go


class SetDetails(SetDetailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
