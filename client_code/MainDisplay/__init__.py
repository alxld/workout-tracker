from ._anvil_designer import MainDisplayTemplate
from ..AddExerciseForm import AddExerciseForm
from anvil import *

class Exercise:
  def __init__(self, name, body_part):
    self._name = name
    self._body_part = body_part
    self._exerciseType = {"Aaron": "UNKNOWN", "Weez": "UNKNOWN"}
    self._sets = {"Aaron": [], "Weez": []}

  def __getitem__(self, key):
    if key == "name":
      return self._name
    if key == "aaron":
      return self._sets['Aaron']
    if key == "weez":
      return self._sets['Weez']

    raise Exception(f"{key} not found in Exercise object")

  def addSet(self, user):
    newset = Set(len(self._sets[user])+1, 0, 0)
    self._sets[user].append(newset)
    return newset

  @property
  def aaron_exercise_type(self):
    return self._exerciseType['Aaron']

  @aaron_exercise_type.setter
  def aaron_exercise_type(self, type):
    self._exerciseType['Aaron'] = type

  @property
  def weez_exercise_type(self):
    return self._exerciseType['Weez']

  @weez_exercise_type.setter
  def weez_exercise_type(self, type):
    self._exerciseType['Weez'] = type

class Set:
  def __init__(self, setNum, weight, reps):
    self.setNum = setNum
    self.weight = weight
    self.reps = reps
    self.prevWeight = 0
    self.prevReps = 0

  def __getitem__(self, key):
    if key == "setNum":
      return self.setNum
    if key == "weight":
      return self.weight
    if key == "reps":
      return self.reps
    if key == "prevWeight":
      return self.prevWeight
    if key == "prevReps":
      return self.prevReps

    raise Exception(f"{key} not found in Set object")
    
class MainDisplay(MainDisplayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self._exercises = []

    #self._exercises.append(Exercise("blah", "no part"))
    self.repeating_panel_1.items = self._exercises

  def add_exercise_button_click(self, **event_args):
    # Pull up AddExerciseForm to get new exercise details
    aef = AddExerciseForm()
    result = alert(title="Add Exercise", content=aef, large=True, buttons=[("OK", True), ("Cancel", False)])

    body_part = aef.body_part_drop_down.selected_value
    exercise = aef.exercise_drop_down.selected_value

    if result:
      this_ex = Exercise(exercise, body_part)
      this_ex.aaron_exercise_type = aef.aaron_exercise_type_drop_down.selected_value
      this_ex.weez_exercise_type = aef.weez_exercise_type_drop_down.selected_value
      #this_ex.addSet("Aaron")
      self._exercises.append(this_ex)
      self.repeating_panel_1.items = self._exercises
    #open_form('AddExerciseForm', show_as_diaklog=True)
    