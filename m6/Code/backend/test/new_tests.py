import pytest
BASE="http://127.0.0.1:5000"
def get_token():
    return "357e339fd825907f23f741bb333e9de0f8ddcd7b12b8b7d5f9f5c08f5302b30a"
def get_user():
    return "21f1002269"

# Tests for Get in ThreadAPI
def test_view_threads_successfull():
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user()}
    requests = requests.get(BASE + "/api/thread", headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='successful'

def test_view_threads_unauthorized():
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user()}
    requests = requests.get(BASE + "/api/thread", headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='unauthorized'


# Tests for Post in ThreadAPI
def test_create_thread_successful():
    params = {"title": "title1", "raw": "raw1", "category": 101}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/thread", params=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='success'

def test_create_thread_unsuccessful():
    params = {"title": "title1", "raw": "raw1", "category": 1000}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/thread", params=params, headers=headers)
    assert requests.status_code == 400
    assert requests.json()['status'] =='unsuccessful'
    assert requests.json()['message'] == 'Thread already exists'


def test_create_thread_unauthorized():
    params = {"title": "title1", "raw": "raw1", "category": 101}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/thread", params=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='Unautthorized'



# Tests for Put in ThreadAPI
def test_edit_thread_successful():
    params = {"post": {"raw": "this is a random description"}}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/thread", json=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='success'

def test_edit_thread_unsuccessful():
    params = {"post": {"raw": "this is a random description"}}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/thread", json=params, headers=headers)
    assert requests.status_code == 400
    assert requests.json()['status'] =='unsuccessful'
    assert requests.json()['message'] == 'Thread already exists'


def test_edit_thread_unauthorized():
    params = {"post": {"raw": "this is a random description"}}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/thread", json=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='Unauthorized'

# Tests for Delete in ThreadAPI
def test_delete_threads_successfull():
    params = {"id": 110}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user()}
    requests = requests.get(BASE + "/api/thread",params=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='successful'

def test_delete_threads_unauthorized():
    params = {"id": 110}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user()}
    requests = requests.get(BASE + "/api/thread",params=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='unauthorized'



# Tests for Get request in ReplyAPI
def test_view_reply_successful():
    params = {"id": 110}
    headers = { "Api-Key" : get_token()
              ,"Api-Username" :get_user()}
    requests = requests.get(BASE + "/api/reply",params=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='successful'

def test_view_threads_unauthorized():
    params = {"id": 110}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user()}
    requests = requests.get(BASE + "/api/reply",params=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='unauthorized'


# Tests for Post in ReplyAPI
def test_create_reply_successful():
    params = {"title": "title1", "raw": "raw1", "topic_id": 110}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/reply", params=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='success'

def test_create_reply_unauthorized():
    params = {"title": "title1", "raw": "raw1", "topic_id": 110}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/reply", params=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='Unauthorized'


# Tests for Put in ReplyAPI
def test_edit_reply_successful():
    params = {"post": {"raw": "this is a random description"}}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/reply", json=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='success'

def test_edit_reply_unauthorized():
    params = {"post": {"raw": "this is a random description"}}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user(),
              "Content-Type" : "application/json"}
    requests = requests.post(BASE + "/api/reply", json=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='Unauthorized'


# Tests for delete in ReplyAPI
def test_delete_reply_successful():
    params = {"id": 110}
    headers = { "Api-Key" : get_token()
              ,"Api-Username" :get_user()}
    requests = requests.get(BASE + "/api/reply",params=params, headers=headers)
    assert requests.status_code == 200
    assert requests.json()['status'] =='successful'

def test_delete_threads_unauthorized():
    params = {"id": 110}
    headers = { "Api-Key" : get_token(),
              ,"Api-Username" : get_user()}
    requests = requests.get(BASE + "/api/reply",params=params, headers=headers)
    assert requests.status_code == 403
    assert requests.json()['status'] =='unauthorized'













