Feature: HomePage Feature
  @test
  Scenario: Verify HomPage Title
    Given open homepage url
    When check homepage
    Then  verify homepage title

  Scenario Outline: Verify Able To Navigate Different Pages
    Given open homepage url
    When I click link "<Page>"
    Then verify page displayed "<Page>"

    Examples:
    | Page      |
	| CART      |
	| MYACCOUNT |

  Scenario: Verify Able To Search Item
    Given open homepage url
    When I search item "Woo Singles"
    Then verify item "Woo Singles" displayed

  Scenario: Verify Able To Sort By Price - Low To High
    Given open homepage url
    When I sort by "Sort by price: low to high"
    Then verify items listed by low to high "Woo Single #2" and "$3.00" and "Ship Your Idea" and "$15.00"

  Scenario: Verify Able To Sort By Price - High To Low
    Given open homepage url
    When I sort by "Sort by price: high to low"
    Then verify items listed by high to low "Patient Ninja" and "$35.00" and "Woo Logo" and "$18.00"

  Scenario: Verify Able To Sort By Popularity
    Given open homepage url
    When I sort by "Sort by popularity"
    Then verify items listed by popularity "Woo Logo" and "$15.00" and "Woo Logo" and "$35.00"

  Scenario: Verify Able To Sort By Latest
    Given open homepage url
    When I sort by "Sort by latest"
    Then verify items listed by latest "Patient Ninja" and "$35.00" and "Ninja Silhouette" and "$20.00"

  Scenario: Verify Able To Sort By Average Rating
    Given open homepage url
    When I sort by "Sort by average rating"
    Then verify items listed by average rating "Patient Ninja" and "$35.00" and "Ninja Silhouette" and "$20.00"

  Scenario: Verify Home Page Display The Items By Default Sorting
    Given open homepage url
    When check homepage
    Then verify "DEFAULT SORTING" option selected
    And verify items listed by default sorting "Flying Ninja" and "$15.00" and "Woo Album #1" and "$9.00"

  Scenario: Verify Able To View Full Product Details
    Given open homepage url
    When I click the item "Flying Ninja"
    Then verify full product details displayed "Flying Ninja"

  Scenario: Verify Able To Navigate To Different Page
    Given open homepage url
    When I click the page number "2"
    Then verify product list page displayed "Showing 13–24 of 24 results"
