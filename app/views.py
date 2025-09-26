from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextid = 4
topics = [{'id':1, 'title': 'routing', 'body': 'Routing is...'},
        {'id':2, 'title': 'view', 'body': 'view is...'},
        {'id':3, 'title': 'model', 'body': 'model is...'}]

def HTMLTemplate(articleTag, id=None):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic['id']}">{topic["title"]}</a></li>'

    return HttpResponse(f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
            {articleTag}
        <ul>
            <li><a href = "/create">create</a></li>
            <li>
                <form action="/delete/" method="POST">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
        </ul>
    </body>
    </html>
    ''')

def index(request):
    article = ''' 
    <h2>Welcome<h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f"<h2>{topic['title']}</h2>{topic['body']}"
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    if request.method == "GET":
        article = '''
        <form action = "/create/" method="post">
            <p><input type = "Text" name = "title" placeholder = "text"></p>
            <p><textarea name = "body" placeholder = "text" ></textarea></p>
            <p><input type = "submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    
    elif request.method == "POST":
        global nextid
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {'id': nextid, 'title': title, 'body': body}
        topics.append(newTopic)
        url = "/read/"+str(nextid)
        nextid += 1 
        return redirect(url)

@csrf_exempt
def delete(request):
    if request.method == "POST":
        request
