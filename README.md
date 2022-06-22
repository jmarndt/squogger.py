# Squat Logger
squogger.py is a simple to to log your squats for the 30/30 Squat Challenge
[http://placeofpersistence.com/30-30-squat-challenge-by-ido-portal/](http://placeofpersistence.com/30-30-squat-challenge-by-ido-portal/)

## Usage
Simply run:
```
squogger.py minutes:seconds
```
Make sure minutes/seconds are in this format or will likely blow up.

Example:
```
squogger.py 2:33
```

## Output
Logs are saved to `squat.json` in the same directory, using the following structure
```
{
  "2022-06-21": {
    "total_minutes": 5.35,
    "sessions": [
      1.1,
      2.5,
      1.75
    ]
  }
}
```