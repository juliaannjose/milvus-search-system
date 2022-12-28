from src.tasks.inference import inference


def get_articles(search_param):
    """
    This function calls the inference api

    Parameters
      ----------
      search_param : dict
          a dict contaning search arguments
          such as query, no_of_results

    Returns
      -------
      postgres_result : list(list)
          a list of lists containing milvus distance, title,
          abstract, authors, url

    """
    results = inference(search_param)
    return results
