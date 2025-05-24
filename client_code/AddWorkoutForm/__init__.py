from ._anvil_designer import AddWorkoutFormTemplate
from anvil import *
import anvil.server
from datetime import datetime


class AddWorkoutForm(AddWorkoutFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.add_workout_date_picker.date = datetime.now().date()
    # Any code you write here will run before the form opens.

  def ok_button_click(self, **event_args):
    self.raise_event("x-close-alert", value=True)

  def cancel_button_click(self, **event_args):
    self.raise_event("x-close-alert", value=False)