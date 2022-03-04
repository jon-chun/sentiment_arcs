
def read_yaml(Corpus_Genre, Corpus_Type):
  '''
  Given a Corpus_Genre (e.g. novels)
  Read and return the long-form titles for both Models and Corpus Texts
  '''

  global models_titles_dt
  global corpus_titles_dt

  # Read SentimentArcs YAML Config Files on Models
  # Model in SentimentArcs Ensemble
  with open("./config/models_ref_info.yaml", "r") as stream:
    try:
      models_titles_dt = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  if Corpus_Genre == 'novels':

    # Novel Text Files
    if Corpus_Type == 'new':
      # Corpus of New Novels
      with open("./config/novels_new_info.yaml", "r") as stream:
        try:
          corpus_titles_dt = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
          print(exc)
    else:
      # Corpus of Reference Novels
      with open("./config/novels_ref_info.yaml", "r") as stream:
        try:
          corpus_titles_dt = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
          print(exc)    

  elif Corpus_Genre == 'finance':

    # Finance Text Files
    if Corpus_Type == 'new':
      # Corpus of New Finance Texts
      with open("./config/finance_new_info.yaml", "r") as stream:
        try:
          corpus_titles_dt = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
          print(exc)
    else:
      # Corpus of Reference Finance Texts
      with open("./config/finance_ref_info.yaml", "r") as stream:
        try:
          corpus_titles_dt = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
          print(exc)

  elif Corpus_Genre == 'social_media':

    # Social Media Text Files
    if Corpus_Type == 'new':
      # Corpus of New Social Media Texts
      with open("./config/social_new_info.yaml", "r") as stream:
        try:
          corpus_titles_dt = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
          print(exc)
    else:
      # Corpus of Reference Social Media Texts
      with open("./config/social_ref_info.yaml", "r") as stream:
        try:
          corpus_titles_dt = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
          print(exc)

  else:
    
    print(f"ERROR: Illegal Corpus_Genre: {Corpus_Type}\n")

  return