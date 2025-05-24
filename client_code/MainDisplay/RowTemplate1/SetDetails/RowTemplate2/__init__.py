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
    if self.item.weight:
      this_weight = self.item.weight
    else:
      this_weight = self.item.prevWeight
      
    if self.item.reps:
      this_reps = self.item.reps
    else:
      this_reps = self.item.prevReps
      
    usf = UpdateSetForm(self.item.prevWeight, self.item.prevReps, this_weight, this_reps)
    #results = alert(content=usf, title="Update Set", large=True, buttons=[("OK", True), ("Cancel", False)], role="large-alert-button-text")
    results = alert(content=usf, title="Update Set", large=True, buttons=[])

    if results:
      print(results)
      return
      self.item.weight = usf.this_weight_text_box.text
      self.item.reps   = usf.this_reps_text_box.text

      self.item.update_database()
      self.item = self.item
