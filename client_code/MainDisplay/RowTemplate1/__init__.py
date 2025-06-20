from ._anvil_designer import RowTemplate1Template
from anvil import *
import plotly.graph_objects as go


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.exercise_details_1.exercise_name_headline.text = self.item['name']
    self.exercise_details_1.aaron_exercise_type.text = self.item.aaron_exercise_type
    self.exercise_details_1.weez_exercise_type.text = self.item.weez_exercise_type
    self.set_details_aaron.repeating_panel_1.items = self.item['aaron']
    self.set_details_weez.repeating_panel_1.items = self.item['weez']

    self.ex_history = {}
    self.ex_history['aaron'] = self.item.exercise_history('aaron')
    self.ex_history['weez']  = self.item.exercise_history('weez')

    print()
