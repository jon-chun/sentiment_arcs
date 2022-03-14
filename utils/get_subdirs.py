
def get_subdirs(Corpus_Genre, Corpus_Type, NotebookModels):
  '''
  Given a two strings: Corpus, Text_type
  Set all global SUB/DIR constants
  '''

  global FNAME_SENTIMENT_RAW
  global DIR_ROOT
  global SUBDIR_SENTIMENTARCS
  global SUBDIR_TEXT_RAW
  global SUBDIR_TEXT_CLEAN
  global SUBDIR_SENTIMENT_RAW
  global SUBDIR_SENTIMENT_CLEAN
  global SUBDIR_TIMESERIES_RAW
  global SUBDIR_TIMESERIES_CLEAN
  global SUBDIR_PLOTS
  global SUBDIR_DATA
  global SUBDIR_UTILS

  if NotebookModels == 'syuzhetr2sentimentr':
    FNAME_SENTIMENT_RAW = f'sentiment_raw_{Corpus_Genre}_{Corpus_Type}_syuzhetr2sentimentr.json'
  elif NotebookModels == 'lex2ml':
    FNAME_SENTIMENT_RAW = f'sentiment_raw_{Corpus_Genre}_{Corpus_Type}_lex2ml.json'
  elif NotebookModels == 'dnn2transformers':
    FNAME_SENTIMENT_RAW = f'sentiment_raw_{Corpus_Genre}_{Corpus_Type}_dnn2transformers.json'
  elif NotebookModels == 'none':
    FNAME_SENTIMENT_RAW = f'[NONE]'
  else:
    print(f'ERROR: Illegal value for NotebookModels: {NotebookModels}')
    return

  SUBDIR_SENTIMENTARCS = '/gdrive/MyDrive/cdh/sentiment_arcs'
  SUBDIR_TEXT_RAW = f"./text_raw/text_raw_{Corpus_Genre}_{Corpus_Type}"
  SUBDIR_TEXT_CLEAN = f"./text_clean/text_clean_{Corpus_Genre}_{Corpus_Type}/"
  SUBDIR_SENTIMENT_RAW = f"./sentiment_raw/sentiment_raw_{Corpus_Genre}_{Corpus_Type}/"
  SUBDIR_SENTIMENT_CLEAN = f"./sentiment_clean/sentiemnt_clean_{Corpus_Genre}_{Corpus_Type}/"
  SUBDIR_TIMESERIES_RAW = f"./timeseries_raw/timeseries_raw_{Corpus_Genre}_{Corpus_Type}/"
  SUBDIR_TIMESERIES_CLEAN = f"./timeseries_clean/timeseries_clean_{Corpus_Genre}_{Corpus_Type}/"
  SUBDIR_PLOTS = f"./plots/"
  SUBDIR_DATA = f"./data/"
  SUBDIR_UTILS = f"./utils/"

  # Verify Directory Structure

  print('Verify the Directory Structure:\n')
  print('-------------------------------\n')

  print(f'           [Corpus Genre]: {Corpus_Genre}\n')
  print(f'            [Corpus Type]: {Corpus_Type}\n\n')

  print(f'    [FNAME_SENTIMENT_RAW]: {FNAME_SENTIMENT_RAW}\n\n')
  print('\n\nINPUTS:')
  print('-------------------------------\n')
  print(f'   [SUBDIR_SENTIMENTARCS]: {SUBDIR_SENTIMENTARCS}\n')
  print('\nSTEP 1: Clean Text')
  print('--------------------\n')
  print(f'        [SUBDIR_TEXT_RAW]: {SUBDIR_TEXT_RAW}\n')
  print(f'      [SUBDIR_TEXT_CLEAN]: {SUBDIR_TEXT_CLEAN}\n')
  print('\nSTEP 2: Get Sentiments')
  print('--------------------\n')
  print(f'   [SUBDIR_SENTIMENT_RAW]: {SUBDIR_SENTIMENT_RAW}\n')
  print(f' [SUBDIR_SENTIMENT_CLEAN]: {SUBDIR_SENTIMENT_CLEAN}\n')
  print('\nSTEP 3: Smooth Time Series and Get Crux Points')
  print('--------------------\n')
  print(f'  [SUBDIR_TIMESERIES_RAW]: {SUBDIR_SENTIMENT_RAW}\n')
  print(f'[SUBDIR_TIMESERIES_CLEAN]: {SUBDIR_SENTIMENT_CLEAN}\n')
  print('\n\nOUTPUTS:')
  print('-------------------------------\n')
  print(f'           [SUBDIR_PLOTS]: {SUBDIR_PLOTS}\n')
  print(f'            [SUBDIR_DATA]: {SUBDIR_DATA}\n')
  print(f'           [SUBDIR_UTILS]: {SUBDIR_UTILS}\n')

  return