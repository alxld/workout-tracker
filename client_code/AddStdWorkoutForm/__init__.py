from ._anvil_designer import AddStdWorkoutFormTemplate
from anvil import *
import anvil.js
import anvil.server


class AddStdWorkoutForm(AddStdWorkoutFormTemplate):
  def __init__(self, md=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.md = md

  def close_me(self):
    self.raise_event("x-close-alert", value=42)

  def add_push1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Chest', exercise='BB Bench Press')
    self.md.add_exercise_button_click(body_part='Chest', exercise='DB Incline Fly')
    self.md.add_exercise_button_click(body_part='Arms', exercise='DB Skull Crushers')
    self.md.add_exercise_button_click(body_part='Arms', exercise='Cable Tricep Push')
    self.close_me()

  def add_pull_1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Back', exercise='Single Arm Lat Pull')
    self.md.add_exercise_button_click(body_part='Back', exercise='Narrow Seated Row')
    self.md.add_exercise_button_click(body_part='Arms', exercise='Hammer Curl')
    self.md.add_exercise_button_click(body_part='Back', exercise='Seated Reverse DB Fly')
    self.close_me()

  def add_legs_1_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Quads', exercise='Squat')
    self.md.add_exercise_button_click(body_part='Hamstrings', exercise='DB Romanian Deadlift')
    self.md.add_exercise_button_click(body_part='Core', exercise='Plank')
    self.md.add_exercise_button_click(body_part='Core', exercise='DB Suitcase Carry Uneven')
    self.close_me()

  def add_push_2_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Chest', exercise='BB Incline Press')
    self.md.add_exercise_button_click(body_part='Chest', exercise='DB Decline Press')
    self.md.add_exercise_button_click(body_part='Shoulders', exercise='Shoulder Press')
    self.md.add_exercise_button_click(body_part='Shoulders', exercise='DB Front/Side Raises')
    self.close_me()
    
  def add_pull_2_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Back', exercise='Bent Row')
    self.md.add_exercise_button_click(body_part='Back', exercise='Overhead DB Pullover')
    self.md.add_exercise_button_click(body_part='Arms', exercise='Cable One-Arm Curl')
    self.md.add_exercise_button_click(body_part='Shoulders', exercise='Wide Grip BB Upright Row')
    self.close_me()

  def add_legs_2_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.md.add_exercise_button_click(body_part='Hamstrings', exercise='Side Lunge')
    self.md.add_exercise_button_click(body_part='Calves', exercise='DB Single Calf Raise')
    self.md.add_exercise_button_click(body_part='Core', exercise='Side Plank')
    self.md.add_exercise_button_click(body_part='Core', exercise='Leg Lifts')
    self.close_me()