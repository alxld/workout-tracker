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

    self._AcurrTimer = datetime(2000,1,1)
    self._WcurrTimer = datetime(2000,1,1)
    #self._timerState = "PAUSED"
    self._AtimerState = "PAUSED"
    self._WtimerState = "PAUSED"

    #self._exercises.append(Exercise("blah", "no part"))
    self.repeating_panel_1.items = self.reorder_completed_exercises(self._exercises)

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

      exercise_order = 0
      if aaron_exercise_type != "None":
        aaron_workout_exercise_id = anvil.server.call("add_exercise_to_workout", workout_id, exercise, aaron_exercise_type, len(self._exercises), "Aaron")
        exercise_order = anvil.server.call("get_exercise_order_for_workout_exercise_id", aaron_workout_exercise_id)
      else:
        aaron_workout_exercise_id = -1
      if weez_exercise_type != "None":
        weez_workout_exercise_id = anvil.server.call("add_exercise_to_workout", workout_id, exercise, weez_exercise_type, len(self._exercises), "Weez")
        exercise_order = anvil.server.call("get_exercise_order_for_workout_exercise_id", weez_workout_exercise_id)
      else:
        weez_workout_exercise_id = -1

      this_ex = Exercise(exercise, body_part, aaron_workout_exercise_id, weez_workout_exercise_id, exercise_order)

      if aaron_exercise_type != "None":
        this_ex.aaron_exercise_type = aaron_exercise_type
      if weez_exercise_type != "None":
        this_ex.weez_exercise_type = weez_exercise_type
      #this_ex.addSet("Aaron")
      self._exercises.append(this_ex)
      self.repeating_panel_1.items = self.reorder_completed_exercises(self._exercises)
      
  def edit_db_button_click(self, **event_args):
    ud_form = UpdateDatabaseForm()
    result = alert(title="Update Database", content=ud_form)

  def reorder_completed_exercises(self, exercises):
    incomplete_exercises = []
    complete_exercises = []
    #print(f"Starting exercises:  {', '.join([ e.name for e in exercises ])}")
    #print(f"Starting incomplete: {', '.join([ e.name for e in incomplete_exercises ])}")
    #print(f"Starting complete:   {', '.join([ e.name for e in complete_exercises ])}")
    
    for exercise in sorted(exercises, key=lambda e: e._exercise_order):
      if exercise.is_complete:
        complete_exercises.append(exercise)
      else:
        incomplete_exercises.append(exercise)

    all = incomplete_exercises + complete_exercises
    #print(f"Ending incomplete:   {', '.join([ e.name for e in incomplete_exercises ])}")
    #print(f"Ending complete:     {', '.join([ e.name for e in complete_exercises ])}")
    #print(f"Ending all:          {', '.join([ e.name for e in all ])}")
    
    return all

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

      print(f"Date: {workout_date}")
      workout_id = anvil.server.call("add_workout", workout_date, workout_notes)
      print(f"Workout ID: {workout_id}")

      curr_exs = anvil.server.call("get_workout_exercises", workout_id)
      for ex_id in curr_exs:
        ex_name = anvil.server.call("get_exercise_name_for_exercise_id", ex_id)
        aaron_workout_exercise_id = anvil.server.call("get_workout_exercise_for_user", workout_id, ex_id, "Aaron")
        weez_workout_exercise_id = anvil.server.call("get_workout_exercise_for_user", workout_id, ex_id, "Weez")
        if aaron_workout_exercise_id != -1:
          exercise_order = anvil.server.call("get_exercise_order_for_workout_exercise_id", aaron_workout_exercise_id)
        else:
          exercise_order = anvil.server.call("get_exercise_order_for_workout_exercise_id", weez_workout_exercise_id)
        body_part = anvil.server.call("get_body_part_for_exercise", ex_id)
        this_ex = Exercise(ex_name, body_part, aaron_workout_exercise_id, weez_workout_exercise_id, exercise_order, from_db=True)
        this_ex.aaron_exercise_type = anvil.server.call("get_exercise_type_for_exercise_id", aaron_workout_exercise_id)
        this_ex.weez_exercise_type = anvil.server.call("get_exercise_type_for_exercise_id", weez_workout_exercise_id)
        self._exercises.append(this_ex)
      if curr_exs:
        self.repeating_panel_1.items = self.reorder_completed_exercises(self._exercises)

  def main_timer_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.datetime_headline.text = datetime.now().strftime("%a %B %d, %Y  %-I:%M %p")
    if self._AtimerState == "PLAYING":
      self._AcurrTimer = self._AcurrTimer + timedelta(seconds=1)
      if self._AcurrTimer > datetime(2000,1,1,minute=30):
        self._AcurrTimercurrTimer = datetime(2000,1,1)
        self._AtimerState = "PAUSED"
      
      if self._AcurrTimer > datetime(2000,1,1,minute=3):
        self.atimer_headline.foreground = 'theme:Secondary 500'
      else:
        self.atimer_headline.foreground = ''
    self.atimer_headline.text = self._AcurrTimer.strftime("  %M:%S")

    if self._WtimerState == "PLAYING":
      self._WcurrTimer = self._WcurrTimer + timedelta(seconds=1)
      if self._WcurrTimer > datetime(2000,1,1,minute=30):
        self._WcurrTimercurrTimer = datetime(2000,1,1)
        self._WtimerState = "PAUSED"

      if self._WcurrTimer > datetime(2000,1,1,minute=3):
        self.wtimer_headline.foreground = 'theme:Secondary 500'
      else:
        self.wtimer_headline.foreground = ''
    self.wtimer_headline.text = self._WcurrTimer.strftime("  %M:%S")

  #def timer_link_click(self, **event_args):
  #  """This method is called when the link is clicked"""
  #  if self._timerState == "PAUSED":
  #    self._timerState = "PLAYING"
  #  elif self._timerState == "PLAYING":
  #    self._timerState = "PAUSED"
  #    self._currTimer = datetime(2000,1,1)
  #    
  #  self.timer_headline.text = self._currTimer.strftime("  %M:%S")

  def atimer_reset_and_run(self):
    """ This method resets Aaron's timer to 0 and starts counting"""
    self._AcurrTimer = datetime(2000, 1, 1)
    self._AtimerState = "PLAYING"

    self.atimer_headline.text = self._AcurrTimer.strftime("  %M:%S")

  def wtimer_reset_and_run(self):
    """ This method resets Weez's timer to 0 and starts counting"""
    self._WcurrTimer = datetime(2000, 1, 1)
    self._WtimerState = "PLAYING"

    self.wtimer_headline.text = self._WcurrTimer.strftime("  %M:%S")

  
  def atimer_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self._AtimerState == "PAUSED":
      self._AtimerState = "PLAYING"
    elif self._AtimerState == "PLAYING":
      self._AtimerState = "PAUSED"
      self._AcurrTimer = datetime(2000,1,1)

    self.atimer_headline.text = self._AcurrTimer.strftime("  %M:%S")

  def wtimer_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self._WtimerState == "PAUSED":
      self._WtimerState = "PLAYING"
    elif self._WtimerState == "PLAYING":
      self._WtimerState = "PAUSED"
      self._WcurrTimer = datetime(2000,1,1)

    self.wtimer_headline.text = self._WcurrTimer.strftime("  %M:%S")
