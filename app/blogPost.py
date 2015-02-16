class BlogPost(object):
  """
    Blog post object. Contains all the data needed for daily blog post.
    Attributes:
      projects: list of list of actions. Sublists represent projects.
      learned: string representing what I learned. Possibly bullet pointed?
      qa: Maybe dictionary? Maybe string? Maybe list of 2 elem lists?
          First elem is question, second elem is answer?
  """

  def __init__(self, projects, learned, qa):
    self.projects = projects
    self.learned = learned
    self.qa = qa
