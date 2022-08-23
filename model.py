{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1be5e8ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import pandas as pd\n",
    "\n",
    "# contains one ML model and only one recommendation system that we have obtained from the\n",
    "# previous steps to recommend top 5 products\n",
    "\n",
    "def predict(username):\n",
    "    '''\n",
    "    Predicting the top recommended products using best ML models\n",
    "    '''\n",
    "    list_data = [[]]\n",
    "    text_info = \"Entered user name is not available. Please enter valid user name!\"\n",
    "    \n",
    "    # load all input files\n",
    "    review_df = pd.read_csv(r'C:\\Users\\nishant\\Downloads\\sample30.csv')\n",
    "    sentiment_clean_df = pd.read_csv(r'sentiment_df.csv')\n",
    "\n",
    "    user_reco_file = open('./pickle/user_recommendation.pkl', 'rb')\n",
    "    user_reco_table = pickle.load(user_reco_file)\n",
    "\n",
    "    sentiment_model_file = open('./pickle/Sentiment_model.pkl', 'rb')\n",
    "    sentiment_model = pickle.load(sentiment_model_file)\n",
    "\n",
    "    tfidf_file = open('./pickle/tfidf_vectorizer.pkl', 'rb')\n",
    "    tfidf_vector = pickle.load(tfidf_file)\n",
    "\n",
    "    # check for valid username\n",
    "    if username in user_reco_table.index:\n",
    "\n",
    "        top20_product_ids = user_reco_table.loc[username].sort_values(ascending=False)[:20]\n",
    "        product_map = pd.DataFrame(review_df[['id','name']]).drop_duplicates()\n",
    "        top20_products = pd.merge(top20_product_ids, product_map, on='id')\n",
    "\n",
    "        # Mapping product with product reviews\n",
    "        product_mapping_review = pd.DataFrame(sentiment_clean_df[['id','text_data','user_sentiment']]).drop_duplicates()\n",
    "        product_review_data =pd.merge(top20_products, product_mapping_review, on='id')\n",
    "\n",
    "        # get features using tfidf vectorizer\n",
    "        test_features= tfidf_vector.transform(product_review_data['text_data'])\n",
    "\n",
    "        # Predict Sentiment Score on the above Product Reviews using the finally selected ML model\n",
    "        product_review_data['predicted_sentiment'] = sentiment_model.predict(test_features)\n",
    "        product_review_data['predicted_sentiment_score'] = product_review_data['predicted_sentiment'].replace(['negative','positive'],[0,1])\n",
    "\n",
    "        # Find positive sentiment percentage for every product\n",
    "        product_pivot = product_review_data.reset_index().pivot_table(values='predicted_sentiment_score', index='name', aggfunc='mean')\n",
    "        product_pivot.sort_values(by='predicted_sentiment_score',inplace= True, ascending= False)\n",
    "        \n",
    "        # Get top 5 products\n",
    "        list_data = [[index, out] for index, out in enumerate (product_pivot.head(5).index, 1)]\n",
    "        text_info = \"Top 5 Recommended products for \\\"\" + username +  \"\\\"\"\n",
    "\n",
    "    return text_info, list_data"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
