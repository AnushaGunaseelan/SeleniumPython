Feature: Checkout Feature
  Scenario: Verify User Able To Checkout Selected Item
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I verify items listed in my cart "T-SHIRT-HAPPY-NINJA"
    And I proceed to checkout
    And I enter the billing details
    And I place the order
    Then I verify order placed successfully

  Scenario: Verify User Able To Checkout Multiple Items
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    And I add items to my cart "T-SHIRT-NINJA-SILHOUETTE"
    When I view my cart
    And I verify items listed in my cart "T-SHIRT-HAPPY-NINJA"
    And I verify items listed in my cart "T-SHIRT-NINJA-SILHOUETTE"
    And I proceed to checkout
    And I enter the billing details
    And I place the order
    Then I verify order placed successfully

  Scenario: Verify Warning Message When I Apply With In-Valid Coupon Code In Checkout Page
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I apply coupon code "SE45678" in checkout page
    Then I verify coupon code status message "Coupon "se45678" does not exist!" in checkout page

  Scenario: Verify Success Message When I Apply With Valid Coupon Code In Checkout Page
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I apply coupon code "1234" in checkout page
    Then I verify coupon code status message "Coupon "1234" applied successfully!" in checkout page

  Scenario: Verify Order Details
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    Then I verify order details "Happy Ninja  × 1" and "$18.00" and "$18.00" and "$20.00" and "$38.00"

  Scenario: Verify Not Able To Place Order Without FirstName And LastName
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I not enter firstname and lastname
    And I place the order
    Then I verify "Billing First name" is a required field message display
    And I verify "Billing Last name" is a required field message display

  Scenario: Verify Not Able To Place Order Without Address
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I not enter address
    And I place the order
    Then I verify "Billing Street address" is a required field message display
    And I verify "Billing Town / City" is a required field message display
    And I verify "Billing Postcode" is a required field message display

  Scenario: Verify Not Able To Place Order Without Phone Number
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I not enter phone number
    And I place the order
    Then I verify "Billing Phone" is a required field message display

  Scenario: Verify Not Able To Place Order Without Email
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I not enter email
    And I place the order
    Then I verify "Billing Email address" is a required field message display

  Scenario: Verify Not Able To Place Order With Invalid Email
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I proceed to checkout
    And I enter invalid email
    And I place the order
    Then I verify Invalid email message display

  Scenario: Verify User Able To Checkout With Order Notes
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I verify items listed in my cart "T-SHIRT-HAPPY-NINJA"
    And I proceed to checkout
    And I enter the billing details
    And I enter the order notes "Please Deliver In The Evening"
    And I place the order
    Then I verify order placed successfully
