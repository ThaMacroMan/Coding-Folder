from flask import Flask,redirect,request, render_template
import stripe

main = Flask(__name__)

@main.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    import os
    main.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))



#if __name__ == '__main__':
#    main.run(host='0.0.0.0', port=8080)




