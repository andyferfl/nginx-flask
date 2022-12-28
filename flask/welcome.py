from flask import Flask, request
  
app = Flask(__name__)
  
@app.route('/', methods=['GET'])
def welcome():
    name = request.args.get("name")
    message = request.args.get("message")
    
    welcome_message = "Hello, do I know you?"
    
    if(name is not None):
        welcome_message = f"Hello {name}! "
    
    if(message is not None):
        welcome_message = welcome_message + message
        
    return f"<h1>{welcome_message}<h1>"
  
  
if __name__ == '__main__':
    app.run()
