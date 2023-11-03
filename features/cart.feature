Feature: Cart Feature
  Scenario: Verify Add Items To Cart
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    Then I verify items listed in my cart "T-SHIRT-HAPPY-NINJA"

  Scenario: Verify Items Remove From Cart
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I remove items from cart "T-SHIRT-HAPPY-NINJA"
    Then I verify items removed from cart "T-SHIRT-HAPPY-NINJA"

  Scenario Outline: Verify User Able To Add Different Items To Cart
    Given open homepage url
    And I add items to my cart "<Items>"
    When I view my cart
    Then I verify items listed in my cart "<Items>"

    Examples:
    | Items                    |
	| T-SHIRT-HAPPY-NINJA      |
	| T-SHIRT-NINJA-SILHOUETTE |
	| POSTER-PREMIUM-QUALITY   |
	| T-SHIRT-PREMIUM-QUALITY  |

  Scenario: Verify Add Items To Cart From Product Details Page
    Given open homepage url
    When I click the item "Flying Ninja"
    And I Add Item To Cart From Product Details Page
    And I view my cart
    Then I verify items listed in my cart "Flying Ninja"

  Scenario: Verify Add Items And Change Quantity To Cart From Product Details Page
    Given open homepage url
    When I click the item "Flying Ninja"
    And I Change the quantity to "3"
    And I Add Item To Cart From Product Details Page
    And I view my cart
    Then I verify items listed in my cart "Flying Ninja"

  Scenario: Verify Added Items Details Correctly Displayed In Cart
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    And I add items to my cart "T-SHIRT-PREMIUM-QUALITY"
    When I view my cart
    Then I verify item details in cart "T-SHIRT-HAPPY-NINJA" and "$18.00" and "1" and "$18.00"
    Then I verify item details in cart "T-SHIRT-PREMIUM-QUALITY" and "$20.00" and "1" and "$20.00"

  @test
  Scenario: Verify Able To Update Cart
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I change quantity to "3" for item "T-SHIRT-HAPPY-NINJA"
    And I Update Cart
    Then I verify cart updated message
    And I verify item details in cart "T-SHIRT-HAPPY-NINJA" and "$18.00" and "3" and "$54.00"

  Scenario: Verify Cart Totals
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    And I add items to my cart "T-SHIRT-NINJA-SILHOUETTE"
    When I view my cart
    Then I verify cart totals "$38.00" and "$20.00" and "$58.00"

  @test
  Scenario: Verify Cart Totals Updated When I Remove Item
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    And I add items to my cart "T-SHIRT-NINJA-SILHOUETTE"
    When I view my cart
    And I remove items from cart "T-SHIRT-HAPPY-NINJA"
    Then I verify items removed from cart "T-SHIRT-HAPPY-NINJA"
    And I verify cart totals "$20.00" and "$20.00" and "$40.00"

  Scenario: Verify Able To Change Shipping Address
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I change shipping address "United Kingdom (UK)" and "West" and "Livin" and "EH11 1EG"
    And I click update address
    Then I verify shipping address updated "United Kingdom (UK)" and "West" and "Livin" and "EH11 1EG"

  Scenario: Verify Warning Message When I Apply With In-Valid Coupon Code
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I apply coupon code "SE45678"
    Then I verify coupon code status message "Coupon "se45678" does not exist!"

  # Not Implemented Due to lack of valis coupon code test data
  Scenario: Verify Success Message When I Apply With Valid Coupon Code
    Given open homepage url
    And I add items to my cart "T-SHIRT-HAPPY-NINJA"
    When I view my cart
    And I apply valid coupon code "123456"
    Then I verify coupon code "123456" applied successfully message display
