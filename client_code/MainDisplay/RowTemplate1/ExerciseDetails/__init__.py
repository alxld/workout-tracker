from ._anvil_designer import ExerciseDetailsTemplate
from ....ExerciseInfoForm import ExerciseInfoForm
from anvil import *
import anvil.server


class ExerciseDetails(ExerciseDetailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

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
    
