
def get_fullpath(text_title_str, ftype='data_clean', fig_no='', first_note = '',last_note='', plot_ext='png', no_date=False):
  '''
  Given a required file_type(ftype:['data_clean','data_raw','plot']) and
    optional first_note: str inserted after Title and before (optional) SMA/Standardization info
            last_note: str insterted after (optional) SMA/Standardization info and before (optional) timedate stamp
            plot_ext: change default *.png extension of plot file
            no_date: don't add trailing datetime stamp to filename
  Generate and return a fullpath (/subdir/filename.ext) to save file to
  '''

  # String with full path/filename.ext to return
  fname = ''

  # Get current datetime stamp as a string
  if no_date:
    date_dt = ''
  else:
    date_dt = f'_{datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")}'

  # Clean optional file notation if passed in
  if first_note:
    fnote_str = first_note.replace(' ', '_')
    fnote_str = '_'.join(fnote_str.split())
    fnote_str = '_'.join(fnote_str.split('.'))
    fnote_str = '_'.join(fnote_str.split('__'))
    fnote_str = fnote_str.lower()

  if first_note:
    text_title_str = f'{text_title_str}_{first_note}'

  # Option (a): Cleaned Model Data (Smoothed then Standardized)
  if ftype == 'data_clean':
    fprefix = 'sa_clean_'
    fname_str = f'{SUBDIR_SENTIMENT_CLEAN}{fprefix}{text_title_str}_{Model_Standardization_Method.lower()}_sma{Window_Percent}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.csv'
    else:
      fname = f'{fname_str}{date_dt}.csv'

  # Option (b): Raw Model Data
  elif ftype == 'data_raw':
    fprefix = 'sa_raw_'
    fname_str = f'{SUBDIR_SENTIMENT_RAW}{fprefix}{text_title_str}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.csv'
    else:
      fname = f'{fname_str}{date_dt}.csv'

  # Option (c): Plot Figure
  elif ftype == 'plot':
    if fig_no:
      fprefix = f'plot_{fig_no}_'
    else:
      fprefix = 'plot_'
    fname_str = f'{SUBDIR_SENTIMENT_PLOTS}{fprefix}{text_title_str}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.{plot_ext}'
    else:
      fname = f'{fname_str}{date_dt}.{plot_ext}'

  # Option (d): Crux Text
  elif ftype == 'crux_text':
    fprefix = 'crux_'
    fname_str = f'{SUBDIR_SENTIMENT_CRUXES}{fprefix}{text_title_str}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.txt'
    else:
      fname = f'{fname_str}{date_dt}.txt'

  else:
    print(f'ERROR: In get_fullpath() with illegal arg ftype:[{ftype}]')
    return f'ERROR: ftype:[{ftype}]'

  return fname

# --------------------------------------------------
def textfile2df(fullpath_str):
  '''
  Given a full path to a *.txt file
  Return a DataFrame with one Sentence per row
  '''

  textfile_df = pd.DataFrame()

  with open(fullpath_str,'r') as fp:
    content_str = fp.read() # .replace('\n',' ')

  sents_ls = text_str2sents(content_str)

  textfile_df['text_raw'] = pd.Series(sents_ls)

  return textfile_df

# --------------------------------------------------
# NOTE: SentimentArcs Main datastructure is a Dictionary(Corpus) of DataFrames(Documents: rows=sentences, cols=sentiment, 1 col per model in ensemble)
#       This complex data structure has 2 special I/O utility functions to read/write to permanent disk storage as *.json files

# Utility functions to read/write nested Dictionary (key=novel) of DataFrames (Cols = Model Sentiment Series) 

def write_dict_dfs(adict, out_file='sentiments.json', out_dir=SUBDIR_SENTIMENT_RAW):
  '''
  Given a Dictionary of DataFrames and optional output filename and output directory
  Write as nested json file
  '''

  # convert dataframes into dictionaries
  data_dict = {
      key: adict[key].to_dict(orient='records') 
      for key in adict.keys()
  }

  # write to disk
  out_fullpath = f'{out_dir}{out_file}'
  print(f'Saving file to: {out_fullpath}')
  with open(out_fullpath, 'w') as fp:
    json.dump(
      data_dict, 
      fp, 
      indent=4, 
      sort_keys=True
    )

  return 

def read_dict_dfs(in_file='sentiments.json', in_dir=SUBDIR_SENTIMENT_RAW):
  '''
  Given a Dictionary of DataFrames and optional output filename and output directory
  Read nested json file into Dictionary of DataFrames
  '''

  # read from disk
  in_fullpath = f'{in_dir}{in_file}'
  with open(in_fullpath, 'r') as fp:
      data_dict = json.load(fp)

  # convert dictionaries into dataframes
  all_dt = {
      key: pd.DataFrame(data_dict[key]) 
      for key in data_dict
  }

  return all_dt

# --------------------------------------------------


# --------------------------------------------------


# --------------------------------------------------