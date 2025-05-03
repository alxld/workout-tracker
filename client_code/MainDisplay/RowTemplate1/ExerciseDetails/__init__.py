from ._anvil_designer import ExerciseDetailsTemplate
from anvil import *


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
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break
        
    self.parent.parent.items[idx].removeSet("Aaron")
    self.parent.parent.items = self.parent.parent.items

  def weez_delete_set_button_click(self, **event_args):
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break
        
    self.parent.parent.items[idx].removeSet("Weez")
    self.parent.parent.items = self.parent.parent.items

  def remove_exercise_button_click(self, **event_args):
    for idx in range(len(self.parent.parent.items)):
      if self.parent.item == self.parent.parent.items[idx]:
        break

    del self.parent.parent.items[idx]
    self.parent.parent.items = self.parent.parent.items