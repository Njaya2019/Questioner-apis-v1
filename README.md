# Questioner api version 1

## Tests

```python

def test_createmeetup(cli_ent):
    now=datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M")
    response=cli_ent.post('api/v1/admin/createmeetup',data=json.dumps(dict(meetup_name="python programming for beginners",meetup_description="We started this to help each other.Regardless of your experince just join us share and learn.Welcome!",location="Mombasa,Kenya",date_created=now)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==201
    assert "congratulations you have created a meet up" in data["message"]

```

How to run the tests.
```
- Run the tests
  - py.test -vv

```