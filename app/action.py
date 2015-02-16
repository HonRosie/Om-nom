class Action(object):
  """
  Action object.
  Attributes:
    description: String representing what the action is
    subTasks: list of actions representing subTasks
    comments: String representing additional details for action
    project: String representing which project this task is for
            Action and big questions are default existing projects
    date: String/date field? representing date action needs to be completed
          Updated to date completed when action is done
    doneness: boolean representing if task is done
  """

  def __init__(self, description, subTasks=[], comments=None,
               project=None, date=None, doneness=False):
    self.description = description
    self.subTasks = subTasks
    self.comments = comments
    self.project = project
    self.date = date
    self.doneness = doneness
