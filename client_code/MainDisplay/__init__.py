from ._anvil_designer import MainDisplayTemplate
from ..AddExerciseForm import AddExerciseForm
from ..UpdateDatabaseForm import UpdateDatabaseForm
from ..Exercise import Exercise, Set
from ..AddWorkoutForm import AddWorkoutForm
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
      global workout_id

      aaron_exercise_type = aef.aaron_exercise_type_drop_down.selected_value
      weez_exercise_type = aef.weez_exercise_type_drop_down.selected_value

      if anvil.server.call("workout_has_exercise", workout_id, exercise):
        alert("Exercise already in workout!")
        return
              
      aaron_workout_exercise_id = anvil.server.call("add_exercise_to_workout", workout_id, exercise, aaron_exercise_type, len(self._exercises), "Aaron")
      #print(f"Aaron's Workout Exercise ID: {aaron_workout_exercise_id}")
      weez_workout_exercise_id = anvil.server.call("add_exercise_to_workout", workout_id, exercise, weez_exercise_type, len(self._exercises), "Weez")
      #print(f"Weez's Workout Exercise ID: {weez_workout_exercise_id}")

      this_ex = Exercise(exercise, body_part, aaron_workout_exercise_id, weez_workout_exercise_id)
      this_ex.aaron_exercise_type = aaron_exercise_type
      this_ex.weez_exercise_type = weez_exercise_type
      #this_ex.addSet("Aaron")
      self._exercises.append(this_ex)
      self.repeating_panel_1.items = self._exercises
      
  def update_db_button_click(self, **event_args):
    ud_form = UpdateDatabaseForm()
    result = alert(title="Update Database", content=ud_form)

  def new_workout_click(self, **event_args):
    global workout_id
    
    awf = AddWorkoutForm()
    awf.workout_notes_text_area.text = anvil.server.call("get_workout_notes", awf.add_workout_date_picker.date)
    result = alert(title="Add Workout", content=awf, large=True, buttons=[("OK", True), ("Cancel", False)])

    if result:
      workout_date = awf.add_workout_date_picker.date
      workout_notes = awf.workout_notes_text_area.text

      workout_id = anvil.server.call("add_workout", workout_date, workout_notes)
      print(f"Workout ID: {workout_id}")

      curr_exs = anvil.server.call("get_workout_exercises", workout_id)
      print("HEY")