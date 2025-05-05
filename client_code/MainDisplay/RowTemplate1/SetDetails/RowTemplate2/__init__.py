from ._anvil_designer import RowTemplate2Template
from anvil_extras import augment
from anvil import *


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    augment.set_event_handler(self, 'click', self.row_click)

  def row_click(self, **event_args):
    print("row clicked")
    # Any code you write here will run before the form opens.
