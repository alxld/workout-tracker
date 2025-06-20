from ._anvil_designer import RowTemplate1Template
from anvil import *
import plotly.graph_objects as go


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self._volume_toggle = False

    # Any code you write here will run before the form opens.
    self.exercise_details_1.exercise_name_headline.text = self.item['name']
    self.exercise_details_1.aaron_exercise_type.text = self.item.aaron_exercise_type
    self.exercise_details_1.weez_exercise_type.text = self.item.weez_exercise_type
    self.set_details_aaron.repeating_panel_1.items = self.item['aaron']
    self.set_details_weez.repeating_panel_1.items = self.item['weez']

    self.ex_set_history = {}
    self.ex_volume_history = {}
    self.ex_weight_history = {}
    self.ex_reps_history = {}
    self.ex_set_history['aaron'], self.ex_volume_history['aaron'], self.ex_weight_history['aaron'], self.ex_reps_history['aaron'] = self.item.exercise_history('aaron')
    self.ex_set_history['weez'],  self.ex_volume_history['weez'],  self.ex_weight_history['weez'],  self.ex_reps_history['weez']  = self.item.exercise_history('weez')

    self.updatePlots()


  def updatePlots(self):
    self.set_details_aaron.volume_plot.layout.margin = dict(t=20, b=20)
    self.set_details_weez.volume_plot.layout.margin = dict(t=20, b=20)

    if self._volume_toggle:
      self.set_details_aaron.volume_plot.layout.yaxis = dict(title="Volume")
      self.set_details_aaron.volume_plot.data = [
        go.Scatter(x=list(self.ex_volume_history['aaron'].keys()), y=list(self.ex_volume_history['aaron'].values()))
      ]

      self.set_details_weez.volume_plot.layout.yaxis = dict(title="Volume")
      self.set_details_weez.volume_plot.data = [
        go.Scatter(x=list(self.ex_volume_history['weez'].keys()), y=list(self.ex_volume_history['weez'].values()))
      ]
        
    else:
      self.set_details_aaron.volume_plot.layout.yaxis  = dict(title="Weight", overlaying="y")
      self.set_details_aaron.volume_plot.layout.yaxis2 = dict(title="Reps", overlaying="y", side='right')

      self.set_details_aaron.volume_plot.data = [
        go.Scatter(x=list(self.ex_weight_history['aaron'].keys()), y=list(self.ex_weight_history['aaron'].values()), name="Weight"),
        go.Scatter(x=list(self.ex_reps_history['aaron'].keys()), y=list(self.ex_reps_history['aaron'].values()), name="Reps") #, yaxis="y2")
      ]

      self.set_details_weez.volume_plot.layout.yaxis  = dict(title="Weight")
      self.set_details_weez.volume_plot.layout.yaxis2 = dict(title="Reps", side='right')
      x_values = list(self.ex_weight_history['weez'].keys())
      y_weight_values = list(self.ex_weight_history['weez'].values())
      y_reps_values   = list(self.ex_reps_history['weez'].values())

      print(x_values)
      print(y_weight_values)
      print(y_reps_values)
      
      self.set_details_weez.volume_plot.data = [
        go.Scatter(x=x_values, y=y_weight_values, name="Weight"),
        go.Scatter(x=x_values, y=y_reps_values, name="Reps") #, yaxis="y2")
#        go.Scatter(x=list(self.ex_weight_history['weez'].keys()), y=list(self.ex_weight_history['weez'].values()), name="Weight"),
#        go.Scatter(x=list(self.ex_reps_history['weez'].keys()),   y=list(self.ex_reps_history['weez'].values()), name="Reps", yaxis="y2")
      ]

