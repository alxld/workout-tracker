from ._anvil_designer import AddExerciseFormTemplate
from anvil import *
import anvil.server


class AddExerciseForm(AddExerciseFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.body_part_drop_down.items = anvil.server.call("get_body_parts")
    self.exercises = anvil.server.call("get_exercise_for_body_part", "Back")

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
