# Questioner api version 1

[![Build Status](https://travis-ci.org/Njaya2019/Questioner-apis-v1.svg?branch=developer)](https://travis-ci.org/Njaya2019/Questioner-apis-v1)

[![Coverage Status](https://coveralls.io/repos/github/Njaya2019/Questioner-apis-v1/badge.png?branch=developer)](https://coveralls.io/github/Njaya2019/Questioner-apis-v1?branch=developer)
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