import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    article_views = views[views['author_id'] == views['viewer_id']]
    article_views=article_views[['author_id']].rename(columns={'author_id':'id'}).drop_duplicates().sort_values(by='id')
    return article_views