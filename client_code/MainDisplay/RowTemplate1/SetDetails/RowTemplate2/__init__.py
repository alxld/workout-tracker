from ._anvil_designer import RowTemplate2Template
from .....UpdateSetForm import UpdateSetForm
from anvil_extras import augment
from anvil import *


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    augment.set_event_handler(self, 'click', self.row_click)

  def row_click(self, **event_args):
    print("row clicked")
    usf = UpdateSetForm(self.item.prevWeight, self.item.prevReps)
    results = alert(content=usf, title="Update Set", large=True, buttons=[("OK", True), ("Cancel", False)])
    print(results)
