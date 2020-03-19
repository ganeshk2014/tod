#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from datetime import datetime
app = Flask(__name__)
@app.route('/default')
def default():
    hour = datetime.now().hour
    return (
        "2" if 5 <= hour <= 11
        else
        "0" if 12 <= hour <= 17
        else
        "1" 
    )
if __name__ =='__main__':
    app.run(debug=True)

