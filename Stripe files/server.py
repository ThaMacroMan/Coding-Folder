#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request

import stripe
# This is your test secret API key.
stripe.api_key = os.environ.get('stripe.api_key')
main = Flask(__name__,
            static_url_path='',
            static_folder='public')

@main.route('/')
def index():
    return '''
        <form action="/create-checkout-session" method="POST">
            <button id="checkout-button">Checkout</button>
        </form>
    '''


YOUR_DOMAIN = 'http://localhost:4242'

@main.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NGSYKKbuL58S9q0v1E6bYMg',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    main.run(port=4242)