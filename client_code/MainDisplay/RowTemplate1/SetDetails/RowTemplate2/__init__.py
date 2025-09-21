from ._anvil_designer import RowTemplate2Template
from .... import MainDisplay
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

    if this_weight == 0 and this_reps == 0:
      this_idx = self.parent.items.index(self.item)
      if this_idx > 0:
        prev_item = self.parent.items[this_idx - 1]
        this_weight = prev_item.weight
        this_reps   = prev_item.reps

    exercise_complete_before = self.item.exercise.is_complete
    usf = UpdateSetForm(self.item.prevWeight, self.item.prevReps, this_weight, this_reps)
    #results = alert(content=usf, title="Update Set", large=True, buttons=[("OK", True), ("Cancel", False)], role="large-alert-button-text")
    results = alert(content=usf, title="Update Set", large=True, buttons=[])

    if results:
      self.item.weight = float(usf.this_weight_text_box.text)
      self.item.reps   = int(usf.this_reps_text_box.text)

      exercise_complete_after = self.item.exercise.is_complete

      if round(self.item.weight, 0) == self.item.weight:
        self.item.weight = int(self.item.weight)

      self.item.update_database()
      self.item = self.item

      md = self.parent.parent.parent.parent.parent.parent.parent.parent.parent

      if self.item.user == "Aaron":
        md.atimer_reset_and_run()
      else:
        md.wtimer_reset_and_run()

      if exercise_complete_after: # and not exercise_complete_before:
        print("BEFORE REORDER")
        self.parent.parent.parent.parent.parent.parent.items = md.reorder_completed_exercises(self.parent.parent.parent.parent.parent.parent.items)
        print("AFTER REORDER")