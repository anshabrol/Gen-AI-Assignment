# Low-Level Technical Specification

## Business Requirement
Build a food delivery application where users can browse restaurants,
place orders, make payments, and track delivery in real time.

## System Modules
- User Management Module
- Restaurant Catalog Module
- Ordering Module
- Payment Module
- Tracking Module
- Delivery Management Module
- Merchant Management Module
- Notification Module

## Database Schema
- **User Management Module**
- users(id, name, email, password_hash, phone, created_at)
- **Merchant Management Module**
- merchants(id, name, email, phone, contact_details)
- **Restaurant Catalog Module**
- restaurants(id, merchant_id_fk, name, description, address, cuisine_type, rating)
- menu_items(id, restaurant_id_fk, name, description, price, category)
- **Ordering Module**
- orders(id, user_id_fk, restaurant_id_fk, order_date, total_amount, status)
- order_items(id, order_id_fk, menu_item_id_fk, quantity, unit_price)
- **Payment Module**
- payments(id, order_id_fk, payment_method, amount, transaction_status, transaction_date)
- **Delivery Management Module**
- drivers(id, name, phone, vehicle_details, status)
- deliveries(id, order_id_fk, driver_id_fk, delivery_address, pickup_time, delivery_time, delivery_status)
- **Tracking Module**
- order_tracking(id, order_id_fk, status_description, timestamp, location)
- **Notification Module**
- notifications(id, recipient_type, recipient_id, message_body, sent_at, is_read)

## API Endpoints
## REST API Endpoints
### User Management Module
 | API | Description |
 | :--- | :--- |
 | POST /users | Create a new user account |
 | GET /users | Retrieve a list of users (filterable) |
 | GET /users/{id} | Retrieve a specific user by ID |
 | PUT /users/{id} | Update user information |
 | DELETE /users/{id} | Deactivate or delete a user account |
 | POST /users/login | Authenticate a user and create a session (or token) |
 | POST /users/{id}/roles | Assign a role to a user |
 | POST /users/password/reset | Initiate password reset process |
 ### Restaurant Catalog Module
 | API | Description |
 | :--- | :--- |
 | POST /restaurants | Create a new restaurant entry |
 | GET /restaurants | Retrieve a list of restaurants (searchable, filterable by location/category) |
 | GET /restaurants/{id} | Retrieve details for a specific restaurant |
 | PUT /restaurants/{id} | Update restaurant details |
 | GET /restaurants/{id}/menus | Retrieve all menus for a specific restaurant |
 | POST /restaurants/{id}/menus | Create a new menu for a restaurant |
 | GET /menus/{menu_id}/items | Retrieve all items within a specific menu |
 | POST /items | Create a new catalog item (e.g., burger, salad) |
 | GET /categories | Retrieve a list of food categories |
 ### Ordering Module
 | API | Description |
 | :--- | :--- |
 | POST /cart/items | Add an item to the user's current shopping cart |
 | GET /cart | Retrieve the contents of the user's current shopping cart |
 | DELETE /cart/items/{item_id} | Remove a specific item from the cart |
 | POST /orders | Submit the cart contents as a new order |
 | GET /orders | Retrieve the current user's order history |
 | GET /orders/{id} | Retrieve details of a specific order |
 | PATCH /orders/{id}/status | Update the status of an order (e.g., confirmed, cancelled) |
 | POST /orders/{id}/cancel | Request cancellation of an order |
 ### Payment Module
 | API | Description |
 | :--- | :--- |
 | POST /payments | Initiate a payment for a specific order |
 | GET /payments/{id} | Retrieve details of a specific payment transaction |
 | POST /payments/{id}/capture | Capture an authorized payment |
 | POST /payments/{id}/refund | Process a refund for a payment |
 | GET /transactions | Retrieve a list of all transactions (Admin/Merchant view) |
 | POST /payment_methods | Add a new saved payment method (e.g., credit card token) |
 ### Tracking Module
 | API | Description |
 | :--- | :--- |
 | GET /orders/{order_id}/tracking | Retrieve real-time status and location information for an order |
 | GET /deliveries/{delivery_id}/route | Retrieve the optimized route map for a delivery |
 | PUT /deliveries/{delivery_id}/location | Update the location (GPS coordinates) of a delivery agent (Internal use) |
 | GET /deliveries/{delivery_id}/events | Retrieve a timeline of tracking events (e.g., picked up, arriving soon) |
 ### Delivery Management Module
 | API | Description |
 | :--- | :--- |
 | GET /drivers | Retrieve a list of all delivery drivers |
 | POST /drivers | Register a new delivery driver |
 | GET /drivers/available | Retrieve a list of currently available drivers |
 | POST /deliveries | Create a new delivery record (usually triggered by an order) |
 | GET /deliveries/{id} | Retrieve details for a specific delivery |
 | PUT /deliveries/{id}/assign | Manually assign a driver to a delivery |
 | PATCH /deliveries/{id}/complete | Mark a delivery as successfully completed |
 | GET /delivery_zones | Retrieve defined delivery service zones |
 ### Merchant Management Module
 | API | Description |
 | :--- | :--- |
 | POST /merchants | Onboard a new merchant partner (restaurant owner) |
 | GET /merchants | Retrieve a list of all registered merchants |
 | GET /merchants/{id} | Retrieve specific merchant account details |
 | PATCH /merchants/{id}/status | Approve, reject, or suspend a merchant account |
 | GET /merchants/{id}/performance | Retrieve performance metrics and sales data for a merchant |
 | GET /merchants/{id}/payouts | Retrieve the history of financial payouts to a merchant |
 | POST /merchant_settings | Update global settings for a merchant (e.g., operating hours) |
 ### Notification Module
 | API | Description |
 | :--- | :--- |
 | GET /notifications | Retrieve all notifications for the current user |
 | PATCH /notifications/{id} | Mark a specific notification as read |
 | DELETE /notifications/{id} | Dismiss/delete a specific notification |
 | POST /notifications/send | Trigger a system notification (Internal API for microservices) |
 | GET /notification_templates | Retrieve a list of available notification templates |
 | PUT /notification_templates/{id} | Update the content of a notification template |

