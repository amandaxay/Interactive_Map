from flask import Flask
from flask import render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # query = request.args.get('search')
    # if query != None:   #if we are given a search query, perform a search over it
    #     page = request.args.get('page')
    #     rws = RecipeWhooshSearch()
    #     if page != None:
    #         results = rws.search(given_query=query, page=int(page)) #if we are given a page number, search for that page
    #         page = int(page)
    #     else:
    #         results = rws.search(query) #if we arent given a page number, get page 1
    #         page = 1
       
    #     total_pages = math.ceil(results['total']/10)    #calculate the total number of results, so we know how many pages there are
       
    #     return render_template('results.html', #render results page
    #                             query=query, 
    #                             results=results['entries'], 
    #                             total_pages=total_pages, 
    #                             curr_page=page,
    #                             advanced=False)
    return render_template('index.html') #if we arent given a query, render the landing page

@app.route('/CAstatePage')
def CAstate():
    return render_template('/state_page.html')

if __name__ == "__main__":
    app.run(debug=True)