from ._anvil_designer import MainDisplayTemplate
from ..AddExerciseForm import AddExerciseForm
from ..UpdateDatabaseForm import UpdateDatabaseForm
from ..Exercise import Exercise, Set
from ..AddWorkoutForm import AddWorkoutForm
from anvil import *
import anvil.server
from datetime import datetime, time, timedelta
 
class MainDisplay(MainDisplayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self._exercises = []

    self._currTimer = datetime(2000,1,1)
    self._timerState = "PAUSED"

    #self._exercises.append(Exercise("blah", "no part"))
    self.repeating_panel_1.items = self._exercises

    #self.body_parts = anvil.server.call("get_body_parts")
    #print(self.body_parts)
 
  
  def add_exercise_button_click(self, **event_args):
    # Pull up AddExerciseForm to get new exercise details
    aef = AddExerciseForm()
    result = alert(title="Add Exercise", content=aef, large=True, buttons=[])

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
      
  def edit_db_button_click(self, **event_args):
    ud_form = UpdateDatabaseForm()
    result = alert(title="Update Database", content=ud_form)

  def new_workout_click(self, **event_args):
    global workout_id
    
    awf = AddWorkoutForm()
    #awf.workout_notes_text_area.text = anvil.server.call("get_workout_notes", awf.add_workout_date_picker.date)
    result = alert(title="Add Workout", content=awf, large=True, buttons=[])

    if result:
      # Workout already exists, populate exercises
      
      # Remove any existing objects
      self.repeating_panel_1.items = []
      self._exercises = []
      
      workout_date = awf.add_workout_date_picker.date
      workout_notes = awf.workout_notes_text_area.text

      workout_id = anvil.server.call("add_workout", workout_date, workout_notes)
      print(f"Workout ID: {workout_id}")

      curr_exs = anvil.server.call("get_workout_exercises", workout_id)
      for ex_id in curr_exs:
        ex_name = anvil.server.call("get_exercise_name_for_exercise_id", ex_id)
        aaron_workout_exercise_id = anvil.server.call("get_workout_exercise_for_user", workout_id, ex_id, "Aaron")
        weez_workout_exercise_id = anvil.server.call("get_workout_exercise_for_user", workout_id, ex_id, "Weez")
        body_part = anvil.server.call("get_body_part_for_exercise", ex_id)
        this_ex = Exercise(ex_name, body_part, aaron_workout_exercise_id, weez_workout_exercise_id, from_db=True)
        this_ex.aaron_exercise_type = anvil.server.call("get_exercise_type_for_exercise_id", aaron_workout_exercise_id)
        this_ex.weez_exercise_type = anvil.server.call("get_exercise_type_for_exercise_id", weez_workout_exercise_id)
        self._exercises.append(this_ex)
      if curr_exs:
        self.repeating_panel_1.items = self._exercises

  def main_timer_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.datetime_headline.text = datetime.now().strftime("%a %B %d, %Y  %-I:%M %p")
    if self._timerState == "PLAYING":
      self._currTimer = self._currTimer + timedelta(seconds=1)
      if self._currTimer > datetime(2000,1,1,minute=30):
        self._currTimer = datetime(2000,1,1)
        self._timerState = "PAUSED"
    self.timer_headline.text = self._currTimer.strftime("  %M:%S")

  def timer_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self._timerState == "PAUSED":
      self._timerState = "PLAYING"
    elif self._timerState == "PLAYING":
      self._timerState = "PAUSED"
      self._currTimer = datetime(2000,1,1)
      
    self.timer_headline.text = self._currTimer.strftime("  %M:%S")