## Pseudocode
```
This high-level pseudocode outlines the primary processes and interactions within the Food Delivery System.

---

## SYSTEM: FOOD DELIVERY APPLICATION

### 1. INITIALIZATION AND USER SETUP

```pseudocode
FUNCTION INITIALIZE_USER_SESSION()
    // User Authentication
    PROMPT_FOR_LOGIN_DETAILS()
    IF AUTHENTICATE_USER(Username, Password) IS FALSE
        DISPLAY_ERROR("Login failed. Please register or try again.")
        RETURN FAILURE
    END IF

    // Location Services
    USER_LOCATION = GET_DEVICE_LOCATION()
    IF USER_LOCATION IS NULL
        PROMPT_FOR_MANUAL_ADDRESS()
        USER_ADDRESS = VALIDATE_ADDRESS(ManualInput)
    ELSE
        USER_ADDRESS = CONVERT_GPS_TO_ADDRESS(USER_LOCATION)
    END IF

    SET_DELIVERY_ZONE(USER_ADDRESS)
    RETURN SUCCESS
END FUNCTION
```

### 2. BROWSING AND CART MANAGEMENT (MAIN LOOP)

```pseudocode
FUNCTION MAIN_ORDERING_FLOW()
    LOOP WHILE USER_SESSION_ACTIVE
        DISPLAY_HOME_SCREEN()
        
        // Step 1: Browse and Filter
        RESTAURANT_LIST = GET_RESTAURANTS_IN_ZONE(DELIVERY_ZONE)
        DISPLAY_RESTAURANT_LIST(RESTAURANT_LIST)
        
        USER_ACTION = GET_USER_INPUT()
        
        IF USER_ACTION IS "SELECT_RESTAURANT"
            SELECTED_RESTAURANT = GET_RESTAURANT_DETAILS(UserInputID)
            DISPLAY_MENU(SELECTED_RESTAURANT)
            
            // Step 2: Add Items to Cart
            LOOP WHILE USER_IS_ADDING_ITEMS
                MENU_ITEM = GET_USER_SELECTION()
                IF MENU_ITEM IS NOT NULL
                    ADD_ITEM_TO_CART(MENU_ITEM)
                ELSE
                    BREAK LOOP
                END IF
            END LOOP
            
        ELSE IF USER_ACTION IS "VIEW_CART"
            DISPLAY_CURRENT_CART()
            PROMPT_FOR_CART_MODIFICATION()
            
        ELSE IF USER_ACTION IS "PROCEED_TO_CHECKOUT"
            IF CART_IS_EMPTY
                DISPLAY_ERROR("Cannot checkout: Cart is empty.")
            ELSE
                BREAK LOOP // Exit ordering flow and move to checkout
            END IF
            
        ELSE IF USER_ACTION IS "LOGOUT"
            TERMINATE_SESSION()
            BREAK LOOP
            
        ELSE
            DISPLAY_ERROR("Invalid action.")
        END IF
    END LOOP

    IF USER_ACTION IS "PROCEED_TO_CHECKOUT"
        CALL PROCESS_CHECKOUT_AND_PAYMENT()
    END IF

