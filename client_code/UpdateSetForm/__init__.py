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
    self.weight_slider.value = prevWeight
    self.weight_quarter_slider.value = prevWeight - math.floor(float(prevWeight))
    
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

  def weight_slider_slide(self, handle, **event_args):
    self.this_weight_text_box.text = round(self.weight_slider.value * 4)/4

  def weight_quarter_slider_change(self, handle, **event_args):
    newval = math.floor(float(self.this_weight_text_box.text)/5)*5 + float(self.weight_quarter_slider.value)
    self.this_weight_text_box.text = newval

  def weight_quarter_slider_slide(self, handle, **event_args):
    self.weight_quarter_slider_change(handle)
