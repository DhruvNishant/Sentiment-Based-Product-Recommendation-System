{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b2c170d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with windowsapi reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "import model\n",
    "from flask import Flask, render_template, request\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# This is the Flask interface file to connect the backend ML models with the frontend HTML code\n",
    "@app.route('/', methods=['POST', 'GET'])\n",
    "def get_recommendations():\n",
    "    '''\n",
    "    Get top 5 recommended products using ML models\n",
    "    '''\n",
    "    if request.method == 'POST':\n",
    "        username = request.form['uname']\n",
    "        data_list = [[]]\n",
    "        title=['Index', 'Product']\n",
    "        text_info = \"Invalid user! please enter valid user name.\"\n",
    "\n",
    "        if len(username) > 0:\n",
    "            text_info, data_list = model.predict(username)                \n",
    "        return render_template('index.html', info=text_info, data=data_list, headings=title)  \n",
    "    else:\n",
    "        return render_template('index.html')  \n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
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