END FUNCTION
```

### 3. CHECKOUT AND PAYMENT PROCESSING

```pseudocode
FUNCTION PROCESS_CHECKOUT_AND_PAYMENT()
    CALCULATE_SUBTOTAL(Cart)
    DELIVERY_FEE = CALCULATE_DELIVERY_FEE(DELIVERY_ZONE, RestaurantDistance)
    TAX = CALCULATE_TAX(Subtotal)
    TOTAL_AMOUNT = Subtotal + DeliveryFee + Tax

    DISPLAY_ORDER_SUMMARY(TOTAL_AMOUNT)

    // Step 1: Select Payment Method
    PROMPT_USER_FOR_PAYMENT_METHOD()
    
    // Step 2: Payment Attempt Loop
    LOOP ATTEMPT_COUNT = 1 TO 3 // Allow up to 3 retries
        PAYMENT_RESPONSE = SUBMIT_PAYMENT(Method, TOTAL_AMOUNT)
        
        IF PAYMENT_RESPONSE IS SUCCESS
            ORDER_ID = GENERATE_UNIQUE_ID()
            PERSIST_ORDER_TO_DATABASE(ORDER_ID, Cart, TOTAL_AMOUNT)
            SEND_CONFIRMATION_EMAIL(ORDER_ID)
            RETURN ORDER_ID
            
        ELSE IF ATTEMPT_COUNT < 3
            DISPLAY_ERROR("Payment failed. Please check details or try another method.")
        ELSE
            DISPLAY_ERROR("Maximum payment attempts reached. Order cancelled.")
            RETURN NULL // Failure
        END IF
    END LOOP
END FUNCTION
```

### 4. ORDER FULFILLMENT AND REAL-TIME TRACKING (ASYNCHRONOUS)

This module runs in the background immediately after the order is placed successfully.

```pseudocode
FUNCTION MANAGE_ORDER_LIFECYCLE(ORDER_ID)
    
    ORDER_STATUS = "PLACED"
    
    // Step 1: Restaurant Confirmation
    SEND_NOTIFICATION_TO_RESTAURANT(ORDER_ID)
    LOOP WHILE RESTAURANT_ACTION IS "PENDING"
        WAIT(10 seconds)
        IF RESTAURANT_REJECTS_ORDER
            UPDATE_ORDER_STATUS(ORDER_ID, "REJECTED")
            NOTIFY_USER("Restaurant could not fulfill order.")
            RETURN
        ELSE IF RESTAURANT_CONFIRMS_ORDER
            UPDATE_ORDER_STATUS(ORDER_ID, "PREPARING")
            BREAK LOOP
        END IF
    END LOOP
    
    // Step 2: Driver Assignment
    LOOP
        DRIVER = ASSIGN_NEAREST_DRIVER(RestaurantLocation)
        IF DRIVER IS NOT NULL
            SEND_TRIP_REQUEST_TO_DRIVER(ORDER_ID, DRIVER)
            WAIT(30 seconds) // Wait for driver response
            
            IF DRIVER_ACCEPTS
                UPDATE_ORDER_STATUS(ORDER_ID, "AWAITING_PICKUP")
                BREAK LOOP
            ELSE
                // Driver rejected, loop to find new driver
            END IF
        ELSE
            // No drivers available
            UPDATE_ORDER_STATUS(ORDER_ID, "DELAYED")
            NOTIFY_USER("Searching for driver...")
            WAIT(60 seconds)
        END IF
    END LOOP
    
    // Step 3: Real-Time Tracking Loop
    LOOP WHILE ORDER_STATUS IS NOT "DELIVERED"
        
        IF ORDER_STATUS IS "AWAITING_PICKUP" AND DRIVER_ARRIVED_AT_RESTAURANT
             DRIVER_CONFIRMS_PICKUP(ORDER_ID)
             UPDATE_ORDER_STATUS(ORDER_ID, "EN_ROUTE")
        END IF
        
        IF ORDER_STATUS IS "EN_ROUTE"
            DRIVER_LOCATION = GET_DRIVER_GPS(DRIVER_ID)
            // Push location update to the user's tracking interface
            PUSH_REAL_TIME_UPDATE_TO_USER(ORDER_ID, DRIVER_LOCATION)
        END IF
        
        IF DRIVER_CONFIRMS_DELIVERY_COMPLETE(ORDER_ID)
            UPDATE_ORDER_STATUS(ORDER_ID, "DELIVERED")
            BREAK LOOP
        END IF
        
        WAIT(5 seconds) // Update frequency
    END LOOP
    
    // Step 4: Finalization
    NOTIFY_USER("Your order has been delivered.")
    PROMPT_USER_FOR_RATING_AND_TIP(ORDER_ID)

END FUNCTION
```
---
```