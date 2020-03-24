(function() {
    var stripe = Stripe('pk_test_s0vrPAXzQaeHLZyRcMfcE8so00552nja3O');
  
    var checkoutButton = document.getElementById('checkout-button-sku_GxvhBJjNakZ86U');
    checkoutButton.addEventListener('click', function () {
      // When the customer clicks on the button, redirect
      // them to Checkout.
      stripe.redirectToCheckout({
        items: [{sku: 'sku_GxvhBJjNakZ86U', quantity: 1}],
  
        // Do not rely on the redirect to the successUrl for fulfilling
        // purchases, customers may not always reach the success_url after
        // a successful payment.
        // Instead use one of the strategies described in
        // https://stripe.com/docs/payments/checkout/fulfillment
        successUrl: 'http://localhost:8000/store/success',
        cancelUrl: 'http://localhost:8000/',
      })
      .then(function (result) {
        if (result.error) {
          // If `redirectToCheckout` fails due to a browser or network
          // error, display the localized error message to your customer.
          var displayError = document.getElementById('error-message');
          displayError.textContent = result.error.message;
        }
      });
    });
  })();