from ._anvil_designer import UpdateSetFormTemplate
from anvil import *
import anvil.server
import math


class UpdateSetForm(UpdateSetFormTemplate):
  def __init__(self, prevWeight, prevReps, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.previous_weight_text_box.text = prevWeight
    self.this_weight_text_box.text = prevWeight
        
    self.previous_reps_text_box.text = prevReps
    self.this_reps_text_box.text = prevReps
    self.reps_slider.value = prevReps

  
  def reps_slider_change(self, handle, **event_args):
    self.this_reps_text_box.text = round(self.reps_slider.value)

  def this_reps_text_box_change(self, **event_args):
    self.reps_slider.value = self.this_reps_text_box.text

  def reps_slider_slide(self, handle, **event_args):
    self.this_reps_text_box.text = round(self.reps_slider.value)

  
  def weight_slider_change(self, handle, **event_args):
    self.this_weight_text_box.text = round(self.weight_slider.value * 4)/4

  def this_weight_text_box_change(self, **event_args):
    self.weight_slider.value = self.this_weight_text_box.text

  def minus_10_button_click(self, **event_args):
    self.this_weight_text_box.text = float(self.this_weight_text_box.text) - 10

  def minus_5_button_click(self, **event_args):
    self.this_weight_text_box.text = float(self.this_weight_text_box.text) - 5

  def minus_2p5_button_click(self, **event_args):
    self.this_weight_text_box.text = float(self.this_weight_text_box.text) - 2.5

  def plus_2p5_button_click(self, **event_args):
    self.this_weight_text_box.text = float(self.this_weight_text_box.text) + 2.5

  def plus_5_button_click(self, **event_args):
    self.this_weight_text_box.text = float(self.this_weight_text_box.text) + 5

  def plus_10_button_click(self, **event_args):
    self.this_weight_text_box.text = float(self.this_weight_text_box.text) + 10