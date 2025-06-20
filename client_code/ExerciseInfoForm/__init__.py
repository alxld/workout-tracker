from ._anvil_designer import ExerciseInfoFormTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server

class ExerciseInfoForm(ExerciseInfoFormTemplate):
  def __init__(self, exercise_id, name, description, comments, youtube_link, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.header.text = f"Exercise Info for {name}"

    if description:
      self.description_text_area.text = description

    if comments:
      self.comments_text_area.text = comments

    if youtube_link:
      self.youtube_video.visible = True
      self.youtube_video.youtube_id = youtube_link
      self.youtube_link_text_box.text = youtube_link
    else:
      self.youtube_video.visible = False

    self._exercise_id = exercise_id

    #exercise_data = anvil.server.call("get_all_weight_rep_data_for_exercise_id", self._exercise_id, user_id=1, workout_type_id=2)
    
  def ok_button_click(self, **event_args):
    self.raise_event("x-close-alert", value=True)

  def cancel_button_click(self, **event_args):
    self.raise_event("x-close-alert", value=False)
