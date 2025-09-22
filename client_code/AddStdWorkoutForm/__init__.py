from ._anvil_designer import AddStdWorkoutFormTemplate
from anvil import *
import anvil.server


class AddStdWorkoutForm(AddStdWorkoutFormTemplate):
  def __init__(self, md=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.md = md

  def add_push1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Chest', exercise='BB Bench Press')
    self.md.add_exercise_button_click(body_part='Chest', exercise='DB Incline Fly')
    self.md.add_exercise_button_click(body_part='Arms', exercise='DB Skull Crushers')
    self.md.add_exercise_button_click(body_part='Arms', exercise='Cable Tricep Push')

  def add_pull_1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Back', exercise='Single Arm Lat Pull')
    self.md.add_exercise_button_click(body_part='Back', exercise='Narrow Seated Row')
    self.md.add_exercise_button_click(body_part='Arms', exercise='Hammer Curl')
    self.md.add_exercise_button_click(body_part='Back', exercise='Seated Reverse DB Fly')

  def add_legs_1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Back', exercise='Single Arm Lat Pull')
    self.md.add_exercise_button_click(body_part='Back', exercise='Narrow Seated Row')
    self.md.add_exercise_button_click(body_part='Arms', exercise='Hammer Curl')
    self.md.add_exercise_button_click(body_part='Back', exercise='Seated Reverse DB Fly')

