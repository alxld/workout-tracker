from ._anvil_designer import MainDisplayTemplate
from ..AddExerciseForm import AddExerciseForm
from ..UpdateDatabaseForm import UpdateDatabaseForm
from ..Exercise import Exercise, Set
from anvil import *
import anvil.server
 
class MainDisplay(MainDisplayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self._exercises = []

    #self._exercises.append(Exercise("blah", "no part"))
    self.repeating_panel_1.items = self._exercises

    #self.body_parts = anvil.server.call("get_body_parts")
    #print(self.body_parts)
 
  
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

  def update_db_button_click(self, **event_args):
    ud_form = UpdateDatabaseForm()
    result = alert(title="Update Database", content=ud_form)