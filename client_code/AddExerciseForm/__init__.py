from ._anvil_designer import AddExerciseFormTemplate
from anvil import *
import anvil.server


class AddExerciseForm(AddExerciseFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.body_part_drop_down.items = anvil.server.call("get_body_parts")

    bp = self.body_part_drop_down.selected_value
    exercises = anvil.server.call("get_exercise_for_body_part", bp)
    self.exercise_drop_down.items = exercises

    workout_type_names = anvil.server.call("get_workout_type_names")
    self.aaron_exercise_type_drop_down.items = workout_type_names
    self.weez_exercise_type_drop_down.items  = workout_type_names

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def body_part_drop_down_change(self, **event_args):
    bp = self.body_part_drop_down.selected_value
    exercises = anvil.server.call("get_exercise_for_body_part", bp)
    self.exercise_drop_down.items = exercises
