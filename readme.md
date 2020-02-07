# requirements:
`pip install -r requirements.txt`
or
`conda env create --file=enviroment.yml`
# how to
`python cam.py`

```
--threshold [int]  how big the area of difference? (DEFAULT: 500)
--delay 0>[int]>100, the bigger the slower the fps (DEFAULT: 100)
```
# todo
- [ ] send telegram notif if movement detected
    - [ ] pics of movement
- [ ] buffer value for recording