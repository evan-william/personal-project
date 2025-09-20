# Vault - The Commitment Marketplace

A command-line prototype application that creates accountability through financial stakes - put your money where your goals are.

## What It Does

This is an early prototype for a startup idea I'm exploring around commitment accountability. The concept is simple: you set a personal goal, stake real money on completing it, assign a trusted witness, and if you fail to meet your deadline, the money automatically goes toward a charitable donation.

Built this prototype to test the core psychological mechanics of financial accountability and see how the commitment system would work in practice before developing a full application.

## The Concept

* Set a personal or professional goal with a specific deadline
* Stake your own money on achieving that goal
* Designate a trusted friend or colleague as your witness
* If you succeed, you get your money back
* If you fail, the stake moves to your donation total for charity

It's designed to leverage loss aversion psychology - people hate losing money more than they like gaining it, which creates powerful motivation to follow through on commitments.

## Features

* User registration and secure login system
* Goal creation with financial stakes
* Automatic deadline monitoring and failure processing
* Balance tracking and donation totals
* MySQL database for persistent data storage
* Password hashing with bcrypt for security

## Project Structure

```
vault-prototype/
├── app.py          # Main application logic and CLI interface
└── README.md       # This file
```

## Requirements

* Python 3.8+
* MySQL server instance
* Required packages:
  - mysql-connector-python
  - bcrypt
  - pyfiglet

Install dependencies:

```bash
pip install mysql-connector-python bcrypt pyfiglet
```

## Setup

The application handles setup automatically:

1. Ensure MySQL server is running
2. Run the script - it will prompt for your database credentials
3. The app creates the `VaultPrototype` database and necessary tables automatically
4. Register a new account or login to start testing

## How to Run

Start the prototype:

```bash
python app.py
```

Follow the prompts to connect to your database, create an account, and start testing commitment scenarios.

## How It Works

The application connects to MySQL, manages user authentication, and tracks commitments with automatic deadline checking. When you return to the main menu, it automatically processes any commitments that have passed their deadline and moves failed stakes to the donation tracker.

This lets me test the core accountability loop and see how the financial consequence system feels in practice.

## What I Learned

* Database design for commitment tracking systems
* User authentication and password security
* Automatic background processing for deadline monitoring
* Command-line interface design for complex workflows
* Financial accountability psychology in application design
* Prototype development for validating startup concepts

## Current Limitations

* Command-line interface only (testing core logic first)
* No actual payment processing or charity integration
* Witness notifications are just text fields for now
* Basic input validation and error handling
* Date-based deadline checking (not time-specific)
* Local testing environment only

## Next Steps for Full Application

The real version would include:
* Web-based interface with mobile responsiveness
* Integrated payment processing for real stakes
* Automated witness notifications and verification
* Direct charity donation processing
* Social features and community challenges
* Advanced goal tracking and analytics
* API for third-party integrations

## Author

**Evan William** - Version 0.1.0 (2025)

Created this prototype to validate my startup idea around commitment accountability systems. It's only for testing the core psychological mechanics and understanding how users might interact with financial stake systems.

This is purely a proof-of-concept to explore the business model and user experience before investing in full development.

*Prototype only - built for concept validation and early testing of the commitment marketplace idea.*
