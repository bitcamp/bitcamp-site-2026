### bitbot
# dependencies
```pip install -r requirements.txt```

# model
```choco install ollama``` / ```brew install ollama``` / ```curl -fsSL https://ollama.com/install.sh | sh```
OR 
manually install ollama from developer documentation

# running
```python
python app.py
```
OR
remove 
```python
if __name__==""__main__"":
    app.run(debug=True, port=3000)
```
, run with
```gunicorn -b 0.0.0.0:3000 bitbot:app```
