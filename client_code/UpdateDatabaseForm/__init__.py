from ._anvil_designer import UpdateDatabaseFormTemplate
from anvil import *


class UpdateDatabaseForm(UpdateDatabaseFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
