from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and
    its data
    '''

    #get general sources
    
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    science_sources = get_sources('science')
    technology_sources = get_sources('technology')
    print(technology_sources)

    title = 'Home - Welcome To Online News Website'
    return render_template('index.html',business = business_sources,health=health_sources,science=science_sources,title=title,sports = sports_sources, technology = technology_sources,entertainment = entertainment_sources ,general=general_sources)

@main.route('/news/<id>')
def news(id):
    '''
    view page function that returns both the news article and it's data
    '''
    articles = get_articles(id)
    print(articles)
    title = 'Home - Welcome to  Online News Website'

    return render_template('news.html', articles=articles, title=title)