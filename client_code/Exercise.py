import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#

class Exercise:
  def __init__(self, name, body_part, aaron_workout_exercise_id, weez_workout_exercise_id, from_db=False):
    self._name = name
    self._body_part = body_part
    self._exerciseType = {"Aaron": "UNKNOWN", "Weez": "UNKNOWN"}
    self._sets = {"Aaron": [], "Weez": []}
    self._defaultSets = 3
    self._aaron_workout_exercise_id = aaron_workout_exercise_id
    self._weez_workout_exercise_id = weez_workout_exercise_id

    if from_db:
      aaron_sets = anvil.server.call("get_sets_for_exercise_id", aaron_workout_exercise_id)
      weez_sets = anvil.server.call("get_sets_for_exercise_id", weez_workout_exercise_id)

      if aaron_sets:
        for set in aaron_sets:
          prev_weight, prev_reps = anvil.server.call("get_previous_set_weight_reps", set[0])
          newset = Set(set[3], prev_weight, prev_reps, set[0])
          if set[1]:
            newset.weight = set[1]
          if set[2]:
            newset.reps = set[2]
          self._sets["Aaron"].append(newset)

      if weez_sets:
        for set in weez_sets:
          prev_weight, prev_reps = anvil.server.call("get_previous_set_weight_reps", set[0])
          newset = Set(set[3], prev_weight, prev_reps, set[0])
          if set[1]:
            newset.weight = set[1]
          if set[2]:
            newset.reps = set[2]
          self._sets["Weez"].append(newset)
    
    else:
      for i in range(self._defaultSets):
        self.addSet('Aaron')
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
    newset = Set(len(self._sets[user])+1, prev_weight, prev_reps, set_id)
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

class Set:
  def __init__(self, setNum, prev_weight, prev_reps, set_id):
    self.setNum = setNum
    self.weight = 0
    self.reps = 0
    self.prevWeight = prev_weight
    self.prevReps = prev_reps
    self.set_id = set_id

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

  def update_database(self):
    anvil.server.call("update_set_weight_reps", self.set_id, self.weight, self.reps)

  def remove_from_database(self):
    anvil.server.call("remove_set_from_exercise", self.set_id)