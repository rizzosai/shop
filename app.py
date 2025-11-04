from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import json
import logging
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """Main sales page with pricing packages"""
    return render_template('index.html')

@app.route('/packages')
def packages():
    """Detailed packages page"""
    return render_template('packages.html')

@app.route('/domain')
def domain_packages():
    """Domain packages selection page for domain.rizzosai.com"""
    return render_template('domain_packages.html')

@app.route('/webhook-test')
def webhook_test_page():
    """Webhook testing dashboard"""
    return render_template('webhook_test.html')

@app.route('/privacy')
def privacy():
    """Privacy policy page"""
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    """Terms and conditions page"""
    return render_template('terms.html')

# Webhook endpoints for Zapier integration
@app.route('/webhook/trial-signup', methods=['POST'])
def trial_signup_webhook():
    """Handle free trial signups from Zapier"""
    try:
        data = request.get_json()
        logger.info(f"Trial signup webhook received: {data}")
        
        # Extract user data
        email = data.get('email')
        name = data.get('name', '')
        package = data.get('package', 'free-trial')
        
        # Log the trial signup
        trial_data = {
            'email': email,
            'name': name,
            'package': package,
            'signup_date': datetime.now().isoformat(),
            'status': 'trial_active',
            'conversion_price': 499,
            'trial_length_days': 3
        }
        
        # Here you would typically save to database
        # For now, we'll just log it
        logger.info(f"New trial user: {trial_data}")
        
        return jsonify({
            'status': 'success',
            'message': 'Trial signup processed',
            'user_id': email,
            'trial_expires': '3_days'
        }), 200
        
    except Exception as e:
        logger.error(f"Trial signup webhook error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/webhook/trial-conversion', methods=['POST'])
def trial_conversion_webhook():
    """Handle trial to paid conversions from Zapier"""
    try:
        data = request.get_json()
        logger.info(f"Trial conversion webhook received: {data}")
        
        # Extract payment data
        email = data.get('email')
        payment_amount = data.get('amount', 499)
        payment_id = data.get('payment_id')
        
        # Process conversion
        conversion_data = {
            'email': email,
            'payment_amount': payment_amount,
            'payment_id': payment_id,
            'conversion_date': datetime.now().isoformat(),
            'status': 'paid_member',
            'package': 'premium',
            'converted_from_trial': True
        }
        
        # Here you would update user status in database
        logger.info(f"Trial converted to paid: {conversion_data}")
        
        return jsonify({
            'status': 'success',
            'message': 'Conversion processed',
            'user_id': email,
            'access_level': 'premium'
        }), 200
        
    except Exception as e:
        logger.error(f"Trial conversion webhook error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/webhook/payment-success', methods=['POST'])
def payment_success_webhook():
    """Handle successful payments from Zapier"""
    try:
        data = request.get_json()
        logger.info(f"Payment success webhook received: {data}")
        
        # Extract payment data
        email = data.get('email')
        amount = data.get('amount')
        package = data.get('package')
        payment_id = data.get('payment_id')
        
        # Process payment
        payment_data = {
            'email': email,
            'amount': amount,
            'package': package,
            'payment_id': payment_id,
            'payment_date': datetime.now().isoformat(),
            'status': 'completed'
        }
        
        # Here you would grant access based on package
        logger.info(f"Payment processed: {payment_data}")
        
        return jsonify({
            'status': 'success',
            'message': 'Payment processed',
            'user_id': email,
            'package': package
        }), 200
        
    except Exception as e:
        logger.error(f"Payment webhook error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/webhook/trial-expired', methods=['POST'])
def trial_expired_webhook():
    """Handle trial expiration notifications from Zapier (3 days)"""
    try:
        data = request.get_json()
        logger.info(f"Trial expired webhook received: {data}")
        
        email = data.get('email')
        
        # Process trial expiration
        expiration_data = {
            'email': email,
            'expiration_date': datetime.now().isoformat(),
            'status': 'trial_expired',
            'action_needed': 'upgrade_to_paid',
            'trial_duration': '3_days'
        }
        
        logger.info(f"Trial expired: {expiration_data}")
        
        return jsonify({
            'status': 'success',
            'message': 'Trial expiration processed',
            'user_id': email,
            'next_action': 'send_upgrade_reminder'
        }), 200
        
    except Exception as e:
        logger.error(f"Trial expiration webhook error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/webhook/test', methods=['GET', 'POST'])
def test_webhook():
    """Test endpoint for webhook testing"""
    if request.method == 'POST':
        data = request.get_json()
        logger.info(f"Test webhook received: {data}")
        return jsonify({
            'status': 'success',
            'message': 'Test webhook working',
            'received_data': data,
            'trial_period': '3_days'
        }), 200
    else:
        return jsonify({
            'status': 'success',
            'message': 'Webhook endpoint is active',
            'trial_period': '3_days',
            'endpoints': [
                '/webhook/trial-signup',
                '/webhook/trial-conversion', 
                '/webhook/payment-success',
                '/webhook/trial-expired',
                '/webhook/test'
            ]
        }), 200

@app.errorhandler(404)
def not_found(error):
    """Custom 404 page"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
