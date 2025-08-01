import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#

class Exercise:
  def __init__(self, name, body_part, aaron_workout_exercise_id, weez_workout_exercise_id, exercise_order, from_db=False):
    self._name = name
    self._body_part = body_part
    self._exerciseType = {"Aaron": "UNKNOWN", "Weez": "UNKNOWN"}
    self._sets = {"Aaron": [], "Weez": []}
    self._defaultSets = 3
    self._exercise_id = None
    self._aaron_workout_exercise_id = aaron_workout_exercise_id
    self._weez_workout_exercise_id = weez_workout_exercise_id
    self._exercise_order = -1

    if from_db:
      if aaron_workout_exercise_id != -1:
        aaron_sets = anvil.server.call("get_sets_for_exercise_id", aaron_workout_exercise_id)
        self._exercise_order = anvil.server.call("get_exercise_order_for_workout_exercise_id", aaron_workout_exercise_id)
      if weez_workout_exercise_id != -1:
        weez_sets = anvil.server.call("get_sets_for_exercise_id", weez_workout_exercise_id)
        if self._exercise_id == -1:
          self._exercise_order = anvil.server.call("get_exercise_order_for_workout_exercise_id", weez_workout_exercise_id)

      if aaron_sets:
        for set in aaron_sets:
          prev_weight, prev_reps = anvil.server.call("get_previous_set_weight_reps", set[0])
          newset = Set(set[3], prev_weight, prev_reps, set[0], "Aaron", self)
          if set[1]:
            newset.weight = set[1]
          if set[2]:
            newset.reps = set[2]
          self._sets["Aaron"].append(newset)

      if weez_sets:
        for set in weez_sets:
          prev_weight, prev_reps = anvil.server.call("get_previous_set_weight_reps", set[0])
          newset = Set(set[3], prev_weight, prev_reps, set[0], "Weez", self)
          if set[1]:
            newset.weight = set[1]
          if set[2]:
            newset.reps = set[2]
          self._sets["Weez"].append(newset)
    
    else:
      for i in range(self._defaultSets):
        if aaron_workout_exercise_id != -1:
          self.addSet('Aaron')
        if weez_workout_exercise_id != -1:
          self.addSet('Weez')

  def __getitem__(self, key):
    if key == "name":
      return self._name
    if key == "aaron":
      return self._sets['Aaron']
    if key == "weez":
      return self._sets['Weez']

    raise Exception(f"{key} not found in Exercise object")

  def addSet(self, user):
    if user == "Aaron":
      wid = self._aaron_workout_exercise_id
    else:
      wid = self._weez_workout_exercise_id
    set_id = anvil.server.call("add_set_to_exercise", wid, len(self._sets[user])+1)
    prev_weight, prev_reps = anvil.server.call("get_previous_set_weight_reps", set_id)
    newset = Set(len(self._sets[user])+1, prev_weight, prev_reps, set_id, user, self)
    self._sets[user].append(newset)
    return newset

  def removeSet(self, user):
    if user == "Aaron":
      wid = self._aaron_workout_exercise_id
    else:
      wid = self._weez_workout_exercise_id

    set_id = self._sets[user][-1].set_id
    self._sets[user] = self._sets[user][:-1]
    anvil.server.call("remove_set_from_exercise", set_id)

  @property
  def is_complete(self):
    for set in self._sets['Aaron'] + self._sets['Weez']:
      if not set.is_complete:
        return False

    # Fall through to True
    return True
  
  def remove_from_database(self):
    for set in self._sets['Aaron'] + self._sets['Weez']:
      set.remove_from_database()

    anvil.server.call("remove_exercise_from_workout", self._aaron_workout_exercise_id)
    anvil.server.call("remove_exercise_from_workout", self._weez_workout_exercise_id)

  @property
  def name(self):
    return self._name
  
  @property
  def aaron_exercise_type(self):
    return self._exerciseType['Aaron']

  @aaron_exercise_type.setter
  def aaron_exercise_type(self, type):
    self._exerciseType['Aaron'] = type

  @property
  def weez_exercise_type(self):
    return self._exerciseType['Weez']

  @weez_exercise_type.setter
  def weez_exercise_type(self, type):
    self._exerciseType['Weez'] = type

  @property
  def exercise_id(self):
    if not self._exercise_id:
      if self._aaron_workout_exercise_id:
        self._exercise_id = anvil.server.call("get_exercise_id_for_workout_exercise", self._aaron_workout_exercise_id)
      else:
        self._exercise_id = anvil.server.call("get_exercise_id_for_workout_exercise", self._weez_workout_exercise_id)
    
    return self._exercise_id
  
  def exercise_history(self, user):
    if user == 'aaron':
      to_return = anvil.server.call("get_all_weight_rep_data_for_exercise_id", self.exercise_id, 'aaron', self.aaron_exercise_type)
    else:
      to_return = anvil.server.call("get_all_weight_rep_data_for_exercise_id", self.exercise_id, 'weez', self.weez_exercise_type)

    volume_data = {}
    weight_data = {}
    reps_data = {}
    for row in to_return:
      if not row['date'] in volume_data:
        if type(row['date']) == 'datetime':
          row['date'] = row['date'].date()
        volume_data[row['date']] = 0
        weight_data[row['date']] = 0
        reps_data[row['date']] = 0
        
      volume_data[row['date']] += row['weight'] * row['reps']
      weight_data[row['date']] += row['weight']
      reps_data[row['date']] += row['reps']

    for date in weight_data:
      weight_data[date] /= len(weight_data)
      reps_data[date] /= len(reps_data)
    
    return to_return, volume_data, weight_data, reps_data
      
class Set:
  def __init__(self, setNum, prev_weight, prev_reps, set_id, user, exercise):
    self.setNum = setNum
    self.weight = 0
    self.reps = 0
    self.prevWeight = prev_weight
    self.prevReps = prev_reps
    self.set_id = set_id
    self.user = user
    self.exercise = exercise

  def __getitem__(self, key):
    if key == "setNum":
      return self.setNum
    if key == "weight":
      return self.weight
    if key == "reps":
      return self.reps
    if key == "prevWeight":
      return self.prevWeight
    if key == "prevReps":
      return self.prevReps

    raise Exception(f"{key} not found in Set object")

  @property
  def is_complete(self):
    if self.weight != 0 and self.reps != 0:
      return True
    else:
      return False
  
  def update_database(self):
    anvil.server.call("update_set_weight_reps", self.set_id, self.weight, self.reps)

  def remove_from_database(self):
    anvil.server.call("remove_set_from_exercise", self.set_id)