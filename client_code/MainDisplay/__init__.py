from ._anvil_designer import MainDisplayTemplate
from anvil import *

class Exercise():
  def __init__(self, name):
    self._name = name
    self._sets = {}
    
class MainDisplay(MainDisplayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self._exercises = []

  def add_exercise_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
