from ._anvil_designer import ExerciseDetailsTemplate
from ....ExerciseInfoForm import ExerciseInfoForm
from anvil import *
import anvil.server


class ExerciseDetails(ExerciseDetailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def aaron_add_set_button_click(self, **event_args):
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break

    self.parent.parent.items[idx].addSet("Aaron")
    self.parent.parent.items = self.parent.parent.items
    
  def weez_add_set_button_click(self, **event_args):
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break

    self.parent.parent.items[idx].addSet("Weez")
    self.parent.parent.items = self.parent.parent.items

  def aaron_delete_set_button_click(self, **event_args):
    results = confirm("Are you sure you want to delete set?", large=True, buttons=[ ("Yes", True), ("No", False) ])
    if not results:
      return
      
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break
        
    self.parent.parent.items[idx].removeSet("Aaron")
    self.parent.parent.items = self.parent.parent.items

  def weez_delete_set_button_click(self, **event_args):
    results = confirm("Are you sure you want to delete set?", large=True, buttons=[ ("Yes", True), ("No", False) ])
    if not results:
      return
      
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break
        
    self.parent.parent.items[idx].removeSet("Weez")
    self.parent.parent.items = self.parent.parent.items

  def remove_exercise_button_click(self, **event_args):
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break

    ex = self.parent.parent.items[idx]

    results = confirm(f"Are you sure you want to delete exercise: {ex.name}?", large=True, buttons=[ ("Yes", True), ("No", False) ])
    if not results:
      return
    
    ex.remove_from_database()
    
    del self.parent.parent.items[idx]
    self.parent.parent.items = self.parent.parent.items

  def highlight_info_button(self):
    if not self.parent or not self.parent.item:
      self.info_button.background = "theme:White"
      return
      
    exercise_id = self.parent.item.exercise_id
    details = anvil.server.call("get_exercise_details_for_exercise_id", exercise_id)
    if 'comments' in details and details['comments'] != None and details['comments'] != "":
      self.info_button.background = "theme:Secondary 500"
    else:
      self.info_button.background = "theme:White"

  def info_button_click(self, **event_args):
    exercise_id = self.parent.item.exercise_id
    details = anvil.server.call("get_exercise_details_for_exercise_id", exercise_id)
    if 'description' in details:
      desc = details['description']
    else:
      desc = None
    if 'comments' in details:
      comm = details['comments']
    else:
      comm = None
    if 'youtube_link' in details:
      link = details['youtube_link']
    else:
      link = None
    eif = ExerciseInfoForm(exercise_id, details['exercise_name'], desc, comm, link)
    result = alert(title="Exercise Info", content=eif, large=True, buttons=[])

    if result:
      anvil.server.call("set_exercise_details_for_exercise_id", exercise_id, eif.description_text_area.text, eif.comments_text_area.text, eif.youtube_link_text_box.text)

    self.highlight_info_button()

  def aaron_history_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.parent._volume_toggle = not self.parent._volume_toggle
    self.parent.updatePlots()

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.highlight_info_button()

    
