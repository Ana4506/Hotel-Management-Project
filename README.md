# Hotel-Management-Project

A Hotel Management system is a software application designed to efficiently organize and manage the day-to-day operations of a hotel, including customer and employee records. It streamlines processes such as room reservation, check-in, check-out, facilities, services, billing, and payments. This README provides an overview of the Hotel Management system project and its features.

## Features
The Hotel Management system project includes the following features for both the Administrator and Customers, aiming to provide an easy, reliable, and user-friendly experience.

### Administrator Features
If the user is an Administrator, they need to provide their ID and password for accessing the database. This login step ensures privacy and user identification.

Once logged in, the Administrator has access to the following features:

  1. Check staff details
  2. Check customer details
  3. Staff salary information
  4. Hotel expenses tracking
  5. Services provided to customers
  6. Monitor staff and customer activities
 
The Administrator has significant control over the system details. They can view, edit, add, and re-order commands within the system. However, if the Administrator needs to make changes again, they have to follow the entire procedure mentioned in the project.

### Customer Features
The Hotel Management system offers various features to meet the basic requirements of customers. These features include:

  1. About Hotel: Information about the hotel's background and services.
  2. Contact Us: Contact details to reach out to the hotel for inquiries or assistance.
  3. Salient Features: Highlighted features and amenities of the hotel.
  4. Reviews and Ratings: Feedback and ratings from previous customers.
  5. Sign in/Log in to Book a Room: Login functionality for customers to book a room.
  6. Offers and Discounts: Information about current offers and discounts available.

Customers can enter their travel details and preferences to search for available rooms. The system prompts for the following information:

  1. Traveling to (destination)
  2. Check-in date
  3. Check-out date
  4. Number of people (adults and children)
  5. Room type (Regular/Deluxe/Luxury)
  
Once a customer has booked a room, the system provides access to the following features and services:

  1. Room service
  2. Food options (Breakfast, Lunch, and Dinner)
  3. Transportation availability and rates
  4. Laundry services availability and rates
  5. Gym and Spa facilities availability and rates
  6. Bill details
  7. Opportunity to describe the overall experience
  
## Modules/Functions Used
The Hotel Management system project utilizes the following built-in and user-defined modules/functions:

### Built-in Modules/Functions
Mysql.connector: A module used for connecting and interacting with the MySQL database.

### User-Defined Modules/Functions
The project defines the following user-defined modules/functions:

  1. admin(): Function for handling administrator-related tasks.
  2. employee_details(): Function for retrieving and managing employee details.
  3. food_bill(): Function for calculating and managing food bills.
  4. water_bill(): Function for calculating and managing water bills.
  5. furniture_bill(): Function for calculating and managing furniture bills.
  6. spw(): Function for managing special requests from customers.
  7. signup(): Function for customer sign-up process.
  8. details(): Function for capturing and managing customer details.

## Getting Started
To run the Hotel Management system project locally, follow these steps:

Ensure you have Python installed on your system.
Install the necessary dependencies, including the mysql.connector module.
Set up a MySQL database to store the hotel-related data.






